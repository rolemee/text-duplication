#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mk make_pair
#define ll long long
#define pii pair<int,int>
#define INF 1000000000
#define all(x) x.begin(), x.end()
#define IOS ios_base :: sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define MOD 1000000007
#define int long long // PROIBIDO EM 27 PAISES
typedef vector<int> vi;
typedef vector<long long> vll;

void testcases() {
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
}

void solve() {
    int n,q;cin>>n>>q;
    vi v(n);
    int odd = 0;
    int even = 0;
    int ans = 0;
    for (int i = 0; i < n; i++) {
        cin >> v[i];
        if (v[i] % 2 == 0){
            even++;
        } else {
            odd++;
        }
        ans += v[i];
    }
    int op,x;
    while (q--) {
        cin >> op >> x;
        if (op == 0) {
            ans += x*even;
            if (x % 2 != 0) {
                odd += even;
                even = 0;
            }
        } else {
            ans += x*odd;
            if (x % 2 != 0) {
                even += odd;
                odd = 0;
            }
        }
        cout << ans << endl;

    }
}

signed main() {

    testcases();
    int t = 1;cin>>t;
    while (t--) {
        solve();
    }

    return 0;
}