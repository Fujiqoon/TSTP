class Stack():
	def __init__(self):
		self.items=[]
	def is_empty(self):
		return self.items==[]
	def push(self,word):
		self.items.append(word)   #itemsを呼び出すことになるので、戻り値なくてよい
	def pop(self):
		return self.items.pop()   #引数とするため戻り値必要
	def peek(self):
		return self.items[len(self.items)-1]
	def size(self):
		return len(self.items)    #引数とするため戻り値必要
	
st=Stack()

for i in 'yesterday':
	st.push(i)

print(st.items)

reversed_string=''

for j in range(st.size()):
	reversed_string += st.pop()
	
print(reversed_string)
