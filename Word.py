class Word:
    """
    A class to contain a word, and the word in hidden form

    Attributes
    ----------
    word : str
        The word or phrase
    hidden_word : list
        list hiding the unrevealed letters of the word

    Methods
    -------
    check_letter(self, letter)
        Checks if a letter is in the word
    check_word(self, word)
        Checks if the word matches the actual word
    update_hidden_letter(self, guess_letter)
        Reveal letters in hidden_word
    update_hidden_word(self, guess_word)
        Reveal word in hidden_word
    """
    def __init__(self, word):
        """
        Construct the word and hidden format of the word

        :param word: Given word
        :type word: str
        """
        self.word = word.lower()
        self.hidden_word = ["_" if x.isalpha() else x for x in word]

    def check_letter(self, letter):
        """
        Checks if a letter is in the word

        :param letter: Letter to check with word
        :type letter: str
        :return: Boolean value if letter if in word
        :rtype: Boolean
        """
        if letter.lower() in self.word:
            return True
        return False

    def check_word(self, word):
        """
        Checks if the word matches the actual word

        :param word: Word to check with actual word
        :type word: str
        :return: Boolean value if word matches actual word
        :rtype: Boolean
        """
        if self.word == word.lower():
            return True
        return False

    def update_hidden_letter(self, guess_letter):
        """
        Reveal letters in hidden_word

        :param guess_letter: Letter to reveal in hidden_word
        :type guess_letter: str
        """
        old_ind = 0
        for letter in self.word:
            if letter == guess_letter.lower():
                new_ind = self.word.find(letter, old_ind)
                self.hidden_word[new_ind] = letter
                old_ind = new_ind+1

    def update_hidden_word(self, guess_word):
        """
        Reveal word in hidden_word

        :param guess_word: word to reveal in hidden_word
        :type guess_word: str
        """
        count = 0
        for letter in guess_word.lower():
            self.hidden_word[count] = letter
            count += 1

    def display_word(self):
        return self.word

    def display_hidden_word(self):
        return "".join(self.hidden_word)
