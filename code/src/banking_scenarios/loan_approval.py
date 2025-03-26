from utils.logger import Logger  # Replace relative import with absolute import

class LoanApproval:
    def assess_risk(self, customer_data):
        # Simulate risk assessment logic
        if customer_data.get("credit_score", 0) < 600:
            return {"status": "rejected", "reason": "Low credit score"}
        return {"status": "approved", "message": "Loan approved"}