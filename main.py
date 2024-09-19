import re

beescript = open("bee-movie.txt", encoding='utf-8').read().lower()


able = r'\b\w+able\b'
able_words = re.findall(able, beescript)

print(able_words)

count = 0

for able_words in able_words:
    count +=1

print("number of -able matches =", count)

