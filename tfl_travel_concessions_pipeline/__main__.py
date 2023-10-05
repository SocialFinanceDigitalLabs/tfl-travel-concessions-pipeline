import click as click

from tfl_travel_concessions_pipeline.tfl import tfl


@click.group()
def cli():
    pass


cli.add_command(tfl)

if __name__ == "__main__":
    cli()
