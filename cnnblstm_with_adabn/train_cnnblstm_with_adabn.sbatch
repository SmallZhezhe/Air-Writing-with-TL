#!/bin/sh
module load nvidia/cuda/10.0
# get general model
# rm -rf ./params_general_cba
# python train_cnnblstm_with_adabn.py train ../dataset/all_train/ ./params_general_cba false false
# python train_cnnblstm_with_adabn.py test ../dataset/all_test/ ./params_general_cba false false
# get dong model
# rm -rf ./params_dong_cba
# python train_cnnblstm_with_adabn.py train ../dataset/all_train/train/ ./params_dong_cba false false
# python train_cnnblstm_with_adabn.py test ../dataset/all_test/test/ ./params_dong_cba false false
python train_cnnblstm_with_adabn.py test ../dataset/all_test/test/ ./params false false
