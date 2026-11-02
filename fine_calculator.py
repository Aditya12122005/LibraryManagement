FINE_PER_DAY = 5

def calculate_fine(overdue_days):
    if not isinstance(overdue_days, int) or overdue_days < 0:
        raise ValueError("overdue_days must be a non-negative integer")
    return overdue_days * FINE_PER_DAY

if __name__ == "__main__":
    print("Fine for 3 overdue days:", calculate_fine(3))