from collections import deque
command = input()
names_collection = deque()
while not command == "End":
    if command == "Paid":
        while names_collection:
            print(names_collection.popleft())
    else:
        names_collection.append(command)
    command = input()
print(f"{len(names_collection)} people remaining.")
