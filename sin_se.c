#include<iostream>
#include<cmath>
using namespace std;
const double TINY_VALUE = 1e-10;  //计算精度

double sin_se(double x) {   //为了和标准库中的sin()函数区别，所以取名为sin_se()函数
     double n = x,sum=0;
      int i = 1;
      do
     {
         sum += n;
         i++;
         n = -n * x*x / (2 * i - 1) / (2 * i - 2);
         
         } while (fabs(n)>=TINY_VALUE);
     return sum;
 }
 int main() {
     int r, s;
     double k;
     cin >> r >> s;
     if (r*r <= s * s) 
         k = sqrt(sin_se(r)*sin_se(r) + sin_se(s)*sin_se(s));
     else 
         k = sin_se(r*s) /2 ;
     cout << k;
     return 0;
 }
