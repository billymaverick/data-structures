"""Trie data structure"""

class Node(object):

    def __init__(self):
        self.edges = {}
        self.word = None

    def __getitem__(self, key):
        return self.edges[key]

    def __setitem__(self, key, value):
        self.edges[key] = value

    # TODO use __contains__ here?
    def __iter__(self):
        return self.edges.iterkeys()

    def __str__(self):
        edges = ' '.join([e for e in self.edges])
        return 'Node(edges: {}, word: {})'.format(edges, self.word)

class Trie(object):

    def __init__(self, strings=[]):
        self.root = Node()
        for string in strings:
            self.insert(string)

    def insert(self, string):
        node = self.root
        for char in string:
            if char not in node:
                node[char] = Node()
            node = node[char]
        node.word = string

    def find(self, string):
        """Return node for last letter in string"""
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        return node

    def has(self, string):
        """Return true if word is in trie"""
        node = self.find(string)
        if not node or not node.word:
            return False
        return True

    def remove(self, string):
        """Remove given string from trie"""
        raise NotImplementedError()

    def words_below(self, substring):
        """Find and return all words below substring"""
        start = self.find(substring)
        stack = [start] if start else []
        words = []
        while stack:
            node = stack.pop()
            if node.word:
                words.append(node.word)
            for edge in node:
                stack.append(node[edge])
        return words

    def __str__(self):
        pass
