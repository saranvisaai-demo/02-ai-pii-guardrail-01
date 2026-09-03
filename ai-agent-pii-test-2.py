from presidio_analyzer import AnalyzerEngine, PatternRecognizer
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
import json
from pprint import pprint

text_to_anonymize = """
Contact John Smith at john.smith@example.com or (415) 555-0132.
Credit card: 4111 1111 1111 1111
Address: 1 Hacker Way, Menlo Park, CA
""".strip()

analyzer = AnalyzerEngine()
# Narrow analysis to a single entity type\n
phone_results = analyzer.analyze(text=text_to_anonymize, entities=["PHONE_NUMBER"], language="en")
print("PHONE_NUMBER results:")
pprint(phone_results)
# Or analyze across default recognizers\n
all_results = analyzer.analyze(text=text_to_anonymize, language="en")
print("All results:")
pprint(all_results)
