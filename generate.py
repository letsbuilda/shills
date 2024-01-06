import json
from pathlib import Path

SHILLS_PATH = Path("shills.json")
TEMPLATE_PATH = Path("template.html")
CERTS_PATH = Path("certs")


def main() -> None:
    entries: dict[str, str | list[str]] = json.loads(SHILLS_PATH.read_text())
    template = TEMPLATE_PATH.read_text()
    CERTS_PATH.mkdir(exist_ok=True)

    for name, shilling in entries.items():
        create_certificate(name, shilling, template)


def create_certificate(name: str, shilling: str | list[str], template: str) -> None:
    if isinstance(shilling, str):
        # Person only shills one thing
        shilling = [shilling]

    cert_html = template.replace("{name}", name).replace(
        "{shilling}", format_csv_with_and(shilling)
    )
    cert_path = CERTS_PATH / f"{name}.html"
    cert_path.write_text(cert_html)

    print(f"{name} -> {cert_path}")


def format_csv_with_and(items: list[str]) -> str:
    """Format a list of items as a comma-separated list with an "and" before the last item."""

    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        return ", ".join(items[:-1]) + f", and {items[-1]}"


if __name__ == "__main__":
    main()
