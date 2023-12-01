class account:
	def __init__(self):
		self.balance=0
		
	def deposit(self):
		amount=int(input("enter the amount to be deposit: "))
		self.balance+=amount
	def withdraw(self):
		amount=int(input("enter the amount to withdraw: "))
		if amount>self.balance :
			print("invalid bank account balance!!! \n please check account balance!!!")
		else:
			self.balance -= amount	
			print(amount,"is withdraw")
			
	def display(self):
		print("balance amount is",self.balance)

myaccount=account()

myaccount.deposit()
myaccount.withdraw()
myaccount.display()		
