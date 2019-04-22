#!/bin/python

import math
import os
import random
import re
import sys

## Hackerrank - Strings: Making Anagrams

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    seen = {}
    count = 0

    for ch in a:
        if ch in seen:
            seen[ch] += 1
        else:
            seen[ch] = 1
    
    # This next loop detemines the length of the anagram
    for ch in b:
        if ch in seen:
            if seen[ch] > 0:
                seen[ch] -= 1
                count += 1
    
    return len(a) - count + len(b) - count

