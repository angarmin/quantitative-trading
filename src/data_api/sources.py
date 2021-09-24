import logging as log
import typing
import pandas as pd

from src import utils
from src.data_api.connections import fetch_connections

logger = log.getLogger(__name__)

# Set Connections and get conf
conns = fetch_connections()
conf = utils.get_conf()


def read_data(filename: str, layer: str = 'processed', *args, **kwargs) -> typing.Union[pd.DataFrame, None]:
    """
    Read a file as pandas DataFrame to a specified layer, given a current connection
    @param filename: desired file to read in (in connection)
    @param layer: layer in connection
    @param args: passed to reading method
    @param kwargs:  passed to reading method
    """
    logger.info(f'Reading: {filename} from layer: {layer}')
    return conns[layer].read_file(filename=filename, *args, **kwargs)