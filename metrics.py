def compute_grade(score):

    if score >= 90:
        return 'O', 10

    elif score >= 80:
        return 'A+', 9

    elif score >= 70:
        return 'A', 8

    elif score >= 60:
        return 'B+', 7

    elif score >= 50:
        return 'B', 6

    elif score >= 40:
        return 'C', 5

    else:
        return 'F', 0




def analyze_class(student_records):

    if not student_records:
        return 0.0, 0.0, 'None'

    total_score = sum(r['score'] for r in student_records)

    avg = total_score / len(student_records)

    passed_count = sum(
        1 for r in student_records if r['score'] >= 40
    )

    pass_rate = (passed_count / len(student_records)) * 100

    top_student = max(
        student_records,
        key=lambda x: x['score']
    )['name']

    return round(avg, 2), round(pass_rate, 2), top_student