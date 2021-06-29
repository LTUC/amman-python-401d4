import nltk
nltk.download('words')

word_list = nltk.corpus.words.words()
# print(word_list[:100])

def count_english_words(sentence):
    words = sentence.split()
    count = 0
    for word in words:
        if word.lower() in word_list or word in word_list:
            count+=1
    return count

def detect_most_english_sentence(sentence):
    # Iterate over all 26 sentences
    # cont how many english words in each sentence using count_english_words function above
    # return the sentence with most English
    pass

def crack(encrypted_sentence):
    pass

if __name__ == '__main__':
    sentences = [
        'My fdrr jy higgg jhj my gghha yhggt jkkkrrf',
        'gh yuhj df vbnmg fgh fg rtyuk vbnme dfghjke',
        'My name is John and gu kjkjk hello welcome'
    ]

    print(count_english_words(sentences[2]))





"""
Code Challenge:

class Node:
    pass

class KArrTree:
    def __init__(self):
        self.root = None

def fizz_buzz_tree(k_ary_tree):
    # Logic for bfs of k_ary_tree
    pass
"""
