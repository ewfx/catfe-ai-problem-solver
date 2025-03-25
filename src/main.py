import sys
from banking_scenarios.kyc_validation import KYCValidation
from banking_scenarios.loan_approval import LoanApproval
from ai_agent.test_case_generator import TestCaseGenerator

def main():
    # Initialize components
    kyc_validator = KYCValidation()
    loan_approver = LoanApproval()
    test_case_generator = TestCaseGenerator(api_key="your-openai-api-key")

    # Example: Generate test cases
    scenario = "Validate KYC process for a new customer."
    test_cases = test_case_generator.generate_test_case(scenario)
    print("Generated Test Cases:")
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