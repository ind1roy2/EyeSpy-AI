import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

import os

# Get the absolute path of the 'Eye new.xlsx' file in the same directory as your script
file_name = 'Eye new.xlsx'
absolute_path = os.path.abspath(file_name)

print("Absolute path of 'Eye new.xlsx':", absolute_path)

st.markdown('<style>body{background-color: black;}</style>', unsafe_allow_html=True)

st.title(":blue[Our Methodology]")

st.markdown('[Click here to visit Google form questionnaire ](https://forms.gle/2sGwugj3DXnmmUJD9)', unsafe_allow_html=True)
st.write("->The above questionnaire was circulated in various educational institutes and we were able to collect the data of 300 students.")
st.write("->To have a look at what we found, you can check column wise graphical analysis below")
#df = pd.read_excel("E:\Project_college\Eye_college\Eye new.xlsx")
df = pd.read_excel(absolute_path)

st.subheader(":orange[Select the feature to be plotted]")
columns = ['Age group','Level of dryness','Gender','Screen time','Family History of myopia']

selected_feature = st.selectbox('Select feature', columns)

if selected_feature != 'Family History of myopia':
    fig = px.bar(df, x=selected_feature, color = 'Spectacles', orientation='v')
    st.plotly_chart(fig)
else:
    fig = px.bar(df, x='Parents', color = 'Spectacles', orientation='v')
    st.plotly_chart(fig)

st.subheader(":orange[Algorithms Vs Accuracy Obtained]")
dict = {'Algorithm':['Logistic Regression','SVM','Decision Tree','Random Forest','KNN','XGBoost'],
        'Accuracy in %':[88.1,88.1,84.7,86.4,86.4,83.0]}

results_df = pd.DataFrame(dict)
st.table(results_df)

st.write("-> Algorithm used for prediction - Logistic Regression")

