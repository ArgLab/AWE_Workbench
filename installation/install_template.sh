#!/usr/bin/env bash

# AWE Workbench Install Script Template
# Author: Caleb Scott

# This script shows how to use the command-line arguments for the fresh_install.sh scripts.

# CASE 1: no dir, no env, no git, main branch, no proto, no data, no java (conda env)
./conda_fresh_install.sh arglab-dev-py312 conda git main proto data java

# CASE 1 (venv)
# ./fresh_install.sh arglab-dev-py312 venv git main proto data java

# CASE 2: dir + env + git, main branch, no proto, no data, java (conda env)
./conda_fresh_install.sh nodir noconda nogit main proto data nojava

# CASE 2 (venv)
# ./fresh_install.sh nodir novenv nogit main proto data nojava
