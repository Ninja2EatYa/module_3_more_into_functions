def single_root_words(root_word, *other_words):
    same_words = []
    root_word = str(root_word).lower()
    for word in other_words:
        word = str(word).lower()
        if word in root_word:
            same_words.append(word)
        elif root_word in word:
            same_words.append(word)
    print(same_words)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
