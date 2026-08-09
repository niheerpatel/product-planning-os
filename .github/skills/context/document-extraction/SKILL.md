---
name: document-extraction
description: "Extract text, tables, and images from business documents into structured markdown for research and decision-making."
argument-hint: "Path to a .pptx, .xlsx, or .pdf file"
---

# Document Extraction

Extract structured content from PowerPoint, Excel, and PDF files into markdown.

## When to Use
- Processing market research decks or customer presentations
- Converting Excel analysis into tables for review
- Pulling text and images from PDFs for synthesis

## Procedure

### Step 1: Identify the file type
Confirm the file extension is one of: `.pptx`, `.xlsx`, `.pdf`.

### Step 2: Choose the extraction method
- PowerPoint: extract slides, speaker notes, tables, images
- Excel: convert sheets and named ranges to markdown tables
- PDF: preserve page flow, page text, and tables

### Step 3: Run extraction
Use the appropriate script in this repository or your local tools.

### Step 4: Review output
- Confirm the extracted markdown captures key insights
- Use `/extract-insights` or other synthesis prompts to summarize findings
- Move relevant content into product context or discovery artifacts

## Output
- Markdown file with extracted text and tables
- Image files for embedded visuals
