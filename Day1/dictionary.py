# Create a dictionary
person={
    "name":"nadiya",
    "age":30,
    "city":"bangalore",
    "email":"nadiya.pathan560@gmail.com",
    "phno":8217594303

}
#length of dict
print(len(person))
#dictionary datatypes
person={
    "name":"nadiya",
    "age":False,
    "city":"bangalore",
    "email":"nadiya.pathan560@gmail.com",
    "phno":8217594303
}
print(person)

#type()
print(type(person))

#using loop
for x in person:
    print(x)
for x in person.keys(): #keys   
 print(x)
for x in person.values(): #values
   print(x) 
for x in person.items(): #items
   print(x)  
   #nested loop
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

  
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child2"]["name"])
