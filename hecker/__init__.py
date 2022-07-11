# SPDX-License-Identifier: GPL-2.0

import click


@click.command("hecker")
@click.argument("text", type=str)
def main(text: str) -> None:
    click.echo(f"*in hacker voice*: {text}")


if __name__ == "__main__":
    main()
