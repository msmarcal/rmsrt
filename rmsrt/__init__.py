from pathlib import Path

import click
from send2trash import send2trash


def remove_file(file_name, force=False):
    '''
    Moves file_name file to the Trash. If force is true, deletes it.
    '''
    if force:
        Path(file_name).unlink()
    else:
        send2trash(file_name)


def error_message(message):
    '''
    Shows an error "message" and exits (1)
    '''
    click.echo(click.style('\nError: ', fg='red', bold=True), nl=False)
    exit(f'{message}')


@click.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('-e', '--extension', default='srt', help='Subtitle extension. DEFAULT = srt.')
@click.option('-f', '--force', is_flag=True, default=False, help="Force deletion. Don't send files to Trash.")
@click.option('-s', '--silent', is_flag=True, default=False, help='Do not show any output.')
def cli(directory, extension, force, silent):
    '''
    Removes orphan subtitle files from a given DIRECTORY
    '''

    target_path = Path(directory)

    if not target_path.is_dir():
        if silent:
            exit(1)
        else:
            error_message(f'"{target_path.absolute()}" is not a directory.')

    subtitle_files = list(target_path.glob('*.' + extension))

    if not subtitle_files:
        if silent:
            exit(1)
        else:
            error_message(f'No "{extension}" files were found in "{target_path.absolute()}"')

    # TODO: Create a tuple of subtitles that have no corresponding video files

    for file in subtitle_files:

        # name without extension
        print(str(file.name).replace(''.join(file.suffixes[-2:]), ''), end=' ')

        # subtitle extension
        print(''.join(file.suffixes[-2:]))

    # TODO: Show orphan subtitles and ask for delet confirmation if no --silent

    # TODO: Delete (--force) or trash files


if __name__ == '__main__':
    cli()
