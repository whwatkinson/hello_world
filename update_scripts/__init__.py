from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


my_names_map = {
    "abc": "ABC",
    "apl": "APL",
    "awk": "AWK",
    "bcpl": "BCPL",
    "coffeescript": "CoffeeScript",
    "cpp": "C++",
    "csharp": "C#",
    "dogescript": "DogeScript",
    "fsharp": "F#",
    "javascript": "JavaScript",
    "javascript_is_weird": "javaScript is weird",
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
