#Parenthesis check

def check(a):
	stack=[]
	open={'(', '[', '{'}
	closed={')': '(', ']': '[', '}': '{'}
	for i in a:
		if i in open:
			stack.append(i)
		elif i in closed:
			if not stack or stack.pop()!=closed[i]:
				return False
	return not stack

print(check('{[()]}'))