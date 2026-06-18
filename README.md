# Secure Hill-Climbing Algorithm for Multi-Issue Negotiation

This repository contains the source code for the secure multi-party computation (MPC) 
programs used in the following paper:

> Takashi Sakuma, Shun Okuhara, and Akinori Kawachi,  
> "Fully Private Hill-Climbing Protocol for Multi-Issue Negotiation,"  
> IEICE Transactions on Information and Systems, Vol.E109-D, No.7, 2026.  
> DOI: 10.1587/transinf.2025AHP0012

## Overview

This repository implements a fully private hill-climbing protocol for multi-issue 
negotiation based on secure multi-party computation (MPC), in which all intermediate 
states generated during the negotiation process are concealed.
The protocols are implemented using the csclib framework.

## Files

| File | Description |
|------|-------------|
| `hill_climbing_random_gen.py` | Generates random numbers and saves them to an external file for reproducibility |
| `hill_climbing_random_read.py` | Reads previously generated random numbers for reproducible experiments |
| `hill_climbing_random_random.py` | Basic implementation with internally generated random numbers |

## Experimental Environment

All experiments were conducted on the following environment:

- **Machine**: MacBook Pro (14-inch)
- **Processor**: Apple M3 Pro (11-core CPU, 14-core GPU, 16-core Neural Engine)
- **Memory**: 18 GB unified memory
- **Storage**: 512 GB SSD
- **OS**: macOS
- **MPC Framework**: csclib v20231212

## Requirements

- Python 3.9+
- csclib (v20231212)

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run with generated random numbers:
```bash
python hill_climbing_random_gen.py <party_id>
```

Run with pre-generated random numbers:
```bash
python hill_climbing_random_read.py <party_id>
```

Run basic implementation:
```bash
python hill_climbing_random_random.py <party_id>
```

## Parameters

- `max_iterations`: Maximum number of iterations (default: 100)
- `q`: Modulus for secret sharing (default: 1024)
- `weights`: Item weights (default: [10, 12, 7, 9, 21, 16])
- `capacity`: Capacity constraint (default: 65)
- `patience`: Maximum allowed iterations without improvement (default: 20)

## Related Repository

The source code for the fully private simulated annealing protocol is available at:  
https://github.com/takashisakuma-git/simulated-annealing-secure

## License

MIT License. See LICENSE for details.

## Citation

```bibtex
@article{sakuma2026hillclimbing,
  author  = {Takashi Sakuma and Shun Okuhara and Akinori Kawachi},
  title   = {Fully Private Hill-Climbing Protocol for Multi-Issue Negotiation},
  journal = {IEICE Transactions on Information and Systems},
  volume  = {E109-D},
  number  = {7},
  year    = {2026},
  doi     = {10.1587/transinf.2025AHP0012}
}
```
