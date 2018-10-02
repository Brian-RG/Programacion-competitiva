# -*- coding: utf-8 -*-
"""
http://codeforces.com/problemset/problem/849/A

Given an integer sequence a1, a2, ..., an of length n. Decide whether it is possible to divide it into an odd number of non-empty subsegments, the each of which has an odd length and begins and ends with odd numbers.

A subsegment is a contiguous slice of the whole sequence. For example, {3, 4, 5} and {1} are subsegments of sequence {1, 2, 3, 4, 5, 6}, while {1, 2, 4} and {7} are not.

Input
The first line of input contains a non-negative integer n (1 ≤ n ≤ 100) — the length of the sequence.

The second line contains n space-separated non-negative integers a1, a2, ..., an (0 ≤ ai ≤ 100) — the elements of the sequence.

Output
Output "Yes" if it's possible to fulfill the requirements, and "No" otherwise.

You can output each letter in any case (upper or lower).

Created on Mon Sep 24 19:47:53 2018
@author: brian

"""

a=int(input())
b=list(map(int,input().split(" ")))
ans="Yes" if a%2 and b[0]%2 and b[-1]%2 else "No"
print(ans)