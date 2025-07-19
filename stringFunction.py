class StringFunction:

    def first_repeated_char(s):
        seen = set()
        repeated = set()
        for char in s:
            if char in seen:
                repeated.add(char)
            else:
                seen.add(char)
        print("seen: ", seen, "repeated: ", repeated)
        return None

    def char_frequency_map(word):
        freq = {}
        for char in word:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return freq

    def first_non_repeating(word):
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
            print("freq[char]", freq[char])
        for char in word:
            if freq[char] == 1:
                return char
        return None
