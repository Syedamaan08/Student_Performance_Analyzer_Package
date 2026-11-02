import performance_analyzer as pa


def main():
    print("=== STUDENT PERFORMANCE ANALYZER ===")

    raw_data = [
        ('Asha', 92.5),
        ('Pass_Boundary', 40.0),
        ('Fail_Boundary', 39.9),
        ('Negative_Score', -15.0),
        ('Overflow_Score', 105.0),
        ('Non_Numeric', 'absent')
    ]

    processed_records = []

    for name, raw_score in raw_data:

        is_valid, score = pa.validate_score(raw_score)

        if is_valid:
            grade, gpa = pa.compute_grade(score)

            processed_records.append({
                'name': name,
                'score': score,
                'grade': grade,
                'gpa': gpa
            })

            print(
                f"[ACCEPTED] {name} | Score: {score} "
                f"| Grade: {grade} | GPA: {gpa}"
            )

        else:
            print(f"[REJECTED] {name} | Invalid Score: {raw_score}")

    avg_score, pass_pct, top_scorer = pa.analyze_class(processed_records)

    print("\n--- CLASS ANALYTICS SUMMARY ---")
    print("Class Average Score:", avg_score)
    print("Class Pass Rate:", pass_pct, "%")
    print("Top Performing Student:", top_scorer)


if __name__ == "__main__":
    main()