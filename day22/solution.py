class PhoneKeypad:
    key_char_mapper = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def __init__(self, pressed_keys):
        self.pressed_keys = pressed_keys

    def get_combinations(self, digits=None, combination=""):
        combinations = []

        if digits is None:
            digits = self.pressed_keys

        if len(digits) == 0 and len(combination) != 0:
            combinations.append(combination)
        else:
            for char in self.key_char_mapper[digits[0]]:
                combinations += self.get_combinations(digits[1:], combination+char)

        return combinations
