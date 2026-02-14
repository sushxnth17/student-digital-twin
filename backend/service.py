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
    inputs_before = {
        "study_hours": study_hours,
        "sleep_hours": sleep_hours,
        "skill_level": skill_level,
        "internship_effort": internship_effort
    }

    improved_study = study_hours + 1
    improved_sleep = max(sleep_hours, 7)
    improved_skill = skill_level + 1
    improved_internship = internship_effort + 1

    inputs_after = {
        "study_hours": improved_study,
        "sleep_hours": improved_sleep,
        "skill_level": improved_skill,
        "internship_effort": improved_internship
    }

    WEIGHTS = {
        "study_hours": 1.5,
        "sleep_hours": 1.0,
        "skill_level": 3.0,
        "internship_effort": 2.5
    }

    impact_breakdown = {}

    for factor in WEIGHTS:
        change = inputs_after[factor] - inputs_before[factor]
        impact = change * WEIGHTS[factor]

        impact_breakdown[factor] = {
            "before": inputs_before[factor],
            "after": inputs_after[factor],
            "change": change,
            "estimated_impact": round(impact, 2)
        }
    total_impact = sum(
        abs(details["estimated_impact"])
        for details in impact_breakdown.values()
    )
    for factor in impact_breakdown:
        if total_impact > 0:
            percent = (
                abs(impact_breakdown[factor]["estimated_impact"]) 
                / total_impact
            ) * 100
        else:
            percent = 0

        impact_breakdown[factor]["percentage_contribution"] = round(percent, 2)
    primary_driver = max(
        impact_breakdown,
        key=lambda x: impact_breakdown[x]["estimated_impact"]
    )


    primary_growth_driver = (
        f"{primary_driver.replace('_', ' ').title()} "
        "contributed the highest improvement."
    )
    return {
    "current": {
        "final_marks": base_results["final_marks"],
        "consistency": base_results["consistency"],
        "career_score": base_results["career_score"],
        "placement_probability": base_results["placement_probability"]
    },
    "progress": base_results["academic_history"],
    "scenario_comparison": scenario_results["comparison"],

    # EXPLAINABLE OUTPUTS
    "impact_breakdown": impact_breakdown,
    "primary_growth_driver": primary_growth_driver,

    "recommendations": base_results["recommendations"],
    "warnings": warnings,
}

