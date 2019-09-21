'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
list1=[]
T=int(input("test case:"))
s=int(input("start"))
e=int(input('end'))
for i in range(1,T+1):
        for i in range(s,e+1):
            list1.append(i)
       # print(list1)
        for i in list1:
            if i%3==0:
                print("Fizz\n",i+1)
        for i in list1:
            if i%5==0:
                print("Buzz\n",i+1)
        for i in list1:
            if i%3==0 and i%5==0:
                print("FizzBuzz\n",i)