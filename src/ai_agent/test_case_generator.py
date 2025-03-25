import openai
import google.generativeai as genai


class TestCaseGenerator:
    def __init__(self, openai_api_key=None, genai_api_key=None):
        self.openai_api_key = openai_api_key
        self.genai_api_key = genai_api_key

        # Configure OpenAI if the API key is provided
        if self.openai_api_key:
            self.openai_client = openai.Client(api_key=self.openai_api_key)

        # Configure Google GenAI if the API key is provided
        if self.genai_api_key:
            genai.configure(api_key=self.genai_api_key)

    def generate_test_case(self, scenario, use_openai=True):
        """
        Generate test cases using OpenAI or Google GenAI based on the `use_openai` flag.
        """
        try:
            if use_openai and self.openai_api_key:
                # Use OpenAI API (Updated Syntax)
                response = self.openai_client.chat.completions.create(
                    model="gpt-3.5-turbo",  # Change to "gpt-3.5-turbo" if needed
                    messages=[
                        {"role": "system", "content": "You are a test automation expert."},
                        {"role": "user",
                         "content": f"Generate functional test cases for the following scenario: {scenario}"}
                    ],
                    max_tokens=10
                )
                return response.choices[0].message.content.strip()

            elif self.genai_api_key:
                # Use Google GenAI
                prompt = (
                    "You are a test automation expert.\n"
                    f"Generate functional test cases for the following scenario: {scenario}"
                )
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                return response.text

            else:
                raise ValueError("No valid API key provided for OpenAI or Google GenAI.")

        except openai.OpenAIError as e:
            return f"OpenAI Error: {str(e)}"
        except genai.GenerativeAIError as e:
            return f"Google GenAI Error: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"


# {
#     "application": "Banking System",
#     "modules": [
#         {
#             "name": "Login",
#             "features": ["User Authentication"],
#             "ui_elements": [
#                 {"name": "username_field", "selector": "//*[@id='username']", "type": "input"},
#                 {"name": "password_field", "selector": "//*[@id='password']", "type": "input"},
#                 {"name": "login_button", "selector": "//*[@id='login']", "type": "button"},
#                 {"name": "error_message", "selector": "//*[@id='error']", "type": "text"}
#             ],
#             "test_cases": [
#                 {"scenario": "Valid Login", "username": "testuser", "password": "testpassword", "expected": "Dashboard"},
#                 {"scenario": "Invalid Login", "username": "wronguser", "password": "wrongpassword", "expected": "Invalid credentials"}
#             ]
#         }
#     ]
# }