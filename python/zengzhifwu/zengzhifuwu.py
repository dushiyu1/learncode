import xlrd  # 导入读取excel模块，目前仅支持读取xls格式！
# import xlwt #导入写入excel模块
print("请输入文件路径")
lujing = input()
file = xlrd.open_workbook(lujing)

file = xlrd.open_workbook(r"/Users/toshigyoku/Downloads/gitcode/python/开门红3.21.xls")#使用绝对路径打开需要处理第文档
sheet1 = file.sheet_by_index(0) # 通过Sheet名字获取要操作的工作表对象
rows = sheet1.nrows # 获取有效行数
cols = sheet1.ncols # 获取有效列数

hangshu = int(rows)

def 黄岩():
    i = 1 ; a = 0 ; b = 0 
    c = 0 ; d = 0 ; e = 1 
    f = 1 ; g = 0 
    k = 0 ; fw3 = 0 ; fw3yilingqu = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "黄岩":
            if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("黄岩网电共发放",a + b)
    print("黄岩网电已领取",a)

    while e <= hangshu - 1:
        s = sheet1.cell_value(e,13)
        jigou = sheet1.cell_value(e,2)
        qudao = sheet1.cell_value(e,3)
        if jigou == "黄岩": 
            if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                if s == "已领用":
                    c += 1
                elif s == "未领用":
                    d += 1
        e += 1
    print("黄岩非电共发放",c + d)
    print("黄岩非网电已领取",c)
    print("黄岩合计共发放", a + b + c + d)
    print("黄岩合计已领取", a + c)

    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = sheet1.cell_value(f,12)
        lingquriqi = str(sheet1.cell_value(f,14))
        if 44256 <= fafangriqi < 44287 :
            if jigou == "黄岩":
                if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "黄岩": 
                    if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                        k += 1
        if 44256 <= fafangriqi < 44287 :
            if jigou == "黄岩":
                if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                    fw3 += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "黄岩": 
                    if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                        fw3yilingqu += 1
        f += 1
    print("黄岩3月网电共发放:",g )
    print("黄岩3月网电已领取:",k)
    print("黄岩3月非网电共发放:",fw3)
    print("黄岩3月非网电已领取:",fw3yilingqu)
    print("黄岩3月合计共发放:",g + fw3)
    print("黄岩3月合计已领取:",k + fw3yilingqu)
    print("-----------------------------------------")

def 路桥():
    i = 1 ; a = 0 ; b = 0 
    c = 0 ; d = 0 ; e = 1 
    f = 1 ; g = 0 
    k = 0 ; fw3 = 0 ; fw3yilingqu = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "路桥":
            if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("路桥网电共发放",a + b)
    print("路桥网电已领取",a)

    while e <= hangshu - 1:
        s = sheet1.cell_value(e,13)
        jigou = sheet1.cell_value(e,2)
        qudao = sheet1.cell_value(e,3)
        if jigou == "路桥": 
            if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                if s == "已领用":
                    c += 1
                elif s == "未领用":
                    d += 1
        e += 1
    print("路桥非电共发放",c + d)
    print("路桥非网电已领取",c)
    print("路桥合计共发放", a + b + c + d)
    print("路桥合计已领取", a + c)

    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = sheet1.cell_value(f,12)
        lingquriqi = str(sheet1.cell_value(f,14))
        if 44256 <= fafangriqi < 44287 :
            if jigou == "路桥":
                if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "路桥": 
                    if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                        k += 1
        if 44256 <= fafangriqi < 44287 :
            if jigou == "路桥":
                if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                    fw3 += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "路桥": 
                    if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                        fw3yilingqu += 1
        f += 1
    print("路桥3月网电共发放:",g )
    print("路桥3月网电已领取:",k)
    print("路桥3月非网电共发放:",fw3)
    print("路桥3月非网电已领取:",fw3yilingqu)
    print("路桥3月合计共发放:",g + fw3)
    print("路桥3月合计已领取:",k + fw3yilingqu)
    print("-----------------------------------------")

