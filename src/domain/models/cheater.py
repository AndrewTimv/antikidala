from dataclasses import dataclass


from domain.models.screen_name import ScreenName
from domain.models.telephone import Telephone
from domain.models.card import Card
from domain.models.proof_links import ProofLink


@dataclass
class Cheater:
    vk_id: str
    screen_name: ScreenName
    fifty: bool
    old_screen_names: list[ScreenName]
    telephones: list[Telephone]
    cards: list[Card]
    proof_links: list[ProofLink]
    