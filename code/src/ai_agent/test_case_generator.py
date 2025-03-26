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
        
    def generate_cucumber_feature(self, scenario, context, use_openai=True):
        """
        Generate a Cucumber feature file for the given scenario and context.
        """
        try:
            if use_openai and self.openai_api_key:
                # Use OpenAI API
                response = openai.ChatCompletion.create(
                    model="gpt-4",  # Change to "gpt-3.5-turbo" if needed
                    messages=[
                        {"role": "system", "content": "You are a test automation expert."},
                        {"role": "user",
                         "content": f"Generate a Cucumber feature file for the following scenario: {scenario} "
                                    f"using the following context: {context}"}
                    ],
                    max_tokens=500
                )
                return response["choices"][0]["message"]["content"].strip()

            elif self.genai_api_key:
                # Use Google GenAI
                prompt = (
                    "You are a test automation expert.\n"
                    f"Generate a Cucumber feature file for the following scenario: {scenario} "
                    f"using the following context: {context}"
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

    def generate_selenium_test(self, scenario, context, use_openai=True):
        """
        Generate a Selenium test script for the given scenario and context.
        """
        try:
            if use_openai and self.openai_api_key:
                # Use OpenAI API
                response = openai.ChatCompletion.create(
                    model="gpt-4",  # Change to "gpt-3.5-turbo" if needed
                    messages=[
                        {"role": "system", "content": "You are a test automation expert."},
                        {"role": "user",
                        "content": f"Generate a Selenium test script in Python for the following scenario: {scenario}. "
                                    f"Use the following UI context: {context}. "
                                    "The application URL is 'http://localhost:4200'. "
                                    "Use 'user' as the username and 'password' as the password for login and registration. "
                                    "Ensure the script uses proper Python 3.x syntax. "
                                    "Avoid using backticks (`expression`) as they are not supported in Python 3.x. "
                                    "Avoid wrapping the code in triple backticks (```python). "
                                    "Provide only plain Python code without any markdown formatting. "
                                    "The script should include only the necessary imports, setup, and test steps. "
                                    "Avoid adding unnecessary comments or irrelevant content. "
                                    "Ensure the script is concise, functional, and adheres to Python 3.x standards."}
                    ],
                    max_tokens=500
                )
                return response["choices"][0]["message"]["content"].strip()

            elif self.genai_api_key:
                # Use Google GenAI
                prompt = (
                    "You are a test automation expert.\n"
                    f"Generate a Selenium test script in Python for the following scenario: {scenario}. "
                    f"Use the following UI context: {context}. "
                    "The application URL is 'http://localhost:4200'. "
                    "Use 'user' as the username and 'password' as the password for login and registration. "
                    "Ensure the script uses proper Python 3.x syntax. "
                    "Avoid using backticks (`expression`) as they are not supported in Python 3.x. "
                    "Avoid wrapping the code in triple backticks (```python). "
                    "Provide only plain Python code without any markdown formatting. "
                    "The script should include only the necessary imports, setup, and test steps. "
                    "Avoid adding unnecessary comments or irrelevant content. "
                    "Ensure the script is concise, functional, and adheres to Python 3.x standards."
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

