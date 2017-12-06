'''
result = 0

for i in range(10):
    result = result + i + 1


for i in range(10):
    result = result + i + 1
    print('in the {}th iteration, new result = {}'.format(i, result))

print(result)
'''
'''
result = 1

#for i in range(10):
#    result = result * i + 1

for i in range(10):
    result = result * i + 1
    print('in the {}th iteration, new result = {}'.format(i, result))

print(result)
'''
#sum of all odd numbers in range 10
result = 0

for i in range(1, 10, 2):
    #the third parameter is the space between the int
    result = result + i

print(i)
print(result)

#sum of all even numbers in range 10
result = 0

for i in range(0, 11, 2):
    #remember bound by upper, so if the range is 0, 10 int(10) is not included!
    result = result + 1

print(i)
print(result)

for x in ['hello']