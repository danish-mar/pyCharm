num = 'String "Sinle"'

num2 = num3 = num4 = 5
#              0           1            2
arr = [[1,2,4],[2,4,5],[6,4,2]]

print(arr[0][1])
#1,"hello",4.43
#string
#num = 2
#int 

def my_func():
    global num
    num = 657
    #print("Run From Function : ", num)

my_func()    
print("Number is  : ", num,num3,num4)
