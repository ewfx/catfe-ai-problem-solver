import pytest
from src.banking_scenarios.kyc_validation import KYCValidation

def test_kyc_validation_success():
    validator = KYCValidation()
    customer_data = {"id_proof": "passport", "address_proof": "utility_bill"}
    result = validator.validate_customer(customer_data)
    assert result["status"] == "success"

def test_kyc_validation_failure():
    validator = KYCValidation()
    customer_data = {"id_proof": ""}
    result = validator.validate_customer(customer_data)
    assert result["status"] == "failed"