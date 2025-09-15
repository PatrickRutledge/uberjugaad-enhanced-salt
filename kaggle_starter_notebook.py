"""
UberJugaad Enhanced SALT Dataset - Starter Notebook
====================================================
Explore 151,673 business communications with ERP data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import warnings
warnings.filterwarnings('ignore')

# Setup
plt.style.use('seaborn-v0_8-darkgrid')
pd.set_option('display.max_columns', None)

print("=" * 80)
print("UBERJUGAAD ENHANCED SALT DATASET EXPLORATION")
print("=" * 80)

# Load the master communications file
print("\n1. Loading Communications Data...")
comms = pd.read_parquet('/kaggle/input/uberjugaad-enhanced-salt/all_communications_master.parquet')
print(f"✓ Loaded {len(comms):,} communications")

# Basic statistics
print("\n2. Dataset Overview")
print("-" * 40)
print(f"Date Range: {comms['timestamp'].min()} to {comms['timestamp'].max()}")
print(f"Unique Senders: {comms['from'].nunique():,}")
print(f"Unique Recipients: {comms['to'].nunique():,}")

# Communication types
print("\n3. Communication Breakdown")
print("-" * 40)
comm_types = comms['communication_class'].value_counts()
for comm_type, count in comm_types.items():
    print(f"{comm_type:20s}: {count:7,} ({count/len(comms)*100:5.1f}%)")

# Urgency Analysis
print("\n4. Urgency Distribution")
print("-" * 40)
urgency_dist = comms['urgency'].value_counts().sort_index()
for level, count in urgency_dist.items():
    bars = "█" * int(count/len(comms)*100)
    print(f"Level {level}: {count:7,} {bars}")

# Sentiment Analysis
print("\n5. Sentiment Analysis")
print("-" * 40)
sentiment_dist = comms['sentiment'].value_counts()
for sentiment, count in sentiment_dist.head(10).items():
    print(f"{sentiment:15s}: {count:7,}")

# Visualizations
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 1. Communications over time
comms['date'] = pd.to_datetime(comms['timestamp']).dt.date
daily_counts = comms.groupby('date').size()
axes[0,0].plot(daily_counts.index, daily_counts.values)
axes[0,0].set_title('Daily Communication Volume')
axes[0,0].set_xlabel('Date')
axes[0,0].set_ylabel('Count')
axes[0,0].tick_params(axis='x', rotation=45)

# 2. Communication types pie chart
comm_types.plot(kind='pie', ax=axes[0,1], autopct='%1.1f%%')
axes[0,1].set_title('Communication Types Distribution')
axes[0,1].set_ylabel('')

# 3. Urgency distribution
urgency_dist.plot(kind='bar', ax=axes[1,0], color='coral')
axes[1,0].set_title('Urgency Level Distribution')
axes[1,0].set_xlabel('Urgency Level')
axes[1,0].set_ylabel('Count')

# 4. Top communication patterns
if 'communication_type' in comms.columns:
    top_types = comms['communication_type'].value_counts().head(10)
    top_types.plot(kind='barh', ax=axes[1,1])
    axes[1,1].set_title('Top 10 Communication Types')
    axes[1,1].set_xlabel('Count')

plt.tight_layout()
plt.show()

# Find interesting patterns
print("\n6. Interesting Patterns")
print("-" * 40)

# Urgent customer issues
urgent_customer = comms[(comms['communication_class'] == 'customer') & (comms['urgency'] >= 4)]
print(f"Urgent customer issues: {len(urgent_customer):,}")

# Spam percentage
spam_pct = len(comms[comms['communication_class'] == 'spam']) / len(comms) * 100
print(f"Spam percentage: {spam_pct:.1f}%")

# Response patterns (where applicable)
if 'communication_type' in comms.columns:
    requests = comms[comms['communication_type'].str.contains('request', na=False)]
    responses = comms[comms['communication_type'].str.contains('response', na=False)]
    if len(requests) > 0:
        response_rate = len(responses) / len(requests) * 100
        print(f"Response rate to requests: {response_rate:.1f}%")

# Word Cloud from email subjects
print("\n7. Generating Word Cloud from Email Subjects...")
subjects = ' '.join(comms['subject'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(subjects)

plt.figure(figsize=(15, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Common Words in Email Subjects')
plt.show()

# Load ERP data
print("\n8. Loading ERP Transaction Data...")
transactions = pd.read_parquet('/kaggle/input/uberjugaad-enhanced-salt/JoinedTables_train.parquet')
print(f"✓ Loaded {len(transactions):,} transactions")

# Transaction statistics
print("\n9. Transaction Overview")
print("-" * 40)
print(f"Unique Customers: {transactions['SOLDTOPARTY'].nunique():,}")
print(f"Unique Products: {transactions['PRODUCT'].nunique():,}")
print(f"Sales Documents: {transactions['SALESDOCUMENT'].nunique():,}")

# Sample of urgent communications
print("\n10. Sample Urgent Communications")
print("-" * 40)
for idx, email in urgent_customer.head(3).iterrows():
    print(f"\nFrom: {email['from_name']}")
    print(f"Subject: {email['subject']}")
    print(f"Urgency: {email['urgency']}")
    print(f"Preview: {email['body'][:100]}...")
    print("-" * 40)

print("\n" + "=" * 80)
print("EXPLORATION COMPLETE!")
print("Ready for deeper analysis: sentiment trends, churn prediction, anomaly detection...")
print("=" * 80)