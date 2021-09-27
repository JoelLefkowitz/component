import os
from typing import Any, Dict, List

def merge_dicts(*args: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Successively merge any number of dictionaries.

    >>> merge_dicts({'a': 1}, {'b': 2})
    {'a': 1, 'b': 2}

    >>> merge_dicts({'a': 1}, {'a': 2}, {'a': 3})
    {'a': 3}

    Returns:
        Dict: Dictionary of merged inputs.
    """
    out = {}  # type: Dict[Any, Any]
    for dct in args:
        out = {**out, **dct}
    return out


def path_head(path: str) -> str:
    """
    Get the head of a path string.

    >>> path_head('/dir1/dir2/path.ext')
    'path.ext'

    >>> path_head('path.ext')
    'path.ext'

    Args:
        path (str): Path string.

    Returns:
        str: Path string's head.
    """
    return os.path.split(path)[1]


def path_tail(path: str, depth: int = 1) -> str:
    """
    Get the tail of a path string.

    >>> path_tail('/dir1/dir2/path.ext')
    '/dir1/dir2'

    >>> path_tail('/dir1/dir2/path.ext', 1)
    '/dir1/dir2'

    >>> path_tail('/dir1/dir2/path.ext', 2)
    '/dir1'

    Args:
        path (str): Path string.

    Returns:
        str: Path string's tail.
    """
    tail = os.path.split(path)[0]
    return tail if depth == 1 else path_tail(tail, depth - 1)


def path_ext(path: str) -> str:
    """
    Get the extension of a path string.

    >>> path_ext('/dir1/dir2/path.ext')
    '.ext'

    >>> path_ext('/dir1/dir2/path.ext.j2')
    '.j2'

    Args:
        path (str): Path string.

    Returns:
        str: Path string's extension.
    """
    return os.path.splitext(path)[1]


def drop_extension(path: str) -> str:
    """
    Get the full name without the final extension of a path string.

    >>> drop_extension('/dir1/dir2/path.ext')
    '/dir1/dir2/path'

    >>> drop_extension('/dir1/dir2/path.ext1.ext2')
    '/dir1/dir2/path.ext1'

    Args:
        path (str): Path string.

    Returns:
        str: Path string without its final extension.
    """
    return os.path.splitext(path)[0]
