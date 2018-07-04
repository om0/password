password = 'a123456'
x = 2 
while x >= 0:
	p = input('請輸入密碼： ')
	if p == password:
		print('登入成功! ')
		break
	elif x <= 0:
		print('密碼輸入錯誤多次，bye!!')
		break
	else:
		print('密碼錯誤！ 還有', x, '次機會' )
		x = x - 1
