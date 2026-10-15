# Liao Wang's homepage

The five root HTML pages are complete files. You can open them directly in a
browser, use a simple local server, or publish them with GitHub Pages. They are
generated from shared source files:

- `head.html` contains the common `<head>`, including metadata, stylesheet, and MathJax.
- `nav.html` contains the common navigation.
- `_content/*.html` contains each page's main content.
- `assets/css/style.css` contains the common styles.
- `scripts/build.py` assembles them into the root pages and marks the current nav link.

After changing the shared files or page content, regenerate the root pages:

```sh
python3 scripts/build.py
```

Then open `index.html` directly to preview. The generated root pages are checked
in so GitHub Pages can serve them without a build step. For a new page, add its
content file to `_content`, add its title and heading to `PAGES` in
`scripts/build.py`, and add its link to `nav.html`.
