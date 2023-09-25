## taeyang's template (1.0.7)
# https://hooongs.tistory.com/311
# https://rccode.tistory.com/m/271
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
# from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################


class TrieNode:
    def __init__(self, count = 0):
        self.children = {}
        self.is_end_of_word = False
        self.count = count


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end_of_word = True


    def dfs_for_counting(self, node, count):
        if node.count == 1:
            return count
        
        # node.is_end_of_word가 True일 경우 한 단어라는 뜻이다.
        res = 0
        if node.is_end_of_word:
            res += count
            
        for nxt_node in node.children.values():
            # 현재 노드 count와 다음 노드 count가 다르다면 입력가능한 다른문자가 있다는 뜻이다.
            if node.count == nxt_node.count:
                nxt_count = count
            else:
                nxt_count = count + 1
            res += self.dfs_for_counting(nxt_node, nxt_count)
            
        return res


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    try:
        while True:
            # input
            n = int(input())
            trie = Trie()
            for _ in range(n):
                trie.insert(input().strip())
            
            # dfs
            cnt = trie.dfs_for_counting(trie.root, 0)
            
            # output
            print(f'{round(cnt/n, 2):.2f}')
    except:
        exit(0)