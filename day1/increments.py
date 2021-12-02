readInput = open("input.txt", 'r')
#readInput = open("testInput.txt", 'r')
lines = readInput.readlines()
total = 0
for line in range(1,len(lines)):
    if(int(lines[line]) > int(lines[line - 1])):
        print("increased")
        total += 1
    else:
        print("\t decreased")

print(total)