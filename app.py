import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Credit Card Approval Prediction App
This app predicts the credit card approval probablity
""")
