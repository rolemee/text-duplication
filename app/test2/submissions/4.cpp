#include<bits/stdc++.h>
using namespace std;
int main()
{
ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    int t;
    cin>>t;
    while(t--){
    int n,q;
    cin>>n>>q;
    int a[n];
    int odd=0,even=0;
    long long sum=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
        if((a[i]&1)==1){
            odd++;
        }
        sum+=a[i];
    }
    even=n-odd;
    
    while(q--){
        int type,x;
        cin>>type>>x;
        if(type==0){
            if((x&1)==1){
                sum+=x*even;
                odd+=even;
                even=0;
            }
            else{
                sum+=x*even;
            }
        }
        if(type==1){
            if((x&1)==1){
                sum+=x*odd;
                even+=odd;
                odd=0;
            }
            else{
                sum+=x*odd;
            }
        }
        cout<<sum<<endl;
    }
    }
    
    return 0;
}