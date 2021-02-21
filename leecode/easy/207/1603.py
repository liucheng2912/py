'''
思路：
实现方式：
    类定义和构造函数的定义
    函数实现：
'''
class ParkingSystem:
    def __init__(self,big,medium,small):
        self.big=big
        self.medium=medium
        self.small=small

    def addCar(self,carType):
        if carType==1:
            self.big-=1
            return self.big>=0
        elif carType==2:
            self.medium-=1
            return self.medium >=0
        elif carType==3:
            self.small-=1
            return self.small>=0
        else:
            return False

park=ParkingSystem(1,1,0)
print(park.addCar(1))
print(park.addCar(2))
print(park.addCar(3))
print(park.addCar(1))