# Network Project

## Overview
This project implements a **multi-path routing algorithm** designed to identify a set of **disjoint paths** in a graph and rank them based on **stability**. Stability is calculated using a **Fuzzy Inference System (FIS)**, which evaluates paths based on energy, speed, and hop count. The path with the highest stability is selected for routing and compared to the shortest path found using the **Breadth-First Search (BFS)** algorithm, demonstrating the advantages of the proposed approach over traditional methods.

### Key Features
1. **Multi-Path Routing Algorithm**:
   - Searches for **disjoint paths** in the graph, ensuring no overlap in nodes.
   - Evaluates paths based on metrics such as energy, speed, and hops.

2. **Stability Ranking**:
   - Uses a **Fuzzy Inference System (FIS)** to calculate path stability.
   - Stability factors include:
     - Residual energy
     - Average speed
     - Hop count
   - Paths are ranked, and the most stable path is selected.

3. **Comparison with BFS**:
   - The best path from the proposed algorithm is compared with the shortest path found using BFS.
   - Demonstrates the effectiveness of the custom algorithm in terms of energy efficiency and network stability.

4. **Interactive GUI**:
   - Provides a visual interface for creating, managing, and analyzing network graphs.
   - Supports node and edge creation, weight assignment, and path visualization.

---

## Installation

### Prerequisites
- Python 3.8+
- Required Python libraries:
  - `numpy`
  - `skfuzzy`
  - `scipy`
  - `PyQt5`

### Steps
1. Clone the repository:
   ```bash
   git clone git@github.com:YuliiaHrabovenko/fuzzy-logic-routing-method.git
   cd fuzzy-logic-routing-method
   python main.py
