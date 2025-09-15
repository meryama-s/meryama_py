def dict_word():
    word= input("enter a word:")
    letters={}
    for index, lett in enumerate(word):
        if lett not in letters :
            letters[lett]=[]
            letters[lett].append(index)
    return letters
result = dict_word()
print(result)