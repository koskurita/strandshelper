# Trie implementation 1: no nodes
# class Trie:
#     def __init__(self):
#         self.root = {"*": *}


#     # add word into the Trie
#     def add_word(self, word):
#         curr_node = self.root
#         for letter in word:
#             if letter not in curr_node:
#                 curr_node[letter] = {}
#             curr_node = curr_node[letter]
#         curr_node["*"] = "*"

#     def does_word_exist(self, word):
#         curr_node = self.root
#         for letter in word:
#             if letter not in curr_node:
#                 return False
#             curr_node = curr_node[letter]
#         return "*" in curr_node

# Trie implementation 2: nodes

import json

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False
    
    def print_subtree(self):
        print(self.letter)
        if self.is_end_of_word:
            print("*")
        for key, values in self.children.items():
            values.print_subtree()
    
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

        

class Trie:
    def __init__(self):
        self.root = TrieNode("*")
    
    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode(letter)
            curr_node = curr_node.children[letter]
        curr_node.is_end_of_word = True
    
    def does_word_exist (self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.is_end_of_word
    
    def print_trie(self):
        curr_node = self.root
        for key, values in curr_node.children.items():
            values.print_subtree()

    def to_JSON(self):
        s = ""
        curr_node = self.root
        for key, values in curr_node.children.items():
            s += values.to_JSON() 
        return s
    
    def save_dictionary(self):
        s = self.to_JSON()
        filename = input("dictionary.txt")
        with open(filename, "w") as f:
        f.write(input())



words_list = ["tree", "trie", "tried", "trope", "trouble", "alive", "alone", "love", "afraid", "lonely", "memory", "membrane"]

d_trie = Trie()
for word in words_list:
    d_trie.add_word(word)

s = d_trie.to_JSON()



# d_trie.print_trie()


# with open("dictionary.json", "w") as f:
#     json.dump(d_trie, f)






# _rowSize = 6
# _columnSize = 8

# charMatrix = [["a" for x in range(_rowSize)] for y in range(_columnSize)] 
# visitedMatrix = [[False for x in range(_rowSize)] for y in range(_columnSize)] 

# cnt = 0
# for i in range(_columnSize):
#     for j in range(_rowSize):
#         charMatrix[i][j] = chr(cnt+ord("a"))
#         cnt+=1
#         if cnt >= 26:
#             cnt = 0
#         print(i, j, cnt)
# print(charMatrix)

# def backtrack(x, y, trie, word, possible_words):
#     print("hi")