# UberJugaad Enhanced SALT Dataset

## Overview
This dataset combines SAP's SALT (simulated S/4HANA ERP data) with comprehensive business communications and documents, creating a realistic enterprise ecosystem for AI/ML applications.

## Dataset Statistics

### Company Profile
- **Company**: UberJugaad GmbH
- **Industry**: Industrial Equipment & Supplies
- **Headquarters**: Frankfurt, Germany
- **Employees**: 1,467 across 7 departments
- **Annual Revenue**: €14.8 Billion
- **Operating Plants**: 3 manufacturing facilities

### Employee Distribution
- Sales: 292 employees
- Customer Service: 238 employees
- Operations: 215 employees
- Finance: 183 employees
- Procurement: 146 employees
- IT: 131 employees
- HR: 108 employees
- Executive Leadership: 154 employees

### Customer Base
- **Total Customers**: 15,606
- **Customer Segments**:
  - Enterprise: 1,124 customers
  - Large: 2,341 customers
  - Medium: 4,682 customers
  - Small: 5,463 customers
  - Micro: 1,996 customers

### Transactional Data
- **Time Period**: January 2019 - December 2020 (24 months)
- **Total Transactions**: 1.9 million sales records
- **Product Catalog**: 10-digit product codes
- **Plants**: 3 primary manufacturing locations
- **Order Volume**: Ranging from single units to 10,000+ unit orders

## Communication Dataset

### Volume
- **Total Communications**: 151,673 business emails
- **Time Span**: Full year 2020 with historical references

### Communication Types
| Type | Count | Description |
|------|-------|-------------|
| Customer Communications | 55,425 | B2B customer interactions, inquiries, complaints |
| Regular Business | 37,285 | Daily operations, sales, finance, procurement |
| Spam/Noise | 42,246 | Realistic inbox noise, vendor solicitations |
| Organizational | 15,593 | IT support, HR, compliance, training |
| Internal Escalations | 1,124 | Cross-department issue handling |

### Communication Characteristics
- **Languages**: English (business standard)
- **Urgency Levels**: 1-5 scale (routine to critical)
- **Sentiment Range**: Positive, neutral, negative, urgent, final
- **Departments Involved**: All 7 departments
- **Response Patterns**: Includes non-responses, delays, escalations

## Supporting Documents

### Document Types
- Purchase Orders matching ERP transactions
- Invoices with payment terms and disputes
- Quality Reports documenting defects
- Shipping Notices with delivery confirmations
- Credit Memos for returns/adjustments
- Meeting Agendas and minutes
- Vendor Scorecards
- Compliance Reports

### Document Statistics
- **Total Documents**: 3,499
- **Document Categories**: 8 types
- **Linked Transactions**: Documents reference actual ERP order numbers
- **Problem Indicators**: Various flags indicating business issues

## Data Schema

### ERP Tables (Original SALT)
- `JoinedTables_train.parquet` - Main transactional data
- `I_SalesDocument_train.parquet` - Sales document headers
- `I_SalesDocumentItem_train.parquet` - Sales line items

### Communication Schema
```python
{
  'message_id': 'unique identifier',
  'timestamp': 'ISO datetime',
  'from': 'sender email',
  'from_name': 'sender name',
  'to': 'recipient email',
  'to_name': 'recipient name',
  'subject': 'email subject',
  'body': 'email content',
  'sentiment': 'emotional tone',
  'urgency': 'priority level (1-5)',
  'communication_type': 'classification',
  'communication_class': 'major category'
}
```

### Document Schema
```python
{
  'document_type': 'document classification',
  'document_id': 'unique identifier',
  'order_number': 'linked ERP transaction',
  'customer_id': 'customer reference',
  'created_date': 'document date',
  'status_flags': 'problem indicators',
  'content': 'document details'
}
```

## Use Cases

### Business Intelligence
- Customer behavior analysis
- Communication pattern detection
- Sentiment trend analysis
- Operational efficiency metrics

### Machine Learning Applications
- Email classification and routing
- Customer churn prediction
- Sentiment analysis
- Document information extraction
- Anomaly detection
- Time series forecasting

### Natural Language Processing
- Named entity recognition
- Email summarization
- Intent classification
- Response generation
- Topic modeling

### Process Mining
- Communication flow analysis
- Response time optimization
- Escalation pattern detection
- Compliance monitoring

## Files Included

| File | Size | Description |
|------|------|-------------|
| `all_communications_master.parquet` | 7.5 MB | Combined all communications |
| `customer_communications_final.parquet` | 2.3 MB | Customer emails |
| `expanded_regular_business_communications.parquet` | 2.2 MB | Daily business emails |
| `expanded_organizational_communications.parquet` | 800 KB | IT/HR/Compliance |
| `spam_communications.parquet` | 1.4 MB | Noise/spam emails |
| `internal_communications.parquet` | 85 KB | Internal escalations |
| `supporting_documents.parquet` | 163 KB | Business documents |
| `regular_business_documents.parquet` | 23 KB | Meeting/report documents |
| `JoinedTables_train.parquet` | 42.8 MB | Main ERP transactions |
| `I_SalesDocument_train.parquet` | 7.5 MB | Sales headers |
| `I_SalesDocumentItem_train.parquet` | 29.8 MB | Sales line items |

## Getting Started

```python
import pandas as pd

# Load all communications
comms = pd.read_parquet('all_communications_master.parquet')
print(f"Total communications: {len(comms):,}")

# Load ERP transactions
transactions = pd.read_parquet('JoinedTables_train.parquet')
print(f"Total transactions: {len(transactions):,}")

# Analyze sentiment distribution
print(comms['sentiment'].value_counts())

# Find urgent communications
urgent = comms[comms['urgency'] >= 4]
print(f"Urgent communications: {len(urgent):,}")
```

## Data Quality Notes

- All PII has been simulated/generated
- Email addresses follow consistent domain patterns
- Timestamps are realistic and chronological
- Document references link to actual transaction IDs
- Communication threads maintain context
- Realistic response rates (~65-80% for required actions)

## Ethical Considerations

This is simulated data created for educational and research purposes. No real company data or personal information is included. The dataset demonstrates realistic business operations without exposing actual business intelligence.

## License

- Original SALT Dataset: SAP License
- Enhanced Communications: MIT License
- Generated Documents: MIT License

## Citation

If you use this dataset, please cite:
```
@dataset{uberjugaad_salt_2024,
  title={UberJugaad Enhanced SALT Dataset},
  author={Patrick Rutledge},
  year={2024},
  publisher={GitHub},
  url={https://github.com/PatrickRutledge/BigQuery-AI}
}
```

## Contact

For questions or issues: [Create an issue on GitHub](https://github.com/PatrickRutledge/BigQuery-AI/issues)

## Acknowledgments

- SAP for the original SALT dataset
- The open-source community for data processing tools
- Anthropic's Claude for assistance in data generation