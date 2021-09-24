import logging as log
import pandas as pd


logger = log.getLogger(__name__)


class Connection:
    def __init__(self, path: str, *args, **kwargs):
        logger.info(f'Creating local FilesConnection for path {path}')

        # Save path
        self.path = path

        logger.info('Finished creation of local FilesConnection')

    def read_file(self, filename: str, *args, **kwargs) -> pd.DataFrame:
        """
        Read input file as local .csv
        :param filename: actual filename with extension
        :param args, kwargs passed to pandas.read_csv
        :return: pandas DataFrame
        """
        logger.info(f'Reading file {self.path}{filename}')
        # Read local DataFrame from a given file type
        df = pd.read_csv(self.path + filename, *args, **kwargs)

        return df

    def read_params(self, filename: str, *args, **kwargs) -> pd.DataFrame:
        """
         Read input params file as local .csv
         :param filename: actual filename with extension
         :param args, kwargs passed to pandas.read_csv
         :return: pandas DataFrame
         """
        logger.info(f'Reading param {self.path}{filename}')

        # Read local DataFrame from .csv file
        df = pd.read_csv(self.path + filename, *args, **kwargs)

        return df

    def write_file(self, data: pd.DataFrame, filename: str, *args, **kwargs):
        """
        Write a pandas DataFrame as local .csv
        @param data: pandas DataFrame
        @param filename: local filename
        @param args: passed to writing method
        @param kwargs: passed to writing method
        """
        logger.info(f'Writing DataFrame {data} to {self.path}{filename}')

        data.to_csv(self.path + filename, *args, **kwargs)
