from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# 1. Initialize the engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# 2. Define your target text
text_to_scrub = "My name is John Doe and my phone number is 212-555-0199. I live in New York. my Credit card number is 1111222233334444"

# 3. Analyze the text to find PII
analysis_results = analyzer.analyze(
    text=text_to_scrub,
    entities=["PERSON", "PHONE_NUMBER", "CREDIT_CARD"], # Specify entities to look for (or omit to search for all)
    language="en"
)

print("--- Analysis Results ---")
for result in analysis_results:
    print(result)

# 4. Anonymize the detected entities
anonymized_result = anonymizer.anonymize(
    text=text_to_scrub,
    analyzer_results=analysis_results
)

print("\n--- Anonymized Text ---")
print(anonymized_result.text)
