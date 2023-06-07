import polars as pl

pl.Config().set_tbl_cols(-1)

silver_df = pl.read_parquet(source='silver_historical_data_2023-06-05.parquet')

ir = 5.25
expected_price = silver_df.with_columns(
    [
        pl.col('Settle'),
        (pl.col('Settle') * (ir/12)).alias('Cash_Cost'),
        (pl.col('Settle') * (ir/12)).add(pl.col('Settle')).alias('Expected_Price')
    ]
)
print(expected_price)