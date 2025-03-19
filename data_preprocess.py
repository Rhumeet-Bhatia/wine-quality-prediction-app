from sklearn.preprocessing import StandardScaler,OneHotEncoder
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()
import pickle
class Process_data:
    def __init__(self,df):
        self.df=df
    def null_values(self):
        if self.df.isna().sum().sum() == 0:
            print('No Null values present in dataset')
        else:
            self.df.fillna(self.df.median(),inplace=True)
            print('Null values updated with its median value')
        return self.df
    def remove_duplicates(self):
        self.df.drop_duplicates(inplace=True)
        return self.df
    def encode_categorical(self):
        categorical_cols = self.df.select_dtypes(include=["object"]).columns
        if len(categorical_cols)>0:
            print(f"Encoding required for: {categorical_cols.tolist()}")
            encoder = OneHotEncoder(sparse_output=False,drop='first') 
            encoded_array = encoder.fit_transform(self.df[categorical_cols])
            encoded_df = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out(categorical_cols))
            encoded_df = encoded_df.reset_index(drop=True)
            self.df = self.df.drop(columns=categorical_cols).join(encoded_df)
        else:
            print("No encoding required.")
        return self.df
    def feature_scaling(self,df):
        self.df=df
        ss=StandardScaler()
        self.X=self.df.drop(os.getenv('output_column'),axis=1)
        input_features=self.X.columns
        self.X=ss.fit_transform(self.X)
        self.df[input_features]=self.X
        pickle.dump(ss,open('scaler.pkl','wb'))
        print('Features are successfully scaled and scaler also saved')
        return self.df
    
if __name__=='__main__':
    obj=Process_data(pd.read_csv('winequality_red.csv'))
    print(obj.encode_categorical())