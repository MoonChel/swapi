from typing import List, Optional
from pydantic import BaseModel, Field


class SwapiPerson(BaseModel):
    birth_year: str
    eye_color: str
    gender: str
    hair_color: str
    height: str
    homeworld: str
    mass: str
    name: str
    skin_color: str
    created: str
    edited: str

    def __repr__(self) -> str:
        return f"{self.name}, {self.birth_year}"


class SwapiPeople(BaseModel):
    next: Optional[str]
    count: int
    results: List[SwapiPerson] = Field(default_factory=list)
