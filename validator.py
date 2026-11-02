def validate_score(score_input):

    try:
        val = float(score_input)

        if 0 <= val <= 100:
            return True, val

        return False, 0.0

    except (ValueError, TypeError):
        return False, 0.0

