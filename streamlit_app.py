
## 00 Import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


##01 Introduction
st.title("Real Estate Agency - California 🏡")


st.image("house2.png",width=400)


## 02 Setup 

page = st.sidebar.selectbox("Select Page",["Introduction📚","Visualization📊"])






df=pd.read_csv("housing.csv")
## dynamic logic within streamlit 


if page == "Introduction📚":
    ## 03 Loading the dataset 
    st.subheader("01 Data Exploration")


    ### display of the dataset
    rows = st.slider("Select the number of rows to display",5,20,5)
    st.dataframe(df.head(rows))

    ### statistical description of the dataset
    st.markdown("#### Statistical description of the dataset")
    st.dataframe(df.describe())
                 

    ### create a logic to display missing values in data and tell the user about it
    st.markdown("#### Missing Values")
    missing = df.isnull().sum()
    st.write(missing)

    if missing.sum() == 0:
        st.success("✅ No missing values found")
    else:
        st.warning("⚠️ You have missing values ")


if page == "Visualization📊":
    st.subheader("02 Data Visualization")
    ## 04 Data Visualizarion part


    col_x = st.selectbox("Select X-axis variable",df.columns,index=0)
    col_y = st.selectbox("Select Y-axis variable",df.columns,index=1)

    tab1, tab2, tab3 = st.tabs(["Bar Chart 📊","Line Chart 📈","Correrlation heatmap🔥"])


    with tab1: 
        ## streamlit bar plot 
        st.subheader("Bar Chart")
        st.bar_chart(df[[col_x,col_y]].sort_values(by=col_x),use_container_width=True)
    with tab2: 
        st.subheader("Line Chart")
        st.line_chart(df[[col_x,col_y]].sort_values(by=col_x),use_container_width=True)

    ## Correlation matrix 
    with tab3:
        st.subheader("Correlation matrix")
        df_numeric = df.drop(["ocean_proximity"],axis=1)

        ## start by creating an empty frame 
        fig_corr, ax_corr = plt.subplots(figsize=(20,14))
        ## create the plot in seaborn 
        sns.heatmap(df_numeric.corr(),annot=True)
        ## render the plot in streamlit 
        st.pyplot(fig_corr)