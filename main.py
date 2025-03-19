import os
from dotenv import load_dotenv
load_dotenv()
from data_read import Read_data
from data_preprocess import Process_data
from feature_engg import Feature_engg
from model import Model_train_test_save
from utils import Performance

obj=Read_data(os.getenv('file_path'))
df=obj.get_df()
obj1=Process_data(df)
df=obj1.null_values()
df=obj1.remove_duplicates()
df=obj1.encode_categorical()
obj2=Feature_engg(df)
obj2.corr_matrix()
df=obj2.feature_selection()
df=obj1.feature_scaling(df)
obj3=Model_train_test_save(df)
X_train,X_test,y_train,y_test=obj3.data_split(df)
LR_model=obj3.model_train(X_train,y_train)
model_test_df,y_pred=obj3.model_test(LR_model,X_test,y_test)
print('Below is the analysis for model tested:')
print(model_test_df)
obj4=Performance(LR_model,y_test,y_pred)
MAE,MSE,RMSE,R2_sq=obj4.evaluate()
print('Below are some of the metrics calculated: ')
print('Mean Absolute Error:',MAE)
print('Mean Squared Error:',MSE)
print('Root Mean Squared Error:',RMSE)
print('R2 squared value:',R2_sq)
obj3.model_save(LR_model)
