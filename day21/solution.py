class LongestPalindromeSubstring:
    def __init__(self, string):
        self.string = string

    def get_local_longest(self, start, end):
        if 0 <= start-1 and end+1 < len(self.string) and self.string[start-1] == self.string[end+1]:
            return self.get_local_longest(start-1, end+1)

        return start, end

    def get(self):
        max_start = 0
        max_end = 0

        # find longest palindromes of odd length
        for index in range(len(self.string)):
            start, end = self.get_local_longest(index, index)
            if (end - start) > (max_end - max_start):
                max_start, max_end = start, end

        # find longest palindromes of even length
        for index in range(len(self.string)):
            if ((index + 1) == len(self.string)) or (self.string[index] != self.string[index + 1]):
                continue

            start, end = self.get_local_longest(index, index+1)
            if (end - start) > (max_end - max_start):
                max_start, max_end = start, end

        return self.string[max_start:max_end+1]
