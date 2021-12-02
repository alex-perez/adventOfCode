readInput = open("input.txt", 'r')
#readInput = open("testInput.txt", 'r')
lines = readInput.readlines()
total = 0
start = 'A'
sumArr = []
for line in range(2,len(lines)):
    # if(int(lines[line]) + int(lines[line - 1]) + int(lines[line - 2])):
    #     #print("increased")
    #     total += 1
    #     start += 1
    # else:
    #     print("\t decreased")
    prod = int(lines[line]) + int(lines[line - 1]) + int(lines[line - 2])
    print(start, prod)
    start = chr(ord(start) + 1)
    sumArr.append(prod)
for n in range(1, len(sumArr)):
    if(int(sumArr[n]) > int(sumArr[n - 1])):
        print("increased")
        total += 1
    else:
        print("\t decreased")
print(total)