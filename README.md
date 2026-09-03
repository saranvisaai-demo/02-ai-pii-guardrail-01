# AI PII Guardrail - Presidio Examples

This project demonstrates how to use Microsoft Presidio to detect and anonymize Personally Identifiable Information (PII) in text. Presidio is an open-source library for PII detection and anonymization.

## Files

### ai-agent-pii-test.py
Basic example showing how to:
- Initialize Presidio analyzer and anonymizer engines
- Detect specific PII entities (PERSON, PHONE_NUMBER, CREDIT_CARD)
- Anonymize detected entities by replacing them with placeholders

**Usage:**
```bash
python3 ai-agent-pii-test.py
```

**Example Output:**
```
--- Analysis Results ---
type: PERSON, start: 11, end: 19, score: 0.85
type: PHONE_NUMBER, start: 43, end: 55, score: 0.75
type: CREDIT_CARD, start: 102, end: 118, score: 1.0

--- Anonymized Text ---
My name is ‹PERSON› and my phone number is ‹PHONE_NUMBER›. I live in New York. my Credit card number is ‹CREDIT_CARD›
```

### ai-agent-pii-test-2.py
Advanced example showing how to:
- Analyze text for a specific entity type (PHONE_NUMBER only)
- Analyze text across all default recognizers (EMAIL_ADDRESS, CREDIT_CARD, PERSON, LOCATION, URL, etc.)
- Compare filtered vs comprehensive PII detection

**Usage:**
```bash
python3 ai-agent-pii-test-2.py
```

**Example Output:**
```
PHONE_NUMBER results:
[type: PHONE_NUMBER, start: 48, end: 62, score: 0.4]

All results:
[type: EMAIL_ADDRESS, start: 22, end: 44, score: 1.0,
 type: CREDIT_CARD, start: 77, end: 96, score: 1.0,
 type: PERSON, start: 8, end: 18, score: 0.85,
 type: LOCATION, start: 120, end: 130, score: 0.85,
 type: URL, start: 22, end: 29, score: 0.5,
 type: URL, start: 33, end: 44, score: 0.5,
 type: PHONE_NUMBER, start: 48, end: 62, score: 0.4]
```

## Installation

Install the required dependencies:
```bash
pip install presidio-analyzer presidio-anonymizer
```

## PII Entity Types

Presidio can detect various PII types including:
- PERSON: Names of individuals
- PHONE_NUMBER: Phone numbers
- EMAIL_ADDRESS: Email addresses
- CREDIT_CARD: Credit card numbers
- LOCATION: Addresses and locations
- URL: Web URLs
- And many more (see Presidio documentation for complete list)

## Use Cases

These examples are useful for:
- Building AI guardrails to prevent PII leakage
- Sanitizing logs and user inputs
- Compliance with data protection regulations (GDPR, CCPA, etc.)
- Protecting sensitive information in chat applications
