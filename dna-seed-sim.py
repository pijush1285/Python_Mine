# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:01:25 2022

@author: PIJHUSH
"""

#! /usr/bin/env python3
# Author: Martin C. Frith 2020

from __future__ import print_function

import argparse
import collections
import itertools
import logging
import math
import os
import random
import sys

alphabet = "acgt"

ambiguityCodes = {"a": "a",
                  "c": "c",
                  "g": "g",
                  "t": "t",
                  "r": "ag",
                  "y": "ct",
                  "w": "at",
                  "s": "cg",
                  "m": "ac",
                  "k": "gt",
                  "b": "cgt",
                  "d": "agt",
                  "h": "act",
                  "v": "acg",
                  "n": "acgt"}

ryAlphabet = "ry"

ryAmbiguityCodes = {"r": "r",
                    "y": "y",
                    "n": "ry"}

def murmur64(k):  # also known as fmix64
    k ^= k >> 33
    k *= 0xff51afd7ed558ccd
    k %= 2 ** 64
    k ^= k >> 33
    k *= 0xc4ceb9fe1a85ec53
    k %= 2 ** 64
    k ^= k >> 33
    return k

def readOneSequence(lines):
    s = []
    for line in lines:
        if line[0] == ">":
            if s: break
        else:
            m = map(alphabet.find, line.lower())
            s.append(bytes(i for i in m if i >= 0))
    return b''.join(s)

def randomSequence(letterFreqs, length):
    return bytes(random.choices(range(len(alphabet)), letterFreqs, k=length))

def evolvedSequence(substitutionMatrix, originalSequence):
    r = range(len(alphabet))
    return bytes(random.choices(r, substitutionMatrix[i])[0]
                 for i in originalSequence)

def randomRelatedSequencePair(letterFreqs, length, substitutionMatrix):
    seq1 = randomSequence(letterFreqs, length)
    seq2 = evolvedSequence(substitutionMatrix, seq1)
    return seq1, seq2

def tamura1992substitutionMatrix(gcPercent, kappa, pam):
    s = 0.005 * gcPercent  # prob(c) = prob(g)
    w = 0.5 - s            # prob(a) = prob(t)
    t = pam * 0.01 / (4 * w * s * kappa + 0.5)
    i = math.exp(-t)
    j = 2 * math.exp(-(kappa + 1) * t / 2)
    wwr = 1 + i + j*s/w
    ssr = 1 + i + j*w/s
    tir = 1 + i - j
    tvr = 1 - i

    wwp = w * w * wwr
    ssp = s * s * ssr
    percentIdentity = 200 * (wwp + ssp)
    obsTiPerTv = 8 * w * s * tir / tvr

    logging.info("percent identity: " + str(percentIdentity))
    logging.info("transitions per transversion: " + str(obsTiPerTv))

    #                       A         C         G         T
    probFromRowToColumn = [[w * wwr,  s * tvr,  s * tir,  w * tvr],  # A
                           [w * tvr,  s * ssr,  s * tvr,  w * tir],  # C
                           [w * tir,  s * tvr,  s * ssr,  w * tvr],  # G
                           [w * tvr,  s * tir,  s * tvr,  w * wwr]]  # T
    return probFromRowToColumn

def complement(seq):
    a = len(alphabet)
    return bytes(a - i for i in seq)

def cyclicLetterOrderSequence(letterOrders, seq, offset):
    rankings = [bytes(map(i.index, alphabet)) for i in letterOrders]
    n = len(letterOrders)
    return bytes(rankings[(i - offset) % n][x] for i, x in enumerate(seq))

def keyGenAlphabetic(seq, end):
    for i in range(end):
        yield seq[i:]

def keyGenCyclic(recodedSeqs, end):
    for i in range(end):
        yield recodedSeqs[i % len(recodedSeqs)][i:]

def keyGenAbb(seq, complementedSeq, end):
    for i in range(end):
        yield seq[i], complementedSeq[i+1:]

def seqCodeMurmur64(seq):
    a = len(alphabet)
    h = 0
    for i in seq:
        h = h * a + i
    assert h < 2 ** 64
    return murmur64(h)

def keyGenMurmur64(seq, wordLength, end):
    a = len(alphabet)
    m = a ** wordLength
    assert m <= 2 ** 64
    w = wordLength - 1
    h = 0
    for i in range(end + w):
        h = h * a % m + seq[i]
        if i >= w:
            yield murmur64(h)

def getKeyGen(orderOpt, seq, keyEnd, keySpan):
    if orderOpt == 4:
        return keyGenMurmur64(seq, keySpan, keyEnd)
    elif orderOpt == 3:
        reducedSeq = bytes(i == 0 for i in seq)
        return keyGenAbb(seq, reducedSeq, keyEnd)
    elif orderOpt == 2:
        complementedSeq = complement(seq)
        return keyGenAbb(seq, complementedSeq, keyEnd)
    elif orderOpt == 1:
        letterOrders = "catg", "gtac"  # so the minimum sequence is: cgcgcg...
        recodedSeqs = [cyclicLetterOrderSequence(letterOrders, seq, offset)
                       for offset in range(len(letterOrders))]
        return keyGenCyclic(recodedSeqs, keyEnd)
    else:
        return keyGenAlphabetic(seq, keyEnd)

def minimizerPositions(args, seq, seqLen, keySpan):
    winLen = args.min_window
    winFin = winLen - 1
    isEndMinimizers = args.min_type == 1 and not args.circular

    if args.min_type == 2 and not args.circular:
        seq *= 2

    keyEnd = seqLen - keySpan + 1
    if args.min_type == 2 or args.circular:
        assert winFin + keySpan - 1 <= seqLen
        keyEnd = seqLen + winFin

    keyGen = getKeyGen(args.min_order, seq, keyEnd, keySpan)

    windowOfKeys = []

    for i, x in enumerate(keyGen):
        windowOfKeys.append(x)
        minKey = min(windowOfKeys)
        if i >= winFin:
            for j, k in enumerate(windowOfKeys):
                if k == minKey:
                    yield (i - winFin + j) % seqLen
            windowOfKeys.pop(0)
        elif isEndMinimizers:
            for j, k in enumerate(windowOfKeys):
                if k == minKey:
                    yield j

    if isEndMinimizers:
        while windowOfKeys:
            minKey = min(windowOfKeys)
            for j, k in enumerate(windowOfKeys):
                if k == minKey:
                    yield keyEnd - len(windowOfKeys) + j
            windowOfKeys.pop(0)

def syncmerPositions(args, seq, seqLen, seedLen):
    winLen = args.syn_window
    winFin = winLen - 1
    wanted = [args.syn_offset - 1] if args.syn_offset else [0, winFin]
    maxCode = (2 ** 64 - 1) // args.syn_sample

    assert seedLen > winFin
    keySpan = seedLen - winFin

    keyEnd = seqLen - keySpan + 1
    if args.circular:
        assert winFin + keySpan - 1 <= seqLen
        keyEnd = seqLen + winFin

    keyGen = getKeyGen(args.syn_order, seq, keyEnd, keySpan)

    windowOfKeys = []

    for i, x in enumerate(keyGen):
        windowOfKeys.append(x)
        if i >= winFin:
            j = min(range(winLen), key=windowOfKeys.__getitem__)
            if j in wanted:
                k = i - winFin
                if seqCodeMurmur64(seq[k:k+seedLen]) <= maxCode:
                    yield k
            windowOfKeys.pop(0)

def wordPositions(args, words, seq, seqLen):
    if args.isRyWords:
        seq = bytes(i & 1 for i in seq)
    return [i for i in range(seqLen) if seq.startswith(words, i)]

def seedPositions(args, words, seq, seqLen, seedLen, isFirstSeq):
    if words:
        return wordPositions(args, words, seq, seqLen)
    elif args.min_window > 1:
        if args.min_order > 3 and not seedLen:
            return None
        keySpan = max(seedLen, 1)
        return sorted(set(minimizerPositions(args, seq, seqLen, keySpan)))
    elif args.syn_window > 1:
        if not seedLen:
            return None
        return list(syncmerPositions(args, seq, seqLen, seedLen))
    elif isFirstSeq:
        if args.Step > 1:
            return range(random.randrange(args.Step), seqLen, args.Step)
        return range(0, seqLen, args.step)
    else:
        return range(seqLen)

def homologousSeedPositions(args, words, seq1, seq2, seedLen):
    pos1 = seedPositions(args, words, seq1, args.length, seedLen, True)
    pos2 = seedPositions(args, words, seq2, args.length, seedLen, False)
    return None if pos1 is None else sorted(set(pos1) & set(pos2))

def expandedWords(alph, ambi, wordList):
    for word in wordList.split(","):
        p = itertools.product(*(ambi[i] for i in word))
        for i in p:
            yield bytes(map(alph.index, i))

def alphabetReducersFromPatterns(commaSeparatedPatterns):
    r = {"@": bytes(x in "ct" for x in alphabet)}

    for j, bases in ambiguityCodes.items():
        i = j.upper()
        r[i] = bytes(k if x in bases else 255 for k, x in enumerate(alphabet))
        r[j] = bytes(0 if x in bases else 255 for x in alphabet)

    for i, j in "#N", "-n", "1N", "0n":
        r[i] = r[j]

    for p in commaSeparatedPatterns.split(","):
        yield [r[i] for i in p]

def positionsWithSeeds(args, words, seq, seqLen, positions, alphabetReducers):
    for r in alphabetReducers:
        seedLen = len(r)
        pos = positions
        if positions is None:
            pos = seedPositions(args, words, seq, seqLen, seedLen, True)
        for b in pos:
            e = b + seedLen
            if e <= len(seq) and all(i[j] != 255 for i, j in zip(r, seq[b:e])):
                yield b

def seedCodes(args, words, seq, seqLen, positions, alphabetReducers,
              isFirstSeq):
    for r in alphabetReducers:
        seedLen = len(r)
        pos = positions
        if positions is None:
            pos = seedPositions(args, words, seq, seqLen, seedLen, isFirstSeq)
        for b in pos:
            e = b + seedLen
            if e <= len(seq):
                seedCode = bytes(i[j] for i, j in zip(r, seq[b:e]))
                if 255 not in seedCode:
                    yield seedCode

def isAnySeedHit(args, words, seq1, seq2, positions, alphabetReducers):
    for r in alphabetReducers:
        seedLen = len(r)
        pos = positions
        if positions is None:
            pos = homologousSeedPositions(args, words, seq1, seq2, seedLen)
        for b in pos:
            e = b + seedLen
            if e <= len(seq1):
                z = zip(r, seq1[b:e], seq2[b:e])
                if all(i[j] == i[k] != 255 for i, j, k in z):
                    return True
    return False

def main(args):
    logLevel = logging.INFO if args.verbose else logging.WARNING
    logging.basicConfig(format="%(filename)s: %(message)s", level=logLevel)

    print("#", os.path.basename(sys.argv[0]), *sys.argv[1:])
    random.seed(args.random_seed)
    baseFreqs = 100 - args.gc, args.gc, args.gc, 100 - args.gc
    words = None
    if args.words:
        wordList = args.words.lower()
        args.isRyWords = all(i in "ryn," for i in wordList)
        if args.isRyWords:
            eWords = expandedWords(ryAlphabet, ryAmbiguityCodes, wordList)
        else:
            eWords = expandedWords(alphabet, ambiguityCodes, wordList)
        words = tuple(sorted(set(eWords)))
    if args.patterns:
        patterns = args.patterns
    else:
        minSeedLength = max(args.min_seed, args.syn_window)
        seedLengths = range(minSeedLength, args.max_seed + 1)
        patterns = [args.unit * i for i in seedLengths]
        patterns = [i.rstrip("0") for i in patterns]
    reducerLists = [list(alphabetReducersFromPatterns(i)) for i in patterns]

    if (args.distances or args.seqFile) and not args.seqFile2:
        if args.seqFile:
            seq = readOneSequence(args.seqFile)
        else:
            seq = randomSequence(baseFreqs, args.length)
        seqLen = len(seq)
        if args.circular:
            seq *= 2
        p = seedPositions(args, words, seq, seqLen, 0, True)
        print("# dist", "count", "seeds", "length", "pattern", sep="\t")
        for i, x in enumerate(reducerLists):
            q = sorted(set(positionsWithSeeds(args, words, seq, seqLen, p, x)))
            c = collections.Counter(q[j] - q[j - 1] for j in range(1, len(q)))
            for distance, count in sorted(c.items()):
                print(distance, count, len(q), seqLen, patterns[i], sep="\t")
    elif args.pam is None or args.seqFile:
        if args.seqFile:
            seq1 = readOneSequence(args.seqFile)
            seq2 = readOneSequence(args.seqFile2)[::-1]
        else:
            seq1 = randomSequence(baseFreqs, args.length)
            seq2 = randomSequence(baseFreqs, args.length)
        seqLen1 = len(seq1)
        seqLen2 = len(seq2)
        if args.circular:
            seq1 *= 2
            seq2 *= 2
        pos1 = seedPositions(args, words, seq1, seqLen1, 0, True)
        pos2 = seedPositions(args, words, seq2, seqLen2, 0, False)
        print("# num1", "num2", "pairs", "length1", "length2", "pattern",
              sep="\t")
        for i, x in enumerate(reducerLists):
            seeds1 = list(seedCodes(args, words, seq1, seqLen1, pos1, x, 1))
            seeds2 = list(seedCodes(args, words, seq2, seqLen2, pos2, x, 0))
            num1 = len(seeds1)
            num2 = len(seeds2)
            counts1 = collections.Counter(seeds1)
            pairs = sum(counts1[s] for s in seeds2)
            print(num1, num2, pairs, seqLen1, seqLen2, patterns[i], sep="\t")
    else:
        mat = tamura1992substitutionMatrix(args.gc, args.kappa, args.pam)
        hitCounts = [0] * len(reducerLists)
        for trial in range(args.trials):
            for i, x in enumerate(reducerLists):
                seq1, seq2 = randomRelatedSequencePair(baseFreqs, args.length,
                                                       mat)
                if args.circular:
                    seq1 *= 2
                    seq2 *= 2
                pos = homologousSeedPositions(args, words, seq1, seq2, 0)
                hitCounts[i] += isAnySeedHit(args, words, seq1, seq2, pos, x)
        print("# hits", "PAM", "kappa", "gc", "length", "pattern", sep="\t")
        for i, x in enumerate(patterns):
            print(hitCounts[i], args.pam, args.kappa, args.gc, args.length,
                  x, sep="\t")

if __name__ == "__main__":
    usage = "%(prog)s [options] [seqFile [seqFile2]]"
    descr = "Assess alignment seeding methods with simulated DNA sequences."
    ap = argparse.ArgumentParser(usage=usage, description=descr,
                                 formatter_class=
                                 argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument("seqFile", nargs='?', type=argparse.FileType(),
                    help="DNA sequence file, raw or FASTA")
    ap.add_argument("seqFile2", nargs='?', type=argparse.FileType(),
                    help="DNA sequence file, raw or FASTA")

    ap.add_argument("-d", "--distances", action="store_true",
                    help="show distances between seed starts")
    ap.add_argument("-L", "--length", type=int, default=100, metavar="N",
                    help="sequence length")
    ap.add_argument("-p", "--pam", type=float,
                    help="PAM distance between related sequences")
    ap.add_argument("-k", "--kappa", type=float, default=1.0, metavar="K",
                    help="transition/transversion rate ratio")
    ap.add_argument("--gc", type=float, default=50.0, metavar="PERCENT",
                    help="percent G+C")
    ap.add_argument("-t", "--trials", type=int, default=1000, metavar="N",
                    help="number of related sequence pairs")
    ap.add_argument("-c", "--circular", action="store_true",
                    help="simulate circular sequences")
    ap.add_argument("-r", "--random-seed", type=int, metavar="INT",
                    help="pseudorandom generator's seed")
    ap.add_argument("-v", "--verbose", action="count",
                    help="show extra information")

    ag = ap.add_argument_group("seed options")
    ag.add_argument("-m", "--min-seed", type=int, default=5, metavar="L",
                    help="minimum seed length")
    ag.add_argument("-M", "--max-seed", type=int, default=15, metavar="L",
                    help="maximum seed length")
    ag.add_argument("-s", "--step", type=int, default=1, metavar="N",
                    help="use seeds starting every Nth position")
    ag.add_argument("-S", "--Step", type=int, default=1, metavar="N",
                    help="use seeds starting every Nth position "
                    "from a random origin")
    ag.add_argument("-w", "--words", metavar="LIST",
                    help="use seeds starting at these words")
    ag.add_argument("-P", "--patterns", action="append", metavar="LIST",
                    help="seed patterns")
    ag.add_argument("-u", "--unit", default="1",
                    help="pattern = unit * length")

    orderings = "0=alphabetic, 1=cg, 2=att, 3=abb, 4=murmur64"

    ag = ap.add_argument_group("minimizer options")
    ag.add_argument("--min-window", type=int, default=1, metavar="LENGTH",
                    help="minimizer window length")
    ag.add_argument("--min-order", type=int, default=0, metavar="N",
                    help="minimizer order: " + orderings)
    ag.add_argument("--min-type", type=int, default=0, metavar="N",
                    help="minimizer type: 0=interior, 1=mixed, 2=circular")

    ag = ap.add_argument_group("syncmer options")
    ag.add_argument("--syn-window", type=int, default=1, metavar="LENGTH",
                    help="syncmer window length k-s+1")
    ag.add_argument("--syn-order", type=int, default=4, metavar="N",
                    help="syncmer order: " + orderings)
    ag.add_argument("--syn-offset", type=int, metavar="N",
                    help="use open syncmers with this offset t")
    ag.add_argument("--syn-sample", type=int, default=1, metavar="N",
                    help="down-sample syncmers by this factor")

    args = ap.parse_args()
    main(args)
