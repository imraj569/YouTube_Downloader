"""Module for defining the Arguments dataclass and method(s) for
parsing and validating arguments.
"""

from dataclasses import dataclass
from typing import Literal, Optional
from colorama import Fore


@dataclass
class Arguments:
    """Args DTO where the attributes' values dictate the flow of the control"""
    channel: bool
    filter: Optional[Literal["latest", "most_viewed"]]
    search_term: str
    valid: bool
    video: bool

def parse_and_validate(latest, most_viewed, search_for, search_term) -> Arguments:
    """Validates the input arguments
    Returns: An Arguments object
    """
    arguments = {"valid": True}
    if search_for == "channel":
        arguments["channel"] = True
        arguments["video"] = False
        if (latest and most_viewed) or (not latest and not most_viewed):
            print(
                Fore.RED +
                "Please pass ONE OF (-l, --latest, -mv, --most_viewed) " \
                "along with the name of the YT channel to search for"
            )
            arguments["valid"] = False
        if latest:
            arguments["filter"] = "latest"
        else:
            arguments["filter"] = "most_viewed"

    elif search_for == "video":
        arguments["filter"] = None
        arguments["channel"] = False
        arguments["video"] = True
        if latest:
            print(Fore.CYAN + "Ignoring the --latest flag as you want to search for the video")
        if most_viewed:
            print(Fore.CYAN + "Ignoring the --most_viewed flag as you want to search for the video")

    arguments["search_term"] = search_term

    return Arguments(
        channel=arguments["channel"],
        filter=arguments["filter"],
        search_term=arguments["search_term"],
        valid=arguments["valid"],
        video=arguments["video"],
    )
