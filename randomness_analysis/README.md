# Operating-System Random Number Generation Analysis

## 1. Objective

The objective of this project is to evaluate operating-system random-number generation mechanisms and investigate their suitability for cryptographic applications.

We will generate at least 1 MiB of random data using three mechanisms:

- Linux `/dev/urandom`
- OpenSSL `rand`
- Windows cryptographic random-number generation API using .NET

The generated data will be analyzed using statistical tests to identify possible biases, patterns, and correlations.

## 2. Project Structure

```text
randomness_analysis/
├── data/
│   ├── urandom.bin
│   ├── openssl.bin
│   └── windows_cng.bin
├── analysis.ipynb
├── README.md
└── requirements.txt
```

### Files and Directories

- `data/`: Stores the generated random data files.
- `urandom.bin`: Data generated using Linux `/dev/urandom`.
- `openssl.bin`: Data generated using OpenSSL.
- `windows_cng.bin`: Data generated using the Windows cryptographic random-number API.
- `analysis.ipynb`: Contains the analysis code, graphs, statistical tests, and interpretation.
- `requirements.txt`: Lists the Python dependencies required for the analysis.

## 3. Technologies Used

- Linux (Ubuntu through WSL)
- Windows
- OpenSSL
- Python
- Jupyter Notebook
- NumPy
- SciPy
- Pandas
- Matplotlib
- .NET cryptographic random-number API

## 4. Methodology

### 4.1 Random Data Generation

At least 1 MiB of random data will be generated using each of the three mechanisms.

The generated binary files will be stored in the `data/` directory.

Linux data can be generated using:

```bash
head -c 1048576 /dev/urandom > data/urandom.bin
```

OpenSSL data can be generated using:

```bash
openssl rand -out data/openssl.bin 1048576
```

Windows data will be generated using the .NET `System.Security.Cryptography.RandomNumberGenerator` API.

### 4.2 Statistical Analysis

The generated data will be analyzed using the following methods:

1. **Byte-frequency distribution:** Examines how frequently each possible byte value occurs.
2. **Bit distribution:** Measures the number of zero and one bits.
3. **Repeated-pattern analysis:** Investigates repeated bytes and short sequences.
4. **Serial correlation:** Measures the relationship between consecutive byte values.
5. **Statistical tests:** Uses appropriate statistical tests to investigate deviations from expected random behavior.

### 4.3 Comparison

The results from the three mechanisms will be compared to identify observable differences in their statistical properties.

The findings will be documented in `analysis.ipynb`, supported by graphs, test results, and explanations.

## 5. Cryptographic Security

Statistical tests can help identify certain biases and patterns in random data. However, passing these tests does not prove that a random-number generator is cryptographically secure.

Cryptographic security also depends on the generator's design, initialization, internal-state management, and resistance to prediction and attacks.

The project will discuss why statistical analysis alone is insufficient to establish cryptographic security.

## 6. How to Run the Analysis

### Step 1: Install dependencies

From the project directory, run:

```bash
pip install -r requirements.txt
```

### Step 2: Generate the datasets

Generate the Linux and OpenSSL datasets using the commands in Section 4.1.

Generate the Windows dataset using the Windows cryptographic API.

Ensure all three files are present in the `data/` directory before running the complete analysis.

### Step 3: Run the notebook

Open `analysis.ipynb` in VS Code with the Jupyter extension installed.

Select the appropriate Python environment and run the notebook cells.

## 7. Results and Conclusion

**Status: Experiment in progress.**

The statistical results, comparisons, and final conclusions will be added after the datasets have been generated and analyzed.

The final report will discuss the observed byte and bit distributions, repeated patterns, serial correlations, statistical test results, and implications for cryptographic applications.

## 8. Team

This project is being developed collaboratively as part of a cryptography lab assignment.