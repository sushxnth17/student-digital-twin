def generate_recommendations(student, results):
    """
    Generate actionable recommendations based on
    student habits and simulation results.
    """

    recommendations = []

    if student.study_hours < 3:
        recommendations.append(
            "Increase daily study time by at least 1 hour for better consistency."
        )

    if student.sleep_hours < 7:
        recommendations.append(
            "Improve sleep to at least 7 hours to avoid burnout."
        )

    if results["consistency"] < 0.6:
        recommendations.append(
            "Focus on maintaining a consistent daily routine."
        )

    if results["career_score"] < 60:
        recommendations.append(
            "Invest more time in skill-building and internships."
        )

    if not recommendations:
        recommendations.append(
            "Your current routine is balanced. Maintain consistency."
        )

    return recommendations
