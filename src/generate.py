import os
import logging
from pathlib import Path
from walkmate import get_child_files

from convert_case import kebab_case, pascal_case, is_kebab_case, is_pascal_case
import shutil
from .parse import parse_template
from .utils import drop_extension, path_head, path_ext, path_tail

logger = logging.getLogger(__file__)


def generate(name: str, output: str) -> None:
    Path(output).mkdir(parents=True, exist_ok=True)

    for path in get_child_files(
        os.path.normpath(os.path.join(__file__, "..", "templates")), max_depth=1
    ):
        if path_ext(path) == ".j2":
            template_head = drop_extension(path_head(path))
            [template_name, *template_exts] = template_head.split(".")

            if is_kebab_case(template_name):
                renamed = kebab_case(name)

            elif is_pascal_case(template_name):
                renamed = pascal_case(name)

            else:
                continue
            
            with open(os.path.join(output, ".".join([renamed, *template_exts])), "w") as stream:
                stream.write(parse_template(path, {"name": name}))

        else:
            target = os.path.join(output, path_head(path))
            shutil.copyfile(path, target)
