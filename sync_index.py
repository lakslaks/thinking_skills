"""Refresh the skill table in agent_instructions.md from skill_index.yaml."""

import re
import sys
from pathlib import Path

from ruamel.yaml import YAML

START = "<!-- skill-index:start -->"
END = "<!-- skill-index:end -->"
COLUMNS = ("reasoning_type", "grounding_mode", "source_display", "confidence_mode")


def render_table(registry: dict) -> str:
    """Return a header row and one compact row per skill."""
    header = " | ".join(["name", "aliases", *COLUMNS])
    rows = [
        " | ".join(
            [name, "; ".join(skill["aliases"]), *(str(skill[c]) for c in COLUMNS)]
        )
        for name, skill in registry["skills"].items()
    ]
    return "\n".join([header, *rows])


def sync(root: Path) -> None:
    """Rewrite the table between the markers in agent_instructions.md."""
    registry = YAML(typ="safe").load((root / "skill_index.yaml").read_text())
    path = root / "agent_instructions.md"
    text = path.read_text()

    pattern = re.compile(re.escape(START) + ".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(text):
        raise ValueError("Index markers not found in agent_instructions.md.")

    block = f"{START}\n{render_table(registry)}\n{END}"
    path.write_text(pattern.sub(lambda _: block, text))


if __name__ == "__main__":
    sync(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent)
