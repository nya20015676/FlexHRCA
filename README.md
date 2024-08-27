# FlexHRCA

## Overview
This repository contains the data and code used in my paper titled "Flexible Task Assignment and Assembly Scheduling for Human-Robot Collaboration Cell considering Uncertainty". 
This paper investigates the optimisation of task assignment and scheduling in a collaborative environment involving multiple humans and robots for multi-product assembly. Considering the preferences of both humans and robots, diverse tasks are assigned to different operation modes, including human-only, robot-only, and collaborative human-robot. In this study, single-valued neutrosophic numbers (SVTN) are used to represent the uncertainty of the HRC task schedule. The goal is to minimize the uncertain product cycle time by fully utilizing human and robot resources while reducing idle time. An improved genetic algorithm (IGA) is proposed to optimise the human-robot task assignment and assembly sequence. It includes human or robot selection, assembly sequence as chromosome coding, and active decoding under the constraints of different HRC types. The proposed model has been tested on a case study involving the assembly of lithium battery packs to demonstrate its feasibility in improving HRC assembly efficiency. Computational results show that the model can effectively reduce cycle time and control uncertainty variance in most scenarios, with SVTN outperforming other methods in uncertainty control.

## Project Structure
- `fuzzyNumber.py`: Fuzzy numbers and single-valued triangular neutrosophic numbers
- `hrcStation.py`: Genetic algorithm for HRCA
- `opTimeData/`: Datasets used in the paper.
- `orthogonalTest/`: Parameters setting for GA and SVTN (Chapter 5.2).
- `HnRnTest/`: Multi-human and multi-robot test (Chapter 5.3.1).
- `comparison/`: CSP, TFN, SVTN comparison test (Chapter 5.3.2 and 5.3.3).

