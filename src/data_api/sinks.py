import logging as log
import pandas as pd

from src import utils
from src.data_api.connections import fetch_connections

logger = log.getLogger(__name__)

# Set Connections and get conf
conns = fetch_connections()
conf = utils.get_conf()


def write_data(df: pd.DataFrame, table_name: str, layer: str = 'processed', *args, **kwargs):
    """
    Write a pandas DataFrame to a specified layer, given a current connection
    @param df: pandas DataFrame
    @param table_name: desired table name (in connection)
    @param layer: layer in connection
    @param args: passed to writing method
    @param kwargs:  passed to writing method
    """
    logger.info(f'Writing: {table_name} in layer: {layer}')
    filename = table_name + '.csv'
    conns[layer].write_file(data=df, filename=filename, *args, **kwargs)