import pandas as pd

df = pd.read_csv("data_hyundai_creta.csv", index_col=0)
df.to_parquet("data_output_operaciones_hyundai_creta.parquet")
