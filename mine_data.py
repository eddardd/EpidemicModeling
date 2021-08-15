import numpy as np
import pandas as pd


# Load complete data
df = pd.read_csv('./data/Bing-COVID19-Data.csv')

# Brazil indices
# Warning: this constains aggregated data (all of brazil), as well as the states
ind1 = np.where(df['Country_Region'].values.astype(str) == 'Brazil')[0]
# Gets aggregated data only
ind2 = np.where(pd.isnull(df['AdminRegion1']))[0]
# Gets data from CE only
ind3 = np.where(df['AdminRegion1'] == 'Ceará')[0]

# Get data from BR (aggregated)
df_br = df.iloc[np.intersect1d(ind1, ind2), :]

# Get data from BR (aggregated)
df_ce = df.iloc[np.intersect1d(ind1, ind3), :]

# Saves dataframes
df_br.to_csv('./data/DadosBR.csv')
df_ce.to_csv('./data/DadosCE.csv')