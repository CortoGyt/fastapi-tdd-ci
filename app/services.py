def compute_bonus(salary: float) -> float:
    if salary < 0:
        raise ValueError("Salary must be positive")
    # ERREUR VOLONTAIRE
    return salary * 0.2