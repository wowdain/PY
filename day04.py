#dictionay comprehension

univ = 'inha university'
#letter_counts = {letter : univ.count(letter) for letter in univ}
#print(letter_counts)


letter_counts = dict()
for letter in univ:
    letter_counts[letter] = univ.count(letter)
print(letter_counts)