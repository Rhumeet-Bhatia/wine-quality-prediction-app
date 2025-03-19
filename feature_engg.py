from statsmodels.stats.outliers_influence import variance_inflation_factor
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
load_dotenv()
import os

class Feature_engg:
    def __init__(self,df):
        self.df=df
    def corr_matrix(self):
        corr_matrix=self.df.corr()
        print('Below is the correlation matrix: ')
        print(corr_matrix)
        sns.heatmap(corr_matrix,annot=True,cmap="coolwarm",linewidths=0.5)
        plt.title("Heatmap of Correlation Matrix")
        plt.show()
    def feature_selection(self):
        if os.getenv('output_column') in self.df.columns:
            self.X=self.df.drop(os.getenv('output_column'),axis=1)
        else:
            self.X=self.df.copy()
        vif=[variance_inflation_factor(self.X,i) for i in range(len(self.X.columns))]
        vif_df=pd.DataFrame()
        vif_df['Columns']=self.X.columns
        vif_df['VIF']=vif
        con=vif_df['VIF']<125
        features_selected=vif_df['Columns'][con].to_list()
        df=pd.DataFrame()
        df[features_selected]=self.X[features_selected]
        df[os.getenv('output_column')]=self.df[os.getenv('output_column')]
        self.df=df
        print('New dataset after feature selection is:')
        print(self.df)
        return self.df

if __name__=='__main__':
    obj=Feature_engg(pd.read_csv('winequality_red.csv'))
    obj.feature_selection()