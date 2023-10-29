# Disk Scheduling Algorithm Simulation with Python and Tkinter

## Overview

This project is a visual demonstration of disk scheduling algorithms in Operating Systems, implemented using Python and the Tkinter library for GUI and Turtle for creating graphical animations. Disk scheduling is a critical component in optimizing disk I/O request servicing, aiming for fairness, high throughput, and minimal traveling head time.

### Disk Scheduling Algorithms Implemented

1. **FCFS Scheduling Algorithm**: Services I/O requests in the order of arrival, ensuring no starvation.

2. **SSTF (Shortest Seek Time First) Algorithm**: Selects the request requiring the least disk arm movement from the current position.

3. **SCAN Scheduling Algorithm**: The disk arm moves in one direction until the end, servicing all requests on its path, and then returns, servicing requests on the way back.

4. **C-SCAN Scheduling Algorithm**: The disk arm moves in one direction until the last cylinder, jumps to the last cylinder in the opposite direction, and then turns back to service the remaining requests.

5. **C-LOOK Scheduling Algorithm**: The disk arm moves outwards, services requests until the highest request cylinder, jumps to the lowest request cylinder, and continues servicing requests.

## Tkinter and Turtle Integration

- We've leveraged Tkinter to create a user-friendly graphical interface for selecting the algorithm and providing input parameters.

- Turtle is used for dynamic animations, providing a visual representation of the disk head movement and the order of request servicing.

## Getting Started

1. Clone the repository:
git clone [](https://github.com/Am-Issath/Disk-Sched-Algo-Python.git)

2. Run the Python scripts:
main.py
disk_scheduling.py
graph.py
visualization.py

3. Use the GUI to select an algorithm, configure input, and visualize the disk scheduling process.

## Demo

**Main GUI**

![EmptyFrame](https://github.com/Am-Issath/Disk-Sched-Algo-Python/assets/74565253/ec2210ee-57ad-43a8-af57-e04cc7fdec53)

**Enter values**
![1](https://github.com/Am-Issath/Disk-Sched-Algo-Python/assets/74565253/a4148311-2e10-43f6-a5d3-bfa9f394b18d)

**FCFS**
![FCFS](https://github.com/Am-Issath/Disk-Sched-Algo-Python/assets/74565253/38931cf7-4a6b-4239-bf66-68989ec02767)

**SSTF**
![SSTF](https://github.com/Am-Issath/Disk-Sched-Algo-Python/assets/74565253/f22b4a50-50d0-4e2e-ae60-f543a346ef15)

**SCAN**
![SCAN](https://github.com/Am-Issath/Disk-Sched-Algo-Python/assets/74565253/ec659c53-25ca-45d5-9272-d9be11860d01)

**CSCAN**
![CSCAN](https://github.com/Am-Issath/Disk-Sched-Algo-Python/assets/74565253/d17fa7fb-5d62-4110-b301-9a9af4e42c97)

**CLOOK**
![CLOOK](https://github.com/Am-Issath/Disk-Sched-Algo-Python/assets/74565253/3c0735a2-c5e1-485d-a5ad-5f3151b358b9)

**Graphically compare each algorithm** 
![Graph](https://github.com/Am-Issath/Disk-Sched-Algo-Python/assets/74565253/6f81aad1-3f57-4315-9c50-49be051dede7)

**By Mohamed Issath**  [](https://github.com/Am-Issath)
