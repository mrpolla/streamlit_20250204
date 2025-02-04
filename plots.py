'''
import plotly.graph_objects as go

def scatterplot(df):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["GDP per capita"],
        y=df["Life Expectancy (IHME)"],
        mode="markers",
        marker=dict(
            size=df["Population"] / df["Population"].max() * 50,  # Normalize population size
            color=df["headcount_ratio_upper_mid_income_povline"],  # Color by poverty rate
            colorscale="Viridis",  # Choose a color scale
            showscale=True
        ),
        text=df["country"],  # Hover text
        hovertemplate="<b>%{text}</b><br>GDP per Capita: %{x}<br>Life Expectancy: %{y}<br><extra></extra>",
    ))

    fig.update_layout(
        title="GDP per Capita vs. Life Expectancy",
        xaxis=dict(title="GDP per Capita (USD)", type="log"),  # Log scale for better distribution
        yaxis=dict(title="Life Expectancy (Years)"),
        template="plotly_white"
    )

    return fig

'''
import plotly.express as px

def scatterplot(df):
    fig = px.scatter(
        df,
        x="GDP per capita",
        y="Life Expectancy (IHME)",
        color="country",  # Change color to 'country' instead of poverty rate
        size="Population",  
        hover_name="country",  # Shows country names on hover
        log_x=True,  
        title="GDP per Capita vs. Life Expectancy",
        labels={
            "GDP per capita": "GDP per Capita (USD)",
            "Life Expectancy (IHME)": "Life Expectancy (Years)",
            "country": "Country",
        }
    )
    return fig
