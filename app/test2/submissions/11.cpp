
#include<iostream>
#include<vector>

using namespace std;
using ll = long long;

int main() {
	cin.tie(0) -> sync_with_stdio(0);
	ll t;

	cin >> t;

	while (t--) {
		ll n, q;

		cin >> n >> q;

		vector<ll> brojevi(n);

		ll ce = 0, se = 0, co = 0, so = 0;
		for (ll &x: brojevi) {
			cin >> x;

			if (x % 2 == 0) {
				ce++;
				se += x;
			} else {
				co++;
				so += x;
			}
		}

		ll a, x;
		while (q--) {
			cin >> a >> x;
			if (!a) {
				se += x * ce;
				if (x % 2 == 1 && ce) {
					co += ce;
					ce = 0;
					so += se;
					se = 0;
				} 
			} else {
				so += x * co;
				if (x % 2 == 1 && co) {
					ce += co;
					co = 0;
					se += so;
					so = 0;
				}
			}

			cout << so + se << '\n';
		}
	}
}