def create_form_letter(template_file, data, output_file):
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
    template = "Dear {name},\n\nThank you for your order of {quantity} {item}(s).\nYour total comes to ${total:.2f}.\n\nSincerely,\nThe Company"
    
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
    
    with open("form_letter.txt", "r") as f:
        print(f.read())
