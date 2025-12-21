import streamlit as st
import pandas as pd
st.title("📊 CSV Explorer")
st.write("Upload a CSV file to explore its contents.")
uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write("File name:",uploaded_file.name)
    df=pd.read_csv(uploaded_file)
    st.subheader("Data Preview:")
    st.divider()
    st.write("Showing length of data:",len(df))
    col1,col2=st.columns(2)
    with col1:
        st.metric("Number of Rowss",df.shape[0])
    with col2:
        st.metric("Number of Columns",df.shape[1])
    st.divider()

    st.dataframe(df)

    st.divider()
    st.subheader("Column Statistics:")

    column_names=df.columns.tolist()
    colum_types=df.dtypes

    column_info=pd.DataFrame({
        "Column Name":column_names,
        "Data Type":colum_types
    })

    st.dataframe(column_info)

    st.divider()
    st.subheader("Summary Statistics:")
    stats=df.describe()
    st.dataframe(stats)
    st.divider()
    st.subheader("Missing Values Analysis:")
    missing_values=df.isnull().sum()
    missing_percentage=missing_values/len(df)*100
    missing_data=pd.DataFrame({
        "Missing Values":missing_values,
        "Percentage (%)":missing_percentage.round(2) 
    })
    missing_data=missing_data[missing_data["Missing Values"]>0]
    if not missing_data.empty:
        st.dataframe(missing_data)
        st.warning(f"⚠️ Found missing values in {len(missing_data)} column(s)")
    else:
        st.success("No missing values found in the dataset.")
else:
    st.info("File is not uploaded yet.")
