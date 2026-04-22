---
name: extract-document
description: "Extract text, tables, and images from PowerPoint (.pptx), Excel (.xlsx), and PDF files into structured markdown. Use when processing research documents, presentations, spreadsheets, or reports for product analysis."
argument-hint: "Path to .pptx, .xlsx, or .pdf file"
---

# Document Extraction

Extract structured content from business documents into markdown format with embedded images.

## When to Use
- Processing PowerPoint presentations (customer decks, internal strategy docs, market research)
- Extracting data from Excel spreadsheets (market data, survey results, financial models)
- Mining PDF reports (analyst reports, whitepapers, research papers)

## Supported Formats
| Format | Script | Extracts |
|--------|--------|----------|
| `.pptx` | [extract_pptx.py](./extract_pptx.py) | Slide text, speaker notes, tables, images |
| `.xlsx` | [extract_xlsx.py](./extract_xlsx.py) | Sheet data as markdown tables, chart titles |
| `.pdf` | [extract_pdf.py](./extract_pdf.py) | Page text, tables, embedded images |

## Procedure

### Step 1: Identify the file
Determine the file type from the extension and confirm the file exists.

### Step 2: Create output directory
Create an output directory next to the source file:
- `<filename>_extracted/` — for markdown output
- `<filename>_extracted/images/` — for extracted images

### Step 3: Run the extraction script
Execute the appropriate Python script via terminal:

**PowerPoint:**
```
python "<skill-path>/extract_pptx.py" "<input-file>" "<output-dir>"
```

**Excel:**
```
python "<skill-path>/extract_xlsx.py" "<input-file>" "<output-dir>"
```

**PDF:**
```
python "<skill-path>/extract_pdf.py" "<input-file>" "<output-dir>"
```

Replace `<skill-path>` with the absolute path to this skill's directory.

### Step 4: Review and refine
1. Read the generated markdown file from the output directory
2. Review the extracted content with the user
3. Use `/extract-insights` to pull structured insights from the extracted content
4. Move relevant findings into the appropriate product files

## Dependencies
Python 3.8+ with packages listed in [requirements.txt](./requirements.txt). Install with:
```
pip install -r "<skill-path>/requirements.txt"
```

## Tips
- For presentations: speaker notes often contain more context than slide text
- For spreadsheets: named ranges and sheet names reveal the document's structure
- For PDFs: page-level extraction preserves document flow better than element-level
- Extracted images are saved at original resolution — use `view_image` to inspect them
---
name: extract-document
description: "Extract text, tables, and images from PowerPoint (.pptx), Excel (.xlsx), and PDF files into structured markdown. Use when processing research documents, presentations, reports, or spreadsheets for product analysis."
argument-hint: "Path to a .pptx, .xlsx, or .pdf file"
---

# Document Extraction

Extracts content from binary document formats (PowerPoint, Excel, PDF) into structured markdown with embedded images.

## When to Use
- Processing research presentations for product insights
- Extracting data from Excel reports
- Converting PDF reports to searchable, quotable markdown
- Preparing source material for analysis with other prompts

## Prerequisites
Python 3.x with required packages. Install via:
```
pip install python-pptx openpyxl PyMuPDF Pillow
```

## Procedure

### 1. Identify File Type
Determine the file extension (.pptx, .xlsx, or .pdf) from the user-provided path.

### 2. Run the Appropriate Script
Execute the extraction script via the terminal:

- **PowerPoint**: `python extract_pptx.py "<input_path>" "<output_dir>"`
- **Excel**: `python extract_xlsx.py "<input_path>" "<output_dir>"`
- **PDF**: `python extract_pdf.py "<input_path>" "<output_dir>"`

Scripts are located in this skill's directory:
- [extract_pptx.py](./extract_pptx.py)
- [extract_xlsx.py](./extract_xlsx.py)
- [extract_pdf.py](./extract_pdf.py)

The `<output_dir>` should be a sibling `processed/` folder next to the source file, or a user-specified location.

### 3. Review Output
The scripts produce:
- A markdown file with extracted text and tables
- An `images/` subfolder with extracted images referenced via `![](./images/...)`

### 4. Post-Processing
After extraction, offer to:
- Run `/extract-insights` on the extracted markdown to pull out key findings
- Run `/organize-research` if this is one of multiple source documents
- Move the output to the appropriate product data location

## Output Structure
```
<output_dir>/
├── <filename>.md          # Extracted content as markdown
└── images/                # Extracted images
    ├── slide1_img1.png
    ├── slide2_img2.png
    └── ...
```
