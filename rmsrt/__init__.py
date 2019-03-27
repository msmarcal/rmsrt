import click
from pathlib import Path


@click.command()
@click.option('--d', help='Target directiory')
def cli(d):
    '''
    Remove orphan srt subtitle files from a given directory
    '''
    target_path = Path(d)

    if not target_path.is_dir():
        exit(f'ERROR: {d} is not a directory')


if __name__ == '__main__':
    cli()
