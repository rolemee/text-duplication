#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> p32;
typedef pair<ll, ll> p64;
typedef pair<double, double> pdd;
typedef vector<ll> v64;
typedef vector<int> v32;
typedef vector<vector<int>> vv32;
typedef vector<vector<ll>> vv64;
typedef vector<vector<p64>> vvp64;
typedef vector<p64> vp64;
typedef vector<p32> vp32;
ll MOD = 998244353;
double eps = 1e-12;
#define forn(i, e) for (ll i = 0; i < e; i++)
#define forsn(i, s, e) for (ll i = s; i < e; i++)
#define rforn(i, s) for (ll i = s; i >= 0; i--)
#define rforsn(i, s, e) for (ll i = s; i >= e; i--)
#define ln "\n"
#define dbg(x) cout << #x << " = " << x << ln
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define INF 2e18
#define fastio()                      \
	ios_base::sync_with_stdio(false); \
	cin.tie(NULL);                    \
	cout.tie(NULL)
#define all(x) (x).begin(), (x).end()
#define sz(x) ((ll)(x).size())
const int N=10e5+10;

ll dp[N];

int fibo(int n){
	if(n==0) return 0;
	if(n==1) return 1;
	if(dp[n]!=-1) return dp[n];
	return dp[n]=fibo(n-1)+fibo(n-2);
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	memset(dp,-1,sizeof(dp));
	int t;
	cin >> t;
	for (int itt = 1; itt <= t; itt++)
	{
		// cout << "Case #" << itt << ": ";
		ll n,q;
		cin>>n>>q;
		ll a[n];
		ll evencount=0,oddcount=0,sum=0;
		forn(i,n)
		{
			cin>>a[i];
			sum+=a[i];
			if(a[i]%2==0)
				evencount++;
			else	
				oddcount++;
		}
		while(q--)
		{
			char c;
			ll x;
			cin>>c>>x;
			if(c=='0')
			{
				if(x%2==0)
				{
					// odd and even counts will remain same 
					sum+=(evencount*x);
				}
				else
				{
					sum+=(evencount*x);
					evencount=0;
					oddcount=n;
					
				}
			}
			else
			{
				if(x%2==0)
				{
					// odd and even counts will remain same 
					sum+=(oddcount*x);
				}
				else
				{
					sum+=(oddcount*x);
					evencount=n;
					oddcount=0;
					
				}
			}
			cout<<sum<<endl;
		}

		
			
	}
	return 0;
}