# Database of corn diseases symptoms
corn_disease_symptoms = {
    'G1': {'P1': True, 'P2': False, 'P3': False, 'P4': False, 'P5': False, 'P6': False},
    'G2': {'P1': True, 'P2': False, 'P3': False, 'P4': False, 'P5': False, 'P6': False},
    'G3': {'P1': True, 'P2': False, 'P3': False, 'P4': False, 'P5': False, 'P6': False},
    'G4': {'P1': True, 'P2': False, 'P3': False, 'P4': False, 'P5': False, 'P6': False},
    'G5': {'P1': True, 'P2': True, 'P3': False, 'P4': False, 'P5': False, 'P6': False},
    'G6': {'P1': False, 'P2': True, 'P3': False, 'P4': False, 'P5': False, 'P6': False},
    'G7': {'P1': False, 'P2': True, 'P3': False, 'P4': False, 'P5': False, 'P6': False},
    'G8': {'P1': False, 'P2': True, 'P3': False, 'P4': False, 'P5': False, 'P6': False},
    'G9': {'P1': False, 'P2': True, 'P3': False, 'P4': False, 'P5': False, 'P6': False},
    'G10': {'P1': False, 'P2': True, 'P3': True, 'P4': False, 'P5': False, 'P6': False},
    'G11': {'P1': False, 'P2': False, 'P3': True, 'P4': False, 'P5': False, 'P6': False},
    'G12': {'P1': False, 'P2': False, 'P3': True, 'P4': False, 'P5': False, 'P6': False},
    'G13': {'P1': False, 'P2': False, 'P3': True, 'P4': False, 'P5': False, 'P6': False},
    'G14': {'P1': False, 'P2': False, 'P3': True, 'P4': False, 'P5': False, 'P6': False},
    'G15': {'P1': False, 'P2': False, 'P3': False, 'P4': True, 'P5': False, 'P6': False},
    'G16': {'P1': False, 'P2': False, 'P3': False, 'P4': True, 'P5': False, 'P6': False},
    'G17': {'P1': False, 'P2': False, 'P3': False, 'P4': True, 'P5': False, 'P6': False},
    'G18': {'P1': False, 'P2': False, 'P3': False, 'P4': True, 'P5': False, 'P6': False},
    'G19': {'P1': False, 'P2': False, 'P3': False, 'P4': True, 'P5': False, 'P6': False},
    'G20': {'P1': False, 'P2': False, 'P3': False, 'P4': False, 'P5': True, 'P6': False},
    'G21': {'P1': False, 'P2': False, 'P3': False, 'P4': False, 'P5': True, 'P6': False},
    'G22': {'P1': False, 'P2': False, 'P3': False, 'P4': False, 'P5': True, 'P6': False},
    'G23': {'P1': False, 'P2': False, 'P3': False, 'P4': False, 'P5': True, 'P6': False},
    'G24': {'P1': False, 'P2': False, 'P3': False, 'P4': False, 'P5': True, 'P6': False},
    'G25': {'P1': False, 'P2': False, 'P3': False, 'P4': False, 'P5': True, 'P6': False},
    'G26': {'P1': False, 'P2': False, 'P3': False, 'P4': False, 'P5': True, 'P6': False},
    'G27': {'P1': False, 'P2': False, 'P3': False, 'P4': False, 'P5': True, 'P6': False},
    'G28': {'P1': False, 'P2': False, 'P3': False, 'P4': False, 'P5': False, 'P6': True},
    'G29': {'P1': False, 'P2': False, 'P3': False, 'P4': False, 'P5': False, 'P6': True},
    'G30': {'P1': False, 'P2': False, 'P3': False, 'P4': False, 'P5': False, 'P6': True},
    'G31': {'P1': False, 'P2': False, 'P3': False, 'P4': False, 'P5': False, 'P6': True}
}

# Mapping between P1-P6 to actual disease names
diseases = {
    'P1': 'Bulai',
    'P2': 'Blight',
    'P3': 'Leaf Rust',
    'P4': 'Burn',
    'P5': 'Stem Borer',
    'P6': 'Cob Borer'
}

# Function to perform disease inference
def infer_disease(selected_symptoms):
    # Count how many times each disease (P1-P6) is matched
    disease_count = {disease: 0 for disease in diseases}
    
    for symptom in selected_symptoms:
        if symptom in corn_disease_symptoms:
            for disease, is_present in corn_disease_symptoms[symptom].items():
                if is_present:
                    disease_count[disease] += 1
    
    # Determine diseases that match more than 3 symptoms
    matched_diseases = [disease for disease, count in disease_count.items() if count >= 3]
    
    if matched_diseases:
        return [diseases[d] for d in matched_diseases]
    else:
        return "No disease matched more than 3 symptoms."

# Main program flow
if __name__ == "__main__":
    # Example: User input of symptoms (G1, G3, G5, etc.)
    selected_symptoms = input("Enter the symptoms (e.g., G1,G3,G5): ").split(',')
    
    # Infer disease
    result = infer_disease(selected_symptoms)
    
    # Display the result
    if isinstance(result, list):
        print("Possible corn diseases based on symptoms:", ', '.join(result))
    else:
        print(result)
