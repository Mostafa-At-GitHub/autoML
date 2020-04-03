import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'], random_state=None)

# Average CV score on the training set was: 0.45371980676328505
exported_pipeline = XGBClassifier(colsample_bylevel=0.7000000000000001, colsample_bytree=0.8, gamma=0.5, learning_rate=0.06780000000000001, max_depth=58, min_child_weight=98, n_estimators=144, nthread=6, reg_alpha=63, reg_lambda=131.1, subsample=0.4)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
