import openai

class TestCaseGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_test_case(self, scenario):
        try:
            # Simulate API call to OpenAI
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"Generate test cases for the following scenario: {scenario}",
                max_tokens=100
            )
            return response.choices[0].text.strip()
        except openai.OpenAIError as e:  # Correct exception handling
            print(f"Error generating test case: {e}")
            return None
