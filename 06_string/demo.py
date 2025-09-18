# Strings

s1 = 'hello'
# s1 = hello # invalid string representation 
print(s1)

s2 = "hello"
print(s2)

s3 = '''hello''' 
print(s3)

s4 = """hello"""
print(s4)

# Above are for single line strings 

# Below are multi line strings
# address = "house no 90 
# zip is 500081
# city is hyderabad"

address = """house no 90 
zip is 500081
city is hyderabad"""
print(address)

address = '''house no 90 
zip is 500081
city is hyderabad'''

print(address)

# caution
question = "How are you ?"
# answer = 'i'm good'
answer = "i'm good"
print(answer)

question = "How are you ?"
# answer = "i"m good"
answer = 'i"m good'
print(answer)

question = "How are you ?"
answer = ''' i"m good' "i'm good '''
print(answer)

# string 
text = "python"

# access whole string 
print(text)

# access character -> Index 
text = "python"
# print(text[index]) 
print(text[0]) 
print(text[3]) 
print(text[-2]) 

# length of string
print(len(text))

    #     0  1  2  3  4  5 (Positive Indexing) (forward)
    #     p  y  t  h  o  n
    #    -6 -5 -4 -3 -2 -1 (Negative Indexing) (backward)

# slicing - slice[start: stop: step]
text = "python"
# print(text[]) # SyntaxError: invalid syntax
print(text[:]) # python
print(text[::]) # python
print(text[0:3]) # pyt 
print(text[1:3]) # yt
print(text[1:3:1]) # yt
print(text[0:5:2]) # pto


                       
    #     0  1  2  3  4  5 (Positive Indexing) (forward)
    #     p  y  t  h  o  n
    #    -6 -5 -4 -3 -2 -1 (Negative Indexing) (backward)

print(text[-4:-1]) # tho
print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # empty
print(text[-4:-6:-1]) # ty
print(text[1:4:-1]) # empty
print(text[-1:-4:]) # empty

# slicing 
print(text[::-1]) # nohtyp

text = "python"
reversed_text = ""

# custom login
for char in text:
    reversed_text = char + reversed_text # ...typ
print(reversed_text)

text = "python"
# print(text[index]) 
print(text[0]) 
print(text[3]) 
# print(text[10]) # IndexError: string index out of range

print(text[0:6:-1])


# string concatenation
s = "good"
m = " morning"
print(s+m) 

a = 10
b = 20
print(a+b)

# string formatting
age = 30
# print("My age is: "+age) # TypeError: can only concatenate str (not "int") to str

# interpolation - {}
print(f"My age is: {age}")   #1st way
print("My age is: ",age)     #2nd way
print("My age is: ", +age)   #3rd way
print("My age is: "+str(age)) #4th way

print("My age after 5 years would be: ", +age+5) 

# String Repetition 
laugh = "Haha"
print(laugh)

laugh_hard = "HahaHahaHahaHahaHahaHahaHahaHahaHaha"
print(laugh_hard)

laugh_hard = laugh * 20
print(laugh_hard)

greet = "hello"
print(greet)
greet = "Hello"
print(greet)

# String Immutability 
# Immutable : cannot be changed 
greet = "hello"
print(greet)
# greet[0] = "H" # TypeError: 'str' object does not support item assignment
print(greet)

print(dir(greet))