# FlexHRCA

## Overview
This repository contains the data and code used in paper titled "Flexible Task Assignment and Assembly Scheduling for Human-Robot Collaboration Cell considering Uncertainty". 

## Project Structure
- `fuzzyNumber.py`: Fuzzy numbers and single-valued triangular neutrosophic numbers
- `hrcStation.py`: Genetic algorithm for HRCA
- `opTimeData/`: Datasets used in the paper.
- `orthogonalTest/`: Parameters setting for GA and SVTN (Chapter 5.2).
- `HnRnTest/`: Multi-human and multi-robot test (Chapter 5.3.1).
- `comparison/`: Comparison algorithms including OR-Tools (OR), Reinforcement Learning (RL), basic GA with TFN (GA-TFN), IGA with CSP (IGA-CSP), and IGA with TFN (IGA-TFN) to benchmark against the proposed IGA with SVTN (IGA-SVTN) (Chapter 5.3.3).

## Reference Code
This codebase partially references the cls1277/gantt-for-JSP-python and ai4co/rl4co project. We acknowledge and appreciate the insights and implementations provided by this project.
