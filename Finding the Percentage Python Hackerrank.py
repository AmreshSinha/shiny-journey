import math

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
# print(student_marks)
query_name = input()
arr = student_marks[query_name]

x = 0
for i in arr:
    x = x + i
    
print('%.2f'%(x/3))
# # using "%" to print value till 2 decimal places  
# print ("The value of number till 2 decimal place(using %) is : ",end="") 
# print ('%.2f'%(x/3)) 
  
# # using format() to print value till 2 decimal places  
# print ("The value of number till 2 decimal place(using format()) is : ",end="") 
# print ("{0:.2f}".format(x/3)) 
  
# # using round() to print value till 2 decimal places  
# print ("The value of number till 2 decimal place(using round()) is : ",end="") 
# print (round(x/3,2)) 