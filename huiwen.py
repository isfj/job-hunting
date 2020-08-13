'''
网易互联网测试开发笔试第一题：
	小易爱回文：小易得到了一个仅包含大小写英文字符的字符串，该字符串可能不是回文串，
	（‘回文串’是一个正读和反读都一样的字符串，比如‘level’或者’noon’等就是回文串，‘asds’就不是回文串）
	小易可以在字符串尾部加入任意数量的任意字符，使其字符串变成回文串
输入描述：
一行包括一个字符串s, 1≤ |s|≤10^3
输出描述：
一行包括一个字符串，代表答案
示例：
输入：
noon
输出：
noon

'''
'''
思路：
判断输入是否为回文，若不是，则在尾部补上不是回文部分的反向
'''
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
		
