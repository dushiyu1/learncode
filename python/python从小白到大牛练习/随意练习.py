'''class Anmmol():
    def __init__(self,age,six=1,wight=0.0):
        self.age = age
        self.sex = six
        self.wight = wight
        print("狗凌",age,"岁","体重",wight,"斤")
    def eat(self):
        self.wight += 1
        
        print("狗凌",self.age,"岁","体重",self.wight,"斤")
    def run(self):
        self.wight -= 1
       
        print("狗凌",self.age,"岁","体重",self.wight,"斤")

dog = Anmmol(2,wight=10)
dog.eat()
dog.run()
'''

f = open("text.txt","w+")
f.write("hello")
f = open("text.txt","a+")
f.write("world")


