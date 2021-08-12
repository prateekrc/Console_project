import pandas as pd 
#Pandas Dataframe
# lis={
# 	'h1':[12,33],
# 	'h2':[34,67]
# }
# var1=pd.Dataframe(lis)
# print(var1)
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myvar = pd.DataFrame(mydataset)
# print(myvar)

#Pandas Series
#lis=[12,3,5,7,98]
#v1=pd.Series(lis,index=['a','b','c','d','e'])
#print(pd.Series(lis,index=['a','b','c','d','e']))

#Reading CSV file
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }}
# var2=pd.DataFrame(data)
# print(var2)
# print(pd.DataFrame(info))

#Use of head in pandas returns 1st 5 elements by default
# var3=pd.read_csv('data.csv')
# #print(var3.to_string())
# print(var3.head())
# print(var3.head(10))
# print(var3.info())

#to remove empty cells
# var4=pd.read_csv('data.csv')
# m1=var4.dropna()
# print(m1.to_string())

#Replacing empty cells with a value
# df=pd.read_csv('data.csv')
# m1=df.fillna(74)#to change original df use(74,inplace=True)
# print(m1.to_string())

#Assigning mean value to empty cells
# df=pd.read_csv('data.csv')
# m1=df['Calories'].mean().round(2)
# m2=df['Calories'].fillna(m1)
# print(m2.to_string())

#Replacing wrong values
# df=pd.read_csv("data.csv")
# df.loc[3,'Duration']=1234
# print(df.to_string)

#Implementations of stack DS 
# stack=[]
# print("Inital Stack is:")
# print(stack)
# stack.append('a')#Push operation in stack
# stack.append('b')
# stack.append('c')

# print(stack)#after push operations
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print(stack)

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