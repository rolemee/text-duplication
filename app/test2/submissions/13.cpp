#include <bits/stdc++.h>            
                    
int main(){                 
                              
    std::ios::sync_with_stdio(false); std::cin.tie(nullptr);

    int T; std::cin >> T;
    while (T--) {
        int N, Q; std::cin >> N >> Q;

        int64_t ans = 0;
        std::array<int,2> par = {0, 0};
        for (int i = 0; i < N; ++i) {
            int a; std::cin >> a;
            ans += a;
            par[a%2]++;   
        }

        while (Q--) {
            int a, b; std::cin >> a >> b;

            ans += int64_t(b) * par[a];
            std::cout << ans << '\n';            

            if (a == 0 && b%2) {                   
                par[1] += par[0];
                par[0] = 0;    
            } else if (a == 1 && b%2) {
                par[0] += par[1];
                par[1] = 0;
            }
            
        }                            
    }                                      
                                       
    return 0;                                               
 
}