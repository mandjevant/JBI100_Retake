import pandas as pd


def get_data() -> pd.DataFrame:
    # Read data
    df = pd.read_csv("jbi100_app/data/tic_data.csv")

    # Any further data preprocessing can go her
    df_groups = ["Religion", "Relationship", "Children", "Education", "Occupation",
                 "Social class", "House owner", "Cars owned", "Health insurance", "Income"]

    for group_name in df_groups:
        if group_name == "Religion":
            df_cols = ["MGODRK", "MGODPR", "MGODOV", "MGODGE"]
            attr_names = ["Roman catholic", "Protestant …", "Other religion", "No religion"]
        elif group_name == "Relationship":
            df_cols = ["MRELGE", "MRELSA", "MRELOV", "MFALLEEN"]
            attr_names = ["Married", "Living together", "Other relation", "Singles"]
        elif group_name == "Children":
            df_cols = ["MFGEKIND", "MFWEKIND"]
            attr_names = ["Household without children", "Household with children"]
        elif group_name == "Education":
            df_cols = ["MOPLHOOG", "MOPLMIDD", "MOPLLAAG"]
            attr_names = ["High level education", "Medium level education", "Lower level education"]
        elif group_name == "Occupation":
            df_cols = ["MBERHOOG", "MBERZELF", "MBERBOER", "MBERMIDD", "MBERARBG", "MBERARBO"]
            attr_names = ["High status", "Entrepreneur", "Farmer", "Middle management", "Skilled labourers",
                          "Unskilled labourers"]
        elif group_name == "Social class":
            df_cols = ["MSKA", "MSKB1", "MSKB2", "MSKC", "MSKD"]
            attr_names = ["Social class A", "Social class B1", "Social class B2", "Social class C", "Social class D"]
        elif group_name == "House owner":
            df_cols = ["MHHUUR", "MHKOOP"]
            attr_names = ["Rented house", "Home owners"]
        elif group_name == "Cars owned":
            df_cols = ["MAUT1", "MAUT2", "MAUT0"]
            attr_names = ["1 car", "2 cars", "No car"]
        elif group_name == "Health insurance":
            df_cols = ["MZFONDS", "MZPART"]
            attr_names = ["National Health Service", "Private health insurance"]
        elif group_name == "Income":
            df_cols = ["MINKM30", "MINK3045", "MINK4575", "MINK7512", "MINK123M", "MINKGEM"]
            attr_names = ["Income < 30.000", "Income 30-45.000", "Income 45-75.000", "Income 75-122.000",
                          "Income >123.000", "Average income"]

        def define_value(row):
            for inx, col in enumerate(df_cols):
                if row[col] == 1:
                    return attr_names[inx]

        df[group_name] = df.apply(lambda row: define_value(row), axis=1)

    return df
