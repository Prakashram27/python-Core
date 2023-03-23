from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
storyWord = []
# print(story)
for line in story:
    line_words = line.decode('utf-8').split
    # print(line_words)
    for word in line_words:
        storyWord.append(word)

