#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

void word_frequency_analysis(string text) {
    map<string, int> frequency;
    string word = "";

    for (char ch : text) {
        if (isalpha(ch)) {
            word += tolower(ch);
        } else {
            if (!word.empty()) {
                frequency[word]++;
                word = "";
            }
        }
    }

    if (!word.empty()) {
        frequency[word]++;
    }

    vector<pair<string, int>> data;

    for (auto x : frequency) {
        data.push_back(x);
    }

    sort(data.begin(), data.end(), [](auto a, auto b) {
        return a.second > b.second;
    });

    cout << "\nWord Frequency Analysis\n";
    cout << "Word\tCount\n";

    for (auto x : data) {
        if (x.first.length() <= 3) {
            cout << x.first << "\t"
                 << x.second << "\n";
        }
    }

    cout << "\nRepeated Words\n";

    for (auto x : data) {
        if (x.second > 1) {
            cout << x.first << " -> "
                 << x.second << " times\n";
        }
    }
}