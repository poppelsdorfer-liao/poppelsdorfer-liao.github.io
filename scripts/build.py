"""Generate directly viewable HTML pages from shared head and nav files."""

from html import escape
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
PAGES = {
    "index.html": ("Home", "Liao Wang"),
    "publications.html": ("Publications and Preprints", "Publications and Preprints"),
    "code.html": ("Code", "Code"),
    "teaching.html": ("Tutoring", "Tutoring"),
    "talks.html": ("Talks", "Talks"),
}


def build():
    head = (ROOT / "head.html").read_text(encoding="utf-8")
    nav = (ROOT / "nav.html").read_text(encoding="utf-8")
    if head.count("__PAGE_TITLE__") != 1:
        raise ValueError("head.html must contain one __PAGE_TITLE__ placeholder")

    for filename, (title, heading) in PAGES.items():
        active_link = f'href="{filename}"'
        if nav.count(active_link) != 1:
            raise ValueError(f"nav.html must link to {filename} exactly once")
        page_nav = nav.replace(active_link, active_link + ' aria-current="page"')
        content = (ROOT / "_content" / filename).read_text(encoding="utf-8").strip()
        document = (
            "<!DOCTYPE html>\n"
            "<html lang=\"en\">\n"
            + head.replace("__PAGE_TITLE__", escape(title))
            + "<body id=\"top\">\n"
            + f"<h1>{escape(heading)}</h1>\n"
            + page_nav
            + "<main>\n"
            + content
            + "\n</main>\n"
            + "</body>\n"
            + "</html>\n"
        )
        (ROOT / filename).write_text(document, encoding="utf-8")
        print(f"Built {filename}")


if __name__ == "__main__":
    try:
        build()
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
