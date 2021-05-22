text = list(input())
data = []

while len(text) > 0:
    data.append(text.pop())

print(''.join(data))