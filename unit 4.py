A= ("PATTERN A")
B= ("PATTERN B")
PA= A.center(38)
PB= B.center(38)
#centers the print message to visually appeal

print(PA)
print("\n")
#\n allows for new line


rows = 10
#rows determined
k = 0
#store of value for loop

for i in range(1, rows+1):
#counts the amount of rows
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
    #gives total number of + in each row
        print("+ ", end="")
        k += 1
   
    k = 0
    print()
#stops the loop
    
print("\n")
print(PB)
print("\n")

row = 11
#had to increase row to 11 since row-1 not row +1

for i in range(row, 1, -1):
    for space in range(0, row-i):
        print("  ", end="")
#vertically cut portion
    for j in range(i, 2*i-1):
    #number of + in each row
        print("+ ", end="")
    for j in range(1, i-1):
        print("+ ", end="")
#second half of pyramid
    print()

