"""Convert markdown file to styled PDF using markdown + xhtml2pdf."""
import sys
from pathlib import Path
import markdown
from xhtml2pdf import pisa

CSS = """
@page {
    size: letter;
    margin: 0.75in 0.85in;
    @frame footer {
        -pdf-frame-content: footerContent;
        bottom: 0.4in;
        margin-left: 0.85in;
        margin-right: 0.85in;
        height: 0.4in;
    }
}
body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.45;
    color: #1a1a1a;
}
h1 {
    font-size: 20pt;
    color: #1a3c6e;
    border-bottom: 2px solid #1a3c6e;
    padding-bottom: 6px;
    margin-top: 18pt;
}
h2 {
    font-size: 15pt;
    color: #1a3c6e;
    border-bottom: 1px solid #cccccc;
    padding-bottom: 4px;
    margin-top: 16pt;
}
h3 {
    font-size: 12pt;
    color: #2a5a9e;
    margin-top: 12pt;
}
h4 {
    font-size: 10.5pt;
    color: #333;
    margin-top: 10pt;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin: 8pt 0;
    font-size: 8.5pt;
}
th {
    background-color: #1a3c6e;
    color: white;
    padding: 5px 6px;
    text-align: left;
    font-weight: bold;
}
td {
    padding: 4px 6px;
    border-bottom: 1px solid #ddd;
    vertical-align: top;
}
tr:nth-child(even) td {
    background-color: #f5f7fa;
}
strong {
    color: #1a1a1a;
}
em {
    color: #555;
}
blockquote {
    border-left: 3px solid #1a3c6e;
    padding-left: 12px;
    margin-left: 0;
    color: #444;
    font-style: italic;
}
ul, ol {
    margin-top: 4pt;
    margin-bottom: 4pt;
}
li {
    margin-bottom: 2pt;
}
code {
    font-family: Courier;
    font-size: 9pt;
    background-color: #f0f0f0;
    padding: 1px 3px;
}
hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 12pt 0;
}
a {
    color: #1a3c6e;
    text-decoration: none;
}
.header-block {
    background-color: #f0f4f8;
    border: 1px solid #d0d8e0;
    padding: 10px 14px;
    margin-bottom: 14pt;
    border-radius: 4px;
}
#footerContent {
    text-align: center;
    font-size: 7.5pt;
    color: #999;
}
"""

def convert(md_path: str, pdf_path: str) -> bool:
    md_text = Path(md_path).read_text(encoding="utf-8")

    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc", "smarty"],
    )

    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"/><style>{CSS}</style></head>
<body>
{html_body}
<div id="footerContent">
    CONFIDENTIAL — Aptiv Product Planning | Page <pdf:pagenumber/>
</div>
</body>
</html>"""

    with open(pdf_path, "wb") as f:
        status = pisa.CreatePDF(html, dest=f)
    return not status.err


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "cv2x-5g-market-research.md"
    dst = sys.argv[2] if len(sys.argv) > 2 else src.replace(".md", ".pdf")
    ok = convert(src, dst)
    if ok:
        print(f"PDF created: {dst}")
    else:
        print("ERROR: PDF conversion failed", file=sys.stderr)
        sys.exit(1)
