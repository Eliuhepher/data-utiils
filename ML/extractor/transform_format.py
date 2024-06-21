from pathlib import Path
import pandas as pd

data_path_read = Path.cwd().parent / "notebooks/data/data_kmeans.csv"
data_path_write = Path.cwd().parent / "notebooks/data/data_kmeans.parquet"
df = pd.read_csv(data_path_read, index_col=0)
df.to_parquet(data_path_write)
