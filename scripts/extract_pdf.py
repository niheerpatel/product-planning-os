"""Extract text, tables, and images from PDF files into markdown.

Usage:
	python extract_pdf.py <input.pdf> <output_dir>
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import fitz


def usage() -> None:
	print("Usage: python extract_pdf.py <input.pdf> <output_dir>")


def sanitize(value: str) -> str:
	cleaned = re.sub(r"[^A-Za-z0-9._ -]", "_", value.strip())
	return cleaned or "document"


def markdown_escape(value: str) -> str:
	return value.replace("|", "\\|").replace("\n", " ").strip()


def rows_to_markdown(rows: list[list[str]]) -> str:
	if not rows:
		return ""

	width = max(len(row) for row in rows)
	padded = [row + [""] * (width - len(row)) for row in rows]

	header = [markdown_escape(cell) or " " for cell in padded[0]]
	divider = ["---"] * width
	lines = [
		"| " + " | ".join(header) + " |",
		"| " + " | ".join(divider) + " |",
	]

	for row in padded[1:]:
		lines.append("| " + " | ".join(markdown_escape(cell) or " " for cell in row) + " |")

	return "\n".join(lines)


def extract_tables(page: fitz.Page) -> list[list[list[str]]]:
	tables: list[list[list[str]]] = []
	finder = getattr(page, "find_tables", None)
	if not callable(finder):
		return tables

	try:
		found = finder()
		for table in found.tables:
			rows = table.extract()
			normalized = [["" if cell is None else str(cell) for cell in row] for row in rows]
			if normalized:
				tables.append(normalized)
	except Exception:
		return tables

	return tables


def main() -> int:
	if len(sys.argv) != 3:
		usage()
		return 1

	input_path = Path(sys.argv[1]).expanduser().resolve()
	output_dir = Path(sys.argv[2]).expanduser().resolve()

	if not input_path.exists() or input_path.suffix.lower() != ".pdf":
		print(f"Invalid PDF input file: {input_path}")
		return 1

	output_dir.mkdir(parents=True, exist_ok=True)
	images_dir = output_dir / "images"
	images_dir.mkdir(parents=True, exist_ok=True)

	markdown_path = output_dir / f"{sanitize(input_path.stem)}.md"

	doc = fitz.open(input_path)
	lines: list[str] = [f"# {input_path.name}", "", f"Pages: {doc.page_count}", ""]

	for page_index in range(doc.page_count):
		page_number = page_index + 1
		page = doc.load_page(page_index)
		lines.append(f"## Page {page_number}")
		lines.append("")

		# Render full page image for diagrams/charts not represented in text.
		page_image_name = f"page_{page_number:04d}.png"
		page_image_path = images_dir / page_image_name
		pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
		pix.save(page_image_path)
		lines.append(f"![Page {page_number}](./images/{page_image_name})")
		lines.append("")

		text = page.get_text("text").strip()
		lines.append("### Text")
		lines.append("")
		lines.append(text if text else "_No extractable text on this page._")
		lines.append("")

		tables = extract_tables(page)
		if tables:
			lines.append("### Tables")
			lines.append("")
			for table_index, table_rows in enumerate(tables, start=1):
				lines.append(f"#### Table {page_number}.{table_index}")
				lines.append("")
				lines.append(rows_to_markdown(table_rows))
				lines.append("")

		embedded = page.get_images(full=True)
		if embedded:
			lines.append("### Embedded Images")
			lines.append("")
			for image_index, image_info in enumerate(embedded, start=1):
				xref = image_info[0]
				try:
					image = doc.extract_image(xref)
				except Exception:
					continue

				ext = image.get("ext", "png")
				image_name = f"page_{page_number:04d}_embedded_{image_index:02d}.{ext}"
				image_path = images_dir / image_name
				image_path.write_bytes(image["image"])
				lines.append(f"- ![Embedded image {page_number}.{image_index}](./images/{image_name})")

			lines.append("")

	doc.close()
	markdown_path.write_text("\n".join(lines), encoding="utf-8")
	print(f"Extracted: {input_path}")
	print(f"Markdown: {markdown_path}")
	print(f"Images: {images_dir}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
