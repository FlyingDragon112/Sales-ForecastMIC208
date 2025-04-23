import pandas as pd
import plotly.graph_objects as go

def simple_exponential_smoothing(alpha):
    # Read the CSV file
    data = pd.read_csv('sales_data.csv')
    data['SES'] = data['Value'].ewm(alpha=alpha, adjust=False).mean()

    # Create the plotly graph
    fig = go.Figure()

    # Add actual values to the plot
    fig.add_trace(go.Scatter(x=data.index, y=data['Value'], mode='lines', name='Actual Values'))

    # Add predicted SES values to the plot
    fig.add_trace(go.Scatter(x=data.index, y=data['SES'], mode='lines', name=f'SES (α={alpha})'))

    # Update layout for better visualization
    fig.update_layout(
        title=f'Simple Exponential Smoothing (α={alpha}) - Monthly Data',
        xaxis_title='Month',
        yaxis_title='Values',
        legend_title='Legend'
    )

    # Calculate errors
    data['Error'] = data['Value'] - data['SES']
    rmse = (data['Error'] ** 2).mean() ** 0.5
    mae = data['Error'].abs().mean()
    mpe = (data['Error'] / data['Value']).mean() * 100

    # Return the figure and errors
    return fig, {'RMSE': rmse, 'MAE': mae, 'MPE': mpe}