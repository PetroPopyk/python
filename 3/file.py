#Чи можливе існування трикутника
print("Enter side values of the traingle:")
side_1 = int(input("First side = "))
side_2 = int(input("Second side = "))
side_3 = int(input("third side = "))
 
if side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_1 + side_3 > side_2:
	print("This triangle can exist")
else:
	print("This triangle can not exist")
#Числа Фібоначчі
def Fibonacci(n):
    a = 0
    b = 1
    for number in range(n):
        a, b = b, a + b
    return a
print(Fibonacci(int(input('Enter value: '))), "- your value")