import logging

from . import __version__
from .generate import generate
from argparse import ArgumentParser

logger = logging.getLogger(__file__)

parser = ArgumentParser(
    "templ8",
    description=f"Templ8 {__version__}",
)

parser.add_argument(
    "name",
    help="",
)

parser.add_argument(
    "--output",
    help="",
)


def main() -> None:
    args = parser.parse_args()

    name = args.name
    output = args.output

    if output is None:
        output = name
    
    generate(name, output)


if __name__ == "__main__":
    main()
