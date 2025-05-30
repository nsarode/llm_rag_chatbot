import random
import time

def get_current_wait_time(hospital: str) -> int | str:
    """Dummy function to generate fake wait times"""

    if hospital not in ["A", "B", "C", "D"]:
        return f"Hospital {hospital} does not exist"

    # Simulate API call delay
    time.sleep(1)
    # in real life, this would be some sort of database query or API call
    return random.randint(0, 10000)