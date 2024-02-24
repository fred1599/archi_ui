import typer
from importlib import import_module

app = typer.Typer()


@app.command()
def main(option: str = typer.Argument(..., help="Choisissez entre 'tk' ou 'qt'.")):
    if option in ("tk", "qt"):
        module = f"main_{option}"
        import_module(module)
    else:
        raise typer.Exit(f"L'option {option} n'existe pas, seulement 'tk' ou 'qt'.")


app()
