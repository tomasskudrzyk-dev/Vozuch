import re
data_regex = r"\b\d{1,2}([./-])\d{1,2}\1\d{4}\b"
date_vzor = re.compile(data_regex)

text_texts = [
    "Datum: 30.3.2026 #shoda",
    "Datum: 30/3/2026 #shoda",
    "Datum: 30-3-2026 #shoda"
]

print("\n Příklad - validace dat pomocí zpětného odkazu")
for text in text_texts:
    match = date_vzor.search(text)
    if match:
        print(f"Text: '{text}' - nalezena shoda: '{match.group(1)}'")
    else:
        print(f" '{text}' ")