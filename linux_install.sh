#!/bin/bash

echo "install python3"
apt-get install python3
apt-get install ipython
apt-get install pip3

echo "install python librairies"
pip3 install gensim
pip3 install pandas
pip3 install tqdm
