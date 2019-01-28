from sklearn import __version__ as sklearn_version
import numpy as np

### IMPORT IRIS FLOWER DATASET TO TRAIN MODELS ON
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data[:, [2,3]]
y = iris.target

### SPLIT UP OUR DATASET INTO SAMPLES FOR TRAINING AND TESTING
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

### SCALE OUR DATA FOR MOST EFFICIENT TRAINING
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

### IMPORT AND TRAIN PERCEPTRON MODEL
from sklearn.linear_model import Perceptron
ppn = Perceptron(max_iter=40, eta0=0.1, random_state=1)
ppn.fit(X_train_std, y_train)

### MAKE PREDICTIONS USING TEST DATA AND PRINT ACCURACY
y_pred = ppn.predict(X_test_std)
from sklearn.metrics import accuracy_score
print('PPN Accuracy: %.3f' % accuracy_score(y_test, y_pred))

### REPEAT THE ABOVE FOR LOGISTIC REGRESSION
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=100.0, random_state=1)
lr.fit(X_train_std, y_train)
y_pred = lr.predict(X_test_std)
print(lr.predict_proba(X_test_std[:3, :]))
print('LR Accuracy: %.3f' % accuracy_score(y_test, y_pred))