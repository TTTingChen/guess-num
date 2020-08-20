import random
r = random.randint(1,100)
count = 0
while True:
	count = count + 1 #count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了！')
		print('這是你猜的第', count, '次')#所以要加這句
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')
	#因為猜中就直接break，所以最後一次會沒有幾次