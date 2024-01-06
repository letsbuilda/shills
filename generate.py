import json
from pathlib import Path

SHILLS_PATH = Path("shills.json")
TEMPLATE_PATH = Path("template.html")
CERTS_PATH = Path("certs")


def main() -> None:
    entries: dict[str, str | list[str]] = json.loads(SHILLS_PATH.read_text())
    template = TEMPLATE_PATH.read_text()
    CERTS_PATH.mkdir(exist_ok=True)

    for name, shillings in entries.items():
        if isinstance(shillings, str):
            # Person only shills one thing
            shillings = [shillings]

        for shilling in shillings:
            create_certificate(name, shilling, template)


def create_certificate(name: str, shilling: str, template: str) -> None:
    cert_html = template.replace("{name}", name).replace("{shilling}", shilling)
    cert_path = CERTS_PATH / f"{name}_{shilling}.html"
    cert_path.write_text(cert_html)

    print(f"Generated {shilling} certificate for {name} at {cert_path}")


if __name__ == "__main__":
    main()
