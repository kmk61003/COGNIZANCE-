d = [ [1, 'x', 90],
     [2, 'y', 95],
     [3, 'z', 85]]
     
print("{:<10} {:<10} {:<10}".format('Roll no','name','marks'))

for i in range(3):
    print(d[1][i],end=" "*10)