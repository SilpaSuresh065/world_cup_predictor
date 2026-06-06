import pandas as pd

# Load dataset
df = pd.read_csv("data/results.csv")

# Display first 5 rows
print(df.head())

# Create result column
def result(row):
    if row["home_score"] > row["away_score"]:
        return "Win"
    elif row["home_score"] < row["away_score"]:
        return "Loss"
    else:
        return "Draw"

df["result"] = df.apply(result, axis=1)

# Display the new column
print(df[["home_team", "away_team", "home_score", "away_score", "result"]].head())

X = df[["home_team", "away_team", "tournament"]]
y = df["result"]

print(X.head())
print(y.head())

# Encoding
from sklearn.preprocessing import LabelEncoder

home_encoder = LabelEncoder()
away_encoder = LabelEncoder()
tour_encoder = LabelEncoder()

X["home_team"] = home_encoder.fit_transform(X["home_team"])
X["away_team"] = away_encoder.fit_transform(X["away_team"])
X["tournament"] = tour_encoder.fit_transform(X["tournament"])

print(X.head())


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestClassifier(
    n_estimators=5,
    random_state=42
)
# Train model
model.fit(X_train, y_train)

print("Model trained successfully!")

from sklearn.metrics import accuracy_score

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)


import joblib

joblib.dump(model, "model/model.pkl")

joblib.dump(home_encoder, "model/home_encoder.pkl")
joblib.dump(away_encoder, "model/away_encoder.pkl")
joblib.dump(tour_encoder, "model/tour_encoder.pkl")

print("Model saved successfully!")