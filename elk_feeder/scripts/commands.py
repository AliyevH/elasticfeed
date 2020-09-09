import click
from elk_feeder.controller import FeedElastic


@click.group()
def cli():
    """ Group cli"""


@cli.command(help="test")
@click.option("--host", default="localhost", help="Specify Elasticsearch host")
@click.option("--port", default="9200", help="Specify Elasticsearch port")
@click.option("--index", required=True, help="Specify Index name")
@click.argument('filename', type=click.Path(exists=True))
def command(host, port, filename, index):
    fe = FeedElastic(host, port, filename, index)
    fe.run()


command()
