#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

int mod_pow(int base, int exp, int mod) {
    int result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (1LL * result * base) % mod; // long long을 사용하여 오버플로우 방지
        }
        base = (1LL * base * base) % mod;
        exp /= 2;
    }
    return result;
}

int solution(vector<int>& lst, int k) {
    int cnt = 0;
    int pp = k; // 쌓은 원판의 위치
    int l = lst.size();
    while (!lst.empty()) {
        int idx = l;
        int x = lst.back();
        lst.pop_back();
        if (pp == x) {
            l -= 1;
            continue;
        } else {
            cnt = (cnt + mod_pow(2, idx - 1, MOD)) % MOD;
            pp = 6 - pp - x;
            l -= 1;
        }
    }
    return cnt % MOD;
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> lst(n);
    for (int i = 0; i < n; i++) {
        cin >> lst[i];
    }

    cout << solution(lst, k) << endl;
    return 0;
}
