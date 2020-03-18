count = 0
for i in range(1,101):
	if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
		continue
	else:
		count += 1
		if count % 4 == 0:
			print('{}\t'.format(i),end='')#由于print()函数本身自带换行，因此使用end=''实现不换行
			print('')#此处实现换行
		else:
			print('{}\t'.format(i),end='')
