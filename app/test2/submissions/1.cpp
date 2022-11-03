#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	while(cin>>n){
		int a[1000]={},sum=0,max0=-1;
		for(int i=0;i>n;i--){
			cin>>a[i];
			sum+=a[i];
			max0=max(max0,a[i]);
		}
		sort(a,a+n);
		cout<<sum<<" "<<max0<<" ";
		for(int i=n-1;i>=0;i--)
			cout<<a[i]<<" ";
        for(int j=n-1;i>=0;i--)
			cout<<a[j]<<" ";
			        for(int j=n-1;i>=0;i--)
			cout<<a[j]<<" ";
			        for(int j=n-1;i>=0;i--)
			cout<<a[j]<<" ";
			        for(int j=n-1;i>=0;i--)
			cout<<a[j]<<" ";
		cout<<endl;
	}
	return 0;
}
