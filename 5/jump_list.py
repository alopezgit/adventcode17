
with open('input.txt') as file:
    jumps = map(int, file.readlines())

print jumps

index = 0
steps = 0
while True:
    new_index = jumps[index] + index
    jumps[index] += 1
    index = new_index
    steps += 1
    if index >= len(jumps):
        break

print steps

### Part two

with open('input.txt') as file:
    jumps = map(int, file.readlines())

index = 0
steps = 0

while True:
    new_index = jumps[index] + index
    if jumps[index] >= 3:
        jumps[index] -= 1
    else:
        jumps[index] += 1
    index = new_index
    steps += 1
    if index >= len(jumps):
        break

print steps, jumps