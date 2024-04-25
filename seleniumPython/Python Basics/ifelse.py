#
# a = 4
# if a > 2:
#     print('Condition matches')
# else:
#     print('Condition do not matches')
#
# print('If else condition code is completed')
#
# #Loops
#
# obj = [2, 3, 5, 7, 9]
# for i in obj:
#     print(i)
#
#
# #print the multiples of 2
# for i in obj:
#     print(i * 2)

#sum of first natural numbers
#range(i, j) -> i to j-1
# summation = 0
# for j in range(1, 6):
#     summation = summation + j
#     print(summation)


# for k in range(10, 2):
#     print(k)
#

#while loop
# b = 10
# while b > 1:
#     if b != 3:
#         print(b)
#     b = b - 1


b = 10
while b > 1:
    if b == 9:
        b = b - 1
        continue
    if b == 3:
        break
    print(b)
    b = b - 1
 