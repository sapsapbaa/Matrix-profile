import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Step 2: Get data
x, y = load_digits(return_X_y=True) #random x,y tuple
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Step 3: Create a model and train it
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)  
model = LogisticRegression(solver='liblinear', C=0.05, multi_class='ovr',
                           random_state=0) #set model parameter here
model.fit(x_train, y_train)  

# Step 4: Evaluate the model
x_test = scaler.transform(x_test)
y_pred = model.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
print(cm)
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(cm)
ax.grid(False)
ax.set_xlabel('Predicted outputs', fontsize=16, color='black')
ax.set_ylabel('Actual outputs', fontsize=16, color='black')
ax.xaxis.set(ticks=range(10))
ax.yaxis.set(ticks=range(10))
ax.set_ylim(9.5, -0.5)
for i in range(10):
    for j in range(10):
        ax.text(j, i, cm[i, j], ha='center', va='center', color='white')
plt.show()
