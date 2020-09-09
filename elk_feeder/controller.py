from elasticsearch import Elasticsearch

from elk_feeder.csv_reader import CsvReader
from elk_feeder.exception import ElkConnectionError
from elk_feeder.elk import Elk

class FeedElastic:
    def __init__(self, host: str, port: int, filename: str, index: str):
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
        self.es = Elasticsearch(f"http://{self.host}:{self.port}", request_timeout=30)

    def check_connection(self):
        """ 
        Checking Elasticsearch connection
        """
        if not self.es.ping():
            raise ElkConnectionError(f"Check connection string. There was error while establishing connection")

    def index_create(self):
        """ 
        Create Elasticsearch index
        """
        self.elk = Elk(self.csv_headers, es_instance=self.es, index=self.index)
    
    def generate_data(self):
        """ 
        Obtain data from csv object. This function will yield rows.
        """
        self.gen_data = self.csv_obj.generate_data()

    def bulk_insert(self):
        """ 
        Bulk insert data from csv object.
        """
        self.elk.bulk_insert(self.gen_data)

    def run(self):
        """ 
        Run method is used to consequently run class method to automate data feeding into Elasticsearch
        """
        self.es_init()
        self.check_connection()
        self.read_csv()
        self.index_create()
        self.generate_data()
        self.bulk_insert()
