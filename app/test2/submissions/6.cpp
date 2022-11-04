#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin>>t;
    while(t--){
    ll n,q;
    cin>>n>>q;
    ll arr[n];
    ll sum=0;
    ll even=0,odd=0;
    for(ll i=0;i<n;i++){
        cin>>arr[i];
        if(((arr[i])^1)==(arr[i]+1)){
            even++;
        }
        sum+=arr[i];
    }
    odd=n-even;
    //  cout<<even<<"_______"<<odd<<endl;
    while(q--){
        ll type,x;
        cin>>type>>x;
        if(type==0){
            if(x%2==0){
                sum+=even*x;
            }
            else{
                sum+=even*x;
                odd+=even;
                even=0;
            }
        }
        else{
            if(x%2==0){
                sum+=odd*x;
            }
            else{
                sum+=odd*x;
                even+=odd;
                odd=0;
            }
        }
        cout<<sum<<endl;
    }
    }
    return 0;
}