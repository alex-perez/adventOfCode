test = False
if test:
    readInput = open("testInput.txt", 'r')
else:
    readInput = open("input.txt", 'r')

lines = readInput.readlines()
total = 0
horizontal = 0
vertical = 0
aim = 0

def parsePos(command, ammount):
    global horizontal
    global vertical
    global aim
    if command == 'forward':
        horizontal += int(ammount)
        vInc =  int(ammount) * aim
        vertical += vInc
    elif command == 'down':
        aim += int(ammount)
    elif command == 'up':
        aim -= int(ammount)
    #print(horizontal, vertical)

for line in lines: 
    diff = line.split(" ")
    print(diff)
    parsePos(diff[0], diff[1])



print(horizontal, vertical)
print("final anser", horizontal*vertical)