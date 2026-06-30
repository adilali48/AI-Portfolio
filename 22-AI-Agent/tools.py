from langchain_core.tools import tool
from datetime import datetime
import math


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.

    Example:
    5+5
    20*4
    sqrt(81)
    """

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {"sqrt": math.sqrt}
        )

        return str(result)

    except Exception:
        return "Invalid mathematical expression."


@tool
def current_date() -> str:
    """Returns today's date."""

    return datetime.now().strftime("%d %B %Y")


@tool
def current_time() -> str:
    """Returns current time."""

    return datetime.now().strftime("%I:%M:%S %p")