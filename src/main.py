import sys
from banking_scenarios.kyc_validation import KYCValidation
from banking_scenarios.loan_approval import LoanApproval
from ai_agent.test_case_generator import TestCaseGenerator

OPENAI_API_KEY = "XXXXXXXXXX"  # Replace with your OpenAI API key
GENAI_API_KEY = "XXXXXXXXX"  # Replace with your GenAI API key

def main():
    # Initialize components
    kyc_validator = KYCValidation()
    loan_approver = LoanApproval()
    # test_case_generator = TestCaseGenerator(api_key="your-openai-api-key")

    # Example: Generate test cases using OpenAI
    # generator = TestCaseGenerator(openai_api_key=OPENAI_API_KEY)
    # scenario = "Validate KYC process for a new customer."
    # test_cases = generator.generate_test_case(scenario, use_openai=True)
    # print("Generated Test Cases (OpenAI):")
    # print(test_cases)

    # Example: Generate test cases using GenAI
    generator = TestCaseGenerator(genai_api_key=GENAI_API_KEY)
    scenario = "Validate KYC process for a new customer."
    test_cases = generator.generate_test_case(scenario, use_openai=False)
    print("Generated Test Cases (Google GenAI):")
    print(test_cases)

    # Example: Run KYC validation
    customer_data = {"id_proof": "passport", "address_proof": "utility_bill"}
    kyc_result = kyc_validator.validate_customer(customer_data)
    print("KYC Validation Result:", kyc_result)

    # Example: Run Loan Approval
    customer_data = {"credit_score": 750}
    loan_result = loan_approver.assess_risk(customer_data)
    print("Loan Approval Result:", loan_result)

if __name__ == "__main__":
    main()