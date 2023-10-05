import click as click


@click.group()
def tfl():
    """Functions for parsing and processing TfL travel concession data"""
    pass


# This is the entrypoint for the pipeline work and an example of the function shape needed to add to click for CLI integration
@tfl.command()
def pipeline():
    print("hello, world - this is the TfL Travel Concession Pipeline")
    return True
