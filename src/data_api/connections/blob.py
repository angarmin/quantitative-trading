import io
import logging as log
import pandas as pd
import os
import azure.storage.blob as azblob

logger = log.getLogger(__name__)


class Connection:
    """
    v12: https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python
    https://docs.microsoft.com/es-es/python/api/azure-storage-blob/azure.storage.blob.blobserviceclient?view=azure-python
    """
    def __init__(
        self, account_name: str, store_name: str, container_name: str, blob_str_conn: str,
        *args, **kwargs,
    ):

        logger.info('Creating Azure Blob Storage Gen1 FilesConnection')

        # Save parameters
        self.account_name = account_name
        self.store_name = store_name
        self.container_name = container_name
        self.blob_str_conn = blob_str_conn

        # Initialize BlockBlobService, which allows reading bytes
        if azblob.__version__ == '2.1.0':
            self.block_blob_serv = azblob.BlockBlobService(
                account_name=account_name,
                account_key=store_name,
            )
        else:
            self.blob_serv_client = azblob.BlobServiceClient.from_connection_string(self.blob_str_conn)
            self.container_client = self.blob_serv_client.get_container_client(self.container_name)


    def read_file(self, filename: str, *args, **kwargs) -> pd.DataFrame:
        logger.info(f'Reading file {filename} from container {self.container_name}')

        # Read blob
        blob_data = self.container_client.download_blob(filename)
        # Create IO stream from bytes (it can be read as a file)
        io_stream = io.BytesIO(blob_data.content_as_bytes())
        # read as pandas DF
        df = pd.read_csv(io_stream, *args, **kwargs)

        return df

    def write_file(self, data: pd.DataFrame, filename: str, *args, **kwargs):
        logger.info(f'Writing DataFrame {data} to container {self.container_name}')

        # Read blob
        blob_client = self.container_client.get_blob_client(filename)
        # TODO: Add direct upload of string stream
        data.to_csv(filename, *args, **kwargs)

        with open(filename, "rb") as data:
            blob_client.upload_blob(data, blob_type="BlockBlob", overwrite=True)

        os.remove(filename)


