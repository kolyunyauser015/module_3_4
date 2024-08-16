def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
    return same_words


print(single_root_words('работ', 'работа', 'среда', 'РАБОТАТЬ', 'прибрать', 'работник'))
