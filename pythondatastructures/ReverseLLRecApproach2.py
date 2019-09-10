#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 08:37:23 2019

@author: balasubramanian
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseRecursive(head):
    #  Given a linked list, reverse it recursively.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if head is None or head.next is None:
        return head,head
    smallHead, smallTail = reverseRecursive(head.next)
    smallTail.next = head
    head.next = None
    return smallHead,head
    

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l,r = reverseRecursive(l)
printll(l)