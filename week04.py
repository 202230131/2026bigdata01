import pandas as pd

scores = [100,90,80,70]
average = pd.Series(scores).mean()

print(average)