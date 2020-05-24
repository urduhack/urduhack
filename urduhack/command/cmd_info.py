# coding: utf8
"""Print info about Urduhack library"""

from pathlib import Path

import click

from urduhack import get_info


@click.command()
@click.argument('markdown', default=False)
def cli(markdown):
    """
     Print system info about Urduhack library.
    """
    data = get_info()
    if markdown is not False:
        markdown_format = []
        for key, value in data.items():
            if isinstance(value, str) and Path(value).exists():
                continue
            markdown_format.append("* **{}:** {}".format(key, value))

        title = "Info about Urduhack library"
        click.echo("\n## {}".format(title))
        click.echo("\n{}\n".format("\n".join(markdown_format)))
    else:
        click.echo(data)
