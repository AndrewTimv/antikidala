# Класс кидалы

from sqlalchemy.orm import Mapper, mapped_column, relationship

from datasource.models import Base


class Cheater(Base):
    """
    Класс кидалы ORM
    """
    __tablename__ = 'cheaters'

    id: Mapper[int] = mapped_column(primary_key=True)
    vk_id: Mapper[str]
    screen_name: Mapper['ScreenName']
    fifty: bool
    old_screen_names: Mapper[list['ScreenName']]
    telephones: Mapper[list['Telephone']]
    cards: Mapper[list['Card']]
    proof_link: Mapper[list['ProofLink']]



class ScreenName(Base):
    """
    Отображаемое имя ORM
    """
    __tablename__ = 'screen_name'

    id: Mapper[int] = mapped_column(primary_key=True)
    name: Mapper[str]
    
