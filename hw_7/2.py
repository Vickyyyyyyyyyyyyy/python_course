import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


titanic_data = pd.read_csv("titanic.csv")


features = ["PClass", "Age", "SexCode"]
X = titanic_data[features]
y = titanic_data["Survived"]


numeric_features = ["Age"]
numeric_transformer = SimpleImputer(strategy="mean")

categorical_features = ["PClass", "SexCode"]
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(drop="first"))
])


preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression())
])


model.fit(X_train, y_train)


predictions = model.predict(X_test)


accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")


sample_passengers = X_test.head(10)
sample_predictions = model.predict(sample_passengers)
print("\nPredictions for 10 passengers:")
for i, prediction in enumerate(sample_predictions):
    print(f"Passenger {i+1}: {'Survived' if prediction == 1 else 'Not Survived'}")
