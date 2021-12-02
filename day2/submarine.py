test = False
if test:
    readInput = open("testInput.txt", 'r')
else:
    readInput = open("input.txt", 'r')

lines = readInput.readlines()
total = 0
horizontal = 0
vertical = 0

def parsePos(command, ammount):
    global horizontal
    global vertical
    if command == 'forward':
        horizontal += int(ammount)
    elif command == 'down':
        vertical += int(ammount)
    elif command == 'up':
        vertical -= int(ammount)
        if vertical < 0:
            vertical = 0
    #print(horizontal, vertical)

for line in lines: 
    diff = line.split(" ")
    print(diff)
    parsePos(diff[0], diff[1])



print(horizontal, vertical)
print("final anser", horizontal*vertical)