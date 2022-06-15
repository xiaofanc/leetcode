def Trie(words):
    word_key = "$"

    trie = {}
    for word in words:
        node = trie
        for letter in word:
            # if letter not in the dictionary, return default {}
            node = node.setdefault(letter, {})
        # mark the existence of a word in trie node
        node[word_key] = word
        print("node", node)
    print(trie)
    return trie

print(Trie(["a", "abc", "acf"]))