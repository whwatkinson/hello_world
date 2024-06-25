from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


linux_commands = {
    "awk": "awk",
    "basename": "basename",
    "cat": "cat",
    "echo": "echo",
    "fmt": "fmt",
    "grep": "grep",
    "head": "head",
    "ls": "ls",
    "printenv": "printenv",
    "pwd": "pwd",
    "sed": "sed",
    "tac": "tac",
    "tail": "tail",
    "whoami": "whoami",
    "xxd": "xxd",
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
    "gnuhello": "GNU Hello",
    "goplus": "Go+",
    "html": "HTML",
    "javascript": "JavaScript",
    "javascript_is_weird": "JavaScript is weird",
    "jq": "JQ",
    "livescript": "LiveScript",
    "php": "PHP",
    "purescript": "PureScript",
    "python2": "Python 2",
    "python3": "Python 3",
    "tclsh": "TclSh",
    "typescript": "TypeScript",
    "vhdl": "VHDL",
    "xml": "XML",
    "yaml": "YAML",
}

my_names_map = {**linux_commands, **programming_languages}

skips = {"new", "linux_commands"}
