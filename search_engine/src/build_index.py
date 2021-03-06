# encoding=utf8

import re
import math
from collections import defaultdict

class BuildIndex:

    def __init__(self, text):
        self.text = text
        self.text_to_terms = self.process_text()        
        self.index = self.reg_index()

    def process_text(self):
        text_to_terms = ''  
        pattern = re.compile('[\W_]+')
        text_to_terms = self.text.lower();
        text_to_terms = pattern.sub(' ', text_to_terms)
        text_to_terms = text_to_terms.split()
        return text_to_terms


    def index_text(self, termlist):
        text_index = defaultdict(list)
        for index, word in enumerate(termlist):
            text_index[word].append(index)
        return text_index

    def make_indices(self, termlist):
        return self.index_text(termlist)

    def reg_index(self):
        return self.make_indices(self.text_to_terms)

    def get_index(self):
        return self.index

    def get_number_of_words(self):
        return len(self.text_to_terms)
