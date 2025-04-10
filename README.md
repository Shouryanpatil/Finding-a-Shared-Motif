# Finding a Shared Motif

This project solves the **Longest Common Substring** problem from a collection of DNA strings in FASTA format. It identifies all the longest substrings that are common across all given DNA sequences.

## 🧬 Problem Statement

Given a collection of up to 100 DNA strings (each up to 1kbp in length) in FASTA format, find the longest substrings that are common to all of them. If there are multiple solutions, return all of them.

### Example Input (FASTA format)

```
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
```

### Example Output

```
AC
TA
CA
```

## 🧠 How It Works

1. Reads DNA sequences from a file (`input.txt`) in FASTA format.
2. Identifies the shortest DNA string (to reduce comparisons).
3. Generates all substrings from longest to shortest.
4. Checks if each substring exists in **all** DNA strings.
5. Collects all substrings that are the longest and shared by all.

## 🐍 Usage

### 1. Prepare Input

Create a file named `input.txt` with your DNA sequences in FASTA format.

### 2. Run the Script

```bash
python longest_common_substrings.py
```

### 3. Output

The script will print all longest common substrings in alphabetical order.

## 📂 Files

- `longest_common_substrings.py` – Main Python script
- `input.txt` – Input file with DNA sequences (FASTA format)

## ✅ Requirements

- Python 3.x

## 📜 License

MIT License. Use freely and contribute!
