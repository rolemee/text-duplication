#include <bits/stdc++.h>

using namespace std;

#define int long long

const int N = 2e5 + 5;

int n;
int a[N];
int q;
int sum;

void solve(){
    cin >> n;
    cin >> q;
    sum = 0;
    int odd = 0,even = 0;
    for(int i = 1;i <= n;i++){
        cin >> a[i];
        sum += a[i];
        if(a[i] & 1)odd++;
        else even ++;
    }
    while(q--){
        int op,x;
        cin >> op >> x;
        if(op == 0){
            sum += even * x;
            if(x & 1){
                odd += even;
                even = 0;
            }
        }else{
            sum += odd * x;
            if(x & 1){
                even += odd;
                odd = 0;
            }
        }
        cout << sum << '\n';
    }
}

signed main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}