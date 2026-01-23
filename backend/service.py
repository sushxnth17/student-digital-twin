from backend.data import Student
from backend.app import run_simulation
from backend.scenario import compare_scenarios


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
}

