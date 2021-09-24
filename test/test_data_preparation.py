import pytest
import numpy as np
import pandas as pd

from src import data_preparation as dataprep

@pytest.fixture
def get_ticker_data():
    index = pd.date_range(start='2021-09-20', end='2021-09-22', freq='B')
    data = [1, 2, 3]
    return pd.Series(index=index, data=data, name='close')


def test_log_returns(get_ticker_data):
    raw_data = get_ticker_data

    res_backwards = dataprep.log_returns(raw_data, tau=1)
    res_forwards = dataprep.log_returns(raw_data, tau=-1)

    exp_backwards = np.array([np.nan, np.log(raw_data[1]/raw_data[0]), np.log(raw_data[2]/raw_data[1])])
    exp_forwards = np.array([np.log(raw_data[0] / raw_data[1]), np.log(raw_data[1] / raw_data[2]), np.nan])

    np.testing.assert_almost_equal(res_backwards.values, exp_backwards)
    np.testing.assert_almost_equal(res_forwards.values, exp_forwards)
