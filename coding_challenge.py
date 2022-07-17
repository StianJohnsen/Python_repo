def check_duplicates(string):
    word_list = string.split()
    print (word_list)

    for word in word_list:
        for letters in word:
            print (letters)
        




#print (check_duplicates("Hello world"))
check_duplicates("Hello world")