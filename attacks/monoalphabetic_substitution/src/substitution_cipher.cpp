#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

using namespace std;

string apply_substitution(string text, string key) {
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string result = "";

    for (char ch : text) {
        if (isalpha(ch)) {
            char upper = toupper(ch);
            int index = alphabet.find(upper);
            char newChar = key[index];

            if (islower(ch))
                newChar = tolower(newChar);

            result += newChar;
        } else {
            result += ch;
        }
    }

    return result;
}

int main() {
    string key = "QWERTYUIOPASDFGHJKLZXCVBNM";

    ifstream input("attacks/monoalphabetic_substitution/testcases/plaintext.txt");

    if (!input) {
        cout << "Could not open plaintext.txt" << endl;
        return 1;
    }

    string plaintext;
    string line;

    while (getline(input, line)) {
        plaintext += line + "\n";
    }

    input.close();

    string ciphertext = apply_substitution(plaintext, key);

    ofstream output("attacks/monoalphabetic_substitution/outputs/ciphertext.txt");

    if (!output) {
        cout << "Could not create ciphertext.txt" << endl;
        return 1;
    }

    output << ciphertext;
    output.close();

    cout << "Plaintext encrypted successfully." << endl;
    cout << endl;
    cout << "Plain alphabet : ABCDEFGHIJKLMNOPQRSTUVWXYZ" << endl;
    cout << "Cipher alphabet: " << key << endl;

    return 0;
}