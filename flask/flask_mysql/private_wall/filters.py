from datetime import datetime

def time_formatter(time):
    date_diff = datetime.now() - time
    seconds_denoms = [(3600, "hour"), (60, "minute"), (1, "second")]
    days_denoms = [(365, "year"), (1, "day")]

    if date_diff.days > 0:
        attr = "days"
        denoms = days_denoms
    else:
        attr = "seconds"
        denoms = seconds_denoms

    for divisor, denom_name in denoms:
        if date_diff.__getattribute__(attr) >= divisor:
            num = date_diff.__getattribute__(attr) // divisor
            if num > 1:
                denom_name += "s"
            return f"{num} {denom_name} ago"
    return "0 seconds ago"