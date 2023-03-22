# Here you can add any global configuations

df_columns = ['MOSTYPE', 'MAANTHUI', 'MGEMOMV', 'MGEMLEEF', 'MOSHOOFD', 'CARAVAN']

df_columns_full = ['ORIGIN', 'MOSTYPE', 'MAANTHUI', 'MGEMOMV', 'MGEMLEEF', 'MOSHOOFD',
                   'MGODRK', 'MGODPR', 'MGODOV', 'MGODGE', 'MRELGE', 'MRELSA', 'MRELOV',
                   'MFALLEEN', 'MFGEKIND', 'MFWEKIND', 'MOPLHOOG', 'MOPLMIDD', 'MOPLLAAG',
                   'MBERHOOG', 'MBERZELF', 'MBERBOER', 'MBERMIDD', 'MBERARBG', 'MBERARBO',
                   'MSKA', 'MSKB1', 'MSKB2', 'MSKC', 'MSKD', 'MHHUUR', 'MHKOOP', 'MAUT1',
                   'MAUT2', 'MAUT0', 'MZFONDS', 'MZPART', 'MINKM30', 'MINK3045',
                   'MINK4575', 'MINK7512', 'MINK123M', 'MINKGEM', 'MKOOPKLA', 'PWAPART',
                   'PWABEDR', 'PWALAND', 'PPERSAUT', 'PBESAUT', 'PMOTSCO', 'PVRAAUT',
                   'PAANHANG', 'PTRACTOR', 'PWERKT', 'PBROM', 'PLEVEN', 'PPERSONG',
                   'PGEZONG', 'PWAOREG', 'PBRAND', 'PZEILPL', 'PPLEZIER', 'PFIETS',
                   'PINBOED', 'PBYSTAND', 'AWAPART', 'AWABEDR', 'AWALAND', 'APERSAUT',
                   'ABESAUT', 'AMOTSCO', 'AVRAAUT', 'AAANHANG', 'ATRACTOR', 'AWERKT',
                   'ABROM', 'ALEVEN', 'APERSONG', 'AGEZONG', 'AWAOREG', 'ABRAND',
                   'AZEILPL', 'APLEZIER', 'AFIETS', 'AINBOED', 'ABYSTAND', 'CARAVAN']

df_groups = ["Religion", "Relationship", "Children", "Education", "Occupation",
             "Social class", "House owner", "Cars owned", "Health insurance", "Income"]


customer_main_types = ["Successful hedonists", "Driven Growers", "Average Family",
                       "Career Loners", "Living well", "Cruising Seniors", "Retired and Religeous",
                       "Family with grown ups", "Conservative families", "Farmers"]
age_types = ["20-30 years", "30-40 years", "40-50 years",
             "50-60 years", "60-70 years", "70-80 years"]
number_of_houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
income_dict = {
    "MINKM30": "Income < 30.000",
    "MINK3045": "Income 30-45.000",
    "MINK4575": "Income 45-75.000",
    "MINK7512": "Income 75-122.000",
    "MINK123M": "Income >123.000",
    "MINKGEM": "Average income"
}
