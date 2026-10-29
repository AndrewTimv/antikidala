# Отображаемые имена

from dataclasses import dataclass
import datetime


@dataclass
class ScreenName:
    """
    Отображаемое имя
    """
    name: str
    added_at: datetime.datetime
    changed: bool
    changed_at: datetime.datetime
