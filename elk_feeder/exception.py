from elasticsearch import exceptions

class ElkConnectionError(Exception):
    def __init__(self, expression):
        self.expression = expression
