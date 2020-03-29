#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define PI 3.141592
double Factorial(int n)
{
	//long long Õ¼8¸ö×Ö½Ú
	double i, factorial = 1;

	for (i = 1; i <= n ; i++)
	{
		factorial *= i;
	}
	
	return factorial;
}

double cos_se(double x)
{
	double cosx = 1.0;
	int m;
	x = (fmod(x,360) * PI / 180);
	for(m = 1; m <= 12; m++)
	{
		if (m % 2 == 0)
		{
			cosx += pow(x, (2 * m )) / Factorial(2 * m );
		}
		else
		{
			cosx -= pow(x, (2 * m )) / Factorial(2 * m );
		}
	}
	return cosx;
}

