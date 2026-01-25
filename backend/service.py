from backend.data import Student
from backend.app import run_simulation
from backend.scenario import compare_scenarios

def _clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def run_full_analysis(
    attendance,
    marks,
    study_hours,
    sleep_hours,
    skill_level,
    internship_effort,
    weeks=12
):
    """
    Single entry point for frontend or API.
    """
    warnings = []

    # Clamp and validate inputs
    attendance = _clamp(attendance, 0, 100)
    marks = _clamp(marks, 0, 100)
    study_hours = _clamp(study_hours, 0, 12)
    sleep_hours = _clamp(sleep_hours, 0, 12)
    skill_level = _clamp(skill_level, 0, 10)
    internship_effort = _clamp(internship_effort, 0, 10)

    if study_hours < 1:
        warnings.append("Very low study hours may lead to stagnation.")

    if sleep_hours < 5:
        warnings.append("Low sleep hours can negatively affect consistency.")

    student = Student(
        attendance=attendance,
        marks=marks,
        study_hours=study_hours,
        sleep_hours=sleep_hours,
        skill_level=skill_level,
        internship_effort=internship_effort
    )

    base_results = run_simulation(student, weeks=weeks)
    scenario_results = compare_scenarios(student, weeks=weeks)

    return {
    "current": {
        "final_marks": base_results["final_marks"],
        "consistency": base_results["consistency"],
        "career_score": base_results["career_score"],
        "placement_probability": base_results["placement_probability"],
    },
    "progress": base_results["academic_history"],
    "scenario_comparison": scenario_results["comparison"],
    "recommendations": base_results["recommendations"],
    "warnings": warnings,
}

