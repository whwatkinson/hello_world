from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


linux_commands = {
    "awk": "AWK",
    "sed": "SED",
    "head": "head",
    "tail": "tail",
    "whoami": "whoami",
    "printenv": "printenv",
    "": "",
    "": "",
    "": "",
    "": "",
    "xxd": "XXD",

}


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
    "javascript_is_weird": "JavaScript is weird",
    "jq": "JQ",
    "livescript": "LiveScript",
    "php": "PHP",
    "purescript": "PureScript",
    "python2": "Python 2",
    "python3": "Python 3",
    "sed": "SED",
    "typescript": "TypeScript",
    "vhdl": "VHDL",
    "xxd": "XXD"
}

skips = {"new"}
