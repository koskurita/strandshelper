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
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium import webdriver

_STRANDS_URL = "https://www.nytimes.com/games/strands"

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

class StrandsMatrix:
    def __init__(self):
        self.x = 0
        self.y = 0
        self._rowSize = 6
        self._columnSize = 8
        self.charMatrix = [["a" for x in range(self._rowSize)] for y in range(self._columnSize)] 
        self.visitedMatrix = [[False for x in range(self._rowSize)] for y in range(self._columnSize)] 


    def scrape(self):
        letter_list = []
        _url = _STRANDS_URL 
        driver = webdriver.Firefox()
        driver.get(_url)
        sleep(3)
        source = driver.page_source
        soup = BeautifulSoup(source, 'lxml')
        letters = soup.find_all('button', class_= "pRjvKq_item")
        for letter in letters:
            letter_list.append(letter.get_text().lower())
        self.createMatrix(letter_list)
        return 

    def createMatrix(self, letter_list):
        cnt = 0
        for i in range(self._columnSize):
            for j in range(self._rowSize):
                self.charMatrix[i][j] = letter_list[cnt]
                cnt += 1
        return 

    def solveMatrix(self, x, y, trie, word, possible_words, path, completepath):
        if self.charMatrix[y][x] not in trie.children:
            return
        word.append(self.charMatrix[y][x])
        path.append([x,y])
        next_trie = trie.children[self.charMatrix[y][x]]
        self.visitedMatrix[y][x] = True
        if next_trie.is_end_of_word:
            possible_words.append(''.join(word))
            completepath.append(path.copy())
            # print(completepath)
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        for i in range(len(dx)):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if self.check_boundaries(next_x, next_y):
                if not self.visitedMatrix[next_y][next_x]:
                    self.solveMatrix(next_x, next_y, next_trie, word, possible_words, path, completepath)
        self.visitedMatrix[y][x] = False
        del word[-1]
        del path[-1]

    def check_boundaries(self, x, y):
        return x >= 0 and x < self._rowSize and y >= 0 and y < self._columnSize
            



d_trie = Trie()
d_trie.parse_dict_to_Tree("new_dictionary.txt", "dictionary.json")
# d_trie.load_JSON("dictionary.json")
# # d_trie.to_JSON("newj.json")


m = StrandsMatrix()
m.scrape()

s = []
words = []
path = []
completepath = []
for i in range(8):
    for j in range(6):
        m.solveMatrix(j, i, d_trie.root, s, words, path, completepath)

# print(completepath)

# with open("res.txt", "w") as f:
#     for i in range(len(words)):
#         s = ''.join('[{},{}]'.format(x[0],x[1]) for x in completepath[i])
#         f.write(words[i] + s + "\n")



wordsetdic = []
for i in range(len(words)):
    wordset = set()
    for tup in completepath[i]:
        wordset.add(tuple(tup))
    wordsetdic.append([words[i], wordset])

def solve(wordsetdic, totalset, start, potentialsolve, solved):
    if len(totalset) == 48:
        solved.append(potentialsolve.copy())
        return
    for i in range(start, len(wordsetdic)):
        if totalset.isdisjoint(wordsetdic[i][1]):
            potentialsolve.append(wordsetdic[i])
            solve(wordsetdic, totalset.union(wordsetdic[i][1]), i, potentialsolve, solved)
            del potentialsolve[-1]

totalset = set()
potentialsolve = []
solved = []
solve(wordsetdic, totalset, 0, potentialsolve, solved)
print(solved)

with open("solved.txt", "w") as f:
    for ans in solved:
        f.write(f"{ans}\n")



