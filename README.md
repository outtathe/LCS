# Longest Common Subsequence (LCS) Algorithm

## Introduction

This repository contains an implementation of the Longest Common Subsequence (LCS) algorithm in Python. The LCS algorithm is used to find the longest subsequence that two sequences have in common. It has applications in various fields, including bioinformatics, data comparison, and text analysis.

## Getting Started

### Prerequisites

Before you can use this algorithm, make sure you have Python (>= 3.0) installed on your system and a code editor or development environment of your choice.

### Installation

You can clone this repository using the following command:

```bash
git clone https://github.com/your-username/lcs-algorithm.git
```
## Example of usage:
In dynamic programming
```python
textX = "AGGTAB"
textY = "GXTXAYB"
c = longestCommonSubsequence
print("LCS длина: ", len(c.lcs(textX, textY)))
```
In recursion
```python
X = "bd0"
Y = "abcd0"
print("LCS длина: ", lcs(X, Y, len(X), len(Y)))
```