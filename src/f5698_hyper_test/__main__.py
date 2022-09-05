"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """F5698_Hyper_Test."""


if __name__ == "__main__":
    main(prog_name="f5698_hyper_test")  # pragma: no cover
