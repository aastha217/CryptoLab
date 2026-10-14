#include <iostream>
#include <string>
#include <cctype>

using namespace std;

string apply_substitution(string text, string key) {
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string result = "";

    for (char ch : text) {

        if (isalpha(ch)) {
            char upper = toupper(ch);

            int index = key.find(upper);

            if (index != string::npos) {
                char newChar = alphabet[index];

                if (islower(ch))
                    newChar = tolower(newChar);

                result += newChar;
            }
            else {
                result += '_';
            }
        }
        else {
            result += ch;
        }
    }

    return result;
}