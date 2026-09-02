#include <iostream>
#include <string>
#include <map>
#include <cctype>

using namespace std;

string apply_substitution(
    const string &ciphertext,
    const map<char, char> &substitution)
{
    string result = ciphertext;

    for (int i = 0; i < (int)result.length(); i++)
    {
        char c = result[i];

        if (isalpha(c))
        {
            char upper = toupper(c);

            if (substitution.find(upper) != substitution.end())
            {
                char replacement = substitution.at(upper);

                if (islower(c))
                {
                    result[i] = tolower(replacement);
                }
                else
                {
                    result[i] = replacement;
                }
            }
            else
            {
                result[i] = '_';
            }
        }
    }

    return result;
}
