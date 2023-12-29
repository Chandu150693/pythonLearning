# We can specify the file path like D:\\myDir\\demofile.txt
f = open("demofile.txt", "r")

# read method will able to execute only once
# print(f.read())
# print(f.read(5))

# readline can call n number of times
# print(f.readline())
# print(f.readline())
# print(f.readline())

# its equal to read line
# for x in f:
#     print(x)

print(f.readline())
f.close()

