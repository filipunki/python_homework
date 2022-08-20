#Quick Exercise:
# Create a function that can take in infinte numbers from user ,
# can perform subtraction on them
#(sub from first num in list)
# if the first number in the arguments is 0 then 
# function should replace it with 1

# Ex: 0,2,3,4,5
#sub= 1-2-3-4-5

def fun(*args):
    
    l = list(args)
    
    if l[0] == 0:
        l[0] = 1
    num = l[0]   
    for _ in l[1:]:
        num -= _
    return num

print(fun(1,2,3,4,5))
        



    
