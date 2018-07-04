password = 'a123456'
x = 3 
while x >0:
	x = x - 1
	p = input('請輸入密碼： ')
	if p == password:
		print('登入成功! ')
		break
	elif x == 0:
		print('密碼輸入錯誤太多次了，bye!!')
		break
	else:
		print('密碼錯誤！ 還有', x, '次機會' )
