list = []
limit = int(input("Enter the limit:"))
for x in range(limit):
    num = int(input("Enter number " + str(x + 1) + ":"));
    if (num > 100):
        num = "over"
    list.append(num)
print(list)
