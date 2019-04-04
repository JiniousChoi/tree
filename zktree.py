#!/usr/bin/python3

from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

class ZNode:
    def __init__(self, path, name, val=None):
        self.path = path
        self.name = name
        self.val = val
        self.children = []

def make_zktree(path = '/'):
    data, stat = zk.get(path)
    name = path.rsplit('/', 2)[-2]
    n = ZNode(path, name, data.decode('utf8') if data else 'null')
    for child in zk.get_children(path):
        c = make_zktree(path + child + '/')
        n.children.append(c)
    return n

def print_zktree(n, header = []):
    if not n:
        return
    print("{}{} ({})".format(''.join(header), n.name, n.val))
    transform_parent(header)
    for c in n.children:
        if c == n.children[-1]:
            header.append('└── ')
            print_zktree(c, header)
            header.pop(-1)
        else:
            header.append('├── ')
            print_zktree(c, header)
            header.pop(-1)

def transform_parent(header):
    if not header:
        return
    if header[-1] == '└── ':
        header[-1] = '    '
    elif header[-1] == '├── ':
        header[-1] = '│   '

def main():
    zktree = make_zktree()
    zktree.name = '/'
    print_zktree(zktree)
