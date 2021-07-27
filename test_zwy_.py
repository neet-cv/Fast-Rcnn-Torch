# 从键盘输入一个身份证号码（18位），然后从身份证号码中截取出生的省份编号、
	#出生的年月日、性别对应的数字。
	#输出的格式如下：
	#您的身份证所在地编号：xx
	#您在xxxx年xx月xx日出生
	#您的性别编号为：x
id = "445224200207011810"
province = id[:2]
print(province)
year = id[6:10]
month = id[10:12]
day = id[12:14]
sex = id[-2]

a=("您的身份证所在地编号：{}".format(str(province)))

print("您在{}年{}月{}日出生" .format(year,month,day))
print("您的性别编号为：{}".format(sex))