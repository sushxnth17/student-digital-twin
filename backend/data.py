class Student:
    def __init__(
        self,
        attendance,
        marks,
        study_hours,
        sleep_hours,
        skill_level,
        internship_effort
    ):
        self.attendance = self._clamp(attendance, 0, 100)
        self.marks = self._clamp(marks, 0, 100)
        self.study_hours = max(0, study_hours)
        self.sleep_hours = max(0, sleep_hours)
        self.skill_level = self._clamp(skill_level, 0, 2)
        self.internship_effort = self._clamp(internship_effort, 0, 3)

    def _clamp(self, value, min_val, max_val):
        return max(min_val, min(value, max_val))

    def consistency_score(self):
        """
        Measures how sustainable the student's routine is (0–1).
        Considers study regularity, sleep, and attendance.
        """
        study_factor = min(self.study_hours / 4, 1)
        sleep_factor = min(self.sleep_hours / 8, 1)
        attendance_factor = self.attendance / 100

        return round(
            (study_factor + sleep_factor + attendance_factor) / 3, 2
        )

    def summary(self):
        """
        High-level snapshot of the student digital twin.
        Useful for UI and analytics.
        """
        return {
            "attendance": self.attendance,
            "marks": self.marks,
            "study_hours": self.study_hours,
            "sleep_hours": self.sleep_hours,
            "skill_level": self.skill_level,
            "internship_effort": self.internship_effort,
            "consistency": self.consistency_score()
        }
