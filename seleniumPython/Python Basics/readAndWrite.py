# file = open('test.txt')
# print(file.read(5))
#
# print(file.readline())
# print(file.readline())

# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# for line in file.readlines():
#     print(line)
# file.close()

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

