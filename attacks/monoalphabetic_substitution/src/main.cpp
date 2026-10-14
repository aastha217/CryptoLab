#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void frequency_analysis(string text);
void word_frequency_analysis(string text);
void pattern_analysis(string text);

string apply_substitution(string text, string key);

void display_partial_plaintext(string text);

void verify_solution(string plaintext, string ciphertext, string key);

string encrypt_text(string text, string key);

int main() {

    ifstream file("attacks/monoalphabetic_substitution/testcases/plaintext.txt");

    if (!file) {
        cout << "Could not open plaintext.txt" << endl;
        return 1;
    }

    string plaintext;
    string line;

    while (getline(file, line)) {
        plaintext += line + "\n";
    }

    file.close();

    cout << "Plaintext loaded successfully.\n";

    string key = "QWERTYUIOPASDFGHJKLZXCVBNM";

    string ciphertext = encrypt_text(plaintext, key);

    cout << "\nEncrypted Text:\n";
    cout << ciphertext << endl;

    ofstream output("attacks/monoalphabetic_substitution/outputs/ciphertext.txt");

    if (!output) {
        cout << "Could not create ciphertext.txt" << endl;
        return 1;
    }

    output << ciphertext;
    output.close();

    cout << "Ciphertext saved successfully.\n";

    frequency_analysis(ciphertext);

    word_frequency_analysis(ciphertext);

    pattern_analysis(ciphertext);

    string partial_plaintext = apply_substitution(ciphertext, key);

    display_partial_plaintext(partial_plaintext);

    verify_solution(plaintext, ciphertext, key);

    return 0;
}