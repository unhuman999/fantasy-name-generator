import json
from pydantic import BaseModel, RootModel


class GenderDataset(BaseModel):
    male: list[str]
    female: list[str]

class RacesDataset(RootModel[dict[str, GenderDataset]]):
    pass 