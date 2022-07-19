def check_duplicates(string):
    word_list = string.split()
    word_counter = -1
    duplicated_words_list = []

    for word in word_list:
        word_counter += 1
        letters_list = []
        for letters in word:
            if letters.lower() not in letters_list:
                letters_list.append(letters.lower())
            else:
                duplicated_words_list.append(word_list[word_counter])
    if len(duplicated_words_list) != 0:
        return [x for x in duplicated_words_list]
    else:
        return False
            
        




#print (check_duplicates("Hello world"))
print(check_duplicates("Lase Stian Marius"))