PATTERN = r"BADGIE\s+TIME"

PATTERN_START = r"<!--\s+" + PATTERN + r"\s+-->"

PATTERN_END = r"<!--\s+END\s+" + PATTERN + r"\s+-->"

PATTERN_GIT_SSH = r"^(?P<user>git)@(?P<host>.*?):(?P<path>.*?)\.git$"
