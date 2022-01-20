#請使用者輸入身高體重
high = input('請問您的身高是多少公分?')
weight = input('請問您的體重是多少公斤?')
#計算BMI
result = float(weight) // (float(high) / 100) ** 2
#分辨作業系統並清除畫面
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()
#顯示出BMI值
print('您的BMI值:', result)
if result >=6 and result <= 15:
    print('您太瘦了')
elif result >= 28 and result <= 100:
    print('您太胖了')
elif result >= 16 and result <= 28:
    print('您的體重正常')
else:
    print('您輸入的資料可能有誤')