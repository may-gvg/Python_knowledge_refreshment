import csv
import sys

import pandas as pd
import logging


def log_exception(e):
    extype, exc, tb = sys.exc_info()
    logging.warning("Exception: " + str(exc))


class ExcelReader:
    def __init__(self):
        self.data = None

    def read_xls(self, filename, **kwargs):
        try:
            self.data = pd.read_excel(filename, **kwargs)
        except FileNotFoundError as e:
            self.data = None
            log_exception(e)
        except Exception as e:
            self.data = None
            log_exception(e)

    def get_row_count(self):
        if self.data is not None:
            return self.data.index.size
        else:
            return 0

    def get_columns_list(self):
        if self.data is not None:
            return self.data.columns.tolist()
        else:
            return []

    def get_row_list(self):
        if self.data is not None:
            return self.data.values.tolist()
        else:
            return []


class Excel2Csv(ExcelReader):
    def __init__(self):
        super().__init__()

    def write_csv(self, filename):
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(self.get_columns_list())
                writer.writerows(self.get_row_list())
                file.close()
                return True
        except Exception as e:
            logging.waring("Error writing csv file " + str(e))
            return False


def run():
    # rozne instancje
    i1 = ExcelReader()
    i1.read_xls("one.xlsx", header=0, engine='openpyxl')
    if i1.data is not None:
        logging.warning("got one.xlsx")
        logging.warning("row count: " + str(i1.get_row_count()))
        print("cols: " + str(i1.get_columns_list()))
        for row in i1.get_row_list():
            print("row: " + str(row))
    i2 = ExcelReader()
    i2.read_xls("two.xls")
    if i2.data is not None:
        logging.warning("got two.xls")
    i3 = ExcelReader()
    i3.read_xls("notfound.xls")
    if i1.data is None:
        logging.warning("got notfound.xlsx")

    # dziedziczenie
    conv = Excel2Csv()

    conv.read_xls("one.xlsx", engine='openpyxl')
    if conv.data is not None:
        logging.warning("writing csv")
        if conv.write_csv("test.csv"):
            logging.warning("written successfully")
        else:
            logging.warning("error writing csv")


if __name__ == '__main__':
    run()
