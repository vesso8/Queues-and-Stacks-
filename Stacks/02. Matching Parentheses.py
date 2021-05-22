arithmetic_expression = input()
data = []
for sub in range(len(arithmetic_expression)):
    index = arithmetic_expression[sub]
    if index == "(":
        data.append(sub)
    elif index == ")":
        last = data.pop()
        print(arithmetic_expression[last:sub + 1])

