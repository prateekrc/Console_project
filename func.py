
#Factorial program
'''n=10
fact1=1
for i in range(1,n+1):
	fact1 *=i
print(fact1)'''	
#print(n)	


#left rotation program
# arr=[1,27,3,89,5]
# n=2
# for i in range(0, n):        
#     first = arr[0]       
#     for j in range(0, len(arr)-1):        
#         arr[j] = arr[j+1]        
#     arr[len(arr)-1] = first           
# for i in range(0, len(arr)):    
#     print(arr[i])


#Exception Handling to print all elements from a sequence
# def func(n):
# 	print(n)
# def catch1():
# 	n=(12,3,4,5,7,8)
# 	for i in range(10):
# 		try:
# 			func(n[i])
# 		except IndexError:
# 			func(0)
# catch1()


#Constructor
# class Hostbooks:
# 	var = "Hostbooks Limited"
# 	def __init__(self,name,empid,designation,addressLine1):
# 		self.name = name
# 		self.empid = empid
# 		self.designation = designation
# 		self.addressLine1 = addressLine1
# 	def display(self):
# 		print("Name:",self.name)
# 		print("EmployeeId:",self.empid)
# 		print("Designation:",self.designation)
# 		print("AddressLine1:",self.addressLine1)

# hb = Hostbooks("Prateek",113,"Trainee","New Delhi")
# print(Hostbooks.var)
# hb.display()


#Multiple Inheritance
# class Calculate1:
# 	def summation(self,a,b):
# 		return a+b
# class Calculate2:
# 	def subtraction(self,a,b):
# 		return a-b
# class Derived(Calculate1,Calculate2):
# 	def fun1(self,a,b):
# 		return a/b	
# div=Derived()
# print(div.summation(12,6))
# print(div.subtraction(12,6))
# print(div.fun1(12,6))


#Method Overriding
# class Bank:
# 	def getroi(self):
# 		return 7
# class SBI(Bank):
# 	def getroi(self):
# 		return 8
# class ICICI(Bank):
# 	def getroi(self):
# 		return 8.2
# class BOB(Bank):
# 	def getroi(self):
# 		return 8.5
# obj1 = Bank()
# obj2 = SBI()
# obj3 = ICICI()
# obj4 = BOB()
# print("Rate of interest",obj1.getroi())
# print("Rate of interest in SBI",obj2.getroi())
# print("Rate of interest in ICICI",obj3.getroi())
# print("Rate of interest in BOB",obj4.getroi())										

# class Man:
# 	__count=0
# 	def __init__(self):
# 		self.__count = self.__count+1
# 	def display(self):
# 		print("Man Count ",self.__count)
# obj = Man()
# try:
# 	print(obj.__count)
# finally:
# 	obj.display()	
			
#Insertion sort
# def Insertionsort(arr):
# 	for i in range(1,len(arr)):
# 		k=arr[i]
# 		j=i-1
# 		while(j>=0 and k<arr[j]):
# 			arr[j+1]=arr[j]
# 			j -=1
# 		arr[j+1]=k
# arr=[1,5,12,5,3]
# Insertionsort(arr)
# print ("Sorted array is:",arr) 
# for i in range(len(arr)): 
#     print ("%d" %arr[i])

#Bubble sort
# def Bubblesort(arr):
# 	for i in range(0,len(arr)-1):
# 		for j in range(len(arr)-1):
# 			if(arr[j] > arr[j+1]):
# 				#var = arr[j]
# 				#arr[j] = arr[j+1]
# 				#arr[j+1] = var
# 				arr[j],arr[j+1]=arr[j+1],arr[j]
# 	return arr	
# arr=[5,3,2,8,1]
# print(Bubblesort(arr)) 	

# #Selection Sort
# def Selectionsort(arr):
# 	for i in range(len(arr)):
# 		var1=i
# 		for j in range(i+1,len(arr)):
# 			if(arr[j]<arr[var1]):
# 				var1=j
# 		arr[i],arr[var1]=arr[var1],arr[i]
# 	return arr		
# arr=[12,3,9,5,4,1]	
# print(Selectionsort(arr))


#Tree ds
class Node:
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data
	def insert(self,data):
		if (self.data):	
			if data<self.data:
				if self.left is None:
					self.left=Node(data)
				else:
					self.left.insert(data)
			elif data>self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data=data	
	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print( self.data)
		if self.right:
			self.right.PrintTree()
root=Node(12)
root.insert(14)
root.insert(5)
root.insert(1)
root.insert(7)
root.PrintTree()
