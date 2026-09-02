#include <iostream>
#include <map>
#include <vector>
#include <cctype>

using namespace std;

string get_pattern(string word) {
    map<char, int> values;
    string pattern = "";
    int number = 0;

    for (char ch : word) {
        ch = tolower(ch);

        if (values.find(ch) == values.end()) {
            values[ch] = number;
            number++;
        }

        pattern += to_string(values[ch]);
    }

    return pattern;
}

void pattern_analysis(string text) {
    map<string, vector<string>> patterns;
    string word = "";

    for (char ch : text) {
        if (isalpha(ch)) {
            word += tolower(ch);
        } else {
            if (!word.empty()) {
                string pattern = get_pattern(word);
                patterns[pattern].push_back(word);
                word = "";
            }
        }
    }

    if (!word.empty()) {
        string pattern = get_pattern(word);
        patterns[pattern].push_back(word);
    }

    cout << "\nPattern Analysis\n";

    for (auto x : patterns) {
        if (x.second.size() > 1) {
            cout << "Pattern " << x.first << " : ";

            for (string word : x.second) {
                cout << word << " ";
            }

            cout << "\n";
        }
    }
}