# latex-autocite-notes-helper

Small helper for a personal Obsidian-based research workflow.

The script reads a LaTeX file that uses `\autocite` / `\autocites`, extracts the citekeys, and creates a simple Markdown overview listing the literature actually used in that text. The overview is intended for use in Obsidian and links to existing notes (one note per citekey) using Obsidian-style wikilinks.

## Context

In my workflow, literature is managed in Zotero and annotations/notes are exported to Obsidian, resulting in one Markdown file per reference. 

This script helps to retroactively (and prospectively) create a publication-specific overview of which references are actually cited in a given LaTeX file, without duplicating or modifying the original notes.

## Assumptions

- LaTeX source uses `\autocite` or `\autocites`
- Citekeys match the filenames of the corresponding Markdown notes
- One Markdown file per reference
