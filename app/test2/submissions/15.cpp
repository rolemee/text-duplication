#include<iostream>
using namespace std;

 

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	int t;cin>>t;
	int n,q,i,j;
	int type,x;
	int even,odd;
	long long a[100005],sum;
	
	while(t--)
	{
		cin>>n>>q;
		odd=0;even=0;
		sum=0;
		for(i=0;i<n;++i)
		{
			cin>>a[i];
			
			if(a[i]%2==0) ++odd;//统计奇偶数 
			else ++even;
			
			sum+=a[i];//初始和 
		}
			
		
		for(i=0;i<q;++i)//q次操作 
		{
			
			cin>>type>>x;
			
			if(type==0) sum=sum+odd*x;
			else sum=sum+even*x;
			cout<<sum<<endl;
			
			if(x%2!=0)//加的数为奇，原来奇偶相反
			{
				if(type==0)
				{
					even+=odd;//偶变奇 
					odd=0;		
				}
				else
				{
					odd+=even;
					even=0;		
				}	
			} 
		}
	}
	return 0;
}