def 三门():
    i = 1 ; a = 0 ; b = 0 
    c = 0 ; d = 0 ; e = 1 
    f = 1 ; g = 0 
    k = 0 ; fw3 = 0 ; fw3yilingqu = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "三门":
            if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("三门网电共发放",a + b)
    print("三门网电已领取",a)

    while e <= hangshu - 1:
        s = sheet1.cell_value(e,13)
        jigou = sheet1.cell_value(e,2)
        qudao = sheet1.cell_value(e,3)
        if jigou == "三门": 
            if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                if s == "已领用":
                    c += 1
                elif s == "未领用":
                    d += 1
        e += 1
    print("三门非电共发放",c + d)
    print("三门非网电已领取",c)
    print("三门合计共发放", a + b + c + d)
    print("三门合计已领取", a + c)

    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = sheet1.cell_value(f,12)
        lingquriqi = str(sheet1.cell_value(f,14))
        if 44256 <= fafangriqi < 44287 :
            if jigou == "三门":
                if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "三门": 
                    if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                        k += 1
        if 44256 <= fafangriqi < 44287 :
            if jigou == "三门":
                if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                    fw3 += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "三门": 
                    if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                        fw3yilingqu += 1
        f += 1
    print("三门3月网电共发放:",g )
    print("三门3月网电已领取:",k)
    print("三门3月非网电共发放:",fw3)
    print("三门3月非网电已领取:",fw3yilingqu)
    print("三门3月合计共发放:",g + fw3)
    print("三门3月合计已领取:",k + fw3yilingqu)
    print("-----------------------------------------")

def 天台():
    i = 1 ; a = 0 ; b = 0 
    c = 0 ; d = 0 ; e = 1 
    f = 1 ; g = 0 
    k = 0 ; fw3 = 0 ; fw3yilingqu = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "天台":
            if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("天台网电共发放",a + b)
    print("天台网电已领取",a)

    while e <= hangshu - 1:
        s = sheet1.cell_value(e,13)
        jigou = sheet1.cell_value(e,2)
        qudao = sheet1.cell_value(e,3)
        if jigou == "天台": 
            if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                if s == "已领用":
                    c += 1
                elif s == "未领用":
                    d += 1
        e += 1
    print("天台非电共发放",c + d)
    print("天台非网电已领取",c)
    print("天台合计共发放", a + b + c + d)
    print("天台合计已领取", a + c)

    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = sheet1.cell_value(f,12)
        lingquriqi = str(sheet1.cell_value(f,14))
        if 44256 <= fafangriqi < 44287 :
            if jigou == "天台":
                if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "天台": 
                    if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                        k += 1
        if 44256 <= fafangriqi < 44287 :
            if jigou == "天台":
                if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                    fw3 += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "天台": 
                    if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                        fw3yilingqu += 1
        f += 1
    print("天台3月网电共发放:",g )
    print("天台3月网电已领取:",k)
    print("天台3月非网电共发放:",fw3)
    print("天台3月非网电已领取:",fw3yilingqu)
    print("天台3月合计共发放:",g + fw3)
    print("天台3月合计已领取:",k + fw3yilingqu)
    print("-----------------------------------------")

def 温岭():
    i = 1 ; a = 0 ; b = 0 
    c = 0 ; d = 0 ; e = 1 
    f = 1 ; g = 0 
    k = 0 ; fw3 = 0 ; fw3yilingqu = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "温岭":
            if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("温岭网电共发放",a + b)
    print("温岭网电已领取",a)

    while e <= hangshu - 1:
        s = sheet1.cell_value(e,13)
        jigou = sheet1.cell_value(e,2)
        qudao = sheet1.cell_value(e,3)
        if jigou == "温岭": 
            if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                if s == "已领用":
                    c += 1
                elif s == "未领用":
                    d += 1
        e += 1
    print("温岭非电共发放",c + d)
    print("温岭非网电已领取",c)
    print("温岭合计共发放", a + b + c + d)
    print("温岭合计已领取", a + c)

    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = sheet1.cell_value(f,12)
        lingquriqi = str(sheet1.cell_value(f,14))
        if 44256 <= fafangriqi < 44287 :
            if jigou == "温岭":
                if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "温岭": 
                    if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                        k += 1
        if 44256 <= fafangriqi < 44287 :
            if jigou == "温岭":
                if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                    fw3 += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "温岭": 
                    if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                        fw3yilingqu += 1
        f += 1
    print("温岭3月网电共发放:",g )
    print("温岭3月网电已领取:",k)
    print("温岭3月非网电共发放:",fw3)
    print("温岭3月非网电已领取:",fw3yilingqu)
    print("温岭3月合计共发放:",g + fw3)
    print("温岭3月合计已领取:",k + fw3yilingqu)
    print("-----------------------------------------")

