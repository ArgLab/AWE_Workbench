#!/usr/bin/env bash

# AWE Workbench Install Script (for conda)
# Author: Caleb Scott

# This script installs all necessary dependencies for AWE
# We make the following assumptions:
# * You have a working conda environment running on python 3.12.
# * You have pip installed in the conda environment.
#   (you can do this by 'conda create --name XXXX python=3.12 pip')

# Sanity Check: let the user know the preconditions.

NEW_DIR=${0:-"arglab-dev-py312"}
NEW_CONDA_ENV=${1:-"noconda"}
NEW_GIT=${2:-"nogit"}
BRANCH=${3:-"main"}
PROTOBUF=${4:-"noproto"}
DATA=${5:-"data"}
NEW_JAVA=${6:-"nojava"}

echo "============================ WARNING =============================="
echo "\nYou are about to install AWE on this system."
echo "\n* Ensure that you are using a python3.12 version."
echo "\n* The following repos are needed: "
echo "\n  > coreferee"
echo "\n  > holmes-extractor-expandable"
echo "\n  > AWE_LanguageTool"
echo "\n  > AWE_SpellCorrect"
echo "\n  > AWE_Lexica"
echo "\n  > AWE_Components"
echo "\n  > AWE_Workbench"
echo "\n"
echo "\nUsage: "
echo "\n  ./conda_fresh_install.sh [DIR] [CONDA] [GIT] [PROTOBUF] [DATA] [JAVA]"
echo "\n  NEW_DIR:  [XXXX/nodir]"
echo "\n  CONDA:    [conda/noconda]"
echo "\n  GIT:      [git/nogit]"
echo "\n  BRANCH:   [XXXX/main]"
echo "\n  PROTOBUF: [proto/noproto]"
echo "\n  DATA:     [data/nodata]"
echo "\n  JAVA:     [java/nojava]"
echo "\n==================================================================="

read -p "\n\n Continue [Y/N]? " -n 1 -r
echo  
if [[ $REPLY =~ ^[Yy]$ ]]
then
    # Set up new dir and cd to it
    if [ $NEW_DIR -ne "nodir" ]
    then 
        echo "Setting up new dev directory..."
        mkdir $NEW_DIR
        cd $NEW_DIR
    fi

    # Set up new conda env
    if [[ $NEW_CONDA_ENV =~ ^conda$ ]]
    then
        echo "Setting up new conda env..."
        conda create --name arglab-dev-py312 python=3.12 pip
    fi

    # Activate the env
    echo "Activating conda env..."
    conda activate arglab-dev-py312

    # Download relevant github repos
    if [[ $NEW_GIT =~ ^git$ ]]
    then
        echo "Pulling github repos..."
        git clone -b $BRANCH git@github.com:ArgLab/coreferee.git
        git clone -b $BRANCH git@github.com:ArgLab/holmes-extractor-expandable.git
        git clone -b $BRANCH git@github.com:ArgLab/AWE_LanguageTool.git
        git clone -b $BRANCH git@github.com:ArgLab/AWE_Lexica.git
        git clone -b $BRANCH git@github.com:ArgLab/AWE_Components.git
        git clone -b $BRANCH git@github.com:ArgLab/AWE_Workbench.git
    fi

    # Install repos
    echo "Installing repos..."
    pip install -e ./coreferee
    pip install -e ./holmes-extractor-expandable
    pip install -e ./AWE_LanguageTool
    pip install -e ./AWE_SpellCorrect
    pip install -e ./AWE_Components
    pip install -e ./AWE_Workbench

    # PROTOBUF fix?
    if [[ $PROTOBUF =~ ^proto$ ]]
    then
        pip install protobuf==3.20.0
    fi

    # Download data
    if [[ $DATA =~ ^data$ ]]
    then
        echo "Downloading data..."
        python -m awe_workbench.setup.data --develop
    fi

    # Install java
    if [[ $JAVA =~ ^java$ ]]
    then
        echo "Installing java sdk..."
        # Source: https://askubuntu.com/questions/1279677/how-to-install-openjdk-14-jdk-on-ubuntu-16-04
        wget https://download.java.net/java/GA/jdk14.0.2/205943a0976c4ed48cb16f1043c5c647/12/GPL/openjdk-14.0.2_linux-x64_bin.tar.gz

        tar xvf openjdk-14.0.2_linux-x64_bin.tar.gz

        mv jdk-14.0.2 /usr/lib/jvm

        update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk-14.0.2/bin/javac" 3
        update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk-14.0.2/bin/java" 3
        update-alternatives --set "javac" "/usr/lib/jvm/jdk-14.0.2/bin/javac"
        update-alternatives --set "java" "/usr/lib/jvm/jdk-14.0.2/bin/java"

        update-alternatives --config java
    fi
fi
