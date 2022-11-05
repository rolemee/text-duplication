///akt2ab ayh ys7by mna zy alfl aho
#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#define ll long long
#define WhoCare ios_base::sync_with_stdio(false);cin.tie(NULL);
#define F first
#define S second
using namespace std;
using namespace __gnu_pbds;
typedef tree<int, null_type, less_equal<int>, rb_tree_tag, tree_order_statistics_node_update> indexed_set;
const int N = 2e5 + 7, M = 32;

void Run_F() {


    int n, q;
    cin >> n >> q;

    ll sum = 0, even  = 0, odd = 0;

    for(int i = 0; i < n; i++) {

        int x;
        cin >> x;
        sum += x;

        even += (x % 2 == 0);
        odd += (x % 2);
    }


    while(q--) {

        int ty, x;
        cin >> ty >> x;

        if(!ty) {

            sum = sum + (x * even);

            if(x % 2)
                odd += even, even = 0;

        } else {

            sum = sum + (x * odd);

            if(x % 2)
                even += odd, odd = 0;
        }


        cout << sum << "\n";

    }





}


int main() {


    WhoCare

    int cases = 1;
    cin >> cases;
    for(int tid = 1; tid <= cases; ++tid) {
        //cout << "Case: " << tid;
        Run_F();

    }

    return 0;
}

