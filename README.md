# CryptoLab Assignment 1

## Team Members
- Aastha
- Mahek

## Overview

This project is the first assignment for the Cryptography Lab. The aim is to build a modular cryptography toolkit in Python that can be expanded in future assignments. For this week, we have created the basic project structure, a menu-driven command-line interface, and a file analysis module. Placeholder options have also been added for encryption, decryption, and attack modules, which will be implemented later.

## Folder Structure

- classical
- attacks
- math
- modern
- analysis
- datasets
- outputs
- docs
- tests
- utils

## Modules

- **Encrypt** *(Coming Soon)* – This module will contain different encryption algorithms.
- **Decrypt** *(Coming Soon)* – This module will be used to decrypt encrypted messages.
- **Attack** *(Coming Soon)* – This module will include cryptanalysis techniques for breaking or analyzing ciphers.
- **File Analysis** – Reads a text file from the `datasets` folder and displays useful statistics such as the number of characters, words, lines, and the frequency of each alphabet letter.

## Working

When the program starts, it displays a menu with five options: Encrypt, Decrypt, Attack, Analyze Text File, and Exit.

- Selecting **Encrypt**, **Decrypt**, or **Attack** currently displays a "Coming Soon!" message, as these features will be implemented in future assignments.
- Selecting **Analyze Text File** prompts the user to enter the name of a text file stored in the `datasets` folder. The program then reads the file and calculates:
  - Total number of characters
  - Total number of words
  - Total number of lines
  - Frequency of each alphabet letter
- Every menu selection made by the user is recorded in the `execution.log` file along with the current date and time.
- Choosing **Exit** closes the program.

## Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub
