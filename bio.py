import streamlit as st
import pandas as pd

# Function to load the dataset
@st.cache_data
def load_data():
    # Adjust the path as per your Streamlit app's file structure
    data = pd.read_excel("modified_dataset.xlsx")
    return data

# Initialize or reset the page state
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Navigation function
def navigate_to(page):
    st.session_state['page'] = page

# Inject custom CSS to make all buttons green
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #4CAF50 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Home Page
if st.session_state['page'] == "home":
    # Center the title using columns
    col1, title_col, col3 = st.columns([1,6,1])
    with title_col:
        st.title("Bioinformatics Omics Project")
    
    # Center the "Explore Data" button just below the title
    col1, button_col, col3 = st.columns([1,2,1])
    with button_col:
        if st.button("Explore Data"):
            navigate_to('explore')

    # Center images using columns below the "Explore Data" button
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(["python.png", "h.jpeg"], width=300)  # Adjust paths and width as necessary

# Data Exploration Page
elif st.session_state['page'] == "explore":
    st.sidebar.title("Explore Settings")

    # Sidebar - Introduction/Instructional Text
    st.sidebar.markdown("### Instructions")
    st.sidebar.text("Select a year and explore\nthe omics study papers")

    data = load_data()
    
    # Sidebar - Year selection dropdown
    selected_year = st.sidebar.selectbox("Select Year", sorted(data['Year'].unique()), key='year_selector')
    
    # Add a back to home button
    if st.button("Back to Home"):
        navigate_to('home')
    
    # Main Area
    st.title("Omics Dataset Viewer")
    filtered_data = data[data['Year'] == selected_year]
    
    st.header(f"Data for {selected_year}")
    if not filtered_data.empty:
        for index, row in filtered_data.iterrows():
            st.subheader(row['Title'])
            st.write(f"PubMed ID: {row['PubMed ID']}")
            st.write(f"Accession Number: {row['Accession Number']}")
            st.write(f"Link: [{row['LINK']}]({row['LINK']})")
            st.write(f"Description: {row['Description']}")
            st.write(f"Research Gap: {row['Research gap']}")
            st.markdown("---")
    else:
        st.write("No records found for this year.")
