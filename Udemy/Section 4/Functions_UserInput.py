#age = input('Enter your age: ')
#new_age = int(age) + 50
#print(new_age)

def age_foo(age):
    new_age = int(age) + 50
    return new_age

age = input('Enter your age: ')
print(age_foo(age))
