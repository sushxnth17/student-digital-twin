def calculate_effective_study(study_hours, sleep_hours):
    """
    Sleep affects how effective study time is.
    Ideal sleep is around 8 hours.
    """
    sleep_factor = min(sleep_hours / 8, 1)
    return study_hours * sleep_factor


def academic_progress(attendance, marks, study_hours, sleep_hours):
    """
    Calculates academic score change based on habits.
    """
    effective_study = calculate_effective_study(study_hours, sleep_hours)

    attendance_penalty = 0
    if attendance < 75:
        attendance_penalty = (75 - attendance) * 0.05

    progress = (effective_study * 0.1) - attendance_penalty
    new_marks = marks + progress

    return max(0, min(new_marks, 100))


def academic_risk_level(attendance, marks):
    """
    Determines academic risk level.
    """
    if attendance < 65 or marks < 40:
        return "High Risk"
    elif attendance < 75 or marks < 60:
        return "Medium Risk"
    else:
        return "Low Risk"
