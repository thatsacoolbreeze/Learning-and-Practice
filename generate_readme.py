"""Generate a Markdown README that lists the Python exercises in this folder."""

# argparse reads options the user types after the script name, such as --watch.
import argparse
# time lets watch mode pause between checks instead of repeatedly scanning at full speed.
import time
# Path provides convenient, cross-platform operations for paths and files.
from pathlib import Path


# __file__ is this script's path. resolve() makes it absolute, and parent gets
# its containing folder. This makes the script work no matter where the terminal
# is currently pointed when the script is run.
ROOT = Path(__file__).resolve().parent

# These are paths relative to ROOT: the README output and this generator itself.
README_PATH = ROOT / "README.md"
GENERATOR_PATH = Path(__file__).resolve()

# Watch mode waits this many seconds between checks of the exercise filenames.
CHECK_INTERVAL_SECONDS = 2

# Map exercise file names (lowercase, without ".py") to helpful README topics.
# Add or edit entries here to customize what the README says about an exercise.
DESCRIPTIONS = {
    "exercise 1": "Practice with variables, strings, floats, integers, and basic type checks.",
    "exercise 2 lists": "Create lists, append values, access items by index, and iterate over a list.",
    "lists exercise": "Practice adding numbers and strings to lists and retrieving a name by index.",
    "basic operators": "Examples of arithmetic, modulo, exponentiation, string operations, and list operations.",
    "basic operations exercise": "Practice object creation, list repetition and concatenation, and counting items.",
    "strings": "Practice string length, indexing, slicing, case conversion, prefix checks, and splitting.",
    "basic strings": "Explore string formatting, searching, slicing, and common string methods.",
    "conditions": "Practice comparisons, Boolean operators, membership, identity, and conditional statements.",
}


def find_scripts() -> list[Path]:
    """Find Python exercises beside this script and return them alphabetically."""
    # glob("*.py") finds .py files directly inside ROOT (not in subfolders).
    # The generator is also a Python file, so filter out its absolute path.
    # casefold() gives a consistent alphabetical sort regardless of capitalization.
    scripts = (
        path
        for path in ROOT.glob("*.py")
        if path.resolve() != GENERATOR_PATH
    )
    return sorted(scripts, key=lambda path: path.name.casefold())


def describe(path: Path) -> str:
    """Look up an exercise topic or make a simple description from its name."""
    # stem is the filename without ".py"; lowercase it to match dictionary keys.
    # dict.get(key, fallback) returns the custom text, or the fallback if missing.
    # replace() makes a filename with underscores more readable in the fallback.
    return DESCRIPTIONS.get(
        path.stem.lower(),
        f"Python practice code covering {path.stem.replace('_', ' ').lower()}.",
    )


def build_readme() -> str:
    """Create the README text in memory and return it as one string."""
    # Get a fresh file list each time this runs. Both normal mode and watch mode
    # use this function, ensuring they generate the same README structure.
    scripts = find_scripts()

    # Each list item represents one line in the Markdown file. Empty strings
    # become blank lines when we join the list at the end.
    lines = [
        "# Coding Practice",
        "",
        "A collection of beginner-friendly Python exercises covering core programming concepts.",
        "",
        "## Exercises",
        "",
        "| File | Topics |",
        "| --- | --- |",
    ]

    if scripts:
        # Add one table row per exercise. The Markdown link points to the file.
        # Angle brackets around the link path allow filenames to contain spaces.
        for path in scripts:
            lines.append(f"| [`{path.name}`](<./{path.name}>) | {describe(path)} |")
    else:
        # Keep the table informative if the folder contains no exercises yet.
        lines.append("| No Python exercises found yet. | |")

    # extend() appends all these additional lines: run instructions and both
    # ways to regenerate the README (once or continuously with --watch).
    lines.extend(
        [
            "",
            "## Run an exercise",
            "",
            "Run a script from this folder with Python 3:",
            "",
            "```powershell",
            "python \"exercise 1.py\"",
            "```",
            "",
            "## Regenerate this README",
            "",
            "To update it once after adding or removing Python exercise files, run:",
            "",
            "```powershell",
            "python generate_readme.py",
            "```",
            "",
            "To keep it updated automatically while you add, remove, or rename Python files, run:",
            "",
            "```powershell",
            "python generate_readme.py --watch",
            "```",
            "",
            "Leave that command running in a terminal. It checks for file changes every two seconds; press Ctrl+C to stop it.",
            "",
        ]
    )

    # join() combines the Markdown lines with newline characters. The last empty
    # line above means the saved README ends with a newline.
    return "\n".join(lines)


def generate_readme() -> None:
    """Build the latest README and save it as UTF-8 text."""
    # build_readme() creates the text; write_text() replaces README.md with it.
    # UTF-8 is a common text encoding that supports a wide range of characters.
    README_PATH.write_text(build_readme(), encoding="utf-8")

    # Show the output path so it is clear which README was updated.
    print(f"README generated: {README_PATH}")


def watch_for_changes() -> None:
    """Keep running; regenerate the README when exercise filenames change."""
    # Save the current filenames as a snapshot. A tuple is an ordered, fixed
    # collection that can be compared with the next snapshot.
    previous_files = tuple(path.name for path in find_scripts())
    print("Watching for Python file changes. Press Ctrl+C to stop.")

    try:
        while True:
            # Wait between checks so the loop doesn't continuously use CPU.
            time.sleep(CHECK_INTERVAL_SECONDS)

            # Find the files again and compare their names with the old snapshot.
            # A different tuple means a file was added, removed, or renamed.
            current_files = tuple(path.name for path in find_scripts())
            if current_files != previous_files:
                generate_readme()

                # Update the saved snapshot. Without this, the same change would
                # be detected over and over on every check.
                previous_files = current_files
    except KeyboardInterrupt:
        # Ctrl+C interrupts the waiting loop. Catch it to exit watch mode neatly.
        print("\nStopped watching.")


if __name__ == "__main__":
    # Python sets __name__ to "__main__" when this file is run directly.
    # This guard prevents the command-line code from running if this file is
    # imported by another Python script.
    parser = argparse.ArgumentParser(
        description="Generate a README for Python exercises."
    )

    # store_true means args.watch is False by default and True when --watch is used.
    parser.add_argument(
        "--watch",
        action="store_true",
        help="keep running and regenerate the README when Python files change",
    )
    args = parser.parse_args()

    # Always generate once immediately. If --watch was supplied, continue
    # checking for file additions/removals/renames after the first generation.
    generate_readme()
    if args.watch:
        watch_for_changes()
