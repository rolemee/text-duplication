#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<string>
#include<cstring>
#include<queue>
#include<set>
#include<unordered_map>
typedef long long ll;
#define ls k<<1
#define rs k<<1|1
#define lowbit(x) x&(-x)
using namespace std;
const int N = 2e5 + 10, M = 2e5 + 10;
const int mod = 998244353, INF = 0x3f3f3f3f;
void solve() {
	int n, q; cin >> n >> q;
	int odd = 0, even = 0;
	ll sum = 0;
	for (int i = 1; i <= n; i++) {
		int x; cin >> x;
		if (x & 1)odd++;
		else even++;
		sum += x;
	}
	while (q--) {
		int op, x; cin >> op >> x;
		if (!op) {
			sum += even * x;
			if (x & 1) {
				odd += even;
				even = 0;
			}
		}
		else {
			sum += odd * x;
			if (x & 1) {
				even += odd;
				odd = 0;
			}
		}
		cout << sum << '\n';
	}
}
int main() {
	ios::sync_with_stdio(false), cin.tie(nullptr);
	int t; cin >> t;
	while (t--)solve();
	return 0;
}