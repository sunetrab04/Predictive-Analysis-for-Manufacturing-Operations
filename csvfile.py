import pandas as pd
import numpy as np

np.random.seed(42)
data = pd.DataFrame({
    "Machine_ID": np.arange(1, 101),
    "Temperature": np.random.randint(50, 120, 100),
    "Run_Time": np.random.randint(100, 500, 100),
    "Downtime_Flag": np.random.choice([0, 1], 100, p=[0.7, 0.3])
})
data.to_csv("manufacturing_data.csv", index=False)
