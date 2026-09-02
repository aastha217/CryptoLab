#include <iostream>
#include <string>
#include <cctype>

using namespace std;

bool verify_solution(
    const string &plaintext,
    const string &ciphertext,
    const string &key)
{
    // A monoalphabetic substitution key must contain
    // 26 letters.
    if (key.length() != 26)
    {
        return false;
    }

    string generated_ciphertext = plaintext;

    // Encrypt the plaintext using the key.
    // key[0] = ciphertext letter for A
    // key[1] = ciphertext letter for B
    // ...
    // key[25] = ciphertext letter for Z

    for (int i = 0; i < (int)generated_ciphertext.length(); i++)
    {
        char c = generated_ciphertext[i];

        if (isalpha(c))
        {
            bool lowercase = islower(c);

            char upper = toupper(c);

            int index = upper - 'A';

            char replacement = key[index];

            if (lowercase)
            {
                generated_ciphertext[i] = tolower(replacement);
            }
            else
            {
                generated_ciphertext[i] = replacement;
            }
        }
    }

    // Compare generated ciphertext with original ciphertext.
    return generated_ciphertext == ciphertext;
}
