#include <stdio.h>
#include <math.h>
#include <stdlib.h>

float cos_se(float);

float cos_se(float x)
{
    #define PI 3.141592
	float cosx = 1.0;
	int m;
	x = (fmod(x,360) * PI / 180);
	for(m = 1; m <= 12; m++)
	{
		float i, factorial = 1;
		for (i = 1; i <= 2*m ; i++)
	{
		factorial *= i;
	}
		if (m % 2 == 0)
		{
			cosx += pow(x, (2 * m )) / factorial;
		}
		else
		{
			cosx -= pow(x, (2 * m )) /factorial;
		}
	}
	return cosx;
}

