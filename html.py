import plotly as py
import plotly.graph_objs as go
import numpy as np
import datetime

 
pyplt = py.offline.plot


def plot(rd3,rd1): 
    # datex：交易日
    aw = 800
    bh = 400
    trace3 = go.Scatter(
        y = rd3,
        fill = 'tonexty',
        #mode= 'lines', # 无边界线
        line_shape = 'spline',
        #width=aw, height=bh,
        name = "Strategy"
    )
    trace1 = go.Scatter(
        y = rd1,
        #mode= 'lines', # 无边界线
        line_shape = 'spline',
        #width=aw, height=bh,
        name = "HS300"
    )
    data = [trace3,trace1]
    
    layout = dict(
                xaxis = dict(),
                yaxis = dict(),
                width=800, height=400,
                margin=dict(l=40, r=40, t=40, b=40),
                #paper_bgcolor='rgba(0,0,0,0)',
                #plot_bgcolor='rgba(0,0,0,0)'
        )
    fig = go.Figure(data = data, layout = layout)
    fig.write_image('./vueblog/hope/.vuepress/public/invest.png',engine='kaleido')

    #pyplt(fig, filename='./vueblog/hope/.vuepress/public/1.html')

def getYesterday():
       # 获取昨天日期的字符串格式的函数
   #获取今天的日期
   today = datetime.date.today()
   #获取一天的日期格式数据
   oneday = datetime.timedelta(days=1)
   #昨天等于今天减去一天
   yesterday = today - oneday
   #获取昨天日期的格式化字符串
   yesterdaystr = yesterday.strftime('%Y-%m-%d')
   #返回昨天的字符串
   return yesterdaystr

yes = getYesterday()
jz = [0,0]

def readtoday():
    #date01 = datetime.date.today()
    #date01 = datetime.datetime.now().strftime('%Y-%m-%d')
    print("录入最新数据")
    print("输入总资产收益率(涨乐基础上加7.32%，直接输入涨乐收益率)：")
    a3 = round(float(input())+7.32,2)
    print("输入沪深300截至收益率,输入华泰沪深300累计")
    b2 = round(float(input())-13.37+3.1,2)
    return [a3,b2]  
    

def writedata(jz):
    f = open('data.txt',"w")
    f.write(str(jz)+'\n')
    print(f)
    f.close
    
def readdata():
    f = open('data.txt',"r")
    file = f.readlines()
    a = len(file)
    print(file)
    i =0 
    datas = []
    d13 = []
    d14 = []
    while i < a:
        tmp = file[i][1:-2]
        print(tmp)
        datas = tmp.split(',')
        d13.append(float(datas[0]))
        d14.append(float(datas[1]))
        i=i+1 
    return d13,d14

def read300():
    f = open('hs300.txt',"r")
    file = f.readlines()
    a = len(file)
    b,c = readdata()
    i= 0
    data=[]
    f = open('1111.txt',"w")
    while i < a:
        tmp = [str(b[i]),str(c[i]),str(file[i][0:-1])]
        i = i+1
        f.write(str(tmp)+'\n')
    f.close

def init():
    writedata(jz)

def updatedata(today):
    f = open('data.txt',"a")
    f.write(str(today)+'\n')
    f.close
    
def update():
    today = readtoday()
    updatedata(today)

print("1=初始化，2=新增,3=绘图")
chose = input()
if chose == '1':
    init()
else:
    if chose == '2':
        update()
        rd3,rd1 = readdata()
        plot(rd3,rd1)
    else:
        rd3,rd1 = readdata()
        plot(rd3,rd1)
        
            

