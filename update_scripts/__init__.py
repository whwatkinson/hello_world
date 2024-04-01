from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


my_names_map = {
    "abc": "ABC",
    "awk": "AWK",
    "bcpl": "BCPL",
    "coffeescript": "CoffeeScript",
    "cpp": "C++",
    "csharp": "C#",
    "dogescript": "DogeScript",
    "fsharp": "F#",
    "javascript": "JavaScript",
    "jq": "JQ",
    "livescript": "LiveScript",
    "php": "PHP",
    "purescript": "PureScript",
    "python2": "Python 2",
    "python3": "Python 3",
    "typescript": "TypeScript",
    "vhdl": "VHDL",
}

skips = {"new"}
