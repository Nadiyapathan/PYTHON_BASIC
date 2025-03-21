#sum of  numbers
def my_fun(a,b,c,d):
    return a+b+c+d
sum=my_fun(121,231,3213,4123)
print(sum)

#avg of  3number

def avg_num(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)

    return avg
print(avg_num(11,22,33))
#length of functions
list=["nadiya","bujji","ayaan","ayesha"]
hero=["chriu","salman","amar","gopi"]
def print_len(list):
    print(len(list))
    #for loop
for item in list:
    print(item,end=" ") 
print(hero)

#factorial function
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=1
    print(fact)  
cal_fact(3)  
    


