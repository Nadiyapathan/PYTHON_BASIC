#filter even numbers
number=[1,2,3,4,5,6,7,8,9,10]
even_number=[num for num in number if num% 2==0]
print("even numbers:",even_number)


#Transfrom data (square of numbers)
numbers =[1,2,3,4,5]
squared_numbers=[num**2 for num in numbers]
print("square numbers:",squared_numbers)

#filter even number and transform (square them)
number=[1,2,3,4,5,6,7,8,9,10]
even_square=[num**2 for num in numbers if num%2==0]
print("square of even numbers:",even_square)

#List comprehension to transform string to uppercase
word=["apple","banana","cherry","date"]
uppercase_words=[word.upper() for word in word]
print("uppercase words:",uppercase_words)

#Extracting values from a list of Dictionaries

students = [
    {"name":"nadi","age":30,"grade":"A"},
    {"name":"bujj","age":25,"grade":"A+"},
    {"name":"Ayesha","age":18,"grade":"A++"}
]
name=[student['name'] for student in students]
grades_A = [student['grade'] for student in students if student['grade'] == 'A']
print("Names of all students:", name)
print("Students with grade 'A':", grades_A)
e_age = [(student['name'], student['age']) for student in students]
print("Names and Ages of students:", 'name,age')

