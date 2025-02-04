import streamlit as st
import pandas as pd
import plotly as plt
from plots import scatterplot

# Set page configuration
st.set_page_config(page_title="Worldwide Analysis of Quality of Life and Economic Factors", 
                   layout="wide")

# Header and subtitle
st.title(":earth_africa: Worldwide Analysis of Quality of Life and Economic Factors")
st.subheader("This app enables you to explore the relationships between poverty, \n            life expectancy, and GDP across various countries and years. \n            Use the panels to select options and interact with the data.")

# Read data set
@st.cache_data 
def load_data():
    return pd.read_csv("./global_development_data.csv")

df = load_data()

# Create tabs
tabs = st.tabs(["Global Overview", "Country Deep Dive", "Data Explorer"])

with tabs[0]:
    st.write("### :earth_americas: Global Overview")
    st.write("Explore global trends in GDP, life expectancy, and poverty levels.")

    # Year selection slider
    year_selected = st.slider("Select a year:", int(df['survey_year'].min()), int(df['survey_year'].max()), int(df['survey_year'].max()))
        
    # Filter data for selected year
    year_df = df[df['survey_year'] == year_selected]
        
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Mean Life Expectancy", value=round(year_df["Life Expectancy (IHME)"].mean(), 2))
    with col2:
        st.metric(label="Median GDP per Capita", value=round(year_df["GDP per capita"].median(), 2))
    with col3:
        st.metric(label="Mean Poverty Rate (Upper Middle Income)", value=round(year_df["headcount_ratio_upper_mid_income_povline"].mean(), 2))
    with col4:
        st.metric(label="Number of Countries", value=year_df["country"].nunique())
     # Scatterplot
    st.write("### GDP vs Life Expectancy")
    fig = scatterplot(year_df)
    st.plotly_chart(fig, use_container_width=True)

with tabs[1]:
    st.write("### :bar_chart: Country Deep Dive")
    st.write("Analyze a specific country’s economic and quality of life factors.")
    

with tabs[2]:
    st.write("### :open_file_folder: Data Explorer")
    st.write("Interact with raw data and customize visualizations.")
    # Country selection
    countries = df['country'].unique()
    selected_countries = st.multiselect("Select countries:", countries, default=countries[:5])
    # Year selection
    year_min, year_max = int(df['survey_year'].min()), int(df['survey_year'].max())
    selected_year_range = st.slider("Select year range:", year_min, year_max, (year_min, year_max))
    
    # Filter Dataset
    filtered_df = df[(df['country'].isin(selected_countries)) & (df['survey_year'].between(*selected_year_range))]
    st.dataframe(filtered_df)

    # Download filtered data
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "filtered_data.csv", "text/csv")

