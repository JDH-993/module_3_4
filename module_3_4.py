def single_root_words(root_word, *other_words):
	same_words = []
	root_word = root_word.upper()
	for i in other_words:
		k = (str(i).upper())
		if k.find(root_word) != -1 or root_word.find(k) != -1:
			same_words.append(i)
	return same_words


print(single_root_words(input(), *list(map(str, input().split()))))
print(single_root_words(input(), *list(map(str, input().split()))))
