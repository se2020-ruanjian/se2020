#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define PI 3.141592

float sin_se(float);

float Factorial(int n)    //阶乘
{
	//long long 占8个字节
	float i, factorial = 1;

	for (i = 1; i <= n ; i++)
	{
		factorial *= i;
	}
	
	return factorial;
}

float sin_se(float x)
{
	float sin_se(x) = 0.0;
	int m;
	x = (fmod(x,360) * PI / 180);
	for(m = 1; m <= 12; m++)    //sinx的泰勒级数，m控制加到后面第几项
	{
		if (m % 2 == 0)
		{
			sin_se(x) -= pow(x, (2 * m - 1 )) / Factorial(2 * m - 1 );
		}
		else
		{
			sin_se(x) += pow(x, (2 * m - 1 )) / Factorial(2 * m - 1 );
		}
	}
	return sin_se(x);
}
