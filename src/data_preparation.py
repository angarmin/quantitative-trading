import numpy as np
import pandas as pd

def log_returns(prices: pd.Series, tau: int) -> pd.Series:
    """
    Compute log returns on time series data
    log(p2/p1) = log(p2) - log(p1)
    @param prices: time series data
    @param tau: differencing period
    @return: returns
    """
    return np.log(prices).diff(tau)

#?????????????????

def pl_targets(data: pd.DataFrame,  tau_fwd: int, column:str) -> pd.DataFrame:
    """
    Target computation on close price 
    @param data: input 
    @param tau_fwd: target time horizon (forwad)
    @return: output 
    """
    data=data.set_index(['ticker',"date"])
    shifted=data[[column]].groupby(level="ticker").shift(tau_fwd)
    data=data.join(shifted.rename(columns=lambda x: x+"_"+str(tau_fwd)+"lag"))
    return(data.reset_index())
# si haces wiki_prices["adj_close"].groupby(level="ticker") devuelve uan serie y puedes asignar al DF original directamente
    


def pl_filter(data: pd.DataFrame, start_dt: str, end_dt: str, column: str) -> pd.DataFrame:    
    """ 
    Apply a filter to index level date  
    @param data: input 
    @param start_dt: Filter start 
    @param end_dt: Filter end 
    @return: output 
    """
    return data[(data[column]>=start_dt)&(data[column]<=end_dt)].reset_index()
    
def pl_features(data: pd.DataFrame, target:str, target_lag:str, tau_fwd:int) -> pd.DataFrame:
    """ 
    Compute feautures: x_returns_5d: 5 
    days momentum indicator, log  returns(p[1-5], p[t]) x
    returns_1 d: 1 day momentum indicator, 
    log_returns(p[t-1], p[t]):param data: input :return: output """
    data["returns_"+str(tau_fwd)+"d"] = np.log(data[target]) - np.log(data[target_lag])
    return(data)




