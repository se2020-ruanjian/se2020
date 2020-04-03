#! /usr/bin/env python   
# -*- coding: utf-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding('utf8') 

from Tkinter import *
import numpy as np
import matlab.engine
from ctypes import *
import math

#调用编写的三角函数的python模块
from sin_se import sin_se_p
from cos_se import cos_se_p
from tan_se import tan_se_p
from cot_se import cot_se_p

root = Tk()

#调用matlab中m文件函数
eng = matlab.engine.start_matlab()

#调用c语言文件中函数
sin_c = CDLL('./sin_se.so')
cos_c = CDLL('./cos_se.so')
tan_c = CDLL('./tan_se.so')
cot_c = CDLL('./cot_se.so')

sin_se_c = sin_c.sin_se
sin_se_c.restype = c_float

cos_se_c = cos_c.cos_se
cos_se_c.restype = c_float

tan_se_c = tan_c.tan_se
tan_se_c.restype = c_float

cot_se_c = cot_c.cot_se
cot_se_c.restype = c_float

sv0=StringVar()    #sv0为输入
sv1=StringVar()    #sv1~4为matlab语言的输出
sv2=StringVar()
sv3=StringVar()
sv4=StringVar()
sv5=StringVar()    #sv5~8为python语言的输出
sv6=StringVar()
sv7=StringVar()
sv8=StringVar() 
sv9=StringVar()    #sv9~12为c语言的输出
sv10=StringVar()
sv11=StringVar()
sv12=StringVar()

#界面编写
l1=Label(text="三角函数计算",font=('KaiTi',12,'bold'))
l1.grid(row=0,column=0,columnspan=2)        #Title and Title Location

#输入网格
i1=Entry()
i1.grid(row=3,column=1)
i1.config(textvariable=sv0)
in1=Label(text="请输入：",font=('KaiTi',12,'bold'))
in1.grid(row=3,column=0)

#输出网格,matlab
in1=Label(text="matlab语言：",font=('KaiTi',12,'bold'))
in1.grid(row=4,column=0)

o1=Entry()
o1.grid(row=6,column=1)
o1.config(textvariable=sv1, state='readonly')
out1=Label(text="sin:",font=('KaiTi',12,'bold'))
out1.grid(row=6,column=0)

o2=Entry()
o2.grid(row=7,column=1)
o2.config(textvariable=sv2, state='readonly')
out2=Label(text="cos:",font=('KaiTi',12,'bold'))
out2.grid(row=7,column=0)

o3=Entry()
o3.grid(row=8,column=1)
o3.config(textvariable=sv3, state='readonly')
out3=Label(text="tan:",font=('KaiTi',12,'bold'))
out3.grid(row=8,column=0)

o4=Entry()
o4.grid(row=9,column=1)
o4.config(textvariable=sv4, state='readonly')
out4=Label(text="cot:",font=('KaiTi',12,'bold'))
out4.grid(row=9,column=0)

#输出网格,python
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

#输出网格,c语言
in1=Label(text="c语言：",font=('KaiTi',12,'bold'))
in1.grid(row=15,column=0)

o9=Entry()
o9.grid(row=16,column=1)
o9.config(textvariable=sv9, state='readonly')
out9=Label(text="sin:",font=('KaiTi',12,'bold'))
out9.grid(row=16,column=0)
o10=Entry()
o10.grid(row=17,column=1)
o10.config(textvariable=sv10, state='readonly')
out10=Label(text="cos:",font=('KaiTi',12,'bold'))
out10.grid(row=17,column=0)
o11=Entry()
o11.grid(row=18,column=1)
o11.config(textvariable=sv11, state='readonly')
out11=Label(text="tan:",font=('KaiTi',12,'bold'))
out11.grid(row=18,column=0)
o12=Entry()
o12.grid(row=19,column=1)
o12.config(textvariable=sv12, state='readonly')
out12=Label(text="cot:",font=('KaiTi',12,'bold'))
out12.grid(row=19,column=0)

#button function,角度/弧度的转换
def h1():         #Angle and radian control button
    if bt1['text']=='弧度':
        bt1['text']='角度'

    else:
        bt1['text']='弧度'


#radian = float(sv0.get()) * np.pi/180

#实现计算
def h2():
    str = float(sv0.get())
    if bt1['text']=='弧度':
        str = str * (180/np.pi)     #所有函数输入角度，这里进行弧度角度转换
    sv1.set(eng.sin_se(str))    #1~4matlab输出值
    sv2.set(eng.cos_se(str))
    sv3.set(eng.tan_se(str))
    sv4.set(eng.cot_se(str))
    
    sv5.set(sin_se_p(str))      #5~8python输出值
    sv6.set(cos_se_p(str))
    sv7.set(tan_se_p(str))
    sv8.set(cot_se_p(str))
    
    a = float(sv0.get()) #9~12c输出值
    if bt1['text']=='弧度':
        a = (a *180/np.pi) + 360   #所有函数输入角度，这里进行弧度角度转换
    a = c_float(a)
    sin = sin_se_c(a)
    cos = cos_se_c(a)
    tan = tan_se_c(a)
    cot = cot_se_c(a)
    
    sin = ("%.16f" % sin)
    cos = ("%.16f" % cos)
    tan = ("%.16f" % tan)
    cot = ("%.16f" % cot)
    
    sv9.set(sin)
    sv10.set(cos)
    sv11.set(tan)
    sv12.set(cot)

bt1=Button(root,text='角度',font=('KaiTi',12,'bold'),width=5,height=2,command=h1)
bt1.grid(row=1,column=0,sticky='e')


bt2=Button(text="计算",font=('KaiTi',12,'bold'),width=5,height=2, command=h2)
bt2.grid(row=1,column=1,sticky='e')

root.mainloop()
