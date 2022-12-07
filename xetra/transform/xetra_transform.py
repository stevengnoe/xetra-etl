from typing import NamedTuple

from xetra.common.s3 import S3BucketConnector


class XetraSourceConfig(NamedTuple):
    """
    Class for source configuration data

    src_first_extract_date: the begin date for extracting from source
    src_columns: source column names
    src_col_date: column name for the date in source
    src_col_isin: column name for the ISIN in source
    src_col_time: column name for the time in source
    src_col_start_price: column name for the starting price in source
    src_col_min_price: column name for the minimum price in source
    src_col_max_proce: column name for the maximum price in source
    src_col_traded_vol: column name for the traded volume in source
    """

    src_first_extract_date: str
    src_columns: list
    src_col_date: str
    src_col_isin: str
    src_col_time: str
    src_col_start_price: str
    src_col_min_price: str
    src_col_max_proce: str
    src_col_traded_vol: str


class XetraTargetConfig(NamedTuple):
    """
    Class for Target configuration data

    tgt_col_date: column name for date in target
    tgt_col_isin: column name for ISIN in target
    tgt_col_open_price: column name for opening price in target
    tgt_col_close_price: column name for closing price in target
    tgt_col_min_price: column name for minimum price in target
    tgt_col_max_proce: column name for maximum price in target
    tgt_col_daily_traded_vol: column name for daily traded volume in target
    tgt_key: the file name of the target file
    tgt_key_date_format: date format for the target file
    tgt_format: file format of the target file
    """

    tgt_col_date: str
    tgt_col_isin: str
    tgt_col_open_price: str
    tgt_col_close_price: str
    tgt_col_min_price: str
    tgt_col_max_proce: str
    tgt_col_daily_traded_vol: str
    tgt_key: str
    tgt_key_date_format: str
    tgt_format: str

class XetraETL():
    """
    Extracts the Xetra data files, transforms the data, and writes the new file to target
    """

    def __init__(self, s3_bucket_src: S3BucketConnector,
                    s3_bucket_tgt: S3BucketConnector, meta_key: str,
                    src_args:XetraSourceConfig, tgt_args: XetraTargetConfig):
        """
        Constructor for Xetra_Transform

        :param s3_bucket_src: connection to source S3 Bucket
        :param s3_bucket_tgt: connection to target S3 Bucket
        :param meta_key: file name for the meta_data file
        :param src_args: NamedTuple class with source configuration data
        :param tgt_args: NamedTuple class with target configuration data
        """

        self.s3_bucket_src = s3_bucket_src
        self.s3_bucket_tgt = s3_bucket_tgt
        self.meta_key = meta_key
        self.src_args = src_args
        self.tgt_args = tgt_args
        self.extract_date = ''
        self.extract_date_list = ''
        self.meta_update_list = ''

    def extract(self): 
        pass

    def transform_report(self):
        pass

    def load(self):
        pass

    def etl_report(self):
        pass
    