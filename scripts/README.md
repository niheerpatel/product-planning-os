# Utility Scripts

This directory contains reusable Python scripts for extracting and converting business documents into structured markdown or PDF. These scripts are used by skills and prompts throughout the Product Planning OS, but can also be run directly from the terminal.

## When to Use
- When you need to extract text, tables, images, or speaker notes from PowerPoint, Excel, or PDF files for research or product analysis
- When you want to convert markdown research summaries into styled PDFs
- When preparing source material for further synthesis or AI-driven analysis

## Scripts

| Script                | Purpose                                                      | Usage Example                                  |
|-----------------------|--------------------------------------------------------------|------------------------------------------------|
| `extract_pdf.py`      | Extracts text, tables, and images from PDF to markdown       | `python scripts/extract_pdf.py input.pdf out/`  |
| `extract_pptx.py`     | Extracts slides, notes, images from PowerPoint to markdown   | `python scripts/extract_pptx.py input.pptx out/`|
| `extract_xlsx.py`     | Extracts tables, charts, images from Excel to markdown       | `python scripts/extract_xlsx.py input.xlsx out/`|
| `md_to_pdf.py`        | Converts markdown files to styled PDF                        | `python scripts/md_to_pdf.py file.md file.pdf`  |
| `requirements.txt`    | Python dependencies for all scripts                          | `pip install -r scripts/requirements.txt`       |

## How to Use
1. Install dependencies:
   ```
   pip install -r scripts/requirements.txt
   ```
2. Run the desired script with the appropriate arguments (see table above).
3. Output will be saved in the specified output directory or file.

## Integration
- These scripts are referenced by skills such as `skills/context/document-extraction/SKILL.md`.
- You can use them standalone or as part of a workflow with prompts and agents.

## Platform Notes
- Some scripts (PPTX/Excel chart rendering) require Windows with PowerPoint/Excel installed for full functionality.
- All scripts are compatible with Python 3.8+.
