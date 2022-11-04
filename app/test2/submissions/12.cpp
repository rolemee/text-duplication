#include <iostream>
#include <vector>
#include <map>

#define int long long

using namespace std;

int32_t main() {
  int tt;
  cin >> tt;
  while (tt--) {
    int n, q;
    cin >> n >> q;
    int x = 0, y = 0, ans = 0;
    for (int i = 0; i < n; ++i) {
      int u;
      cin >> u;
      ans += u;
      if (u & 1) {
        ++y;
      } else {
        ++x;
      }
    }
    for (int i = 0; i < q; ++i) {
      int t, lx;
      cin >> t >> lx;
      if (t == 0) {
        if (lx % 2 == 0) {
          ans += lx * x;
        } else {
          ans += lx * x;
          y = n;
          x = 0;
        }
      } else {
        if (lx % 2 == 0) {
          ans += lx * y;
        } else {
          ans += lx * y;
          x = n;
          y = 0;
        }
      }
      cout << ans << endl;
    }
  }
}
