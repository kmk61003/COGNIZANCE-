lst = []
n = int(input("Enter number of rows : "))
print("Enter the roll no, name and marks to output a table")
for i in range(0, n):
    ele = [input(), input(),input()]
    lst.append(ele)
print("Enter the heading for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for a in lst:
    for b in a:
        print(b,end=" "*10)
    print()