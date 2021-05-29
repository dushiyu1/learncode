#列出1-100的所有素数
#输出200-300所有能被5整除或6整除的数


#1
list2 = [i for i in range(200,301) if i%5 == 0 or i%6 == 0]
print(list2)
