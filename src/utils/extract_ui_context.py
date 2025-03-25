import os
import json
from bs4 import BeautifulSoup

def extract_ui_context_from_html(file_path):
    """
    Extracts UI elements and metadata from an Angular/HTML template file.
    """
    module_name = os.path.splitext(os.path.basename(file_path))[0]  # Extract module name from filename
    context = {
        "module": module_name,
        "ui_elements": []
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')

            # Extract input fields
            for input_tag in soup.find_all('input'):
                name = input_tag.get('name', 'unknown_field')
                element = {
                    "name": f"{name}_field",
                    "selector": f"//*[@id='{input_tag.get('id', name)}']" if input_tag.get('id') else f"//input[@name='{name}']",
                    "type": "input",
                    "placeholder": input_tag.get('placeholder', ''),
                    "required": "required" in input_tag.attrs
                }
                context["ui_elements"].append(element)

            # Extract buttons
            for button_tag in soup.find_all('button'):
                element = {
                    "name": button_tag.get_text(strip=True).lower().replace(" ", "_") + "_button",
                    "selector": f"//button[@type='{button_tag.get('type', 'button')}']",
                    "type": "button",
                    "text": button_tag.get_text(strip=True)
                }
                context["ui_elements"].append(element)

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

    return context

def generate_ui_context(directory):
    """
    Recursively parses all HTML templates in the given directory and generates UI context for each.
    """
    ui_contexts = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                ui_context = extract_ui_context_from_html(file_path)
                ui_contexts[file] = ui_context  # Store UI context using the file name

    return ui_contexts

def generate_test_cases(ui_context):
    """
    Adds test cases for UI elements.
    """
    test_cases = [
        {
            "scenario": "Valid Registration",
            "username": "validuser",
            "password": "validpassword",
            "expected": "Registration successful"
        },
        {
            "scenario": "Invalid Registration - Missing Username",
            "username": "",
            "password": "validpassword",
            "expected": "Username is required"
        },
        {
            "scenario": "Invalid Registration - Missing Password",
            "username": "validuser",
            "password": "",
            "expected": "Password is required"
        }
    ]
    ui_context["test_cases"] = test_cases
    return ui_context

if __name__ == "__main__":
    # If running standalone, process all HTML files and save their UI context
    templates_directory = "aiservice-ui/src/app"  # Update this path as needed
    ui_contexts = generate_ui_context(templates_directory)

    # Save each UI context separately
    output_dir = "src/context/ui_contexts"
    os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

    for file_name, context in ui_contexts.items():
        context_with_tests = generate_test_cases(context)
        output_file = os.path.join(output_dir, f"{context['module']}_ui_context.json")

        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(context_with_tests, json_file, indent=4)

        print(f"Saved UI context: {output_file}")

