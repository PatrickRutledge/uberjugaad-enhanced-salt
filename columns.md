# Column Descriptions

## all_communications.parquet (151,673 emails)
- message_id: Unique email identifier
- timestamp: Send datetime (ISO format)
- from: Sender email address
- to: Recipient email address
- from_name: Sender full name
- to_name: Recipient full name
- from_role: Sender job title
- to_role: Recipient job title
- from_company: Sender organization
- subject: Email subject line
- body: Email content text
- customer_id: Links to SOLDTOPARTY in ERP data
- customer_name: Customer company name
- cc: Carbon copy recipients
- triggered_by: Reference to original message (for threads)
- department_from: Sender department
- department_to: Recipient department
- department: Primary department
- vendor: Vendor name (when applicable)

## erp_transactions.parquet (1.9M transactions)
- SALESDOCUMENT: Order number (primary key)
- SOLDTOPARTY: Customer ID
- PRODUCT: 10-digit product code
- PLANT: Manufacturing location
- CREATIONDATE: Order date
- NETAMOUNT: Order value
- CUMULATIVEORDERQUANTITY: Total quantity
- Additional standard SAP fields

## supporting_documents.parquet (3,467 documents)
- document_type: PO/INVOICE/SHIPPING_NOTICE/QUALITY_REPORT/CREDIT_MEMO
- document_id: Unique document identifier
- order_number: Links to SALESDOCUMENT
- customer_id: Links to SOLDTOPARTY
- customer_name: Customer company name
- order_date: Purchase order date
- requested_delivery: Requested delivery date
- product: Product code
- quantity: Order quantity
- unit_price: Price per unit
- total_amount: Total order value
- invoice_number: Invoice identifier
- invoice_date: Invoice issue date
- due_date: Payment due date
- billed_amount: Invoice total
- shipment_number: Shipping identifier
- ship_date: Shipment date
- expected_delivery: Expected arrival
- actual_delivery: Actual arrival
- carrier: Shipping company
- tracking_number: Tracking code
- Additional transaction fields

## business_documents.parquet (32 documents)
- document_type: MEETING_AGENDA/QUALITY_METRICS_REPORT/etc
- document_id: Unique identifier
- created_date: Document creation date
- created_by: Creator email
- title: Document title
- content: Document content (JSON structure)

## Key Relationships
- SALESDOCUMENT links transactions to documents
- customer_id = SOLDTOPARTY across all files
- order_number = SALESDOCUMENT in documents
- All timestamps are synchronized chronologically