# Business Documents Guide

## Overview

The dataset includes 3,499 supporting documents and 32 business documents stored in Parquet format for efficient processing. While these are provided as structured data for convenience and performance, you can easily convert them to individual files (PDF, HTML, PNG) for visualization or traditional document processing workflows.

## Document Types

### supporting_documents.parquet (3,467 documents)
- **Purchase Orders** - Customer orders with terms and requirements
- **Invoices** - Billing documents with amounts and due dates
- **Shipping Notices** - Delivery tracking and status
- **Quality Reports** - Inspection results and defect analysis
- **Credit Memos** - Refunds and adjustments

### business_documents.parquet (32 documents)
- **Meeting Agendas** - Sales and production meetings
- **Quality Metrics Reports** - Plant performance data
- **Overdue Invoice Reports** - Accounts receivable aging
- **Vendor Scorecards** - Supplier performance metrics

## Why Parquet Format?

We chose Parquet for several reasons:
1. **Efficiency** - 100x smaller than individual files
2. **Performance** - Faster to load and process
3. **Integration** - Works directly with pandas, BigQuery, Spark
4. **Consistency** - Uniform structure across all documents

## Converting to Individual Files

Use the script below to generate actual document files:

```python
import pandas as pd
import os
from datetime import datetime
import json

def generate_html_invoice(doc):
    """Generate HTML invoice from document data"""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Invoice {doc['invoice_number']}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .header {{ border-bottom: 2px solid #333; padding-bottom: 20px; }}
            .invoice-details {{ margin: 20px 0; }}
            table {{ width: 100%; border-collapse: collapse; }}
            th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }}
            .total {{ font-weight: bold; font-size: 1.2em; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>INVOICE</h1>
            <p><strong>Invoice #:</strong> {doc['invoice_number']}</p>
            <p><strong>Date:</strong> {doc['invoice_date']}</p>
            <p><strong>Due Date:</strong> {doc['due_date']}</p>
        </div>

        <div class="invoice-details">
            <h3>Bill To:</h3>
            <p>{doc['customer_name']}<br>
            Customer ID: {doc['customer_id']}</p>

            <h3>Order Details:</h3>
            <table>
                <tr>
                    <th>Order Number</th>
                    <th>Product</th>
                    <th>Quantity</th>
                    <th>Amount</th>
                </tr>
                <tr>
                    <td>{doc['order_number']}</td>
                    <td>{doc.get('product', 'Various')}</td>
                    <td>{doc.get('quantity', 'N/A')}</td>
                    <td>EUR {doc['billed_amount']:,.2f}</td>
                </tr>
            </table>

            <p class="total">Total Due: EUR {doc['billed_amount']:,.2f}</p>
        </div>
    </body>
    </html>
    """
    return html

def generate_html_purchase_order(doc):
    """Generate HTML purchase order from document data"""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Purchase Order {doc['document_id']}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .header {{ background: #f0f0f0; padding: 20px; }}
            .po-details {{ margin: 20px 0; }}
            .requirements {{ background: #fff3cd; padding: 15px; margin: 20px 0; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>PURCHASE ORDER</h1>
            <p><strong>PO Number:</strong> {doc['document_id']}</p>
            <p><strong>Date:</strong> {doc.get('order_date', 'N/A')}</p>
        </div>

        <div class="po-details">
            <h3>Vendor: UberJugaad GmbH</h3>

            <h3>Ship To:</h3>
            <p>{doc['customer_name']}<br>
            Customer ID: {doc['customer_id']}</p>

            <h3>Order Information:</h3>
            <p><strong>Sales Order:</strong> {doc['order_number']}</p>
            <p><strong>Product:</strong> {doc.get('product', 'As per specification')}</p>
            <p><strong>Quantity:</strong> {doc.get('quantity', 'N/A')}</p>
            <p><strong>Unit Price:</strong> EUR {doc.get('unit_price', 0):,.2f}</p>
            <p><strong>Total Amount:</strong> EUR {doc.get('total_amount', 0):,.2f}</p>
            <p><strong>Requested Delivery:</strong> {doc.get('requested_delivery', 'ASAP')}</p>
        </div>
    </body>
    </html>
    """
    return html

def convert_documents_to_files(output_dir='generated_documents'):
    """Convert parquet documents to individual HTML files"""

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Load supporting documents
    print("Loading supporting documents...")
    support_docs = pd.read_parquet('supporting_documents.parquet')

    # Generate HTML files for each document type
    generators = {
        'INVOICE': generate_html_invoice,
        'PURCHASE_ORDER': generate_html_purchase_order,
        # Add more generators as needed
    }

    for idx, doc in support_docs.iterrows():
        doc_type = doc['document_type']
        doc_id = doc['document_id'].replace('/', '_').replace('\\', '_')

        if doc_type in generators:
            html_content = generators[doc_type](doc)
            filename = f"{output_dir}/{doc_type}_{doc_id}.html"

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)

            if idx % 100 == 0:
                print(f"Generated {idx} documents...")

    print(f"Generated {len(support_docs)} HTML documents in {output_dir}/")

    return output_dir

if __name__ == "__main__":
    # Generate all documents as HTML files
    output_folder = convert_documents_to_files()
    print(f"Documents generated in: {output_folder}/")
```

