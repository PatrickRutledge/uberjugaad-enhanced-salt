# Data Provenance

## Sources

### Original Data Foundation
The foundation of this dataset is SAP's SALT (Synthetic Anonymized Sales Transactions) dataset, originally created by SAP for testing and demonstration purposes. SALT contains 1.9 million synthetic B2B transactions from a German industrial supplier, designed to mirror real SAP ERP system patterns without exposing actual business data.

**SALT Dataset Characteristics:**
- 1.9 million sales transactions (2019-2020)
- 15,606 unique customers
- 243,717 sales document headers
- 1.9 million sales line items
- Realistic business patterns: seasonality, customer distribution, product hierarchies
- Generated from actual SAP ERP schemas and business rules
- Follows typical B2B industrial supplier operations
- Customer distribution follows realistic Pareto principle (80/20 rule)

### Enhancement Data Sources
The enhanced components were synthetically generated based on:
- Analysis of transaction patterns in the original SALT data
- Common enterprise communication patterns
- Typical B2B business scenarios
- Real-world email volume ratios (28% spam rate based on enterprise studies)
- Standard business document workflows (PO → Shipping → Invoice → Quality)

## Collection Methodology

### Phase 1: Transaction Analysis and Pattern Detection
**Automated Analysis Process:**
- Python scripts analyzed 1.9M transactions to identify behavioral patterns
- Clustering algorithms grouped customers by order frequency, amounts, and timing
- Time series analysis identified seasonal patterns and anomalies
- Statistical analysis determined realistic email-to-transaction ratios
- Identified 50+ business patterns including:
  - Customer churn indicators
  - Payment risk signals
  - Quality issues
  - Operational bottlenecks
  - Seasonal variations

**Pattern Classification System:**
- Behavioral patterns (declining_giant, growth_star, occasional_buyer)
- Business health patterns (payment_risk, quality_issues, supply_chain_stress)
- SAP operational patterns (order_modifications, delivery_delays, pricing_disputes)
- Seasonal patterns (year_end_rush, summer_slowdown, quarter_panic)

### Phase 2: Customer and Contact Generation
**Customer Classification:**
- Analyzed all 15,606 customers from SALT
- Classified by size tiers based on revenue (ENTERPRISE, LARGE, MEDIUM, SMALL, MICRO)
- Assigned personas (DISTRIBUTOR, MANUFACTURER, DEALER, SERVICE_COMPANY, SMALL_BUSINESS, OCCASIONAL)
- Generated 40,190 customer contacts with role-based assignments
- Created 1,467 internal UberJugaad GmbH employees across departments

**Contact Generation Rules:**
- Large customers: 5-10 contacts (executives, purchasing, operations)
- Medium customers: 3-5 contacts (management, purchasing)
- Small customers: 1-3 contacts (owner, purchasing)
- Internal structure: Sales (450), Operations (320), Finance (200), IT (150), HR (100), others

### Phase 3: Email Communication Generation
**Template-Based Generation Pipeline:**
- Created 500+ subject line templates
- Developed 1,000+ body paragraph combinations
- Each email triggered by specific transaction events:
  - Large orders (>€100K) → account manager follow-ups
  - Delayed deliveries → customer complaints
  - Payment delays → AR reminders
  - Quality issues → escalation chains

**Email Volume Distribution:**
- Customer communications: 55,425 (36.5%)
- Regular business: 37,285 (24.6%)
- Spam/vendor: 42,246 (27.9%)
- IT/HR/Compliance: 15,593 (10.3%)
- Internal escalations: 1,124 (0.7%)

**Natural Language Variations:**
- Realistic typos and formatting inconsistencies
- Variable tone based on context (urgent, frustrated, professional)
- Email threading with triggered_by references
- Timestamps synchronized with transaction dates

### Phase 4: Document Synthesis
**Document Generation Workflow:**
- Documents generated deterministically from transactions
- Each significant order → Purchase Order document
- Each shipment → Shipping Notice
- Each billing → Invoice
- Random subset (3%) → Quality Reports
- Special cases → Credit Memos

