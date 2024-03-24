class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, list):
        word_letters = [letter for letter in self.word]
        found_word = []
        for word in list:
            letters = [letter for letter in word]
            if (sorted(word_letters) == sorted(letters)):
                found_word.append(word)
        return found_word