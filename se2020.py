#! /usr/bin/env python   
# -*- coding: utf-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding('utf8') 

from Tkinter import *
import numpy as np
import matlab.engine
from ctypes import *

#调用编写的三角函数的python模块
from sin_se import sin_se_p
from cos_se import cos_se_p
from tan_se import tan_se_p
from cot_se import cot_se_p

root = Tk()

#调用matlab中m文件函数
eng = matlab.engine.start_matlab()

#加载编译好的so文件
#sinse = CDLL('./sin_se.so')
#调用c文件的函数sin_se.sin_se(),实现sin的计算

sv0=StringVar()
sv1=StringVar()
sv2=StringVar()
sv3=StringVar()
sv4=StringVar()
sv5=StringVar()
sv6=StringVar()
sv7=StringVar()
sv8=StringVar()  #Input and output initialization

#界面编写
l1=Label(text="三角函数",font=('KaiTi',12,'bold'))
l1.grid(row=0,column=0,columnspan=2)        #Title and Title Location

#input grid location initialization
i1=Entry()
i1.grid(row=3,column=1)
i1.config(textvariable=sv0)
in1=Label(text="请输入角度",font=('KaiTi',12,'bold'))
in1.grid(row=3,column=0)

in1=Label(text="matlab语言：",font=('KaiTi',12,'bold'))
in1.grid(row=4,column=0)

#output grid location initialization
o1=Entry()
o1.grid(row=5,column=1)
o1.config(textvariable=sv1, state='readonly')
out1=Label(text="sin:",font=('KaiTi',12,'bold'))
out1.grid(row=5,column=0)

o2=Entry()
o2.grid(row=6,column=1)
o2.config(textvariable=sv2, state='readonly')
out2=Label(text="cos:",font=('KaiTi',12,'bold'))
out2.grid(row=6,column=0)

o3=Entry()
o3.grid(row=7,column=1)
o3.config(textvariable=sv3, state='readonly')
out3=Label(text="tan:",font=('KaiTi',12,'bold'))
out3.grid(row=7,column=0)

o4=Entry()
o4.grid(row=8,column=1)
o4.config(textvariable=sv4, state='readonly')
out4=Label(text="cot:",font=('KaiTi',12,'bold'))
out4.grid(row=8,column=0)

in1=Label(text="python语言：",font=('KaiTi',12,'bold'))
in1.grid(row=10,column=0)

o5=Entry()
o5.grid(row=11,column=1)
o5.config(textvariable=sv5, state='readonly')
out5=Label(text="sin:",font=('KaiTi',12,'bold'))
out5.grid(row=11,column=0)

o6=Entry()
o6.grid(row=12,column=1)
o6.config(textvariable=sv6, state='readonly')
out6=Label(text="cos:",font=('KaiTi',12,'bold'))
out6.grid(row=12,column=0)

o7=Entry()
o7.grid(row=13,column=1)
o7.config(textvariable=sv7, state='readonly')
out7=Label(text="tan:",font=('KaiTi',12,'bold'))
out7.grid(row=13,column=0)

o8=Entry()
o8.grid(row=14,column=1)
o8.config(textvariable=sv8, state='readonly')
out8=Label(text="cot:",font=('KaiTi',12,'bold'))
out8.grid(row=14,column=0)


#button function,角度/弧度的转换
def h1():         #Angle and radian control button
    if bt1['text']=='弧度':
        bt1['text']='角度'
        print('弧度')
    else:
        bt1['text']='弧度'
        print('角度')

#radian = float(sv0.get()) * np.pi/180

#实现计算
def h2():
    radian = float(sv0.get())
    sv1.set(round(eng.sin_se(radian),3))
    sv2.set(eng.cos_se(radian))           #精度已在cos_se的m文件中控制
    sv3.set(round(eng.tan_se(radian),3))
    sv4.set(round(eng.cot_se(radian),3))
    sv5.set(round(sin_se_p(radian),3))
    sv6.set(round(cos_se_p(radian),3))
    sv7.set(round(tan_se_p(radian),3))
    sv8.set(round(cot_se_p(radian),3))

bt1=Button(root,text='弧度',font=('KaiTi',12,'bold'),width=5,height=2,command=h1)
bt1.grid(row=1,column=0,columnspan=1,rowspan=2,sticky='e')

if bt1['text']=='角度' :
    str = float(sv0.get() * np.pi/180)
else:
    str = sv0.get()    #Conversion formula of angle and radian

bt2=Button(text="计算",font=('KaiTi',12,'bold'),width=5,height=2, command=h2)
bt2.grid(row=1,column=1,columnspan=1,rowspan=2,sticky='e')

root.mainloop()
