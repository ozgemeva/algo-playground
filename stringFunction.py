from collections import Counter

class StringFunction:

    def first_repeated_char(self, s):
        seen = set()
        repeated = set()
        for char in s:
            if char in seen:
                repeated.add(char)
            else:
                seen.add(char)
        print("seen: ", seen, "repeated: ", repeated)
        return None

    def char_frequency_map(self, word):
        freq = {}
        for char in word:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return freq

    def first_non_repeating(self, word):
        word = word.lower()
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
            print("freq[char]", freq[char])
        for char in word:
            if freq[char] == 1:
                return char
        return None

    def most_frequent(self, word):
        word = word.lower()
        word_dict = {}
        for char in word:
            word_dict[char] = word_dict.get(char, 0) + 1
        print(word_dict)
        maxValue = max(word_dict.values(), default=0)
        for char in word:
            if word_dict[char] == maxValue:
                return char
        return None

    def is_anagram(self, str1, str2):
        str1 = str1.lower().replace(" ", "")
        str2 = str2.lower().replace(" ", "")
        str1_counter = Counter(str1)
        str2_counter = Counter(str2)

        print("str1_counter:", str1_counter)
        print("str2_counter:", str2_counter)

        return str1_counter == str2_counter