def 仙居():
    i = 1 ; a = 0 ; b = 0 
    c = 0 ; d = 0 ; e = 1 
    f = 1 ; g = 0 
    k = 0 ; fw3 = 0 ; fw3yilingqu = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "仙居":
            if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("仙居网电共发放",a + b)
    print("仙居网电已领取",a)

    while e <= hangshu - 1:
        s = sheet1.cell_value(e,13)
        jigou = sheet1.cell_value(e,2)
        qudao = sheet1.cell_value(e,3)
        if jigou == "仙居": 
            if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                if s == "已领用":
                    c += 1
                elif s == "未领用":
                    d += 1
        e += 1
    print("仙居非电共发放",c + d)
    print("仙居非网电已领取",c)
    print("仙居合计共发放", a + b + c + d)
    print("仙居合计已领取", a + c)

    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = sheet1.cell_value(f,12)
        lingquriqi = str(sheet1.cell_value(f,14))
        if 44256 <= fafangriqi < 44287 :
            if jigou == "仙居":
                if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "仙居": 
                    if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                        k += 1
        if 44256 <= fafangriqi < 44287 :
            if jigou == "仙居":
                if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                    fw3 += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "仙居": 
                    if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                        fw3yilingqu += 1
        f += 1
    print("仙居3月网电共发放:",g )
    print("仙居3月网电已领取:",k)
    print("仙居3月非网电共发放:",fw3)
    print("仙居3月非网电已领取:",fw3yilingqu)
    print("仙居3月合计共发放:",g + fw3)
    print("仙居3月合计已领取:",k + fw3yilingqu)
    print("-----------------------------------------")

def 玉环楚门():
    i = 1 ; a = 0 ; b = 0 
    c = 0 ; d = 0 ; e = 1 
    f = 1 ; g = 0 
    k = 0 ; fw3 = 0 ; fw3yilingqu = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "玉环" or jigou == "楚门":
            if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("玉环楚门网电共发放",a + b)
    print("玉环楚门网电已领取",a)

    while e <= hangshu - 1:
        s = sheet1.cell_value(e,13)
        jigou = sheet1.cell_value(e,2)
        qudao = sheet1.cell_value(e,3)
        if jigou == "玉环" or jigou == "楚门": 
            if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                if s == "已领用":
                    c += 1
                elif s == "未领用":
                    d += 1
        e += 1
    print("玉环楚门非电共发放",c + d)
    print("玉环楚门非网电已领取",c)
    print("玉环楚门合计共发放", a + b + c + d)
    print("玉环楚门合计已领取", a + c)

    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = sheet1.cell_value(f,12)
        lingquriqi = str(sheet1.cell_value(f,14))
        if 44256 <= fafangriqi < 44287 :
            if jigou == "玉环" or jigou == "楚门":
                if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "玉环" or jigou == "楚门": 
                    if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                        k += 1
        if 44256 <= fafangriqi < 44287 :
            if jigou == "玉环" or jigou == "楚门":
                if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                    fw3 += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "玉环" or jigou == "楚门": 
                    if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                        fw3yilingqu += 1
        f += 1
    print("玉环楚门3月网电共发放:",g )
    print("玉环楚门3月网电已领取:",k)
    print("玉环楚门3月非网电共发放:",fw3)
    print("玉环楚门3月非网电已领取:",fw3yilingqu)
    print("玉环楚门3月合计共发放:",g + fw3)
    print("玉环楚门3月合计已领取:",k + fw3yilingqu)
    print("-----------------------------------------")

