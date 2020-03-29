#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define PI 3.141592

double Factorial(int n)      //阶乘
{
	//long long 占8个字节
	double i, factorial = 1;

	for (i = 1; i <= n ; i++)
	{
		factorial *= i;
	}
	
	return factorial;
}

double tan_se(double x)
{
	if (x != 0 && (fmod(x,90)== 0 || fmod(x,-90) == 0))
	{
	return 9999;
	}
	else
	{
		double y = 0.0,z = 1.0;  //y = sinx;z = cos x
	int m1,m2;
	x = (fmod(x,360) * PI / 180);    
	for(m1 = 1; m1 <= 20; m1++)    //sinx 的泰勒，m1控制后面加到第几项
	{
		if (m1 % 2 == 0)
		{
			y -= pow(x, (2 * m1 - 1 )) / Factorial(2 * m1 - 1 );   
		}
		else
		{
			y += pow(x, (2 * m1 - 1 )) / Factorial(2 * m1 - 1 );
		}
	}
	for(m2 = 1; m2 <= 20; m2++)    //cosx 的泰勒，m2控制后面加到第几项
	{
		if (m2 % 2 == 0)
		{
			z += pow(x, (2 * m2 )) / Factorial(2 * m2 );
		}
		else
		{
			z -= pow(x, (2 * m2 )) / Factorial(2 * m2 );
		}
	}
	return  y/z;
	}
}

int main()
{
	//获得参数并转换为int
	double x;
	printf("请输入需要计算的角度值：\n");
	scanf("%lf", &x);
	printf("%.3lf\n", tan_se(x));
	system("PAUSE");
	return 0;
}