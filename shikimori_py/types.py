import datetime
from lib2to3.pytree import Base
from pydantic import BaseModel

__all__ = [
    "AnimeItem",
    "MangaItem",
    "RanobeItem"
]


class Image(BaseModel):
    original: str
    preview: str
    x96: str
    x48: str


class BaseItem(BaseModel):
    id: int
    name: str
    russian: str
    image: Image
    url: str
    kind: str
    score: str
    status: None | str
    aired_on: None | datetime.date
    released_on: None | datetime.date

class AnimeItem(BaseItem):
    episodes: int
    episodes_aired: int

class MangaItem(BaseItem):
    volumes: int
    chapters: int

class RanobeItem(BaseItem):
    volumes: int
    chapters: int


