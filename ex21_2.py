class Stack():
	def __init__(self):
		self.items=[]
	def is_empty(self):
		return self.items==[]   #return
	def push(self,item):
		self.item=item
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
	def size(self):
		return len(self.items)

st=Stack()

for i in range(9):
	st.push(i+1)
print(st.items)

reverse_st=[]

for i in range(9):
	reverse_st.append(st.items.pop())

print(reverse_st)
