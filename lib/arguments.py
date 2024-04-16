"""Module for defining the Arguments dataclass and
the method for parsing and validating arguments.
"""

from dataclasses import dataclass
from typing import Literal, Optional
from colorama import Fore


@dataclass
class Arguments:
    """Args DTO where the attributes' values dictate the flow of control"""
    channel: bool
    filter: Optional[Literal["latest", "most_viewed"]]
    search_term: str
    valid: bool
    video: bool

def parse_and_validate(
    latest: Optional[bool],
    most_viewed: Optional[bool],
    search_for: Literal["channel", "video"],
    search_term: str
) -> Arguments:
    """Validates the input arguments.
    Returns: An Arguments object
    """
    arguments = {"valid": True}
    if search_for == "channel":
        arguments["channel"] = True
        arguments["video"] = False
        if (latest and most_viewed) or (not latest and not most_viewed):
            arguments["valid"] = False
            return Arguments(
                channel=arguments["channel"],
                filter=None,
                search_term="",
                valid=arguments["valid"],
                video=arguments["video"],
            )
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
