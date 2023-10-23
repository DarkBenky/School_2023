import string 

def Print_Plus(word : str):
    """
    just print for string
    :param word: string
    returns: None
    """
    word_to_write = []
    letters  = " " + string.digits + string.ascii_letters + string.punctuation + string.whitespace
    for i in range(len(word)):
        for letter in letters:
            if word[i] == letter:
                word_to_write.append(letter)
    print("".join(word_to_write))

Print_Plus("Hello World")