#!/bin/sh
module load nvidia/cuda/10.0
# get general model
# rm -rf ./params_general_cb.pkl
# python train_cnnblstm.py train ../dataset/all_train/ ./params_general_cb.pkl false false
# python train_cnnblstm.py test ../dataset/all_test/ ./params_general_cb.pkl false false
# get dong model
rm -rf ./params_dong_cb.pkl
python train_cnnblstm.py train ../dataset/all_train/train/ ./params_dong_cb.pkl false false
python train_cnnblstm.py test ../dataset/all_test/test/ ./params_dong_cb.pkl false false
