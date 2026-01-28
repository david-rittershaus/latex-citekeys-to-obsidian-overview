import re
from typing import List, Pattern
from pathlib import Path


DEFAULT_ITEM_RE: Pattern = re.compile(
    r'''\\autocites?
        (?:\s*
            (?:\[[^\]]*\]
            | \{[^}]*\}
            )
        )*
        \s*\{(?P<citekey>[^}]*)\}
    ''',
    re.DOTALL | re.VERBOSE
)


class LatexCitationProcessor:
    """Extracts citekeys from LaTeX files using \\autocite or \\autocites."""

    def __init__(
        self,
        latex_filename: str | Path,
        item_re: Pattern = DEFAULT_ITEM_RE,
    ):
        self.latex_filename = Path(latex_filename)
        self.ITEM_RE = item_re

    def read_latex(self) -> List[tuple]:
        """
        Returns a list of tuples:
        (None, None, citekeys)
        """
        with open(self.latex_filename, "r", encoding="utf-8") as file:
            text = file.read()

        return [
            (None, None, m.group("citekey").strip())
            for m in self.ITEM_RE.finditer(text)
            if m.group("citekey") != "quote"
        ]
