# coding: utf8
"""Entry point for cli"""
import os

import click

cmd_folder = os.path.join(os.path.dirname(__file__))
cmd_prefix = 'cmd_'


class CLI(click.MultiCommand):
    """Main class for handling commands"""

    def list_commands(self, ctx):
        """
         Obtain a list of all available commands.
        Args:
            ctx: Click context
        Returns:
            List of sorted commands
        """
        commands = []

        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename.startswith(cmd_prefix):
                commands.append(filename[4:-3])

        commands.sort()

        return commands

    def get_command(self, ctx, name):
        """
         Get a specific command by looking up the module.
        Args:
            ctx: Click context
            name: Command name
        Returns:
            Module's cli function
        """
        ns = {}

        filename = os.path.join(cmd_folder, cmd_prefix + name + '.py')

        with open(filename) as f:
            code = compile(f.read(), filename, 'exec')
            eval(code, ns, ns)

        return ns['cli']


@click.command(cls=CLI)
def cli():
    """ Commands to help manage your project. """
    pass
