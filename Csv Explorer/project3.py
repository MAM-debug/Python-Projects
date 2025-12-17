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
        st.metric("Number of Rows",df.shape[0])
    with col2:
        st.metric("Number of Columns",df.shape[1])
    st.divider()

    st.dataframe(df)


else:
    st.info("File is not uploaded yet.")
