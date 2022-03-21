def all_anagrams(words):
    usporadana_slova = []
    if len(words) == 0:
        return False
    for i in words:
        if type(i) != str:
            return False
        else:
            usporadana_slova.append(sorted(i.lower()))
    if len(usporadana_slova) == usporadana_slova.count(usporadana_slova[0]):
        return True
    else:
        return False


print(all_anagrams(["Hist","This","Hits","Shit","tsih","sthi","name"]))

