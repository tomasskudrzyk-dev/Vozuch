import re

text = "Regulární výraz (zkratky regexp, regex či RE z anglického regular expression) je textový řetězec, který slouží jako vzor pro vyhledávání textu."
regex_slova = r"\w+"
vsechna_slova = re.findall(regex_slova, text)
print(vsechna_slova)

regex_mezery = r"\x20"
vsechny_mezery = re.findall(regex_mezery, text)
print(f"Počet mezer je: {len(vsechny_mezery)}")