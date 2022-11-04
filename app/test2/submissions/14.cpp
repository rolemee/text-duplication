#include <bits/stdc++.h>
using namespace std;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    int t;
    cin >> t;
    while (t--)
    {
        int n, q;
        cin >> n >> q;
        long long ans = 0;
        int even = 0, odd = 0;
        for (int i = 0; i < n; i++)
        {
            int a;
            cin >> a;
            ans += a;
            if (a % 2 == 0) even++;
            else odd++;
        }
        while (q--)
        {
            int a, b;
            cin >> a >> b;
            if (a == 0)
            {
                ans += even * b;
                if (b % 2 == 1)
                {
                    odd += even;
                    even = 0;
                }
            }
            else
            {
                ans += odd * b;
                if (b % 2 == 1)
                {
                    even += odd;
                    odd = 0;
                }
            }
            cout << ans << '\n';
        }
    }
}