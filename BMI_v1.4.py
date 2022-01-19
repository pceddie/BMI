high = input('請問您的身高是多少公尺?')
weight = input('請問您的體重是多少公斤?')
result = float(weight)//float(high) ** 2

import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

print('您的BMI值: ', result)