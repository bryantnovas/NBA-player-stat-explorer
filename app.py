import base64
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

# CODE TO BE EXECUTED WHEN RAN AS SCRIPT

st.title('NBA Player Stats Explorer')

st.markdown("""
![logo](https://media.tenor.com/images/426aa93de195958c7bb2407c29af2209/tenor.gif) 

This app performs simple webscraping of NBA player stats data!
* **Python libraries:** base64, pandas, streamlit, flask, sqlalchemy
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2021))))



# Fetch data from database
@st.cache
def load_data(year):
    df = pd.read_json(f'https://nba-stat-api.herokuapp.com/api?year={year}&limit=100000')
    df = df.drop('id', axis=1)
    return df

playerstats = load_data(selected_year)
st.set_option('deprecation.showPyplotGlobalUse', False)

# Sidebar - Team selection
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Sidebar - Position selection
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering data
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Display Player Stats of Selected Team(s)')
st.write(f'Data Dimension: {df_selected_team.shape[0]} rows and {df_selected_team.shape[1]} columns.')
st.dataframe(df_selected_team)

# Sidebar - Chart selection
chart = ['Heatmap', 'Linear', 'Histogram']
selected_chart =  st.sidebar.selectbox('Chart', chart)

# Download NBA player stats data
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# Heatmap
if selected_chart == 'Heatmap':
    st.header('Intercorrelation Matrix Heatmap')
    df_selected_team.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')
    df = df.drop('Year', axis=1)

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot()

# Linear Regression
elif selected_chart == 'Linear':
    st.header('Predict PTS with FGA')
    df = pd.read_csv('output.csv')
    df = df.drop('Year', axis=1)
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        sns.regplot(x="FGA", y="PTS", data=df, color='r', scatter_kws={'color': 'b'})
    st.pyplot()

# Histogram
elif selected_chart == 'Histogram':
    df = pd.read_csv('output.csv')
    plt.hist(df['Age'])
    plt.title('Players Age Histogram')
    plt.xlabel('Player Ages')
st.pyplot()