https://www.hackerrank.com/challenges/ctci-ransom-note/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def createNote(note):
    # note=note.split(' ')
    noteDict={}
    for word in note:
        noteDict[word]=noteDict.get(word,0)+1
    return noteDict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    #magazine and note are strings.
    #Create a list of magazine.done
    #Create a dict of note.key is the word. value is the            frequency.done
    #Iterate through the magazine list. If note empty then         #return true. If magazine list empty and note not empty;       #Return false.O(magazine) 
    # magazine=magazine.split(' ')
    note=createNote(note)
    for x in magazine:
        if x in note.keys():
            if note[x]>0:
                note[x]=note.get(x)-1
            elif note[x]<1:
                note.pop(x)
    for x in note:
        if note[x]!=0:
            print("No")
            return
    print("Yes")
    return










    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
