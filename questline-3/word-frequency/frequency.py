import pprint

with open("test.txt", "r") as file:
    text = file.read()

words = text.split(" ")

count = {}

for i in words:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1


pprint.pprint(count)
