import streamlit as st
import pandas as pd
import seaborn as sns

# Displaying the title
st.title('Data Analysis')
st.subheader('Data analysis using python and Streamlit')

# Uploading a dataset
upload = st.file_uploader('Upload your Dataset (In CSV Format)')
if upload is not None:
    data = pd.read_csv(upload)

# show dataset
if upload is not None:
    if st.checkbox('Preview Dataset'):
        if st.button('Head'):
            st.write(data.head(5))
        if st.button('Tail'):
            st.write(data.tail(5))

# check Datatype of each column
if upload is not None:
    if st.checkbox('Datatype of each column'):
        st.text('DataTypes')
        st.write(data.dtypes.astype(str))

# check shape of the dataset
if upload is not None:
    data_shape = st.radio('What dimensions do yo want to check?',('Rows','Columns'))
    
    if data_shape=='Rows':
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.write(data.shape[1])