#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

void frequency_analysis(string text) {
    map<char, int> frequency;
    int total = 0;

    for (char ch : text) {
        if (isalpha(ch)) {
            ch = toupper(ch);
            frequency[ch]++;
            total++;
        }
    }

    vector<pair<char, int>> data;

    for (auto x : frequency) {
        data.push_back(x);
    }

    sort(data.begin(), data.end(), [](auto a, auto b) {
        return a.second > b.second;
    });

    cout << "\nFrequency Analysis\n";
    cout << "Letter\tCount\tPercentage\n";

    for (auto x : data) {
        double percentage = (double)x.second / total * 100;

        cout << x.first << "\t"
             << x.second << "\t"
             << percentage << "%\n";
    }
}