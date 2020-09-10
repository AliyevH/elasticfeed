from pprint import pprint
from elasticsearch import Elasticsearch, helpers
from elasticsearch.exceptions import NotFoundError
from pprint import pprint

class Elastic:
    def __init__(
        self, 
        headers: list, 
        es_instance: Elasticsearch, 
        index: str,
        properties: dict = None,
        ):

        self.es = es_instance
        self.index = index.lower()

        self.headers = headers
        self.properties = properties

        if not self.get_indices():
            self.create_indices()       
    
    def headers_coord_check(self):
        """If lat and lon in headers replace it with coords. Custom case function
        """
        if "lat" in self.headers and "lon" in self.headers:
            self.headers.append("coord")
            self.headers.remove("lat")
            self.headers.remove("lon")       

    def create_schema_map(self):
        self.mapping = {
            "mappings": {
                "properties": self.properties
            }
        }
    
    def create_indices(self):
        if self.properties:
            self.es.indices.create(
                index = self.index,
                body = self.mapping
            )
        else:
            self.es.indices.create(
                index = self.index,
            )

    
    def get_indices(self):
        try:
            self.es.indices.get(self.index)
            print(f"{self.index} index found. Skipping index creation")
            return True
        except NotFoundError as err:
            print(err)
            print(f"{self.index} index not found. Creating index.")
            return False

    def bulk_insert(self, gen_data):
        try:
            print("Begining bulk insert")
            helpers.bulk(self.es, gen_data, index=self.index)
        except Exception as err:
            print("Got err -> ", err)