text = "this is a collection of words of nice words this is a fun thing it is"
word_to_count = {}
words = text.lower().split(" ")

for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

sorted_words = sorted(word_to_count.keys())
max_length = max(len(word) for word in sorted_words)
for word in sorted_words:
    print(f"{word:{max_length}} : {word_to_count[word]}")