def 临海杜桥():
    i = 1 ; a = 0 ; b = 0 ; c = 0 ; d = 0 ; e = 1 
    f = 1 ; g = 0 ; k = 0 ; fw3 = 0 ; fw3yilingqu = 0
    
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "临海" or jigou == "杜桥":
            if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("临海杜桥门网电共发放",a + b)
    print("临海杜桥网电已领取",a)

    while e <= hangshu - 1:
        s = sheet1.cell_value(e,13)
        jigou = sheet1.cell_value(e,2)
        qudao = sheet1.cell_value(e,3)
        if jigou == "临海" or jigou == "杜桥": 
            if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                if s == "已领用":
                    c += 1
                elif s == "未领用":
                    d += 1
        e += 1
    print("临海杜桥非电共发放",c + d)
    print("临海杜桥非网电已领取",c)
    print("临海杜桥合计共发放", a + b + c + d)
    print("临海杜桥合计已领取", a + c)

    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = sheet1.cell_value(f,12)
        lingquriqi = str(sheet1.cell_value(f,14))
        if 44256 <= fafangriqi < 44287 :
            if jigou == "临海" or jigou == "杜桥":
                if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "临海" or jigou == "杜桥": 
                    if qudao == "电销" or qudao == "梦客" or qudao == "网销":
                        k += 1
        if 44256 <= fafangriqi < 44287 :
            if jigou == "临海" or jigou == "杜桥":
                if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                    fw3 += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "临海" or jigou == "杜桥": 
                    if qudao != "电销" and qudao != "梦客" and qudao != "网销":
                        fw3yilingqu += 1
        f += 1
    print("临海杜桥3月网电共发放:",g )
    print("临海杜桥3月网电已领取:",k)
    print("临海杜桥3月非网电共发放:",fw3)
    print("临海杜桥3月非网电已领取:",fw3yilingqu)
    print("临海杜桥3月合计共发放:",g + fw3)
    print("临海杜桥3月合计已领取:",k + fw3yilingqu)
    print("-----------------------------------------")

def 本级车商():
    i = 1;a = 0;b = 0
    f = 1;k = 0;g = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "本级":
            if qudao == "车商":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("本级车商共发放:",a + b )
    print("本级车商已领取:",a)
    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = str(sheet1.cell_value(f,12))
        lingquriqi = str(sheet1.cell_value(f,14))
        if str(44256) <= fafangriqi < str(44287) :
            if jigou == "本级":
                if qudao == "车商":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "本级": 
                    if qudao == "车商":
                        k += 1
        f += 1
    print("本级车商3月共发放:",g )
    print("本级车商3月已领取:",k)
    print("-----------------------------------------")

def 本级新渠道():
    i = 1;a = 0;b = 0
    f = 1;k = 0;g = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "本级":
            if qudao == "电销" or qudao == "梦客":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("本级新渠道共发放:",a + b )
    print("本级新渠道已领取:",a)
    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = str(sheet1.cell_value(f,12))
        lingquriqi = str(sheet1.cell_value(f,14))
        if str(44256) <= fafangriqi < str(44287) :
            if jigou == "本级":
                if qudao == "电销" or qudao == "梦客":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "本级": 
                    if qudao == "电销" or qudao == "梦客":
                        k += 1
        f += 1
    print("本级新渠道3月共发放:",g )
    print("本级新渠道3月已领取:",k)
    print("-----------------------------------------")

def 本级经代():
    i = 1;a = 0;b = 0
    f = 1;k = 0;g = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "本级":
            if qudao == "经代":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("本级经代共发放:",a + b )
    print("本级经代已领取:",a)
    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = str(sheet1.cell_value(f,12))
        lingquriqi = str(sheet1.cell_value(f,14))
        if str(44256) <= fafangriqi < str(44287) :
            if jigou == "本级":
                if qudao == "经代":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "本级": 
                    if qudao == "经代":
                        k += 1
        f += 1
    print("本级经代3月共发放:",g )
    print("本级经代3月已领取:",k)
    print("-----------------------------------------")

def 本级门店():
    i = 1;a = 0;b = 0
    f = 1;k = 0;g = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "本级":
            if qudao == "门店":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("本级门店共发放:",a + b )
    print("本级门店已领取:",a)
    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = str(sheet1.cell_value(f,12))
        lingquriqi = str(sheet1.cell_value(f,14))
        if str(44256) <= fafangriqi < str(44287) :
            if jigou == "本级":
                if qudao == "门店":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "本级": 
                    if qudao == "门店":
                        k += 1
        f += 1
    print("本级门店3月共发放:",g )
    print("本级门店3月已领取:",k)
    print("-----------------------------------------")

