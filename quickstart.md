# UberJugaad Enhanced SALT Dataset - Quick Start

## Load and Explore the Data

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load communications
comms = pd.read_parquet('all_communications_master.parquet')
print(f"Total communications: {len(comms):,}")
print(f"Date range: {comms['timestamp'].min()} to {comms['timestamp'].max()}")

# Communication types
print("\nCommunication breakdown:")
print(comms['communication_class'].value_counts())

# Urgency distribution
print("\nUrgency levels:")
print(comms['urgency'].value_counts().sort_index())

# Sentiment analysis
print("\nSentiment distribution:")
print(comms['sentiment'].value_counts())

# Load ERP data
transactions = pd.read_parquet('JoinedTables_train.parquet')
print(f"\nTotal transactions: {len(transactions):,}")

# Load documents
documents = pd.read_parquet('supporting_documents.parquet')
print(f"\nSupporting documents: {len(documents):,}")
print(documents['document_type'].value_counts())
```

## Sample Analysis - Find Urgent Customer Issues

```python
# Find urgent customer communications
urgent_customer = comms[
    (comms['communication_class'] == 'customer') &
    (comms['urgency'] >= 4)
]

print(f"Urgent customer issues: {len(urgent_customer):,}")

# Sample urgent issues
for idx, email in urgent_customer.head(3).iterrows():
    print(f"\nFrom: {email['from_name']}")
    print(f"Subject: {email['subject']}")
    print(f"Urgency: {email['urgency']}")
    print(f"Sentiment: {email['sentiment']}")
    print(f"Preview: {email['body'][:100]}...")
```

## Analyze Communication Patterns

```python
# Communications per day
comms['date'] = pd.to_datetime(comms['timestamp']).dt.date
daily_counts = comms.groupby('date').size()

# Plot communication volume over time
plt.figure(figsize=(12, 4))
daily_counts.plot()
plt.title('Daily Communication Volume')
plt.xlabel('Date')
plt.ylabel('Number of Emails')
plt.show()

# Department communication patterns
dept_comms = comms[comms['department'].notna()]
dept_counts = dept_comms['department'].value_counts()

plt.figure(figsize=(10, 6))
dept_counts.plot(kind='bar')
plt.title('Communications by Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
```

## Link Communications to Transactions

```python
# Example: Find communications about specific orders
sample_order = transactions['SALESDOCUMENT'].iloc[0]
print(f"Looking for communications about order: {sample_order}")

# Search in email bodies (note: this is simplified, real analysis would be more sophisticated)
order_comms = comms[comms['body'].str.contains(str(sample_order), na=False)]
print(f"Found {len(order_comms)} communications mentioning this order")
```
