import click
from pathlib import Path


@click.command()
@click.option('-e', default='srt', help='Subtitle extension. DEFAULT = srt')
@click.argument('directory', type=click.Path(exists=True))
def cli(directory, e):
    '''
    Remove orphan srt subtitle files from a given directory
    '''

    target_path = Path(directory)

    print(target_path.absolute(), e)


if __name__ == '__main__':
    cli()
