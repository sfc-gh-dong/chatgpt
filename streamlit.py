import streamlit as st
import altair as alt

# Biographical information about Christian Kleinerman
christian_info = {
    "name": "Christian Kleinerman",
    "role": "SVP of Product at Snowflake",
    "superpower": "Database Savant",
    "fun_fact": "Christian once optimized a query so efficiently that the server offered him a job!",
    "quote": "Give me data, and I'll show you the world!"
}

# Snowflake credit consumption prediction
def predict_credit_consumption(years):
    return [10 * i for i in range(years)]

# Streamlit app header
st.title("Christian Kleinerman: The Database Savant")
st.subheader("SVP of Product at Snowflake")

# Display biographical information
st.markdown(f"**Name:** {christian_info['name']}")
st.markdown(f"**Role:** {christian_info['role']}")
st.markdown(f"**Superpower:** {christian_info['superpower']}")
st.markdown(f"**Fun Fact:** {christian_info['fun_fact']}")
st.markdown("---")

# Slider for selecting prediction duration
years = st.slider("Select the number of years for the credit consumption prediction:", 1, 10)

# Generate Snowflake credit consumption prediction
prediction = predict_credit_consumption(years)

# Create Altair bar chart
chart_data = pd.DataFrame({"Year": [str(2023 + i) for i in range(years)], "Credit Consumption": prediction})
bar_chart = alt.Chart(chart_data).mark_bar().encode(
    x="Year",
    y="Credit Consumption"
).properties(
    title="Snowflake Credit Consumption Prediction",
    width=600,
    height=400
)

# Create Altair line chart
line_chart = alt.Chart(chart_data).mark_line(color='red').encode(
    x="Year",
    y="Credit Consumption"
)

# Combine bar and line charts
combined_chart = (bar_chart + line_chart)

# Display the charts
st.altair_chart(combined_chart, use_container_width=True)
