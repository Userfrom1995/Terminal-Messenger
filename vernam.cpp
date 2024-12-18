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

void solve(string s, string key) {
    if(s.size() != key.size()) {
        cout << "The length of the key should be equal to the length of the string to be encrypted." << endl;
        return;
    }
    string ans = "";
    for(int i = 0; i < s.size(); i++) {
        ans+=s[i]^key[i];
    }
    cout << "Encrypted string: " << ans <<": ending" <<endl;
    for(int i = 0; i < ans.size(); i++) {
        cout << int(ans[i]) << " ";
    }   
    string decrypted = "";
    for(int i = 0; i < s.size(); i++) {
        decrypted+=ans[i]^key[i];
    }
    cout << "Decrypted string: " << decrypted << endl;
}

int main() {
    
    
    string s;
    
    cout << "Enter the string to be encrypted: ";
    getline(cin, s);
    string key;
    cout << "Enter the key: ";
    getline(cin, key);

    
    solve(s,key);
    
    return 0;
}