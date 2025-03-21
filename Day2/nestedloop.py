#multiplication table
row=5
columns=5
for i in range(1, row + 1):
    for j in range(1,columns + 1):
        print(i*j, end="\t")
    print()#move to next row

# Alphabet grid
rows=5
for i in range(rows):
    for j in range(rows):
        print(chr(65+j),end=" ")
    print() 
# Define a dictionary
person = {
    "name": "nadiya",
    "age": 25,
    "city": "Bengaluru",
    "profession": "Engineer"
}

# Iterate through the values
print("dictionary values:")
for value in person.values():
    print(value)
 # Iterate through keys and values
print("keys and their corresponing values:") 
for key,values in person.items():
    print(f"{key}:{values}")
   

