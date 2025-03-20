# Context-Aware Testing System for Financial Ecosystems

## Overview
This project implements a context-aware testing system that dynamically generates, modifies, and adapts test cases for financial ecosystems. It leverages Generative AI tools like OpenAI, Hugging Face, LangChain, GPT-J, LLaMA, and Agentic-AI to automate test scenario generation and execution.

## Features
- AI-driven test case generation and adaptation.
- Real-world banking activities: KYC validation, loan approvals, payment services testing, fraud detection, and compliance monitoring.
- Self-updating test cases based on system changes.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd catfe-ai-problem-solver
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the system:
   ```bash
   python main.py
   ```

## Testing Instructions
1. **Unit Tests**:
   - Run the unit tests using `pytest`:
     ```bash
     pytest
     ```

2. **Manual Testing**:
   - Modify the `main.py` file to test specific scenarios by changing the `prompt` variable.
   - Example: Test fraud detection by updating the prompt:
     ```python
     prompt = "Generate a test case for real-time fraud detection in a banking system."
     ```

3. **Simulate Real-World Activities**:
   - Use the `simulate_real_world_activity` function in `test_scenarios.py` to simulate activities like KYC validation or loan approvals:
     ```python
     simulate_real_world_activity("KYC validation")
     ```

## Deliverables
- Architecture diagram (`architecture-diagram.png`).
- Presentation (`presentation.pptx`).
- Codebase for the testing system.
- Optionally, a demo video showcasing the solution.
