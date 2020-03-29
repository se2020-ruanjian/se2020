function [t]=sin_se(s)
%初始化
x = 1;
y = 0;
z = s * pi /180;
a = 0;
d = 1;
k = 0.6073; %k为增益
x = k*x;
while a<100 %此处不能判断d的负号控制循环，会死循环。应用a次数控制。
    if z>=0
        d = 1;
    else d = -1;
    end
%迭代
    xNew = x;
    x = xNew-(y*d*(1/2^a));
    y = y+(xNew*d*(1/2^a));
    z = z-(d*(atan(1/2^a)));
    a = a+1;
end
t = y;
end
