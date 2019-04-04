#!/usr/bin/python3

from collections import namedtuple
from enum import Enum

class PIPES(Enum):
    MID = '├── '
    END = '└── '
    CONT = '│   '
    EMPTY = '    '

class Tree:
    def __init__(self, decos, traverser, print_node):
        self.decos = decos
        self.traverser = traverser
        self.print_node = print_node

    def print(self):
        for (dstack, node) in self.traverser:
            self._print_decos(dstack)
            self.print_node(node)

    def _print_decos(self, dstack):
        if not dstack:
            return
        for d in dstack[:-1]:
            if d == self.decos.END:
                print(self.decos.EMPTY.value, end='')
            elif d == self.decos.MID:
                print(self.decos.CONT.value, end='')
            else:
                print(d, end='')
        print(dstack[-1].value, end='')
