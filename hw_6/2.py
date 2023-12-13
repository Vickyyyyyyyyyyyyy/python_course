import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

class MyNeuralNetwork:
    def __init__(self, input_dim, hidden1_units, hidden2_units):
        self.input_dim = input_dim
        self.hidden1_units = hidden1_units
        self.hidden2_units = hidden2_units
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Dense(self.hidden1_units, input_dim=self.input_dim, activation='relu'))
        model.add(Dense(self.hidden2_units, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def prepare_data(self, X, y, test_size=0.2, random_state=42):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        return X_train, X_test, y_train, y_test

    def train(self, X_train, y_train, epochs=15, batch_size=10, verbose=2):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=verbose)

    def inference(self, X):
        return self.model.predict(X)

# Example usage:
# Assuming X_train, y_train are your training data
# and X_test, y_test are your testing data
# You need to replace this with your actual data
X_train, X_test, y_train, y_test = np.random.rand(100, 8), np.random.rand(25, 8), np.random.randint(2, size=100), np.random.randint(2, size=25)

# Create an instance of MyNeuralNetwork
nn = MyNeuralNetwork(input_dim=X_train.shape[1], hidden1_units=12, hidden2_units=8)

# Prepare data
X_train, X_test, y_train, y_test = nn.prepare_data(X_train, y_train)

# Train the model
nn.train(X_train, y_train)

# Make predictions
predictions = nn.inference(X_test)
print(predictions)
