# coding: utf8
"""Entry point for cli"""
import os
from typing import Any, List

import click

CMD_FOLDER = os.path.join(os.path.dirname(__file__))
CMD_PREFIX = 'cmd_'


class CLI(click.MultiCommand):
    """Main class for handling commands"""

    def list_commands(self, ctx: Any) -> List:
        """
         Obtain a list of all available commands.
        Args:
            ctx (Any): Click context
        Returns:
            (List) List of sorted commands
        """
        commands = []

        for filename in os.listdir(CMD_FOLDER):
            if filename.endswith('.py') and filename.startswith(CMD_PREFIX):
                commands.append(filename[4:-3])

        commands.sort()

        return commands

    def get_command(self, ctx: Any, cmd_name: str) -> Any:
        """
         Get a specific command by looking up the module.
        Args:
            ctx (Any): Click context
            cmd_name (str): Command name
        Returns:
            (Any) Module's cli function
        """
        n_s = {}

        filename = os.path.join(CMD_FOLDER, CMD_PREFIX + cmd_name + '.py')

        with open(filename) as file:
            code = compile(file.read(), filename, 'exec')
            eval(code, n_s, n_s)

        return n_s['cli']


@click.command(cls=CLI)
def cli():
    """ Commands to help manage your project. """
