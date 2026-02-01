import sys

input = sys.stdin.readline

A = int(input())

if A % 4 == 1 or A % 4 == 0: print("goose")
else: print("duck")