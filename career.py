def calculate_career_score(
    skill_level,
    internship_effort,
    consistency_score,
    final_marks
):
    """
    Calculates overall career readiness score (0–100)
    """

    # Normalize inputs
    skill_score = (skill_level / 2) * 30
    internship_score = (internship_effort / 3) * 25
    consistency_score = consistency_score * 25
    academic_score = (final_marks / 100) * 20

    total_score = (
        skill_score +
        internship_score +
        consistency_score +
        academic_score
    )

    return round(total_score, 2)


def placement_probability(career_score):
    """
    Converts career score into placement probability category
    """

    if career_score >= 75:
        return "High"
    elif career_score >= 50:
        return "Medium"
    else:
        return "Low"
if __name__ == "__main__":
    score = calculate_career_score(
        skill_level=1,
        internship_effort=2,
        consistency_score=0.7,
        final_marks=65
    )

    print("Career Score:", score)
    print("Placement Probability:", placement_probability(score))
