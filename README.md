# [xdesign] linear algebra SVD

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Usage](#usage)
* [References](#References)
* [Contributing](#contributing)



<!-- ABOUT THE PROJECT -->
## About The Project
Using high level synthesis to accelerate singular value decomposition (SVD), the most common matrix  method. 

**Directory structure**
* **README.md** - introduce the project, algorithm, reference ....
* **code/**
  * original - original code from open source if there is 
  * final (use inline pragma) - include both host and kernel code ※Note: host code must do auto-check
* **code-opt/** - Note it may have multiple code directories for different code structure, named by code-opt  (opt refer to optimization method, e.g. code-OoO  Out-Of-Order)
  * including library modification
* **testdata/** - include input test data, and output result data
* **script/** - makefile
* **impl/** - result of the implementation, only the metafile, and report, e.g. vitis summary file, HLS csynth report

<!-- USAGE EXAMPLES -->
## Usage
```
README.md
design/
    svd.h
    svd.cpp
testbench/
    svd_tb.cpp
hls_library/
    hls_svd.cpp
pynq_python/
    svd.py	
```

1. fpga board setup

We use **Xilinx ZedBoard Evaluation and Development Kit** to evaulate this project

2. using HLS vivado to simulation and synthesis

3. export RTL

4. generate .bit from vivado

3. python test
```sh
 python svc.py
```
## References
* xilinx vivado design examples

<!-- CONTRIBUTING -->
## Contributing
* fix negtive slack
* experiment on different scale floating number