**Document Field Population:**
- Fields pulled directly from ERP data ensuring consistency
- Status flags and delays calculated from date comparisons
- Problem indicators embedded based on pattern analysis
- All documents linked via SALESDOCUMENT numbers

### Phase 5: Spam and Noise Injection
**Realistic Inbox Simulation:**
- 28% spam rate based on real enterprise inbox studies
- Vendor parodies with intentional misspellings:
  - eye-BM (IBM parody)
  - Orackle (Oracle parody)
  - SAPP (SAP parody)
  - Mikerosoft (Microsoft parody)
- Temporal distribution follows real spam patterns
- Content generated from actual B2B spam templates

### Phase 6: Database Assembly
**SQLite Email Database Creation:**
- Consolidated 151,673 emails into Exchange-style database
- Extracted 18,819 unique contacts
- Created folder hierarchy (Inbox, Sent, Archive, etc.)
- Added metadata simulating Exchange Server 2019
- Built indexes for efficient querying

### Phase 7: Data Cleaning for Discovery
**Pattern Obfuscation:**
- Removed all columns revealing patterns (sentiment, urgency, classifications)
- Kept only factual business data
- Ensured patterns must be discovered through analysis
- Validated all cross-references and relationships
- Removed any pre-labeled training data

### Technical Implementation
**Tools and Technologies:**
- Python 3.11 with pandas, numpy, faker libraries
- SQLite for database creation
- Parquet format for efficient storage
- Git for version control
- Random seed (42) for reproducibility where applicable

**Quality Assurance:**
- Automated validation of all foreign keys
- Statistical tests for realistic distributions
- Manual review of 1,000 sample emails
- Verification that patterns are discoverable but not labeled
- Cross-validation of dates and amounts

**Computational Resources:**
- 2 weeks of development and generation
- 100+ hours of compute time
- Multiple iterations for realism validation
- Final dataset: ~160 MB compressed

## Citations

### Enhanced Dataset Repository
**GitHub Repository**
- URL: https://github.com/PatrickRutledge/uberjugaad-enhanced-salt
- Author: Patrick Rutledge
- Year: 2025
- License: MIT (for enhancements)

### Original SALT Dataset Sources

**SAP Official Repository**
- URL: https://github.com/SAP-samples/salt
- Organization: SAP SE
- License: SAP Sample Code License
- Purpose: Official SAP samples repository

**Hugging Face Dataset**
- URL: https://huggingface.co/datasets/SAP/SALT
- Organization: SAP
- Format: Parquet files
- Access: Public dataset hub

**Academic Publication**
```bibtex
@inproceedings{klein2024salt,
  title={{SALT}: Sales Autocompletion Linked Business Tables Dataset},
  author={Tassilo Klein and Clemens Biehl and Margarida Costa and Andre Sres and Jonas Kolk and Johannes Hoffart},
  booktitle={NeurIPS 2024 Third Table Representation Learning Workshop},
  year={2024},
  url={https://openreview.net/forum?id=UZbELpkWIr}
}
```

### Usage Attribution
When using this dataset, please cite both:
1. The enhanced dataset (Rutledge, 2025)
2. The original SALT dataset (Klein et al., 2024)

The original SALT authors are not affiliated with the enhancements in this repository. All synthetic communications, documents, and embedded patterns were added independently to create a comprehensive enterprise dataset for AI/ML applications.

### Ethical Considerations
- All data is synthetic - no real company or personal information
- Email addresses use fictional @uberjugaad.com domain
- Customer names are anonymized IDs from original SALT
- Safe for public use and model training
- No sensitive or private information included

### Reproducibility Note
While the exact dataset cannot be regenerated due to random elements in the generation process, the methodology documented here allows for similar datasets to be created following the same approach:
1. Start with SAP SALT dataset from official sources
2. Apply pattern detection algorithms to identify business behaviors
3. Generate communications using transaction-based triggers
4. Create documents matching transaction data
5. Build contact database from communication participants
6. Inject realistic noise and spam
7. Remove all revealing labels for discovery-oriented learning