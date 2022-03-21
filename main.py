def all_anagrams(words):
    usporadana_slova = []
    if len(words) == 0:
        return False
    for i in words:
        if type(i) != str:
            return False
        else:
            usporadana_slova.append(sorted(i))
    for i in range(len(usporadana_slova)):
        if usporadana_slova[i] in usporadana_slova[i:]:
            return True

print(all_anagrams(['ship', 'hips', 'name']))

