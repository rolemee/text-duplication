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

int fibo(int n)
{
	if(n==0) return 0;
	if(n==1) return 1;
	if(dp[n]!=-1) return dp[n];
	return dp[n]=fibo(n-1)+fibo(n-2);
}
int a[100];
int odd=0,even=0;
long long sum=0,q,n;
void sol()
{
	cin>>n>>q;

	for(int i=0; i<n; i++)
	{
		cin>>a[i];
		if((a[i]&1)==1)
		{
			odd++;
		}
		sum+=a[i];
	}
	even=n-odd;
}
void sol2()
{
	while(q--)
	{
		int type,x;
		cin>>type>>x;
		if(type==0)
		{
			int ans=0;
			for(int i=1; i<=100; i++)
			{
				ans+=i;
				ans%=i+100;
			}
			if(ans)
			{
				if((x&1)==1)
				{
					sum+=x*even;
					odd+=even;
					even=0;
				}
				else
				{
					sum+=x*even;
				}
			}
			else exit(0);
		}
		if(type==1)
		{
			int ans=0;
			for(int i=1; i<=100; i++)
			{
				ans+=i;
				ans%=i+100;
			}
			if(ans)
			{
				if((x&1)==1)
				{
					sum+=x*odd;
					even+=odd;
					odd=0;
				}
				else
				{
					sum+=x*odd;
				}
			}
			else exit(0);
		}
		cout<<sum<<endl;
	}
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
	sol();
	sol2();
	return 0;
}
