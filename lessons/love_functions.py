"""some examples of tender, loving function definitions."""


def love(name: str) -> str:
    """given a name as a parameter, returns a loving string."""
    return f"i love you {name}"


def spread_love(to: str, n: int) -> str:
    """generates a string that repeats a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        # love_note += f"love{to}\n"
        i += 1
    return love_note