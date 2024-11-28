#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self._value = value
        else:
            self._value = ''
            print("The value must be a string.")  # Print error message if value is not a string

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")  # Print error message when trying to set a non-string

    def is_sentence(self):
        """Returns True if the string ends with a period."""
        return self._value.endswith('.')
    
    def is_question(self):
        """Returns True if the string ends with a question mark."""
        return self._value.endswith('?')
    
    def is_exclamation(self):
        """Returns True if the string ends with an exclamation mark."""
        return self._value.endswith('!')
    
    def count_sentences(self):
        """Returns the number of sentences in the string."""
        # Use regex to split by sentence-ending punctuation: ., !, or ?
        sentences = re.split(r'[.!?]+', self._value.strip())
        # Remove empty strings and return the count of non-empty sentences
        return len([sentence for sentence in sentences if sentence])

