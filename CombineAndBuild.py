# encoding: utf-8

import pandas as pd
from WDAtoV4 import makeV4


# Rates
ratesFiles = [
    "RatesWDA2014.csv",
    "RatesWDA2015.csv",
    "RatesWDA2016.csv"
]


allDataFrames = []
for f in ratesFiles:

    df = pd.read_csv(f)
    df.fillna("", inplace=True)
    df = df[:-1]
    allDataFrames.append(df)

rates = pd.concat(allDataFrames)
rates.to_csv("WDA_Combined_Rates.csv", index=False)
makeV4("WDA_Combined_Rates.csv", geo="K02000001")


# Rates
membershipFiles = [
    "MembershipWDA2014.csv",
    "MembershipWDA2015.csv",
    "MembershipWDA2016.csv"
]


allDataFrames = []
for f in membershipFiles:

    df = pd.read_csv(f)
    df.fillna("", inplace=True)
    df = df[:-1]

    df["Dim_ID_4"][df["Dim_ID_4"] == "Public Private Sector"] = "Public / Private Sector"
    df["dimension_Label_Eng_4"] =  df["Dim_ID_4"]

    allDataFrames.append(df)

rates = pd.concat(allDataFrames)
rates.to_csv("WDA_Combined_Membership.csv", index=False)
makeV4("WDA_Combined_Membership.csv", geo="K02000001")

