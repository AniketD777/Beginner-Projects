#include<stdio.h>
#include<math.h>

int fac(int n)
{
	if(n==0 || n==1)
	{
		return 1;
	}
	return n*fac(n-1);
}

int main()
{
	float ang,rad;
	printf("Enter degrees to calculate sine value: ");
	scanf("%f",&ang);
	//If angle greater than 360 degrees
	while(ang>=360)
	{
		ang=ang-360;
	}
	int sign=0; //0=>+ve && 1=>-ve
	float finAng;
	//Now to set sign for different quadrants 
	if(ang>270)
	{
		finAng=360-ang;
		sign=1;
	}
	else if(ang>180)
	{
		finAng=ang-180;
		sign=1;
	}
	else if(ang>90)
	{
		finAng=180-ang;
	}
	else
	{
		finAng=ang;
	}
	rad=(finAng/180)*3.14159265;
	float Sin=0;
	int check=0;
	float x=rad;
	/*We can take no. of expressions('n') by user also but lets consider 15
      printf("Enter n: ");
	  scanf("%d",&n);*/
    int n=15;
	for(int i=1;i<=n;i+=2)
	{
		if(check==0)
		{
			Sin+=pow(x,i)/fac(i);
			check=1;
		}
		else
		{
			Sin-=pow(x,i)/fac(i);
			check=0;
		}
	}
	if(sign==0)
	{
		printf("By Series Expansion: %f\n",Sin);
	}
	else
	{
	    printf("By Series Expansion: -%f\n",Sin);
	}
	rad=(ang/180)*3.14159265; //Using the input ang directly as radians
	printf("By inbuilt function using <math.h> lib: %f\n",sin(rad));
	return 0;
}
