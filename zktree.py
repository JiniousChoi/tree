#!/usr/bin/python3

from tree import Tree, Deco
from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

class Node:
    def __init__(self, path, name, val=None):
        self.path = path
        self.name = name
        self.val = val

def traverse(path, name, dstack=[]):
    data, stat = zk.get(path)
    n = Node(path, name, data.decode('utf8') if data else 'null')
    yield (dstack, n)
    children = zk.get_children(path)
    if not children:
        return

    for cname in children[:-1]:
        dstack.append(Deco.MID)
        yield from traverse(path + cname + '/', cname, dstack)
        dstack.pop(-1)

    cname = children[-1]
    dstack.append(Deco.END)
    yield from traverse(path + cname + '/', cname, dstack)
    dstack.pop(-1)

def print_node(n):
    print("{} ({})".format(n.name, n.val))

def main():
    traversor = traverse('/', '/')
    Tree(traversor, print_node).print()

main()
