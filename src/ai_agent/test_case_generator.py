import openai
import google.generativeai as genai


class TestCaseGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_test_case(self, scenario):
        try:
            # Using ChatCompletion instead of the outdated Completion API
            client = genai.configure(api_key="AIzaSyBU3bl_b4SqgRE05HtwCTKUc360V9iSA2I")
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(
                "Generate possible test case scenarios for an input field that should only accept emails. "
                "Taking the following context, generate a sample test case in BDD language: "
            )

            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

            # response = openai.ChatCompletion.create(
            #     model="gpt-4",  # Change to "gpt-3.5-turbo" if needed
            #     messages=[
            #         {"role": "system", "content": "You are a test automation expert."},
            #         {"role": "user",
            #          "content": f"Generate functional test cases for the following scenario: {scenario}"}
            #     ],
            #     max_tokens=200
            # )
            return response["choices"][0]["message"]["content"].strip()
        except openai.OpenAIError as e:  # Correct exception handling
            print(f"Error generating test case: {e}")
            return None

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