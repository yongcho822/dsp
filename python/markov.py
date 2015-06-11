#!/usr/bin/env python
import sys
import random
import string

class markov(object):
    
    def __init__(self, filename, gensize):
        self.wordlog = {}
        self.filename = filename
        self.words = self.file_to_words()
        self.size = len(self.words)
        self.gensize = int(gensize)
        self.catalog()

    def file_to_words(self):
        with open(self.filename, "r") as file_opened:
            text = file_opened.read().translate(None, string.punctuation)
            mixedcasewords = text.split()
            words = [x.lower() for x in mixedcasewords]
            return words
        
    def triples(self):
        for i in range((self.size)-2):
            yield (self.words[i], self.words[i+1], self.words[i+2])       
        
    def catalog(self):
        for w1, w2, w3 in self.triples():
            self.wordlog.setdefault((w1, w2), []).append(w3)
        return self.wordlog
                
    def generate(self):
        startseed = random.randint(0, self.size - 2)
        w1, w2 = self.words[startseed], self.words[startseed+1]
        wordlist = [] 
        for i in range(self.gensize):
            wordlist.append(w1)
            w1, w2 = w2, random.choice(self.wordlog[w1, w2])
        wordlist.append(w2)
        
        print " ".join(wordlist) + "."

if __name__ == '__main__':
    if len(sys.argv) > 1:
        alice = markov(sys.argv[1], sys.argv[2]).generate()
        
        
        
#alice = markov("alice.txt", 40).generate()
