import streamlit as st
from sma import simple_moving_average
from wma import weighted_moving_average  # Placeholder for Weighted MA function
from es import exponential_smoothing  # Placeholder for Exponential Smoothing function

# Streamlit app layout
st.set_page_config(layout="wide")

# Streamlit app title
st.title("Moving Average Viewer")

# Create two columns for layout
col1, col2 = st.columns([1, 3])

# Slider and table in the first column
with col1:
    ma_type = st.selectbox("Select the type of moving average:", ["SMA", "Weighted MA", "Exponential Smoothing"])
    n = st.slider("Select the window size for moving average:", min_value=1, max_value=10, value=1, step=1)

    try:
        if ma_type == "SMA":
            fig, errors = simple_moving_average(n)
        elif ma_type == "Weighted MA":
            fig, errors = weighted_moving_average(n/10)  # Placeholder for Weighted MA function
        elif ma_type == "Exponential Smoothing":
            fig, errors = exponential_smoothing(n,weights)  # Placeholder for Exponential Smoothing function

        # Display errors in a table
        st.subheader("Error Metrics")
        st.table(errors)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Graph in the second column
with col2:
    try:
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"An error occurred: {e}")