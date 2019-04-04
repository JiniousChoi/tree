#!/usr/bin/python3

import unittest
from tree import Tree, DECOS
ASTERISKS = DECOS('* ', '* ', '* ', '* ')

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

def make_simple_node():
    root = Node('/')
    dir1 = Node('dir1')
    dir2 = Node('dir2')
    root.children = [dir1, dir2]
    return root

def make_complex_node():
    root = Node('/')
    dir1 = Node('dir1')
    dir2 = Node('dir2')
    dir3 = Node('dir3')
    dir4 = Node('dir4')
    file5 = Node('file5')
    dir1.children = [dir2, dir3, dir4]
    dir2.children = [file5]
    root.children = [dir1, dir1]
    return root

def traverse(node, dstack=[]):
    if not node:
        return

    yield (dstack, node)

    if not node.children:
        return

    for child in node.children[:-1]:
        dstack.append(ASTERISKS.MID)
        yield from traverse(child, dstack)
        dstack.pop(-1)

    last_child = node.children[-1]
    dstack.append(ASTERISKS.END)
    yield from traverse(last_child, dstack)
    dstack.pop(-1)

def print_node(node):
    print(node.name)
    
class TreeTest(unittest.TestCase):
    def test_asterisk_simple(self):
        print(" --- tree with asterisks simple ---")
        root = make_simple_node()
        tree = Tree(ASTERISKS, traverse(root), print_node)
        tree.print()

    def test_asterisk_complex(self):
        print(" --- tree with asterisks complex ---")
        root = make_complex_node()
        tree = Tree(ASTERISKS, traverse(root), print_node)
        tree.print()


unittest.main()
