def all_anagrams(words):
    usporadana_slova = []
    if len(words) == 0:
        return False
    for i in words:
        usporadana_slova.append(sorted(i))




