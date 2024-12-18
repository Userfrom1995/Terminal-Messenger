#include <bits/stdc++.h>
using namespace std;

void solve(string text, int key) {
    int s = text.size();

    // Rail Fence matrix for encryption
    vector<vector<char>> rail(key, vector<char>(s, '\0'));
    bool dir_down = false;
    int row = 0, col = 0;

    // Step 1: Fill the rail matrix for encryption
    for (int i = 0; i < s; i++) {
        if (row == 0 || row == key - 1)
            dir_down = !dir_down; // Change direction

        rail[row][col++] = text[i];

        dir_down ? row++ : row--;
    }

    // Step 2: Read the matrix to construct the encrypted text
    string encrypted;
    for (int i = 0; i < key; i++) {
        for (int j = 0; j < s; j++) {
            if (rail[i][j] != '\0') {
                encrypted.push_back(rail[i][j]);
            }
        }
    }
    cout << "Encrypted text: " << encrypted << endl;

    //Step 3: Reconstruct the rail matrix for decryption
    vector<vector<char>> rail_decrypt(key, vector<char>(s, '\0'));
    row = 0, col = 0;
    dir_down = false;

    // Mark the positions to place the characters
    for (int i = 0; i < s; i++) {
        if (row == 0 || row == key - 1)
            dir_down = !dir_down;

        rail_decrypt[row][col++] = '*';

        dir_down ? row++ : row--;
    }

   // Place the characters in the marked positions
    int idx = 0;
    for (int i = 0; i < key; i++) {
        for (int j = 0; j < s; j++) {
            if (rail_decrypt[i][j] == '*' && idx < encrypted.size()) {
                rail_decrypt[i][j] = encrypted[idx++];
            }
        }
    }

    // Step 4: Read the matrix to construct the decrypted text
    string decrypted;
    row = 0, col = 0;
    dir_down = false;

    for (int i = 0; i < s; i++) {
        if (row == 0 || row == key - 1)
            dir_down = !dir_down;

        decrypted.push_back(rail_decrypt[row][col++]);

        dir_down ? row++ : row--;
    }

    cout << "Decrypted text: " << decrypted << endl;
    
}

int main() {
    int k;
    cout << "Enter the key: ";
    cin >> k;

    string text;
    cout << "Enter the text to be encrypted: ";
    cin >> text;

    solve(text, k);

    return 0;
}
