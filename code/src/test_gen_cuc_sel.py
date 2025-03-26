import os
import json

from ai_agent.test_case_generator import TestCaseGenerator


# Define directories
ui_context_dir = "src/context/ui_contexts"
features_dir = "src/features"
tests_dir = "src/tests"

GENAI_API_KEY = "xXXXXX"

# Create directories if they don't exist
os.makedirs(features_dir, exist_ok=True)
os.makedirs(tests_dir, exist_ok=True)

# Load all JSON UI contexts
ui_contexts = {}
for file_name in os.listdir(ui_context_dir):
    if file_name.endswith("_ui_context.json"):
        file_path = os.path.join(ui_context_dir, file_name)
        with open(file_path, 'r', encoding='utf-8') as json_file:
            ui_contexts[file_name] = json.load(json_file)

# Initialize the TestCaseGenerator
generator = TestCaseGenerator(genai_api_key=GENAI_API_KEY)

# Scenarios for different UI components
scenarios = {
    "app.component_ui_context.json": "Ensure the main app component loads correctly without errors.",
    "login.component_ui_context.json": "Validate the login functionality for valid and invalid user credentials.",
    "logout.component_ui_context.json": "Verify that the logout functionality works correctly.",
    "register.component_ui_context.json": "Validate the registration functionality for valid and invalid inputs."
}

# Generate Cucumber and Selenium test cases
for file_name, context in ui_contexts.items():
    module_name = context["module"]
    scenario = scenarios.get(file_name, "General UI testing scenario.")

    # Generate Cucumber feature file
    cucumber_feature = generator.generate_cucumber_feature(scenario, context)
    feature_file_path = os.path.join(features_dir, f"{module_name}.feature")
    with open(feature_file_path, 'w', encoding='utf-8') as feature_file:
        feature_file.write(cucumber_feature)
    print(f"Saved Cucumber feature file: {feature_file_path}")

    # Generate Selenium test script
    selenium_script = generator.generate_selenium_test(scenario, context)
    test_file_path = os.path.join(tests_dir, f"test_{module_name}.py")
    with open(test_file_path, 'w', encoding='utf-8') as test_file:
        test_file.write(selenium_script)
    print(f"Saved Selenium test script: {test_file_path}")
