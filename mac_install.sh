#!/bin/bash

#### Install or update brew
which -s brew
if [[ $? != 0 ]] ; then
    # Install Homebrew
    echo "Installing Homebrew"
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    echo "Homebrew installed"
else
    echo "updated Homebrew"
    brew update
    echo "Homebrew updated"
fi

echo "install python"
brew install python3
brew install ipython
brew install pip3

echo "install python librairies"
pip3 install gensim
pip3 install pandas
pip3 install tqdm
