from elasticsearch import Elasticsearch

from elastic_feeder.csv_reader import CsvReader
from elastic_feeder.exception import ElkConnectionError
from elastic_feeder.elastic import Elastic
from elasticsearch.exceptions import AuthenticationException

from http import HTTPStatus

import requests
import sys

class FeedElastic:
    def __init__(self, host: str, port: int, filename: str, index: str, properties: dict=None, http_auth: list=None):
        """ 
        FeedElastic class is used to create and insert data from csv into Elasticsearch
        
        param :: host : Elasticsearch instance ip address or hostname
        param :: port : Elasticsearch instance port number
        param :: filename : CSV file full path
        param :: index : Index name to create indice in Elasticsearch
        """
        self.host = host
        self.port = port
        self.filename = filename
        self.index = index
        self.properties = properties
        self.http_auth = http_auth

    def read_csv(self):
        """
        Read csv file and extract headers for creation index mapping properties.
        By default it will create all properties types as `search_as_you_type`
        """
        self.csv_obj = CsvReader(self.filename)
        self.csv_headers = self.csv_obj.csv_header
    
    def es_init(self):
        """ 
        Initialize Elasticsearh object with default request_timeout=30
        """
        self.es = Elasticsearch(f"http://{self.host}:{self.port}", request_timeout=30, http_auth=self.http_auth)

    def check_connection(self):
        """ 
        Checking Elasticsearch connection
        Checking Authentication
        """
        try:
            self.es.ping()
        except Exception as err:
            print("Checking connection failed. Host or port is unavailable")    


        try:
            response = requests.get(f"http://{self.host}:{self.port}", auth = self.http_auth)
            if response.status_code == HTTPStatus.UNAUTHORIZED:
                raise Exception("Authentication failed. Username or password is incorrect")
        except Exception as err:
            print(err)
            sys.exit(0)
        
        
    def index_create(self):
        """ 
        Create Elasticsearch index
        """
        self.elastic = Elastic(self.csv_headers, es_instance=self.es, index=self.index, properties=self.properties)
    
    def generate_data(self):
        """ 
        Obtain data from csv object. This function will yield rows.
        """
        self.gen_data = self.csv_obj.generate_data()

    def bulk_insert(self):
        """ 
        Bulk insert data from csv object.
        """
        self.elastic.bulk_insert(self.gen_data)        

    def run(self):
        pass
        """ 
        Run method is used to consequently run class method to automate data feeding into Elasticsearch
        """
        self.es_init()
        self.check_connection()
        self.read_csv()
        self.index_create()
        self.generate_data()
        self.bulk_insert()
