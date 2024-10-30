'''

We will be going over Python Operators
that we can input into Python

'''


# a = 10
# b = 6
# c = 7
# d = a % b
# e = a % c
# f = b % c
# print(d)
# print(e)
# print(f)






'''

Trying out '+', '-', '*', '/', '%', '**' operators on 'str' and 'int'.

'''


# a = 'Hello'
# b = 'World'
# c = a * 100
# print(c)





'''

Finding a character/ letter in the 'str'.

'''

# hello = 'Hello'
# c = 'e' in hello
# print('H' not in hello)
# print(c)


# Trying to find 'str' in List.
'''
my_pets = ['Dog', 'Cat', 'Horse']
result = 'Dog' in my_pets
print(result)
my_pets = ['Dog', 'Cat', 'Horse']
result = 'Mouse' in my_pets
print(result)
'''

# Trying to find 'str' in Dictionary.
'''
my_pets = {
'D': 'Dog',
'C': 'Cat',
'H': 'Horse'
}
result = 'C' in my_pets
# It will only print the 'result' var. if it's referring to the key, not the actual value in the key (value = Dog, Cat, Horse, etc.).
print(result)
'''




'''

Using operators in the '+=', '-=', '*=', '/=', '%=', '**=' operators...

'''

# Testing out the different types of operators for each type of use (might have some errors!).
'''
a = 10

print(a)
a -= 1
print(a)
a += 2
print(a)
a /= 3
print(a)
a *= 4
print(a)
'''




'''

My Free Style

'''

Food_A = {'Cost': 1.00, 'Name': 'Apples'}
Food_B = {'Cost': 1.25, 'Name': 'Bread'}
Food_C = {'Cost': .70, 'Name': 'Cilantro'}
Total_Change = 20

Grocery_List = [

Food_A,
Food_B,
Food_C

]

print('Caesar King| How is the grocery shopping so far?')
print('Caesar King| Just a reminder! We need to get ' + Food_A['Name'] + ', ' + Food_B['Name'], 'and ' + Food_C['Name'] + '!')
print('Caesar King| Remember, we only have $' + str(Total_Change), 'left!')
print('Caesar King| One more thing, one more thing! I want 5 ' + Food_A['Name'] + ', 10 pieces of ' + Food_B['Name'] + ", and one bundle of " + Food_C['Name'] + ', okay?')
print("Caesar King| Alright hun', I love you!")