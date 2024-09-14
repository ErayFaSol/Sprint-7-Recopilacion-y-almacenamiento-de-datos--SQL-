# preprocessing.py
import pandas as pd

def load_data():
    df1 = pd.read_csv("datasets/project_sql_result_01.csv")
    df2 = pd.read_csv("datasets/project_sql_result_04.csv")
    df3 = pd.read_csv("datasets/project_sql_result_07.csv")
    return df1, df2, df3

def inspect_data(df):
    print(df.head())
    print(df.info())

def clean_data(df):
    return df.dropna().drop_duplicates()
