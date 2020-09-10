import click
from elastic_feeder.controller import FeedElastic


@click.group()
def cli():
    """ Group cli"""


@cli.command(help="Example: elasticfeed --host 127.0.0.1 --port 9200 <full filepath>")
@click.option("--host", default="localhost", help="Specify Elasticsearch host", show_default=True)
@click.option("--port", default="9200", help="Specify Elasticsearch port", show_default=True)
@click.option("--index", required=True, help="Specify Index name")
@click.argument('filename', type=click.Path(exists=True))
def command(host, port, filename, index):
    fe = FeedElastic(host, port, filename, index)
    fe.run()


command()
