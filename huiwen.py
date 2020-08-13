def is_huiwen(l):
	if len(l) == 0:
		return False
	if len(l) == 1:
		return True
	i = 0
	while(i<(len(l)-1)):
		if l[i] != l[len(l)-1-i]:
			return False
		i += 1
	return True


###get input
s = input()
tmp = s
s = list(s)
add_s = []
while(not is_huiwen(s) and s != None):
	
	add_s.append(s.pop(0))
add_s.reverse()
tmp = list(tmp)
tmp = tmp+add_s
print(tmp)	
		
