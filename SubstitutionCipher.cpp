#include <bits/stdc++.h>
using namespace std;

// Shortcuts for common data types
using ll = long long;

// Caesar Cipher Encryption Function
string solve(string s, ll shift) {
    string ans = "";
    string alphabet = "abcdefghijklmnopqrstuvwxyz";

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == ' ') {
            ans += ' ';
        } else if (s[i] >= 'a' && s[i] <= 'z') {
            int index = alphabet.find(s[i]);
            int new_index = (index + shift) % 26;
            ans += alphabet[new_index];
        } else if (s[i] >= 'A' && s[i] <= 'Z') {
            int index = alphabet.find(tolower(s[i]));
            int new_index = (index + shift) % 26;
            ans += toupper(alphabet[new_index]);
        } else {
            ans += s[i]; // Non-alphabetic characters remain unchanged
        }
    }
    return ans;
}

// Caesar Cipher Decryption Function
string desolve(string s, ll shift) {
    shift = shift % 26;
    string ans = "";
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    shift = 26 - shift; // Reverse shift for decryption

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == ' ') {
            ans += ' ';
        } else if (s[i] >= 'a' && s[i] <= 'z') {
            int index = alphabet.find(s[i]);
            int new_index = (index + shift) % 26;
            ans += alphabet[new_index];
        } else if (s[i] >= 'A' && s[i] <= 'Z') {
            int index = alphabet.find(tolower(s[i]));
            int new_index = (index + shift) % 26;
            ans += toupper(alphabet[new_index]);
        } else {
            ans += s[i]; // Non-alphabetic characters remain unchanged
        }
    }
    return ans;
}

int main() {
    ll shift;
    cout << "Enter the shift value: ";
    cin >> shift;

    string s;
    cout << "Enter the string: ";
    cin.ignore();
    getline(cin, s);

    string encrypted = solve(s, shift);
    cout << "Encrypted string: " << encrypted << endl;

    string decrypted = desolve(encrypted, shift);
    cout << "Decrypted string: " << decrypted << endl;

    return 0;
}
