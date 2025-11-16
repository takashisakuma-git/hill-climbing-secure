# Secure Hill-Climbing Algorithm for Multi-Issue Negotiation

This repository provides the source code for the hill-climbing algorithm used in our paper:

**Title:** [Fully Private Hill-Climbing Protocol for Multi-Issue Negotiation]  
**Authors:** [Takashi SAKUMA, Shun OKUHARA, and Akinori KAWACHI]  
**DOI:** [DOI or preprint link]

---

## Overview
This code implements a secure hill-climbing algorithm for multi-issue negotiation using secret sharing.  
We provide three versions for different purposes:

- `hill_climbing_random.py`: Basic implementation (random numbers generated internally).
- `hill_climbing_random_gen.py`: Generates random numbers and saves them to an external file for reproducibility.
- `hill_climbing_random_read.py`: Reads previously generated random numbers for reproducible experiments.

---

## Requirements
- Python 3.9+
- `csclib` (custom library for secure computation)

Install dependencies:
```bash
pip install -r requirements.txt

---

## How to Run
Run the basic implementation:
```bash
python src/test_random.py <party_id>
```
Run with generated random numbers:
```bash
python src/test_random_gen.py <party_id>
- This will create a file random_index_<timestamp>.txt in the current directory.
```
Run with pre-generated random numbers:
- Place the generated random index file in the working directory and run:
```bash
python src/test_random_read.py <party_id>
```

---

## Parameters
- max_iterations: Maximum number of iterations (default: 100)
- q: Modulus for secret sharing (default: 1024)
- weights: Item weights (default: [10, 12, 7, 9, 21, 16])
- capacity: Capacity constraint (default: 65)
- patience: Maximum allowed iterations without improvement (default: 20)

---

## Stopping Criteria
The algorithm stops when:
- Stop when max_iterations is reached or when no improvement occurs for patience iterations.

---

## Experimental Settings
To reproduce experiments:
Run test_random_gen.py to generate random numbers.
Use the generated file with test_random_read.py.

---

## License
MIT License. See LICENSE for details.

## Citation
If you use this code, please cite:
@article{sakuma2025hillclimbing,
author    = {Takashi Sakuma and Shun Okuhara and Akinori Kawachi},
title     = {Fully Private Hill-Climbing Protocol for Multi-Issue Negotiation},
journal   = {IEICE Transactions on Information and Systems},
volume    = {E108-D},    % 実際の巻号を記載
number    = {xx},        % 実際の号数を記載
pages     = {xxx--xxx},  % ページ範囲を記載
year      = {2025},
doi       = {DOI or preprint link}
}
