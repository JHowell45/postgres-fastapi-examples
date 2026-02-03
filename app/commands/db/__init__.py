import typer

from app.commands.db import populate

cli = typer.Typer(no_args_is_help=True)
cli.add_typer(populate.cli, name="populate")
