# Input the student's score
score=int(input("Enter the marks (out of 100):"))
if score>=90:
    grade="A"
    print(f"excellent")

elif score>=80:
    grade="B"
    print(f"above avg")
elif score>=70:
    grade="C" 
    print(f"avg")
elif score>=60:
    grade="D"
    print(f"upto mark")
elif score>=50:
    grade="E" 
    print(f"poor")
else:
    grade="F" 
    print(f"fail")   

# Check if a year is a leap year
year=int(input("enter a year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
        print(f"{year} is a leap year")
else:
        print(f"{year}is not leap year")    20