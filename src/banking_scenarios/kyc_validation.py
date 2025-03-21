from utils.logger import Logger  # Replace relative import with absolute import

class KYCValidation:
    def __init__(self):
        self.logger = Logger()

    def validate_customer(self, customer_data):
        # ...existing code...
        if not customer_data.get("id_proof"):
            self.logger.log("KYC validation failed: ID proof missing")
            return False, "ID proof missing"
        # ...existing code...
        self.logger.log("KYC validation successful")
        return True, "Validation successful"
