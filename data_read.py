import pandas as pd

class Read_data:
    def __init__(self,path):
        self.df=pd.read_csv(path)
    def get_df(self):
        return self.df
    

if __name__=="__main__":
    obj=Read_data('winequality_red.csv')
    df1=obj.get_df()
    print(df1.head())