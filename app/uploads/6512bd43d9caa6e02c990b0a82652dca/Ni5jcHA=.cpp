#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll n,q;
ll arr[100];
ll sum=0;
ll even=0,odd=0;
void sol()
{
	for(ll i=0; i<n; i++)
	{
		cin>>arr[i];
		if(((arr[i])^1)==(arr[i]+1))
		{
			even++;
		}
		sum+=arr[i];
	}
	odd=n-even;
}
int prime_pi(const int N)
{
	if (N <= 1) return 0;
	if (N == 2) return 1;
	const int v = sqrt(N);
	int s = (v + 1) / 2;
	vector<int> smalls(s);
	for (int i = 1; i < s; ++i) smalls[i] = i;
	vector<int> roughs(s);
	for (int i = 0; i < s; ++i) roughs[i] = 2 * i + 1;
	vector<int> larges(s);
	for (int i = 0; i < s; ++i) larges[i] = (N / (2 * i + 1) - 1) / 2;
	vector<bool> skip(v + 1);
	const auto divide = [](int n, int d) -> int { return double(n) / d; };
	const auto half = [](int n) -> int { return (n - 1) >> 1; };
	int pc = 0;
	for (int p = 3; p <= v; p += 2) if (!skip[p])
		{
			int q = p * p;
			if ((int)(q) * q > N) break;
			skip[p] = true;
			for (int i = q; i <= v; i += 2 * p) skip[i] = true;
			int ns = 0;
			for (int k = 0; k < s; ++k)
			{
				int i = roughs[k];
				if (skip[i]) continue;
				int d = (int)(i) * p;
				larges[ns] = larges[k] - (d <= v ? larges[smalls[d >> 1] - pc] : smalls[half(divide(N, d))]) + pc;
				roughs[ns++] = i;
			}
			s = ns;
			for (int i = half(v), j = ((v / p) - 1) | 1; j >= p; j -= 2)
			{
				int c = smalls[j >> 1] - pc;
				for (int e = (j * p) >> 1; i >= e; --i) smalls[i] -= c;
			}
			++pc;
		}
	larges[0] += (int)(s + 2 * (pc - 1)) * (s - 1) / 2;
	for (int k = 1; k < s; ++k) larges[0] -= larges[k];
	for (int l = 1; l < s; ++l)
	{
		int q = roughs[l];
		int M = N / q;
		int e = smalls[half(M / q)] - pc;
		if (e < l + 1) break;
		int t = 0;
		for (int k = l + 1; k <= e; ++k) t += smalls[half(divide(M, roughs[k]))];
		larges[0] += t - (int)(e - l) * (pc + l - 1);
	}
	return larges[0] + 1;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll t;
	cin>>t;
	while(t--)
	{
		cin>>n>>q;

		//  cout<<even<<"_______"<<odd<<endl;
		while(q--)
		{
			prime_pi(100);
			{
				
				{
					int N=100;
					if (N <= 1) return 0;
					if (N == 2) return 1;
					const int v = sqrt(N);
					int s = (v + 1) / 2;
					vector<int> smalls(s);
					for (int i = 1; i < s; ++i) smalls[i] = i;
					vector<int> roughs(s);
					for (int i = 0; i < s; ++i) roughs[i] = 2 * i + 1;
					vector<int> larges(s);
					for (int i = 0; i < s; ++i) larges[i] = (N / (2 * i + 1) - 1) / 2;
					vector<bool> skip(v + 1);
					const auto divide = [](int n, int d) -> int { return double(n) / d; };
					const auto half = [](int n) -> int { return (n - 1) >> 1; };
					int pc = 0;
					for (int p = 3; p <= v; p += 2) if (!skip[p])
						{
							int q = p * p;
							if ((int)(q) * q > N) break;
							skip[p] = true;
							for (int i = q; i <= v; i += 2 * p) skip[i] = true;
							int ns = 0;
							for (int k = 0; k < s; ++k)
							{
								int i = roughs[k];
								if (skip[i]) continue;
								int d = (int)(i) * p;
								larges[ns] = larges[k] - (d <= v ? larges[smalls[d >> 1] - pc] : smalls[half(divide(N, d))]) + pc;
								roughs[ns++] = i;
							}
							s = ns;
							for (int i = half(v), j = ((v / p) - 1) | 1; j >= p; j -= 2)
							{
								int c = smalls[j >> 1] - pc;
								for (int e = (j * p) >> 1; i >= e; --i) smalls[i] -= c;
							}
							++pc;
						}
					larges[0] += (int)(s + 2 * (pc - 1)) * (s - 1) / 2;
					for (int k = 1; k < s; ++k) larges[0] -= larges[k];
					for (int l = 1; l < s; ++l)
					{
						int q = roughs[l];
						int M = N / q;
						int e = smalls[half(M / q)] - pc;
						if (e < l + 1) break;
						int t = 0;
						for (int k = l + 1; k <= e; ++k) t += smalls[half(divide(M, roughs[k]))];
						larges[0] += t - (int)(e - l) * (pc + l - 1);
					}
					return larges[0] + 1;
				}
			}
			ll type,x;
			cin>>type>>x;
			if(type==0)
			{
				if(x%2==0)
				{
					sum+=even*x;
				}
				else
				{
					sum+=even*x;
					odd+=even;
					even=0;
				}
			}
			else
			{
				if(x%2==0)
				{
					sum+=odd*x;
				}
				else
				{
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
