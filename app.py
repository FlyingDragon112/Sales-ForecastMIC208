import streamlit as st
from sma import simple_moving_average
from wma import weighted_moving_average  # Placeholder for Weighted MA function
from es import simple_exponential_smoothing  # Placeholder for Exponential Smoothing function

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
            # Add weight sliders dynamically based on the value of n
            weights = []
            for i in range(n):
                weight = st.slider(f"Weight {i+1}", min_value=0.0, max_value=1.0, value=1.0/n, step=0.01, key=f"weight_{i}")
                weights.append(weight)

            # Normalize weights to ensure their sum is 1
            total_weight = sum(weights)
            if total_weight != 0:
                weights = [w / total_weight for w in weights]
            else:
                st.error("The sum of weights cannot be zero.")

            fig, errors = weighted_moving_average(n, weights)  # Placeholder for Weighted MA function
        elif ma_type == "Exponential Smoothing":
              # Example weights for Exponential Smoothing
            fig, errors = simple_exponential_smoothing(n/10)  # Placeholder for Exponential Smoothing function

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