from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os
from dotenv import load_dotenv
import pandas as pd
import pickle
load_dotenv()

class Model_train_test_save:
    def __init__(self,df):
        self.df=df
    def data_split(self,df):
        print(self.df)
        print('Data splitted successfully')
        return train_test_split(self.df.drop(os.getenv('output_column'),axis=1),self.df[os.getenv('output_column')],test_size=0.2,random_state=1234)
    def model_train(self,X_train,y_train):
        model=LinearRegression()
        model.fit(X_train,y_train)
        print('Model trained successfully')
        return model
    def model_test(self,LR_model,X_test,y_test):
        y_pred=LR_model.predict(X_test)
        model_df=X_test.copy()
        model_df['y_actual']=y_test
        model_df['y_pred']=y_pred
        model_df['Residual']=model_df['y_actual']-model_df['y_pred']
        model_df['Squared Residual']=model_df['Residual']**2
        print('Model tested successfully')
        return model_df,y_pred
    def model_save(self,LR_model):
        pickle.dump(LR_model,open('WineQualityRed_model.pkl','wb'))
        print('Model saved successfully')