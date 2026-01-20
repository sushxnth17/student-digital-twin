
from backend.data import Student
from backend.recommendations import generate_recommendations
from backend.simulation import simulate_academic_journey
from backend.career import calculate_career_score, placement_probability

def run_simulation(student, weeks=12):
    """
    Runs full academic + career simulation for a student.
    """

    academic_history = simulate_academic_journey(
        attendance=student.attendance,
        initial_marks=student.marks,
        study_hours=student.study_hours,
        sleep_hours=student.sleep_hours,
        weeks=weeks
    )

    final_marks = academic_history[-1]["marks"]
    consistency = student.consistency_score()

    career_score = calculate_career_score(
        skill_level=student.skill_level,
        internship_effort=student.internship_effort,
        consistency_score=consistency,
        final_marks=final_marks
    )

    placement_chance = placement_probability(career_score)
    recommendations = generate_recommendations(
        student,
        {
            "consistency": consistency,
            "career_score": career_score
        }
    )
    return {
        "academic_history": academic_history,
        "final_marks": final_marks,
        "consistency": consistency,
        "career_score": career_score,
        "placement_probability": placement_chance,
        "recommendations": recommendations
    }


if __name__ == "__main__":
    # Temporary demo student (for testing only)
    student = Student(
        attendance=72,
        marks=60,
        study_hours=2,
        sleep_hours=6,
        skill_level=1,
        internship_effort=2
    )

    results = run_simulation(student, weeks=12)

    print("Final Marks:", results["final_marks"])
    print("Consistency Score:", results["consistency"])
    print("Career Score:", results["career_score"])
    print("Placement Probability:", results["placement_probability"])
    