#include<bits/stdc++.h>
using namespace std;

#define fastio() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define endl                    "\n"
#define ff                      first
#define ss                      second
#define pb                      push_back
#define ppb                     pop_back
#define eb                      emplace_back
#define mp                      make_pair
#define sz(x)                   (int)((x).size())
#define setbits(x)              __builtin_popcount(x) // # setbits i.e, # 1
#define zrobits(x)              _builtin_ctzll(x) // # 0 before the first 1 bit
#define INF                     1e18
#define MOD                     1000000007
#define PI                      3.141592653589793238462
#define ps(x,y)                 fixed<<setprecision(y)<<x // if x double and we need precision till y decimal places
#define w(tt)                   int tt; cin>>tt; while(tt--) //for multiple test cases
#define loop(i,a,b)              for(int i = a; i < b; i++)
#define revloop(i,a,b)			 for(int i = a; i >= b; i--)
#define trav(it,a)               for(auto &it: a)
#define all(x)                  x.begin(), x.end()
#define rall(x)                 x.rbegin(), x.rend()

typedef long long ll;
typedef unsigned long long ull;
typedef long double lld;

// string to_binary(int x) {
// 	string s;
// 	while(x > 0) {
// 		s += (x % 2 ? '1' : '0');
// 		x /= 2;
// 	}
// 	reverse(s.begin(), s.end());
// 	return s;
// }

int main() 
{
	fastio();
	w(tt)
	{
		int n,q,odd=0,even=0; cin >> n >> q;
		vector<int> a(n);
		ll sum = 0;
		loop(i,0,n)
		{
			cin >> a[i];
			if(a[i]%2 == 0)
				even++;
			else
				odd++;
			sum += a[i];
		}	
		loop(i,0,q)
		{
			int a,b; cin >> a >> b;
			if(a == 0)
			{
				sum += even*b;
				if(b%2 != 0)
				{
					odd += even;
					even = 0;
				}
				cout << sum << endl;
			}	
			else
			{
				sum += odd*b;
				if(b%2 != 0)
				{
					even += odd;
					odd = 0;
				}
				cout << sum << endl;
			}
		}
	}	
	return 0;
}