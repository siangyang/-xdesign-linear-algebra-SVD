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
```
README.md
code/
    svd.h
    svd.cpp
code_opt/
    svd.h
    svd.cpp
    hls_library/
        hls_svd.cpp
testdata/
    svd.py
    pynq_python/
        svd.py
script/
    directives.tcl
    run_hls.tcl
impl/
    svd_top_csynth.rpt
```

<!-- USAGE EXAMPLES -->
## Usage

1. fpga board setup

We use **Xilinx ZedBoard Evaluation and Development Kit** to evaulate this project

2. using HLS vivado to simulation and synthesis

3. export RTL

4. generate .bit from vivado

3. python test
```shell 
 python svd.py
```
## References
* xilinx vivado design examples

<!-- CONTRIBUTING -->
## Contributing
* fix negtive slack
* experiment on different scale floating number
