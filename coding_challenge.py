def check_duplicates(string):
    word_list = string.split()
    word_counter = -1

    for word in word_list:
        word_counter += 1
        letters_list = []
        for letters in word:
            if letters.lower() not in letters_list:
                letters_list.append(letters.lower())
            else:
                return (f'The word: {word_list[word_counter]} has duplicate letters')
            
        




#print (check_duplicates("Hello world"))
print(check_duplicates("Lasse Stian Mariurs"))