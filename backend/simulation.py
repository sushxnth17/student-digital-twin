from backend.logic import academic_progress


def simulate_academic_journey(
    attendance,
    initial_marks,
    study_hours,
    sleep_hours,
    weeks=12
):
    """
    Simulates academic progress over a given number of weeks.
    Returns a list of marks after each week.
    """

    marks = initial_marks
    history = []

    for week in range(1, weeks + 1):
        weekly_marks = academic_progress(
            attendance=attendance,
            marks=marks,
            study_hours=study_hours,
            sleep_hours=sleep_hours
        )

        # Add slight improvement momentum over time
        growth_bonus = week * 0.05

        marks = weekly_marks + growth_bonus

        # Keep marks within valid range
        marks = max(0, min(marks, 100))


        history.append({
            "week": week,
            "marks": round(marks, 2)
        })

    return history

