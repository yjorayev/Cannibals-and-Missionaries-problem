import copy
import itertools

class riverBank:
	def __init__(self, c, m):
		self.cannibals = c
		self.missionaries = m

	def valid(self):
		if self.cannibals <= self.missionaries or self.missionaries ==0:
			return True
		else:
			return False

	def goal(self):
		if self.cannibals ==3 and self.missionaries == 3:
			return True
		else:
			return False

class state:
	def __init__(self, data):
		self.data = data
		self.parent = None

	#explore method explores possible actions and adds them to the tree
	def explore_children(self):
		children = []
		temp = copy.deepcopy(self.data)
		if self.data["boat"] == "left":
			#Moving 2 cannibals on a boat
			if temp["left"].cannibals >= 2:
				temp["left"].cannibals = temp["left"].cannibals - 2
				temp["right"].cannibals = temp["right"].cannibals + 2
				temp["boat"] = "right"
				if temp["left"].valid() and temp["right"].valid():
					child = state(temp)
					child.parent = self
					children.append(child)

			temp = copy.deepcopy(self.data)     #need to reset temp to parent for exploring other children
			#Moving 2 missionaries on a boat
			if temp["left"].missionaries >= 2:
				temp["left"].missionaries = temp["left"].missionaries - 2
				temp["right"].missionaries = temp["right"].missionaries + 2
				temp["boat"] = "right"
				if temp["left"].valid() and temp["right"].valid():
					child = state(temp)
					child.parent = self
					children.append(child)

			temp = copy.deepcopy(self.data)     #need to reset temp to parent for exploring other children
			#Moving 1 cannibal on a boat
			if temp["left"].cannibals >= 1:
				temp["left"].cannibals = temp["left"].cannibals - 1
				temp["right"].cannibals = temp["right"].cannibals + 1
				temp["boat"] = "right"
				if temp["left"].valid() and temp["right"].valid():
					child = state(temp)
					child.parent = self
					children.append(child)

			temp = copy.deepcopy(self.data)     #need to reset temp to parent for exploring other children
			#Moving 1 missionary on a boat
			if temp["left"].missionaries >= 1:
				temp["left"].missionaries = temp["left"].missionaries - 1
				temp["right"].missionaries = temp["right"].missionaries + 1
				temp["boat"] = "right"
				if temp["left"].valid() and temp["right"].valid():
					child = state(temp)
					child.parent = self
					children.append(child)

			temp = copy.deepcopy(self.data)     #need to reset temp to parent for exploring other children
			#Moving 1 missionary and 1 cannibal on a boat
			if temp["left"].missionaries >= 1 and temp["left"].cannibals >= 1:
				temp["left"].missionaries = temp["left"].missionaries - 1
				temp["right"].missionaries = temp["right"].missionaries + 1
				temp["left"].cannibals = temp["left"].cannibals - 1
				temp["right"].cannibals = temp["right"].cannibals + 1
				temp["boat"] = "right"
				if temp["left"].valid() and temp["right"].valid():
					child = state(temp)
					child.parent = self
					children.append(child)


		elif self.data["boat"] == "right":
			#Moving 2 cannibals on a boat
			if temp["right"].cannibals >= 2:
				temp["right"].cannibals = temp["right"].cannibals - 2
				temp["left"].cannibals = temp["left"].cannibals + 2
				temp["boat"] = "left"
				if temp["left"].valid() and temp["right"].valid():
					child = state(temp)
					child.parent = self
					children.append(child)

			temp = copy.deepcopy(self.data)     #need to reset temp to parent for exploring other children
			#Moving 2 missionaries on a boat
			if temp["right"].missionaries >= 2:
				temp["left"].missionaries = temp["left"].missionaries + 2
				temp["right"].missionaries = temp["right"].missionaries - 2
				temp["boat"] = "left"
				if temp["left"].valid() and temp["right"].valid():
					child = state(temp)
					child.parent = self
					children.append(child)

			temp = copy.deepcopy(self.data)     #need to reset temp to parent for exploring other children
			#Moving 1 cannibal on a boat
			if temp["right"].cannibals >= 1:
				temp["left"].cannibals = temp["left"].cannibals + 1
				temp["right"].cannibals = temp["right"].cannibals - 1
				temp["boat"] = "left"
				if temp["left"].valid() and temp["right"].valid():
					child = state(temp)
					child.parent = self
					children.append(child)

			temp = copy.deepcopy(self.data)     #need to reset temp to parent for exploring other children
			#Moving 1 missionary on a boat
			if temp["right"].missionaries >= 1:
				temp["left"].missionaries = temp["left"].missionaries + 1
				temp["right"].missionaries = temp["right"].missionaries - 1
				temp["boat"] = "left"
				if temp["left"].valid() and temp["right"].valid():
					child = state(temp)
					child.parent = self
					children.append(child)

			temp = copy.deepcopy(self.data)     #need to reset temp to parent for exploring other children
			#Moving 1 missionary and 1 cannibal on a boat
			if temp["right"].missionaries >= 1 and temp["right"].cannibals >= 1:
				temp["left"].missionaries = temp["left"].missionaries + 1
				temp["right"].missionaries = temp["right"].missionaries - 1
				temp["left"].cannibals = temp["left"].cannibals + 1
				temp["right"].cannibals = temp["right"].cannibals - 1
				temp["boat"] = "left"
				if temp["left"].valid() and temp["right"].valid():
					child = state(temp)
					child.parent = self
					children.append(child)	
		return children
	

					


#method for comparing states. state.data
#def same(d1, d2):
#	if d1 and d2:
#		s1 = d1.data
#		s2 = d2.data
#		if(s1["boat"] == s2["boat"] and 
#			s1["left"].cannibals == s2["left"].cannibals and s1["left"].missionaries == s2["left"].missionaries and
#			s1["right"].cannibals == s2["right"].cannibals and s1["right"].missionaries == s2["right"].missionaries):
#			return True
#	return False

def contains(s1, q):
	s1 = s1.data
	for s2 in q:
		s2 = s2.data
		if(s1["boat"] == s2["boat"] and 
			s1["left"].cannibals == s2["left"].cannibals and s1["left"].missionaries == s2["left"].missionaries and
			s1["right"].cannibals == s2["right"].cannibals and s1["right"].missionaries == s2["right"].missionaries):
			return True
	return False


left = riverBank(3, 3)
right = riverBank(0, 0)
root_data = {"left": left, "right": right, "boat": "left"}

explored = []
nodes = []      #this is a list holding all nodes or the frontier in book language
path = []
nodes.append(state(root_data))

#finding goal state
while len(nodes)>0:
	g = nodes.pop(0)
	explored.append(g)
	if g.data["right"].goal():
		path.append(g)
	else:
		next_children = g.explore_children()
		for x in next_children:
			if not contains(x, nodes) and not contains(x, explored):
					nodes.append(x)

#printing a path


print("Path:")
while g.parent:
	g = g.parent
	path.append(g)

for p in reversed(path):
	print("Left C: %s. Left M: %s. Right C: %s. Right M: %s. Boat: %s" 
		%(p.data["left"].cannibals, p.data["left"].missionaries, p.data["right"].cannibals, p.data["right"].missionaries,
			p.data["boat"]))
print("End of Path!")
