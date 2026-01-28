from pathlib import Path

from src.processor import LatexCitationProcessor


# === Configuration ===

# Path to the LaTeX file to analyse
LATEX_FILE = Path("path/to/your.tex")

# Manually set the project / publication name
PROJECT_NAME = "example-project"

# Path to the Obsidian vault
OBSIDIAN_VAULT = Path("path/to/your/obsidian/vault")

# Overview file name derived from the project name
OVERVIEW_FILENAME = f"{PROJECT_NAME}-used-literature.md"

def main() -> None:
    processor = LatexCitationProcessor(LATEX_FILE)
    items = processor.read_latex()

    # collect all used citekeys (split on comma, strip whitespace)
    used_literature = {
        key.strip()
        for _, _, citekeys in items
        for key in citekeys.split(",")
        if key.strip()
    }

    overview_file = OBSIDIAN_VAULT / OVERVIEW_FILENAME

    with open(overview_file, "w", encoding="utf-8") as f:
        f.write(f"# Used literature – {PROJECT_NAME}\n\n")
        for key in sorted(used_literature):
            # Obsidian wikilink – assumes file name == citekey
            f.write(f"- [[{key}]]\n")

    print(f"Wrote overview to {overview_file}")


if __name__ == "__main__":
    main()
