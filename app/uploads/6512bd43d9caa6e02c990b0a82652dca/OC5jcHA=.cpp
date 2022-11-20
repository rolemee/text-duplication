#include<bits/stdc++.h>
using namespace std;
int main(){
    long long sum;
    int num0,num1;
    int n,u,t,q;
    scanf("%d",&t);
    while(t--){
        scanf("%d%d",&n,&q);
        num0=num1=sum=0;
        while(n--){
            scanf("%d",&u);
            sum+=u;
            if(u&1)num1++;
            else num0++;
        }
        while(q--){
            scanf("%d%d",&n,&u);
            if(n==0){
                sum+=num0*u;
                if(u&1){
                    num1+=num0;
                    num0=0;
                }
            }
            else{
                sum+=num1*u;
                if(u&1){
                    num0+=num1;
                    num1=0;
                }
            }
            cout<<sum<<'\12';
        }
    }
    return 0;
}
