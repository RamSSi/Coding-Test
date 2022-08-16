# 5397 : 키로거
from email import header
import sys
import re

class Node:

    def __init__(self, data, prev = None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

head = Node(None, None, None)

def addHead(data):
    node = Node(data, None, head)
    head = node
    return node

def add(data, pNode, nNode):
    node = Node(data, pNode, nNode)
    pNode.next = node
    nNode.prev = node
    return node
    

# L = int(input())

cases = [sys.stdin.readline().strip() for _ in range(1)]

for case in cases:
    head = Node(None, None, None)
    curr = head
    for ch in range(len(case)):
        if case[ch] == '<':
            print("<")
            if curr.prev != None:
                curr = curr.prev
        elif case[ch] == '>':
            print(">")
            if curr.next != None:
                curr = curr.next
        elif case[ch] == '-':
            print("-")
            if curr.prev != None and curr.next != None:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
        else:
            print("문자")
            if curr.data == None :
                curr.next = Node(case[ch], curr, None)
                curr = curr
            else:
                if curr.next != None:
                    a = Node(case[ch], curr, curr.next)
                    curr.next.prev = a
                    curr.next = a
                    curr = a
                else:
                    a = Node(case[ch], curr, None)
                    curr.next = a
                    curr = a
        print(curr.data, curr.prev, curr.next)

    while head.next:
        print(head.data, end='')
        head = head.next
