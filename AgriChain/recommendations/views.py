from django.shortcuts import render
import os
import json
import pickle
import numpy as np
from scipy import stats


# # Loading all Crop Recommendation Models

# crop_knn_pipeline = pickle.load(
#     open("media/models/crop_recommendation/knn_pipeline.pkl", "rb")
# )
# crop_label_dict = pickle.load(
#     open("media/models/crop_recommendation/label_dictionary.pkl", "rb")
# )


# # Loading all Fertilizer Recommendation Models
# fertilizer_xgb_pipeline = pickle.load(
#     open("media/models/fertilizer_recommendation/xgb_pipeline.pkl", "rb")
# )
# fertilizer_rf_pipeline = pickle.load(
#     open("media/models/fertilizer_recommendation/rf_pipeline.pkl", "rb")
# )
# fertilizer_svm_pipeline = pickle.load(
#     open("media/models/fertilizer_recommendation/svm_pipeline.pkl", "rb")
# )
# fertilizer_label_dict = pickle.load(
#     open("media/models/fertilizer_recommendation/fertname_dict.pkl", "rb")
# )
# soiltype_label_dict = pickle.load(
#     open("media/models/fertilizer_recommendation/soiltype_dict.pkl", "rb")
# )
# croptype_label_dict = pickle.load(
#     open("media/models/fertilizer_recommendation/croptype_dict.pkl", "rb")
# )


# crop_label_name_dict = {}
# for crop_value in croptype_label_dict:
#     crop_label_name_dict[croptype_label_dict[crop_value]] = crop_value

# soil_label_dict = {}
# for soil_value in soiltype_label_dict:
#     soil_label_dict[soiltype_label_dict[soil_value]] = soil_value


# def convert(o):
#     if isinstance(o, np.generic):
#         return o.item()
#     raise TypeError


# Create your views here.

def recommend(request):
    return render(request,'recommend/recommend.html')

def result(request):
    return render(request,'recommend/result.html')
