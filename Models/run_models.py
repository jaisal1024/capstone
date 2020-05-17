import pandas as pd
import numpy as np


def run_H20_DRF(test, train):
    import h2o
    from h2o.estimators import H2ORandomForestEstimator

    h2o.init()

    cols_cat = list(x.select_dtypes(exclude="number").columns)
    for col in cols_cat:
        train[col] = train[col].asfactor()

        # Build and train the model:
    drf = H2ORandomForestEstimator(ntrees=50, max_depth=16)
    drf.train(y="sale_price", training_frame=train)


def run_lr(test, train):
    from sklearn.linear_model import LinearRegression

    y_test = test.sale_price
    y_train = train.sale_price
    x_test = test.drop(column="sale_price", inplace=True)
    x_train = train.drop(column="sale_price", inplace=True)

    lr = LinearRegression(normalize=True, n_jobs=-1)
    lr.fit(x_train)
