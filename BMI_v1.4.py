#請使用者輸入身高體重
high = input('請問您的身高是多少公尺?')
weight = input('請問您的體重是多少公斤?')

#計算BMI
result = float(weight)//float(high) ** 2

#分辨作業系統並清除畫面
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

#顯示出BMI值
print('您的BMI值: ', result)