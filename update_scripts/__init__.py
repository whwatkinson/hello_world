from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


linux_commands = {
    "awk": "awk",
    "basename": "basename",
    "cat": "cat",
    "echo": "echo",
    "fmt": "fmt",
    "head": "head",
    "printenv": "printenv",
    "pwd": "pwd",
    "sed": "sed",
    "tac": "tac",
    "tail": "tail",
    "whoami": "whoami",
    "xxd": "XXD",
}


programming_languages = {
    "abc": "ABC",
    "apl": "APL",
    "bcpl": "BCPL",
    "coffeescript": "CoffeeScript",
    "cpp": "C++",
    "csharp": "C#",
    "dogescript": "DogeScript",
    "fsharp": "F#",
    "javascript": "JavaScript",
    "javascript_is_weird": "JavaScript is weird",
    "jq": "JQ",
    "livescript": "LiveScript",
    "php": "PHP",
    "purescript": "PureScript",
    "python2": "Python 2",
    "python3": "Python 3",
    "typescript": "TypeScript",
    "vhdl": "VHDL",
}

my_names_map = {**linux_commands, **programming_languages}

skips = {"new"}
