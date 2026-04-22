"""
Extract text, tables, and images from PDF files into structured markdown.
Renders full pages as images (capturing vector diagrams, charts, etc.)
and extracts individual embedded images. Uses PyMuPDF (fitz).

Usage: python extract_pdf.py <input.pdf> <output_dir>
"""

import sys
import os
from pathlib import Path

# Minimum embedded image size to keep (bytes). Filters out tiny icons.
MIN_IMAGE_SIZE = 10_000
# DPI for full-page rendering (higher = sharper but larger files)
RENDER_DPI = 200


def extract_pdf(input_path: str, output_dir: str) -> str:
    import fitz  # PyMuPDF

    doc = fitz.open(input_path)
    output_path = Path(output_dir)
    images_dir = output_path / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    filename = Path(input_path).stem
    md_lines = [f"# Extracted: {filename}\n"]
    md_lines.append(f"**Source**: {Path(input_path).name}\n")
    md_lines.append(f"**Pages**: {len(doc)}\n")

    # Extract metadata
    metadata = doc.metadata
    if metadata:
        if metadata.get("title"):
            md_lines.append(f"**Title**: {metadata['title']}\n")
        if metadata.get("author"):
            md_lines.append(f"**Author**: {metadata['author']}\n")

    md_lines.append("---\n")

    embedded_count = 0

    for page_num, page in enumerate(doc, 1):
        md_lines.append(f"\n## Page {page_num}\n")

        # --- Full-page render (captures everything visual) ---
        page_image_name = f"page{page_num}_full.png"
        page_image_path = images_dir / page_image_name
        try:
            zoom = RENDER_DPI / 72  # 72 DPI is PDF default
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            pix.save(str(page_image_path))
            md_lines.append(f"![Page {page_num}](./images/{page_image_name})\n")
        except Exception as e:
            md_lines.append(f"*[Page render failed: {e}]*\n")

        # --- Extract text ---
        text = page.get_text("text")
        if text.strip():
            lines = text.split("\n")
            cleaned_lines = []
            prev_blank = False
            for line in lines:
                is_blank = not line.strip()
                if is_blank and prev_blank:
                    continue
                cleaned_lines.append(line)
                prev_blank = is_blank
            md_lines.append("\n".join(cleaned_lines))

        # --- Extract tables ---
        tables = page.find_tables()
        if tables:
            for table_num, table in enumerate(tables, 1):
                md_lines.append(f"\n**Table {table_num}**:\n")
                data = table.extract()
                if data and len(data) > 0:
                    headers = [str(cell) if cell else "" for cell in data[0]]
                    md_lines.append("| " + " | ".join(headers) + " |")
                    md_lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
                    for row in data[1:]:
                        cells = [str(cell).replace("|", "\\|").replace("\n", " ") if cell else "" for cell in row]
                        md_lines.append("| " + " | ".join(cells) + " |")
                    md_lines.append("")

        # --- Extract individual embedded images (high-res only) ---
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            try:
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)

                # Skip tiny images (icons, bullets, decorative)
                if pix.width * pix.height < 10000:
                    continue

                # Convert CMYK to RGB if needed
                if pix.n - pix.alpha > 3:
                    pix = fitz.Pixmap(fitz.csRGB, pix)

                # Check byte size
                img_bytes = pix.tobytes("png")
                if len(img_bytes) < MIN_IMAGE_SIZE:
                    continue

                embedded_count += 1
                image_name = f"page{page_num}_embed{embedded_count}.png"
                image_path = images_dir / image_name
                pix.save(str(image_path))

                md_lines.append(f"\n![Embedded image from page {page_num}](./images/{image_name})\n")
            except Exception:
                pass

        md_lines.append("\n---\n")

    page_count = len(doc)
    doc.close()

    # Write markdown
    md_path = output_path / f"{filename}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"Extracted {page_count} pages, {page_count} page renders, {embedded_count} embedded images")
    print(f"Output: {md_path}")
    return str(md_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_pdf.py <input.pdf> <output_dir>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_directory = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Error: File not found: {input_file}")
        sys.exit(1)

    extract_pdf(input_file, output_directory)
