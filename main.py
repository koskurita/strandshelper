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
        self.is_end_of_word = False
        self.children = {}
    
    def print_subtree(self):
        print(self.letter, end="")
        if self.is_end_of_word:
            print("*", end="")
        for key, values in self.children.items():
            values.print_subtree()
    
    # def load_JSON(self):

        

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

    def to_JSON(self, fijs):
        curr_node = self.root
        with open(fijs, "w") as f:
            json.dump(self, f, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)
        return

    def load_JSON(self, fijs):
        curr_node = self.root
        with open(fijs) as f:
            node_data = json.load(f)
            cock = node_data["root"]["children"]
            self.bfs(curr_node, cock)

    def bfs(self, cur_node, nodedic):
        for i, j in nodedic.items():
            pp = j["letter"]
            newNode = TrieNode(j["letter"])
            newNode.is_end_of_word = j["is_end_of_word"]
            cur_node.children[j["letter"]] = newNode
            self.bfs(newNode, j["children"])

    # only takes words of length 4 > and writes it into a new file
    def convert_dict(self, fulldic, newdic):
        words_list = []
        with open(fulldic) as f:
            for word in f:
                if len(word) > 4:
                    words_list.append(word)
        with open(newdic, "w") as f:
            for word in words_list:
                f.write(word)
    
    # takes in file, creates a tree
    def parse_dict_to_Tree(self, fidic, fijs):
        with open(fidic) as f:
            for word in f:
                word = word.strip()
                self.add_word(word)
        self.to_JSON(fijs)





d_trie = Trie()
d_trie.parse_dict_to_Tree("new_dictionary.txt", "dictionary.json")




# new_tree = Trie()
# new_tree.load_JSON()
# print("\n")
# new_tree.print_trie()
# print("\n")


# s = d_trie.to_JSON()




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