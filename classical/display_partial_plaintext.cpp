#include <iostream>
#include <string>
#include <map>

using namespace std;

// Declaration of apply_substitution()
string apply_substitution(
    const string &ciphertext,
    const map<char, char> &substitution);

void display_partial_plaintext(
    const string &ciphertext,
    const map<char, char> &substitution)
{
    cout << "\n========================================\n";
    cout << "          PARTIAL PLAINTEXT\n";
    cout << "========================================\n";

    string partial_plaintext =
        apply_substitution(ciphertext, substitution);

    cout << partial_plaintext << endl;

    cout << "========================================\n";
}
