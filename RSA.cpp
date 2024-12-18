#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// Function to calculate the greatest common divisor (GCD)
int gcd(int a, int b) {
    if (b == 0) 
        return a;
    return gcd(b, a % b);
}

// Function to calculate (base^exponent) % mod using modular exponentiation
long long modExpo(long long base, long long exponent, long long mod) {
    long long result = 1;
    base = base % mod;
    while (exponent > 0) {
        if (exponent % 2 == 1) { 
            result = (result * base) % mod;
        }
        exponent = exponent >> 1; // Divide exponent by 2
        base = (base * base) % mod;
    }
    return result;
}

// Function to calculate the modular inverse of 'e' under modulo 'phi'
long long modInverse(long long e, long long phi) {
    for (long long d = 1; d < phi; d++) {
        if ((e * d) % phi == 1) {
            return d;
        }
    }
    return -1; // Inverse not found
}

int main() {
    srand(time(0));
    
    // Step 1: Select two prime numbers p and q
    int p = 61; // First prime number
    int q = 53; // Second prime number
    cout << "Selected primes: p = " << p << ", q = " << q << endl;

    // Step 2: Compute n = p * q
    long long n = p * q;
    cout << "n (p * q) = " << n << endl;

    // Step 3: Compute phi(n) = (p-1) * (q-1)
    long long phi = (p - 1) * (q - 1);
    cout << "phi(n) = " << phi << endl;

    // Step 4: Choose e such that 1 < e < phi(n) and gcd(e, phi) = 1
    long long e = 17; // A common choice for e
    while (gcd(e, phi) != 1) {
        e++;
    }
    cout << "Public exponent (e) = " << e << endl;

    // Step 5: Compute d, the modular inverse of e mod phi
    long long d = modInverse(e, phi);
    cout << "Private exponent (d) = " << d << endl;

    // Step 6: Public and private keys
    cout << "Public Key: {" << e << ", " << n << "}" << endl;
    cout << "Private Key: {" << d << ", " << n << "}" << endl;

    // Step 7: Encryption
    long long message;
    cout << "\nEnter a message to encrypt (as a number): ";
    cin >> message;
    if (message > n) {
        cout << "Message is too large! Must be less than n." << endl;
        return 0;
    }

    long long encryptedMessage = modExpo(message, e, n);
    cout << "Encrypted Message: " << encryptedMessage << endl;

    // Step 8: Decryption
    long long decryptedMessage = modExpo(encryptedMessage, d, n);
    cout << "Decrypted Message: " << decryptedMessage << endl;

    return 0;
}
