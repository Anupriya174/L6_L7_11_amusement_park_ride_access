
import math


def validate_height_and_fastpass(rider_spec):
    if not isinstance(rider_spec, str):
        raise ValueError("Rider specification must be a string")

    parts = rider_spec.strip().split(':')
    if len(parts) != 2:
        raise ValueError("Invalid rider specification")

    height_str, pass_str = parts

    try:
        height = int(height_str.strip())
    except ValueError:
        raise ValueError("Height must be a valid integer")

    pass_str = pass_str.strip().upper()
    if pass_str not in ("YES", "NO"):
        raise ValueError("FastPass must be YES or NO")

    has_fastpass = pass_str == "YES"
    eligible = height >= 120
    status = "FastPass Priority" if has_fastpass else "Standard Entry"

    return f"Height {height}cm: {'Approved' if eligible else 'Denied'} ({status})"


def compute_dispatch_throughput(ride_metric_str):
    if not isinstance(ride_metric_str, str):
        raise ValueError("Ride metrics must be a string")

    parts = ride_metric_str.strip().split('/')
    if len(parts) != 2:
        raise ValueError("Invalid ride metrics")

    riders_str, mins_str = parts

    try:
        riders = float(riders_str.strip())
        cycle_mins = float(mins_str.strip())
    except ValueError:
        raise ValueError("Riders and minutes must be valid numbers")

    if not (
        math.isfinite(riders)
        and math.isfinite(cycle_mins)
        and riders > 0
        and cycle_mins > 0
    ):
        raise ValueError("Riders and minutes must be positive")

    return round(riders / cycle_mins, 2)


def resolve_safety_restraint_code(zone_code):
    if not isinstance(zone_code, str):
        raise ValueError("Zone code must be a string")

    prefix = zone_code.strip().upper()[:3]

    restraint_types = {
        "CST": "Over-the-Shoulder Harness",
        "WTR": "Lap Bar and Seatbelt",
        "DRP": "Hydraulic Shoulder Vest",
        "WHL": "Manual Safety Bar"
    }

    if prefix not in restraint_types:
        raise ValueError("Unknown safety restraint code")

    return restraint_types[prefix]


def main():
    print("==== Running validate_height_and_fastpass ====")
    r_input = input("Enter rider spec (Height:FastPass, e.g. 140:YES): ")
    print(validate_height_and_fastpass(r_input))

    print("\n==== Running compute_dispatch_throughput ====")
    t_input = input("Enter riders/mins (e.g. 48/2.5): ")
    print("Throughput (riders/min):", compute_dispatch_throughput(t_input))

    print("\n==== Running resolve_safety_restraint_code ====")
    z_input = input("Enter ride zone code (e.g. CST_01, WTR_A): ")
    print("Restraint:", resolve_safety_restraint_code(z_input))


if __name__ == "__main__":
    main()
