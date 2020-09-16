import re

s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'

m = re.findall(r'([a-z]+)@([a-z]+)\.com', s)
print(m)
print(type(m))
# print(m.match)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

result = re.sub(r'([a-z]+)@([a-z]+)\.com', 'new-address', s)
print(result)
# new-address, new-address, ccc@zzz.net

s = ['4 ,(1,2)', '32 ,(1,3)', '16 ,(1,4)', '8 ,(2,2)', '64 ,(2,3)', '128 ,(2,4)', '4 ,(3,2)', '32 ,(3,3)', '256 ,(3,4)', '2 ,(4,2)', '8 ,(4,3)', '32 ,(4,4)']
tdary = [
		[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0]
	]
for item in s:
	m = re.findall(r'([0-9]+) ,\(([0-9]+),([0-9]+)\)',item)
	m = m[0]
	print(m[0],m[1],m[2])

	tdary[int(m[2])-1][int(m[1])-1] =int(m[0])
	
	
for i in tdary:

	print(i)