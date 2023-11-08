import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import KFold

from sklearn.ensemble import RandomForestClassifier

# Parameters
C = 1.0
n_splits = 5
output_file = f'model_C={C}.bin'
max_depth = 2
min_samples_leaf = 1
random_state = 1


# Data preparation
data = "bank-additional-full.csv"

df = pd.read_csv(data, sep=";")
df.columns = df.columns.str.replace('.', '_')
df.y = (df.y == 'yes').astype(int)

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)


# Variable declaration
categorical = list(df.dtypes[df.dtypes == 'object'].index)
numerical = list(df.dtypes[df.dtypes != 'object'].index)

numerical.remove('y') # remove our target variable
numerical.remove('duration')
numerical.remove('pdays')


# Write Train/Predict functions
def train(df_train, y_train, C=1.0):
    dicts = df_train[categorical + numerical].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = RandomForestClassifier(n_estimators=200,
                            max_depth=max_depth,
                            min_samples_leaf=min_samples_leaf,
                            random_state=random_state)
    model.fit(X_train, y_train)
    
    return dv, model

def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred


# validation
print(f"validating model with C={C}")

kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)

scores = []
fold = 0

for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train.y.values
    y_val = df_val.y.values

    dv, model = train(df_train, y_train, C=C)
    y_pred = predict(df_val, dv, model)

    auc = roc_auc_score(y_val, y_pred)
    scores.append(auc)

    print(f"auc on fold {fold} is {auc}")
    fold += 1

print("validation results:")
print('C=%s %.3f +- %.3f' % (C, np.mean(scores), np.std(scores)))


# train final model
print("training final model...")

dv, model = train(df_full_train, df_full_train.y.values, C=C)
y_pred = predict(df_test, dv, model)

y_test = df_test.y.values
auc = roc_auc_score(y_test, y_pred)
print(f"auc={auc}")


# saving model (pickling)
with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f"model is saved to {output_file}")