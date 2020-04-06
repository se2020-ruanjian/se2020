# se2020
1.项目说明
========
   该软件基于python,matlab,C三种语言开发，实现了三角函数(sin,cos,tan,cot)的计算，目前处于1.0版本。
   目标：使用python语言完成主函数，界面以及接口设计；使用python,matlab和C语言分别实现四种三角函数。使用三种语言，方便后期在测试阶段进行精度比较，在2.0版本可以进行取舍，选择精度更高的两种语言。
   
2.文件说明
--------
   项目中一共涉及四种文件，分别为py文件，c文件，so文件，m文件
   py文件：①se2020.py是程序的主函数，1.0版本功能是对软件的总体界面进行搭建、角度弧度转换以及接口设计(对三种语言设计的三角函数进行调用)。界面一共包括软件标题、角度弧度转换按钮、计算按钮、一个输入框、12个输出框（三种语言的四个三角函数输出）。界面展示图在下面第4部分。
          ②sin_se.py：是实现sin函数的功能模块，其他三个py文件功能相同。
   c文件：sin_se.c是c语言编写的文件，实现sin函数的功能模块，其他三个c文件功能相同。
   so文件：sin_se.so，so文件是通过gcc对c文件进行编译得到，用来python语言对c语言写的模块进行调用。
   m文件：sin_se.m是matlab语言编写的文件，实现sin函数的功能模块，其他三个m文件功能相同。
   说明文档.doc文件：对本项目的说明，包括可行性研究报告，需求分析文档，项目计划书（流程框图表示）。

3.软件安装
--------
   请先下载该项目github上的所有程序文件，本软件需要安装matlab和python。(经测试matlab2016支持python2.7/3.3/3.4版本，matlab2019支持python2.7/3.6/3.7)
   安装完成之后，请运行se2020.py文件，由于本软件使用python语言调用matlab语言混合编程，如若报错“ImportError: No module named matlab.engine"，请查看教程：https://blog.csdn.net/william_hehe/article/details/82828873 以解决。

4.使用说明及界面展示
---------
   运行se2020.py，启动三角函数计算器，界面如下：
   ![](https://raw.githubusercontent.com/se2020-ruanjian/se2020/master/1.png)
   点击角度弧度按钮可以实现输入角度和输入弧度进行转换，在输入框进行输入后，点击计算按钮进行计算，结果将展示在输出框内，如下图：
   输入角度：45°
   ![](https://raw.githubusercontent.com/se2020-ruanjian/se2020/master/2.png)
   输入弧度:1.4072(π/3)
   ![](https://raw.githubusercontent.com/se2020-ruanjian/se2020/master/3.png)

