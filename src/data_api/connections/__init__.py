import os

from src import utils


# Setting local paths
root_path = os.environ.get("LOCAL_PATH")
conf_path = os.path.join(root_path, "conf", "")
data_path = os.path.join(root_path, "data", "")
raw_path = os.path.join(data_path, "raw", "")
interim_path = os.path.join(data_path, "interim", "")
processed_path = os.path.join(data_path, "processed", "")

def get_connection(kind: str, *args, **kwargs):
    """
    Create connection from module specified by 'kind' argument
    :param kind: module to use
    :return: connection
    """

    if kind == 'local':
        from . import local
        return local.Connection(*args, **kwargs)

    if kind == 'blob':
        from . import blob
        return blob.Connection(*args, **kwargs)

    #elif kind == 'mllab':
        # from . import mllab
        #return mllab.Connection(*args, **kwargs)


def fetch_connections(*args, **kwargs):
    """
    Retrieve connections
    :return: connections as tuples
    """

    return {
        'raw': conn_raw,
        'interim': conn_interim,
        'proc': conn_proc
    }

# Connections
# Local
local_meta_raw = {'path': raw_path}
local_meta_interim = {'path': interim_path}
local_meta_proc = {'path': processed_path}
# Blob


# Set conf
conf = utils.get_conf()


# Set Connections
conn_raw = get_connection(**conf['input'],  **local_meta_raw)
conn_interim = get_connection(**conf['input'],  **local_meta_interim)
conn_proc = get_connection(**conf['input'], **local_meta_proc)

