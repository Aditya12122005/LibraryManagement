def calculate_fine(overdue_days):

    if not isinstance(overdue_days, int) or isinstance(overdue_days, bool):
        raise ValueError("Invalid overdue days")

    if overdue_days < 0:
        raise ValueError("Days cannot be negative")

    return overdue_days * 5


if __name__ == "__main__":
    print("Library Fine Calculator")
    print("Fine for 5 days:", calculate_fine(5))