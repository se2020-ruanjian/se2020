#include<iostream>
#include<cmath>
using namespace std;
const double TINY_VALUE = 1e-10;  //计算精度

double se_sin(double x) {   //为了和标准库中的sin()函数区别，所以取名为se_sin()函数
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
         k = sqrt(se_sin(r)*se_sin(r) + se_sin(s)*se_sin(s));
     else 
         k = se_sin(r*s) /2 ;
     cout << k;
     return 0;
 }
