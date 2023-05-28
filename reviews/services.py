def kmp_search(word, text):
    m = len(word)
    n = len(text)
    lps = [0] * m  # Создаем массив длин префиксов и суффиксов

    # Строим массив lps
    j = 0
    i = 1
    while i < m:
        if word[i].lower() == word[j].lower():
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    # Используем алгоритм КМП для поиска совпадения слова в тексте
    i = j = 0
    while i < n:
        if word[j].lower() == text[i].lower():
            i += 1
            j += 1
            if j == m:
                return True  # Найдено совпадение слова в тексте
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False  # Совпадение слова не найдено
