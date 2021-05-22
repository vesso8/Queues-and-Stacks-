from collections import deque

players = input().split()
steps = int(input())

players_collection = deque(players)

while len(players_collection) > 1:
    for num in range(steps - 1):
        players_collection.append(players_collection.popleft())
    print(f"Removed {players_collection.popleft()}")
print(f"Last is {players_collection.popleft()}")