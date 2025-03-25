import openai


class TestCaseGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_test_case(self, scenario):
        try:
            # Using ChatCompletion instead of the outdated Completion API
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Change to "gpt-3.5-turbo" if needed
                messages=[
                    {"role": "system", "content": "You are a test automation expert."},
                    {"role": "user",
                     "content": f"Generate functional test cases for the following scenario: {scenario}"}
                ],
                max_tokens=200
            )
            return response["choices"][0]["message"]["content"].strip()
        except openai.OpenAIError as e:  # Correct exception handling
            print(f"Error generating test case: {e}")
            return None