def 本级网销():
    i = 1;a = 0;b = 0
    f = 1;k = 0;g = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "本级":
            if qudao == "网销":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("本级网销共发放:",a + b )
    print("本级网销已领取:",a)
    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = str(sheet1.cell_value(f,12))
        lingquriqi = str(sheet1.cell_value(f,14))
        if str(44256) <= fafangriqi < str(44287) :
            if jigou == "本级":
                if qudao == "网销":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "本级": 
                    if qudao == "网销":
                        k += 1
        f += 1
    print("本级网销3月共发放:",g )
    print("本级网销3月已领取:",k)
    print("-----------------------------------------")

def 本级银保():
    i = 1;a = 0;b = 0
    f = 1;k = 0;g = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "本级":
            if qudao == "银保":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("本级银保共发放:",a + b )
    print("本级银保已领取:",a)
    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = str(sheet1.cell_value(f,12))
        lingquriqi = str(sheet1.cell_value(f,14))
        if str(44256) <= fafangriqi < str(44287) :
            if jigou == "本级":
                if qudao == "银保":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "本级": 
                    if qudao == "银保":
                        k += 1
        f += 1
    print("本级银保3月共发放:",g )
    print("本级银保3月已领取:",k)
    print("-----------------------------------------")

def 本级直管():
    i = 1;a = 0;b = 0
    f = 1;k = 0;g = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "本级":
            if qudao == "直管":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("本级直管共发放:",a + b )
    print("本级直管已领取:",a)
    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = str(sheet1.cell_value(f,12))
        lingquriqi = str(sheet1.cell_value(f,14))
        if str(44256) <= fafangriqi < str(44287) :
            if jigou == "本级":
                if qudao == "直管":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "本级": 
                    if qudao == "直管":
                        k += 1
        f += 1
    print("本级直管3月共发放:",g )
    print("本级直管3月已领取:",k)
    print("-----------------------------------------")

def 本级重客():
    i = 1;a = 0;b = 0
    f = 1;k = 0;g = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "本级":
            if qudao == "重客":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("本级重客共发放:",a + b )
    print("本级重客已领取:",a)
    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = str(sheet1.cell_value(f,12))
        lingquriqi = str(sheet1.cell_value(f,14))
        if str(44256) <= fafangriqi < str(44287) :
            if jigou == "本级":
                if qudao == "重客":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "本级": 
                    if qudao == "重客":
                        k += 1
        f += 1
    print("本级重客3月共发放:",g )
    print("本级重客3月已领取:",k)
    print("-----------------------------------------")

def 本级综拓():
    i = 1;a = 0;b = 0
    f = 1;k = 0;g = 0
    while i <= hangshu - 1:
        s = sheet1.cell_value(i,13)
        jigou = sheet1.cell_value(i,2)
        qudao = sheet1.cell_value(i,3)
        if jigou == "本级":
            if qudao == "综拓":
                if s == "已领用":
                    a += 1
                elif s == "未领用":
                    b += 1
        i += 1
    print("本级综拓共发放:",a + b )
    print("本级综拓已领取:",a)
    while f <= hangshu-1:  # 当行数小于总行数即行数有效时，执行以下代码
        s = sheet1.cell_value(f,13) # 获取第i行，第13列第单元格内第值，可根据时间需要更改
        jigou = sheet1.cell_value(f,2)
        qudao = sheet1.cell_value(f,3)
        fafangriqi = str(sheet1.cell_value(f,12))
        lingquriqi = str(sheet1.cell_value(f,14))
        if str(44256) <= fafangriqi < str(44287) :
            if jigou == "本级":
                if qudao == "综拓":
                    g += 1
        if len(lingquriqi) != 0:                
            if str(44256) <= lingquriqi < str(44287) :
                if jigou == "本级": 
                    if qudao == "综拓":
                        k += 1
        f += 1
    print("本级综拓3月共发放:",g )
    print("本级综拓3月已领取:",k)
    print("-----------------------------------------")

本级车商()
本级新渠道()
本级经代()
本级门店()
本级网销()
本级银保()
本级直管()
本级重客()
本级综拓()
黄岩()
路桥()
玉环楚门()
临海杜桥()
三门()
天台()
温岭()
仙居()