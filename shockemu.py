import string, sys

letters = 0, 11, 8, 2, 14, 3, 5, 4, 34, 38, 40, 37, 46, 45, 31, 35, 12, 15, 1, 17, 32, 9, 13, 7, 16, 6
nums = 29, 18, 19, 20, 21, 23, 22, 26, 28, 25

keys = dict(
	space=49, 
	enter=36, 
	control=59, option=58, command=55, 
	up=126, 
	down=125, 
	left=123, 
	right=124, 
	shift=56, 
	capslock=57, 
	tab=48, 
	backtick=50, 
	comma=43, period=47, slash=44, backslash=42, 
	delete=51, 
	escape=53, 
)

buttons = 'dpadUp dpadLeft dpadRight dpadDown X O square triangle PS touchpad options share L1 L2 L3 R1 R2 R3'.split(' ')

axes = 'leftX- leftX+ leftY- leftY+ rightX- rightX+ rightY- rightY+'.split(' ')

for i, x in enumerate(letters):
	keys[chr(ord('a') + i)] = x
for i, x in enumerate(nums):
	keys[str(i)] = x

def parse(data):
	lines = (line.split('#', 1)[0].strip() for line in data.split('\n'))
	return dict(map(string.strip, line.split('=', 1)) for line in lines if line)

with file('mapKeys.h', 'w') as fp:
	for k, v in parse(file(sys.argv[1]).read()).items():
		if k in keys or k == 'leftMouse' or k == 'rightMouse':
			if k in keys:
				k = 'DOWN(%i)' % keys[k]
			if v in buttons:
				print >>fp, '%s = %s;' % (v, k)
			elif v in axes:
				print >>fp, 'if(%s) %s %s= 1;' % (k, v[:-1], v[-1])
			else:
				print 'Unknown button:', v
		elif k == 'mouseLook':
			print 'mouseLook', v
		else:
			print 'Unknown key:', k
