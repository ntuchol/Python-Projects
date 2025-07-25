import re

class BibTeXParser:
    def __init__(self, bibtex_string):
        self.bibtex_string = bibtex_string
        self.parsed_data = {}

    def parse(self):
        entry_pattern = r"@book\{([^,]+),\s*(.+)\}"
        match = re.match(entry_pattern, self.bibtex_string, re.DOTALL)
        if not match:
            raise ValueError("Invalid BibTeX format")

        key = match.group(1).strip()
        fields = match.group(2).strip()

        field_pattern = r"(\w+)\s*=\s*\{([^{}]+)\}"
        fields_dict = dict(re.findall(field_pattern, fields))

        self.parsed_data = {"key": key, "fields": fields_dict}
        return self.parsed_data

bibtex_entry = """
@book{exampleKey,
    author = {John Doe},
    title = {Example Book Title},
    year = {2025},
    publisher = {Example Publisher}
}
"""

parser = BibTeXParser(bibtex_entry)
parsed_data = parser.parse()
print(parsed_data)
