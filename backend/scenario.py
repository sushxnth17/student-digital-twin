from copy import deepcopy
from backend.app import run_simulation


def compare_scenarios(student, weeks=12):
    """
    Compare current student habits with an improved-habits scenario.
    Returns both outcomes and the difference.
    """

    # Run current scenario
    current_results = run_simulation(student, weeks=weeks)

    # Create an improved copy of the student
    improved_student = deepcopy(student)

    # Apply realistic improvements
    improved_student.study_hours = min(improved_student.study_hours + 1, 6)
    improved_student.sleep_hours = min(improved_student.sleep_hours + 1, 8)

    # Run improved scenario
    improved_results = run_simulation(improved_student, weeks=weeks)

    # Compare key metrics
    comparison = {
        "final_marks_change": (
            improved_results["final_marks"] - current_results["final_marks"]
        ),
        "career_score_change": (
            improved_results["career_score"] - current_results["career_score"]
        ),
        "placement_probability_before": current_results["placement_probability"],
        "placement_probability_after": improved_results["placement_probability"],
    }

    return {
        "current": current_results,
        "improved": improved_results,
        "comparison": comparison,
    }
