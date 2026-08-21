import random,csv

# 完成“游戏”功能函数PlayGame()（40分）

def PlayGame():
    print('*****游戏开始*****')
    p2=input("请输入您想要的3张牌的牌号(1~52，用空格分隔不同牌号)").split()
    a=int(p2[0])
    b=int(p2[1])
    c=int(p2[2])
    p=[]
    com=[]
    p1=[]
    c1=[]
    p.append(a)
    p.append(b)
    p.append(c)   



    suits = ['♦', '♣', '♥', '♠']

    faces = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
    def j(n):
        n=n-1
        f=n//4
        s=n%4
        cs=suits[s]+faces[f]
        return cs
    d=random.randint(1, 52)
    e=random.randint(1, 52)
    f=random.randint(1, 52)
    com.append(d)
    com.append(e)
    com.append(f)
    p1.append(j(a))
    p1.append(j(b))
    p1.append(j(c))
    c1.append(j(d))
    c1.append(j(e))
    c1.append(j(f))
    l1=max(p)
    l2=max(com)
    print(f"您抽到的牌分别是：{p1}")
    print(f"电脑抽到的牌分别是：{c1}")
    if l1>=l2:
        print(f"您最大的牌是：{j(int(max(p)))},电脑最大的牌是{j(max(com))}。您赢了……")
    else:
        print(f"您最大的牌是：{j(int(max(p)))},电脑最大的牌是{j(max(com))}。您输了……")
    


    






    

    
    print('*****游戏结束*****\n') 


# 完成“学习”功能函数Learning()（50分）
def Learning():
    d=[]
    with open('学习资料.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            d.append(row)
    print("--学习<二级菜单>--")       
    print("1：自学")
    print("2：自测")
    print("0：返回主菜单")
    print("----------------")
    n=int(input("请输入操作选项："))
    def l1():
        for i in d[1::]:
            print()
            print(i[0])
            if i[5] in ['A','a']:
                print(f"答案：{i[1]}")
            if i[5] in ['B','b']:
                print(f"答案：{i[2]}")
            if i[5] in ['C','c']:
                print(f"答案：{i[3]}")
            if i[5] in ['D','d']:
                print(f"答案：{i[4]}")
        print()
        print("----这是底线----")
            
    def l2():
        r=0
        t=0
        for i in range(5):
            n=random.randint(1,11)
            print(d[n][0])
            print(f"<A>{d[n][1]}")
            print(f"<B>{d[n][2]}")
            print(f"<C>{d[n][3]}")
            print(f"<D>{d[n][4]}")
            o=input("请输入：")
                
            if o in [d[n][5],d[n][5].lower()]:
                r+=20
                t+=1
                
                print("正确")
            else:
                print("错误")
        print(f"本次自测，答对{t}题，成绩为：{r}分。")
        print("*****自测结束*****")
        
            
        









        
    if n==1:
        l1()
    elif n==2:
        l2()
    # 读取csv文件
    # 显示二级菜单，选择【自学】、【自测】或【返回主菜单】
    # 选择【自学】的操作
    # 选择【自测】的操作
    
    # 请在该行下方完成Learning()函数

    ''' 该部分为可能用到的输出信息模板
    ----这是底线----
    输入选项错误，请重试……      
    随机抽取5道测试题，答对1题得20分，答错则不得分。
    *****自测开始*****
    *****自测结束*****
    请选择:
    本次自测，答对N题，成绩为S分。
    '''
    
    # 请在该行上方完成Learning()函数


# 主程序（10分）
# 若主程序能够正常启动运行，最高可得10分
while True: 
    print('==课程项目<主菜单>==')
    print('1：学习\n2：游戏\n0：退出')
    print('------------------')
    oprate=input('请输入操作选项：')
    print()
    if oprate=='1':        
        Learning()
        
    elif oprate=='2':        
        PlayGame()
        
    elif oprate == '0':
        break
    else:
        print('输入选项错误，请重试……')
   
print('===退出<课程项目>===')
