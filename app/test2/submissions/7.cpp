#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, q;
        cin >> n >> q;

        vector<long long> a(n);
        long long s = 0;
        int c_odd = 0;
        int c_even = 0;

        int c[2];
        c[0] = c[1] = 0;

        for (int i = 0; i < n; i++) {
            cin >> a[i];
            s += a[i];
            c[a[i] % 2] += 1;
        }

        for (int i = 0; i < q; i++) {
            long long type, x;
            cin >> type >> x;

            int c_copy = c[type];
            s += c[type] * x;

            if (x % 2 != 0) {
                // Нужно сменить четность тех элементов, к которым прибавили x
                c[(type + 1) % 2] += c[type];
                c[type] = 0;
            }

            cout << s << endl;
        }
    }
    return 0;
}