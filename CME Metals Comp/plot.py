import polars as pl
import plotly.graph_objects as go
from plotly.subplots import make_subplots

silver_df = pl.read_parquet(source='silver_historical_data_2023-06-05.parquet')
recent_silver_df = silver_df.filter(pl.col("Date") >= pl.datetime(2020,7,1))

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=recent_silver_df['Date'], y=recent_silver_df['Change'], name="Change", line=dict(color='lightgrey')),
    secondary_y=True
)
fig.add_trace(
    go.Scatter(x=recent_silver_df['Date'], y=recent_silver_df['Settle'], name="Settle"),
    secondary_y=False,
)

# Add figure title
fig.update_layout(
    title_text="Silver Settle Price"
)

# Set x-axis title
fig.update_xaxes(title_text="Date")

# Set y-axes titles
fig.update_yaxes(title_text="Change", secondary_y=True)
fig.update_yaxes(title_text="Settle", secondary_y=False)

fig.show()