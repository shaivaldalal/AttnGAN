#!/bin/bash
# coding: utf-8
import numpy as np
import os
import sys
import pickle
import shutil
import random
import subprocess
np.random.seed(3462)

# Declaring directories
DATA_DIR = '<directory_for_train_data>'
SAMPLED_TRAIN = '<directory_for_sampled_train_data>'
SAMPLED_VAL = '<directory_for_sampled_validation_data>'
SAMPLED_TEST = '<directory_for_sampled_test_data>'

DATA_FAKE = '<directory_for_generated_images>''
DATA_REAL = '<directory_for_real_images>'

SAMPLED_FAKE = '<directory_for_sampled_generated_images>'
SAMPLED_REAL = '<directory_for_sampled_real_images>'

# Set working directory
os.chdir(DATA_FAKE)


# Function to copy files
def copyWithSubprocess(cmd):        
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


#### Copying training files
# Randomly sampling data from the "DATA_DIR" and copying files to "SAMPLED_TRAIN"
files = []
for f in os.scandir(DATA_DIR):
    if 'train' in f.name:
        files.append(f.name)
sampled_files = np.random.choice(files, size=10000, replace=False)

# To optimise retrieval times, convert to set
tmp_filenames = set(tmp_filenames)


# Initialise the copy process
copied=0
total=len(tmp_filenames)
for f in tmp_filenames:
    copyWithSubprocess(['cp',DATA_DIR+f,SAMPLED_TRAIN])
    copied+=1
    done = (copied/total)*100
    if done%10==0:
        print('Done: {0:.2f}%%'.format(done))


##### Copying validation files
# Randomly sampling data from the "DATA_DIR" and copying files to "SAMPLED_VAL"
files_val = []
for f in os.scandir(DATA_DIR):
    if 'val' in f.name:
        files_val.append(f.name)
sampled_files_val = np.random.choice(files_val, size=10000, replace=False)


# To optimise retrieval times, convert to set
tmp_filenames_val = set(tmp_filenames_val)

# Initialise the copy process
copied = 0
total = len(tmp_filenames_val)
for f in tmp_filenames_val:
    copyWithSubprocess(['cp',DATA_DIR+f,SAMPLED_VAL])
    copied+=1
    done = (copied/total)*100
    if done%10==0:
        print('Done: {0:.2f}%'.format(done))


#### Copying test data
# In[14]:
# Randomly sampling data from the "DATA_DIR" and copying files to "SAMPLED_DIR"
files_test = []
for f in os.scandir(DATA_DIR):
    if 'test' in f.name:
        files_test.append(f.name)
sampled_files_test = np.random.choice(files_test, size=10000, replace=False)


# To optimise retrieval times, convert to set
tmp_filenames_test = set(tmp_filenames_test)

# Initialise the copy process
copied=0
total=len(tmp_filenames_test)
for f in tmp_filenames_test:
    copyWithSubprocess(['cp',DATA_DIR+f,SAMPLED_TEST])
    copied+=1
    done = (copied/total)*100
    if done%10==0:
        print('Done: {0:.2f}%'.format(done))


#### Sampling generated and fake images for FID score
# Randomly sampling data from the "DATA_FAKE"
files = []
for f in os.scandir(DATA_FAKE):
    files.append(f.name)
sampled_files = np.random.choice(files, size=1000, replace=False)

# To optimise retrieval times, convert to set
tmp_filenames = set(sampled_files)


# In[16]:
# Copying from "DATA_FAKE" to "SAMPLED_FAKE"
copied=0
total=len(tmp_filenames)
for f in tmp_filenames:
    copyWithSubprocess(['cp',DATA_FAKE+f,SAMPLED_FAKE])
    copied+=1
    done = (copied/total)*100
    if done%10==0:
        print('Done: {0:.2f}%%'.format(done))


# In[26]:
# Randomly sampling data from the "DATA_REAL" and copying files to "SAMPLED_REAL"
files_real = [x[:-8]+'.jpg' for x in tmp_filenames]
copied=0
total=len(files_real)
for f in files_real:
    copyWithSubprocess(['cp',DATA_REAL+f,SAMPLED_REAL])
    copied+=1
    done = (copied/total)*100
    if done%10==0:
        print('Done: {0:.2f}%%'.format(done))
