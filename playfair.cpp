#include <bits/stdc++.h>
using namespace std;

// Shortcuts for common data types
using ll = long long;
using vi = vector<int>;
using vll = vector<long long>;
using pii = pair<int, int>;
using pll = pair<long long, long long>;

// Constants
const int MOD = 1e9 + 7;
const int INF = 1e9;
const ll LINF = 1e18;

// Shortcuts for common functions
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x.size())

// Looping shortcuts
#define f(i, a, b) for (ll i = a; i < b; i++)
#define r(i, n) FOR(i, 0, n)

// Debugging shortcuts (optional, can be removed)
#define DEBUG(x) cerr << #x << " = " << (x) << endl

void solve(){
    string text;
   unordered_set<char> alphabets;
    cout << "Enter the string to be encrypted: ";
    getline(cin, text);
    for(int i = 0; i < 25; i++){
        char temp = 'a' + i;
       if(text.find(temp)){
           alphabets.insert(temp);
       }
    }
    for(int i = 0; i < 25; i++){
        char temp = 'a' + i;
        if(alphabets.find(temp) == alphabets.end()){
            alphabets.insert(temp);
        }
    }


}


int main() {
    solve();
    return 0;
}