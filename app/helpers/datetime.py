import datetime


def generate_utc_dt() -> datetime.datetime:
    """Generate timezone-aware UTC datetime."""
    return datetime.datetime.now(datetime.timezone.utc)


def generate_utc_dt_naive() -> datetime:
    """Generate naive UTC datetime."""
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
