#include<iostream>
using namespace std;
int a[100010];
int main()
{
	int t;
	cin >> t;
	while(t--)
	{
		int n, q, j, jj, sumj = 0, sumo = 0;
		cin >> n>> q;
		for(int i = 0; i < n; i++) cin >> a[i];
		for(int i = 0; i < n; i++)
		{
			if(a[i] % 2 == 0) sumo++;
			else sumj++;
		}
		long long int sum = 0;
		for(int i = 0; i < n; i++)
		{
			sum += a[i];
		}
		while(q--)
		{
			cin >> j >> jj;
			if(j == 0)
			{
				sum += jj * sumo;
			}
			else sum += jj * sumj;
			cout<<sum<<endl;
			if(j == 0)
			{
				if(jj % 2 != 0)
				{
					sumj += sumo;
					sumo = 0;
				}
			}
			else
			{
				if(jj % 2 != 0)
				{
					sumo += sumj;
					sumj = 0;
				}
			}
		}
	}
	return 0;
}
 	  		 	   				  	 	 	 	 	 				