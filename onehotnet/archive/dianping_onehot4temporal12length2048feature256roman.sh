#!/bin/bash

# Archived program command-line for experiment
# Copyright 2016 Xiang Zhang
#
# Usage: bash {this_file} [additional_options]

set -x;
set -e;

qlua main.lua -driver_location models/dianping/onehot4temporal12length2048feature256roman -train_data_file data/dianping/train_pinyin_string.t7b -test_data_file data/dianping/test_pinyin_string.t7b "$@";
