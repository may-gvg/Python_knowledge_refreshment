import csv
import logging
import pandas as pd


class ExcelReader:
    def __init__(self):
        self.data = None

    def read_xlsx(self, filename, **args):
        try:
            self.data = pd.read_excel(filename, engine='openpyxl', **args)
            return True
        except Exception as e:
            self.data = None
            logging.warning("file could not be read: " + str(e))
            return False

    def read_xls(self, filename, **args):
        try:
            self.data = pd.read_excel(filename, **args)
            return True
        except Exception as e:
            self.data = None
            logging.warning("file could not be read: " + str(e))
            return False

    def get_row_count(self):
        if self.data is not None:
            return len(self.data.index)
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
            file = open(filename, 'w', newline='')
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
    res = i1.read_xlsx("one.xlsx", header=0)
    if res:
        logging.warning("got one.xlsx")
        logging.warning("row count: " + str(i1.get_row_count()))
        print("cols: " + str(i1.get_columns_list()))
        for row in i1.get_row_list():
            print("row: " + str(row))
    i2 = ExcelReader()
    res = i2.read_xls("two.xls")
    if res:
        logging.warning("got two.xls")
    i3 = ExcelReader()
    if not i3.read_xls("notfound.xls"):
        logging.warning("got notfound.xlsx")

    # dziedziczenie
    conv = Excel2Csv()

    if conv.read_xlsx("one.xlsx"):
        logging.warning("writing csv")
        if conv.write_csv("test.csv"):
            logging.warning("written successfully")
        else:
            logging.warning("error writing csv")


if __name__ == '__main__':
    run()
