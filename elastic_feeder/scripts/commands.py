import click
from elastic_feeder.controller import FeedElastic


@click.group()
def cli():
    """ Group cli"""


@cli.command(help="Example: elasticfeed --host 127.0.0.1 --port 9200 <full filepath>")
@click.option("--host", default="localhost", help="Host name or Ip address", show_default=True)
@click.option("--port", default="9200", help="Port number", show_default=True)
@click.option("--index", required=True, help="Index name")
@click.option("--username", help="username")
@click.option("--password", help="password")
@click.argument('filename', type=click.Path(exists=True))
def command(host, port, filename, index, username, password):
    if username and password:
        http_auth = (username, password)
    else:
        http_auth = None

    fe = FeedElastic(
        host=host,
        port=port,
        filename=filename,
        index=index,
        http_auth=http_auth
        )

    fe.run()


command()
