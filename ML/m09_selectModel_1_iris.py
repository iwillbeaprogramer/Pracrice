import warnings
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.utils.testing import all_estimators
from sklearn.datasets import load_iris


warnings.filterwarnings('ignore')
datasets = load_iris()
x = datasets.data
y = datasets.target
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=44)
allAlgorithms = all_estimators(type_filter = 'classifier')

best=[]
for (name,algorithm) in allAlgorithms:
    try:
        model = algorithm()
        model.fit(x_train,y_train)
        y_pred = model.predict(x_test)
        print(name, "\'s accuracy : ", accuracy_score(y_test,y_pred))
        best.append(accuracy_score(y_test,y_pred))
    except:
        print(name, '없음')
        continue
print('Best : ',max(best))


'''
Best :  1.0
Tensorflow : 1.0
'''