'''
for i in range(100,1000):
    
    d = (i/100)%10
    c = (i/10)%10
    b = (i/1)%10

    if int(d)**3 + int(c)**3 + int(b)**3 == i:
        print(i)
'''

a = 100

    
while a < 1000:
    j = (a/100)%10
    q = (a/10)%10
    k = (a/1)%10


    if a == int(j)**3 + int(q)**3 + int(k)**3:
        print(a)
    a += 1
print("输出完毕")