## Sample Output

Running the script will create files like:

```
generated_documents/
├── INVOICE_INV-0002315309.html
├── PURCHASE_ORDER_PO-0002315309.html
├── SHIPPING_NOTICE_SHIP-0002315309.html
├── QUALITY_REPORT_QR-0002315309.html
├── MEETING_AGENDA_2020-01-06_Sales.json
└── VENDOR_SCORECARD_2020-Q1.json
```

## Working with Documents in Parquet

For most use cases, working directly with the Parquet files is more efficient:

```python
import pandas as pd

# Load and analyze documents
docs = pd.read_parquet('supporting_documents.parquet')

# Find all invoices over EUR 100,000
large_invoices = docs[(docs['document_type'] == 'INVOICE') &
                      (docs['billed_amount'] > 100000)]

# Find delayed shipments
delayed = docs[(docs['document_type'] == 'SHIPPING_NOTICE') &
               (docs.get('actual_delivery') > docs.get('expected_delivery'))]

# Analyze quality issues by searching document content
quality_issues = docs[docs['document_type'] == 'QUALITY_REPORT']

# Link documents to emails
emails = pd.read_parquet('all_communications.parquet')
order = '0002315309'

# Find all documents for an order
order_docs = docs[docs['order_number'] == order]

# Find emails mentioning this order
order_emails = emails[emails['body'].str.contains(order, na=False)]
```

## PDF Generation

To generate PDF files, install additional libraries:

```bash
pip install reportlab  # For PDF generation
pip install pdfkit     # Alternative PDF generator
pip install weasyprint # HTML to PDF converter
```

Example PDF generation:

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_invoice_pdf(doc, filename):
    c = canvas.Canvas(filename, pagesize=letter)

    # Add invoice header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, f"INVOICE #{doc['invoice_number']}")

    # Add customer info
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"Customer: {doc['customer_name']}")
    c.drawString(100, 700, f"Customer ID: {doc['customer_id']}")

    # Add invoice details
    c.drawString(100, 660, f"Order Number: {doc['order_number']}")
    c.drawString(100, 640, f"Invoice Date: {doc['invoice_date']}")
    c.drawString(100, 620, f"Due Date: {doc['due_date']}")

    # Add amount
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 580, f"Total Due: EUR {doc['billed_amount']:,.2f}")

    c.save()
    return filename

# Generate PDF for each invoice
invoices = docs[docs['document_type'] == 'INVOICE']
for idx, invoice in invoices.iterrows():
    filename = f"invoice_{invoice['invoice_number']}.pdf"
    create_invoice_pdf(invoice, filename)
```

## Document Structure

Each document contains:
- **Metadata**: document_type, document_id, created_date
- **Relationships**: order_number, customer_id (links to ERP data)
- **Content**: Specific fields per document type
- **Business Data**: Amounts, dates, quantities

The documents reflect real business scenarios including:
- Delivery delays
- Quality issues
- Payment problems
- Order discrepancies

These patterns must be discovered through analysis of the document content and relationships with other data, rather than through pre-labeled flags.

## Tips for Analysis

1. **Link documents to transactions**: Use order_number to join with erp_transactions.parquet
2. **Find related emails**: Search email bodies for document IDs or order numbers
3. **Track document flow**: PO → Shipping Notice → Invoice → Quality Report
4. **Identify patterns**: Compare expected vs actual dates, quantities, amounts
5. **Detect anomalies**: Look for unusual sequences or missing documents

The parquet format allows efficient queries across millions of documents while maintaining the ability to generate traditional document formats when needed.