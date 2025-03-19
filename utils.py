from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error,root_mean_squared_error

class Performance:
    def __init__(self,LR_model,y_test,y_pred):
        self.LR_model=LR_model
        self.y_test=y_test
        self.y_pred=y_pred
    def evaluate(self):
        MAE=mean_absolute_error(self.y_test,self.y_pred)
        MSE=mean_squared_error(self.y_test,self.y_pred)
        RMSE=root_mean_squared_error(self.y_test,self.y_pred)
        R2_sq=r2_score(self.y_test,self.y_pred)
        return MAE,MSE,RMSE,R2_sq