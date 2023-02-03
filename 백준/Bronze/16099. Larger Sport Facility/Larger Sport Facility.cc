#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(void){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        long long lt, wt, le, we;
        cin >> lt >> wt >> le >> we;
        if (lt*wt > le*we) cout << "TelecomParisTech" << endl;
        else if (lt*wt < le*we) cout << "Eurecom" << endl;
        else cout << "Tie" << endl;
    }
}