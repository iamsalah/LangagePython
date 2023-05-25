class LanguageDetector:

    def __init__(self):

        self.english_letter_freq = {'e': 12.02, 't': 9.10, 'a': 8.12, 'o': 7.68, 'i': 7.31, 'n': 6.95, 's': 6.28, 'r': 6.02,
                                    'h': 5.92, 'd': 4.32, 'l': 3.98, 'u': 2.88, 'c': 2.71, 'm': 2.61, 'f': 2.30, 'y': 2.11,
                                    'w': 2.09, 'g': 2.03, 'p': 1.82, 'b': 1.49, 'v': 1.11, 'k': 0.69, 'x': 0.17, 'q': 0.11,
                                    'j': 0.10, 'z': 0.07}
        self.french_letter_freq = {'e': 14.71, 'a': 8.11, 's': 7.79, 'i': 7.24, 't': 7.20, 'n': 7.15, 'r': 6.65, 'u': 6.36,
                                   'l': 5.98, 'o': 5.87, 'd': 3.67, 'c': 3.24, 'p': 3.02, 'm': 2.96, 'v': 1.94, 'q': 1.84,
                                   'b': 1.42, 'g': 1.16, 'f': 1.11, 'h': 0.99, 'j': 0.83, 'x': 0.42, 'y': 0.32, 'z': 0.15,
                                   'k': 0.07, 'w': 0.06}
        self.spanish_letter_freq = {'a': 11.96, 'e': 11.38, 'o': 8.69, 's': 7.88, 'n': 6.83, 'r': 6.41, 'i': 5.28, 'l': 4.97,
                                    'u': 4.96, 't': 4.61, 'd': 4.53, 'c': 4.15, 'p': 2.89, 'm': 2.88, 'y': 1.74, 'q': 1.53,
                                    'b': 1.49, 'h': 1.18, 'g': 1.01, 'f': 0.69, 'v': 0.68, 'j': 0.52, 'ñ': 0.31, 'x': 0.19,
                                    'z': 0.08, 'k': 0.07, 'w': 0.01}



    def calculate_letter_frequency(self, text):
        letter_freq = {}
        text = text.lower()
        for char in text:
            if char.isalpha():
                if char in letter_freq:
                    letter_freq[char] += 1
                else:
                    letter_freq[char] = 1
        total_letters = sum(letter_freq.values())
        letter_freq = {char: (count / total_letters * 100) for char, count in letter_freq.items()}
        return letter_freq

    def compare_letter_frequency(self, freq1, freq2):
        error_margin = 1  # Adjust this value for tolerance
        for char, freq in freq1.items():
            if char in freq2:
                if abs(freq - freq2[char]) > error_margin:
                    return False
            else:
                return False
        return True

    def detect_language(self, text):
        letter_freq = self.calculate_letter_frequency(text)

        if self.compare_letter_frequency(letter_freq, self.english_letter_freq):
            return "English"
        elif self.compare_letter_frequency(letter_freq, self.french_letter_freq):
            return "French"
        elif self.compare_letter_frequency(letter_freq, self.spanish_letter_freq):
            return "Spanish"
        else:
            return "Unknown"
