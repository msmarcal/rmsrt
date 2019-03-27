import click
from pathlib import Path


@click.command()
@click.argument('directory', type=click.Path(exists=True))
def cli(directory):
    '''
    Remove orphan srt subtitle files from a given directory
    '''
    target_path = Path(directory)

    print(target_path.absolute())


if __name__ == '__main__':
    cli()
