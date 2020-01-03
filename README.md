# EQ Works Task
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/94e08cf33e484c62ac347c81d978a7cc)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Abdelrahman-IK/eqworks_task&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/Abdelrahman-IK/eqworks_task.svg?branch=master)](https://travis-ci.org/Abdelrahman-IK/eqworks_task)

This repo contains solutions for the following tasks:
```
1- Cleanup
2- Labeling
3- Analysis
4b- Pipeline Dependency
```
#### Prerequisite

```
Python: 3.5+
Pandas: 0.25.3 
```

#### Note
```
If you want to run tasks 1,2,3 on specific datasets
Please include them into data directory
and pass them to input when you start Analysis.py
otherwise ignore the input names and it will load
the default datasets from data directory.
```

#### Quick Start

```
git clone https://github.com/Abdelrahman-IK/eqworks_task
cd eqworks_task
#For tasks 1,2,3
python3 Analysis.py
#For task 4b
python3 DAG.py
```
#### Workflow

```
- Tasks 1,2,3:
    A- Case using the default datasets:
        1- Run python3 Analysis.py
        2- Ignore datasets inputs
        3- Check the results in result directory
    B- Case using different datasets:
        1- Run python3 Analysis.py
        2- Enter requests dataset's name
        3- Enter POIs dataset's name
        4- Check the results in result directory
- Task 4b:
    1- Run python3 DAG.py
    2- Check the output in terminal
```
#### Copyright and License

```
MIT License

Copyright (c) 2019 Abdelrahman Ikram

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```