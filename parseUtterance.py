#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import itertools

utterance = "Alexa, set (_|my|the) {target} (_|light|lights|lamp|lamps) to {#} percent (_|please)"
utterance2 = "Alexa, finde meine Smart-Home-Geräte"

def convertTuple(tup): 
    conv =  ''.join(tup) 
    return conv

def convertPermutated(permutated):
    utterances = []
    for sentence in permutated:
        converted = convertTuple(sentence)
        # FORMATTING
        # converted = converted.replace("_", "")
        # converted = converted.replace("  ", " ")
        converted = converted.replace(" _", "")
        converted = converted.replace("_ ", "")
        # print(converted)
        utterances.append(converted)
    return utterances

def parseUtterance(utterance): #returns a list of strings
    #split string
    splits = re.split("[()]", utterance)

    #for loop to iterate over words array
    for i,split in enumerate(splits):
        splits.remove(split)
        if '|' in split:
            splits.insert(i,split.split('|'))
        else:
            splits.insert(i,[split])

    # using itertools.product()   
    # to compute all possible permutations 
    permutated = list(itertools.product(*splits)) 
    # converting tuples returned by itertools to string
    utterances = convertPermutated(permutated)
    return utterances

def test(utterance):
    utterances = parseUtterance(utterance)
    for utterance in utterances:
        print(utterance)

# test(utterance2)