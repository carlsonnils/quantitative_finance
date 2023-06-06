import os
import requests
import polars as pl
import json

key = os.environ['NASDAQ_API_KEY']
base_url = os.environ['NASDAQ_BASE_URL']
cme_hg1_futures_code = os.environ['NASDAQ_SILVER']

copper_response = requests.request(method='get', url=base_url+'/'+cme_hg1_futures_code)

copper_data = copper_response.json()['dataset']['data']
copper_column_names = copper_response.json()['dataset']['column_names']
copper_df = pl.DataFrame(data=copper_data, schema=copper_column_names)
copper_df.write_parquet('silver_historical_data_2023-06-05.parquet', use_pyarrow=True)
print(copper_df)