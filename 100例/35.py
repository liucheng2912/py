"""
文本颜色设置
思路：
类的定义和调用
"""
class bcolors:
    HEADER='\033[95m'
    OKBLUE='\033[94m'
    OKGREEN='\033[92m'
    WARNING='\033[93m'
    ENDC='\033[0m'

print(bcolors.WARNING+"警告的颜色字体?"+bcolors.ENDC)