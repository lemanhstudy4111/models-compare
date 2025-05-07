# models-compare
Final Project CS589

Steven Tang: My machine runs Ubuntu 24.04.2 LTS, and the following packages need to installed:
gcc make perl python3-tk

Install with "sudo apt-get install gcc make perl python3-tk"

--How to run--

    // create your virtual python environment
    python3 -m venv myvenv

    source myvenv/bin/activate

    // install necessary packages
    pip install -r requirements.txt

    // create csv file
    python3 run.py > handwritten.csv
