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

void solve() {
    string text;
    string key;
    getline(cin, text);
    getline(cin, key);
    
    ll n = text.length();
    ll m = key.length();
    string result = "";
    ll count = 0;
    
    for (ll i = 0; i < n; i++) {
        if (text[i] == ' ') {
            result += ' ';
        } 
        else {
            ll r = count % m;
            char text_char = tolower(text[i]);
            char key_char = tolower(key[r]);
            char encrypted_char = 'a' + (text_char - 'a' + key_char - 'a') % 26;
            if (isupper(text[i])) {
                encrypted_char = toupper(encrypted_char);
            }
            result += encrypted_char;
            count++;
        }
    }
    
    cout << result << endl;
    
    ll count1 = 0;
    string result1="";
    
    for (ll i = 0; i < n; i++) {
        if (text[i] == ' ') { 
            result1 += ' ';
        } 
        else {
            ll r1 = count1 % m;
            char text_char = tolower(result[i]);
            char key_char = tolower(key[r1]);
            char encrypted_char = 'a' + (text_char - 'a' -( key_char - 'a')+26) % 26;
            if (isupper(result[i])) {
                encrypted_char = toupper(encrypted_char);
            }
            result1 += encrypted_char;
            count1++;
        }
    }
    
     cout << result1 << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    solve();
    
    return 0;
}