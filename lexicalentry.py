def delete_field(lexical_entry, field_name):
  """
  Deletes a specified field from a lexical entry (dictionary).

  Args:
    lexical_entry: The dictionary representing the lexical entry.
    field_name: The name of the field (key) to delete.
  """
  if field_name in lexical_entry:
    del lexical_entry[field_name]
  else:
    print(f"Warning: Field '{field_name}' not found in lexical entry.")

# Example usage:
my_lexical_entry = {
    "word": "hello",
    "part_of_speech": "noun",
    "definition": "a greeting",
    "synonyms": ["hi", "hey"]
}

print("Before deletion:", my_lexical_entry)

delete_field(my_lexical_entry, "part_of_speech")

print("After deletion:", my_lexical_entry)

delete_field(my_lexical_entry, "example_field") # Example of a non-existent field