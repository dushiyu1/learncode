
class people:
    def __init__(self,n,g):
        self.name = n
        self.gonghao = g
    def guimian(self):
        print("%s 的工号为：%s " % (self.name,self.gonghao))

s = input("请输入柜员姓名")
s1 = input("请输入对应工号")
l1 = {s:s1}
p1 = people(s,s1)
p1.guimian()
