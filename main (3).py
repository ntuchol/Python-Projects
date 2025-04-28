def create_form_letter(template_file, data, output_file):
    """
    Creates a form letter by replacing placeholders in a template file with data.

    Args:
        template_file (str): Path to the template file.
        data (dict): Dictionary containing the data to fill in the template.
        output_file (str): Path to save the generated form letter.
    """
    try:
        with open(template_file, 'r') as f:
            template = f.read()
    except FileNotFoundError:
        return "Error: Template file not found."

    try:
        with open(output_file, 'w') as f:
            f.write(template.format(**data))
    except KeyError as e:
         return f"Error: Missing key in data: {e}"
    return "Form letter created successfully!"

if __name__ == "__main__":
    # Example usage
    template = "Dear {name},\n\nThank you for your order of {quantity} {item}(s).\nYour total comes to ${total:.2f}.\n\nSincerely,\nThe Company"
    
    # Save the template to a file
    with open("template.txt", "w") as f:
        f.write(template)

    data = {
        'name': 'John Doe',
        'quantity': 2,
        'item': 'widget',
        'total': 29.98
    }
    
    result = create_form_letter('template.txt', data, 'form_letter.txt')
    print(result)
    
    # Display the content of the created form letter
    with open("form_letter.txt", "r") as f:
        print(f.read())