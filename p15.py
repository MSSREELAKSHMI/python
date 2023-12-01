def add(num1,num2):
	return num1+num2
def subtract(num1,num2):
	return num1-num2
def multiply(num1,num2):
	return num1*num2
def divide(num1,num2):
	return num1/num2
def power(num1,num2):
	return num1**num2
def calculator(num1,operator,num2):
	if operator=="+":
		return add(num1,num2)
	if operator=="-":
		return subtract(num1,num2)
	if operator=="*":
		return multiply(num1,num2)
	if operator=="/":
		return divide(num1,num2)
	if operator=="**":
		return power(num1,num2)
num1=int(input("enter first number"))
num2=int(input("enter second number"))
operator=input("choose an operation")
result=calculator(num1,operator,num2)
print(result)	
