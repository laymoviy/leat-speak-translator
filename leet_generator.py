class LeetSpeakGenerator:
    def __init__(self):
        self.english_dict = {
            'a': '4', 'A': '4',
            'e': '3', 'E': '3',
            'i': '1', 'I': '1',
            'o': '0', 'O': '0',
            's': '5', 'S': '5',
            't': '7', 'T': '7',
            'l': '1', 'L': '1',
            'g': '9', 'G': '9',
            'b': '8', 'B': '8',
            'z': '2', 'Z': '2'
        }
        
        self.russian_dict = {
            'а': '4', 'А': '4',
            'е': '3', 'Е': '3',
            'и': '1', 'И': '1',
            'о': '0', 'О': '0',
            'с': '5', 'С': '5',
            'т': '7', 'Т': '7',
            'л': '1', 'Л': '1',
            'г': '9', 'Г': '9',
            'в': '8', 'В': '8',
            'з': '2', 'З': '2',
            'ё': '3', 'Ё': '3',
            'ч': '4', 'Ч': '4',
            'ш': '6', 'Ш': '6',
            'щ': '6', 'Щ': '6'
        }
    
    def convert_to_leet(self, text):
        result = ""
        for char in text:
            if char in self.english_dict:
                result += self.english_dict[char]
            elif char in self.russian_dict:
                result += self.russian_dict[char]
            else:
                result += char
        return result
