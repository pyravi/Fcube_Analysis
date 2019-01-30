import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {
        "colour": ["red", "blue", "green", "red", "red", "yellow", "blue"],
        "direction": ["up", "up", "down", "left", "right", "down", "down"],
    }
)

categorical_features = ["colour", "direction"]
fig, ax = plt.subplots(1, len(categorical_features))
for i, categorical_feature in enumerate(df[categorical_features]):
    df[categorical_feature].value_counts().plot("bar", ax=ax[i]).set_title(categorical_feature)
plt.show()
