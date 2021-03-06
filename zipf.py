import csv
import string
import sys

translate = str.maketrans('', '', string.punctuation)

word_count = {}
input_file = sys.argv[1]
text = open(input_file).read()

words = text.split()
for word in words:
    word = word.translate(translate).lower()
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count
rank = 1
out_file = sys.argv[2]
word_count_list = sorted(word_count, key=word_count.get, reverse=True)
file_out = open(out_file, 'w')
writer = csv.writer(file_out)
for word in word_count_list:
    writer.writerow([word, word_count[word], rank])
    rank += 1
