#include <iostream>
#include <string>
#include <cctype>

using namespace std;

string encrypt_text(string text, string key) {
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string result = "";

    for (char ch : text) {

        if (isalpha(ch)) {
            char upper = toupper(ch);

            int index = alphabet.find(upper);

            if (index != string::npos) {
                char newChar = key[index];

                if (islower(ch))
                    newChar = tolower(newChar);

                result += newChar;
            }
        }
        else {
            result += ch;
        }
    }

    return result;
}

void verify_solution(string plaintext, string original_ciphertext, string key) {

    string new_ciphertext = encrypt_text(plaintext, key);

    if (new_ciphertext == original_ciphertext) {
        cout << "\nSolution verified successfully.\n";
    }
    else {
        cout << "\nSolution verification failed.\n";
    }
}