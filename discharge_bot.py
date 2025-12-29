import time

def ai_parse_notes(notes):
    """Simulates an LLM parsing unstructured text"""
    print("🤖 AI Agent: Reading doctor notes...")
    time.sleep(1)
    
    # In real life, this calls OpenAI/Gemini API
    # Here we mock the extraction
    return {
        "status": "Ready for Discharge",
        "justification": "Patient hemodynamically stable. Afebrile for 24hrs. SpO2 98%.",
        "action_required": ["Notify Billing", "Notify Housekeeping"]
    }

def process_discharge(patient_id, notes):
    print(f"\n[TRIGGER] Discharge initiated for {patient_id}")
    
    # AI Step
    result = ai_parse_notes(notes)
    
    # Parallel Alerts
    print(f"\n[PARALLEL 1] Billing Alert: Start Claim. Reason: {result['justification']}")
    print(f"[PARALLEL 2] Housekeeping Alert: Prep room for {patient_id}")

# --- Test Execution ---
mock_notes = "Pt stable, chest clear. Plan discharge."
process_discharge("PAT-302-A", mock_notes)
