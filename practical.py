import streamlit as st

# Set page configuration
st.set_page_config(page_title="Worldwide Analysis of Quality of Life and Economic Factors", 
                   layout="wide")

# Header and subtitle
st.title("Worldwide Analysis of Quality of Life and Economic Factors")
st.subheader("This app enables you to explore the relationships between poverty, \n            life expectancy, and GDP across various countries and years. \n            Use the panels to select options and interact with the data.")

# Create tabs
tabs = st.tabs(["Global Overview", "Country Deep Dive", "Data Explorer"])

with tabs[0]:
    st.write("### Global Overview")
    st.write("Explore global trends in GDP, life expectancy, and poverty levels.")
    
with tabs[1]:
    st.write("### Country Deep Dive")
    st.write("Analyze a specific country’s economic and quality of life factors.")
    
with tabs[2]:
    st.write("### Data Explorer")
    st.write("Interact with raw data and customize visualizations.")
