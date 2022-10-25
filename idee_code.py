 def convert_words_to_leet(words):
        words_in_leet = []
        for word in words:
            characters_in_leet = []
            for char in word:
                if(char in ["a", "A"]):
                    characters_in_leet.append('4')
                elif(char in ["b", "B"]):
                    characters_in_leet.append('8')
                elif(char in ["e", "E"]):
                    characters_in_leet.append('3')
                elif(char in ["i", "I"]):
                    characters_in_leet.append('1')
                elif(char in ["o", "O"]):
                    characters_in_leet.append('0')
                elif(char in ["s", "S"]):
                    characters_in_leet.append('5')
                elif(char in ["z", "Z"]):
                    characters_in_leet.append('2')
                elif(char in ["t", "T"]):
                    characters_in_leet.append('7')
                elif(char in ["g", "G"]):
                    characters_in_leet.append('6')
                elif(char in ["l", "L"]):
                    characters_in_leet.append('1')
            words_in_leet.append("".join(characters_in_leet))
        return words_in_leet