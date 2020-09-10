import csv
from elasticsearch import Elasticsearch, helpers
from elastic_feeder.elastic import Elastic
from elastic_feeder.helper import dict_data


class CsvReader:
    """ 
    Class reading, extracting headers, generating data from csv file
    """
    def __init__(self, csv_data, encoding="utf-8-sig"):
        self.csv_data = csv_data
        self.encoding = encoding
        self.extract_headers()
        
    def extract_headers(self):
        """ 
        Extract headers (first column) from csv file
        """
        with open(self.csv_data, encoding=self.encoding) as csv_file:
            self.csv_obj = csv.reader(csv_file)

            for row in self.csv_obj: 
                self.csv_header = [i for i in row if i]
                break

    def generate_data(self):
        """
        Yield data from csv file.
        Header of csv file will be used as a key for Elasticsearch
        """
        with open(self.csv_data, encoding=self.encoding) as csv_file:
            self.csv_obj = csv.reader(csv_file)

            head_row = True
            line_number = 0
            failed = 0

            for row in self.csv_obj: 
                # Append to HEADERS list column names if head_row is True
                if head_row:
                    self.csv_header = [i for i in row if i]
                    head_row = False                    
                    continue

                else:
                    # Create a dictonary with two lists HEADERS and row. Example: {HEADERS[0]: row[0]}
                    data = dict_data(row, self.csv_header)
                    
                    if data is None:
                        failed += 1
                        print(line_number)

                    line_number += 1
                    yield  data

            print(f"Failed {failed} docs")
            print(f"Inserted {line_number} docs")