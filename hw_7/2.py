import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the dataset
titanic_data = pd.read_csv("titanic.csv")

# Select relevant features
features = ["PClass", "Age", "SexCode"]
X = titanic_data[features]
y = titanic_data["Survived"]

# Define transformers for numerical and categorical columns
numeric_features = ["Age"]
numeric_transformer = SimpleImputer(strategy="mean")

categorical_features = ["PClass", "SexCode"]
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(drop="first"))
])

# Combine transformers using ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with the preprocessor and logistic regression model
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression())
])

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Make predictions on 10 passengers
sample_passengers = X_test.head(10)
sample_predictions = model.predict(sample_passengers)
print("\nPredictions for 10 passengers:")
for i, prediction in enumerate(sample_predictions):
    print(f"Passenger {i+1}: {'Survived' if prediction == 1 else 'Not Survived'}")
