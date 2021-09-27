import logging
import os
from typing import Any, Dict, List

from convert_case import (
    camel_case,
    kebab_case,
    pascal_case,
    sentence_case,
    snake_case,
    title_case,
    upper_case,
)

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from .utils import path_head, path_tail, merge_dicts

logger = logging.getLogger(__file__)


def parse_template(path: str, render_context: Dict[str, Any]) -> str:
    env = Environment(
        loader=FileSystemLoader([path_tail(path)]),
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=True,
        keep_trailing_newline=True,
        undefined=StrictUndefined,
    )

    env.filters = merge_dicts(
        env.filters,
        {
            "camel_case": camel_case,
            "kebab_case": kebab_case,
            "pascal_case": pascal_case,
            "sentence_case": sentence_case,
            "snake_case": snake_case,
            "title_case": title_case,
            "upper_case": upper_case,
        },
    )

    return env.get_template(path_head(path)).render(**render_context)
