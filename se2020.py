from tkinter import *
import numpy as np
import matlab.engine
eng = matlab.engine.start_matlab()

root = Tk()

sv0=StringVar()
sv1=StringVar()
sv2=StringVar()
sv3=StringVar()
sv4=StringVar()    #Input and output initialization

l1=Label(text="三角函数",font=('KaiTi',12,'bold'))
l1.grid(row=0,column=0,columnspan=2)        #Title and Title Location

#input grid location initialization
i1=Entry()
i1.grid(row=3,column=1)
i1.config(textvariable=sv0)
in1=Label(text="请输入",font=('KaiTi',12,'bold'))
in1.grid(row=3,column=0)

#output grid location initialization
o1=Entry()
o1.grid(row=4,column=1)
o1.config(textvariable=sv1, state='readonly')
out1=Label(text="sin:",font=('KaiTi',12,'bold'))
out1.grid(row=4,column=0)

o2=Entry()
o2.grid(row=5,column=1)
o2.config(textvariable=sv2, state='readonly')
out2=Label(text="cos:",font=('KaiTi',12,'bold'))
out2.grid(row=5,column=0)

o3=Entry()
o3.grid(row=6,column=1)
o3.config(textvariable=sv3, state='readonly')
out3=Label(text="tan:",font=('KaiTi',12,'bold'))
out3.grid(row=6,column=0)

o4=Entry()
o4.grid(row=7,column=1)
o4.config(textvariable=sv4, state='readonly')
out4=Label(text="cot:",font=('KaiTi',12,'bold'))
out4.grid(row=7,column=0)


#button function,角度/弧度的转换
def h1():         #Angle and radian control button
    if bt1['text']=='弧度':
        bt1['text']='角度'
        print('弧度')
    else:
        bt1['text']='弧度'
        print('角度')

#实现计算
def h2():
    sv1.set(eng.sin_se(float(sv0.get())))
    sv2.set(eng.cos_se(float(sv0.get())))
    sv3.set(eng.tan_se(float(sv0.get())))
    sv4.set(eng.cot_se(float(sv0.get())))

bt1=Button(root,text='弧度',font=('KaiTi',12,'bold'),width=5,height=2,command=h1)
bt1.grid(row=1,column=0,columnspan=1,rowspan=2,sticky='e')

if bt1['text']=='角度' :
    str = float(sv0.get() * np.pi/180)
else:
    str = sv0.get()    #Conversion formula of angle and radian

bt2=Button(text="计算",font=('KaiTi',12,'bold'),width=5,height=2, command=h2)
bt2.grid(row=1,column=1,columnspan=1,rowspan=2,sticky='e')

root.mainloop()
