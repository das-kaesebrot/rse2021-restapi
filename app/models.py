from typing import Optional
from pydantic import BaseModel

class Preset(BaseModel):
    id: int
    name: str
    saturation: float
    eotf: str
    colorGamut: str
    colorRange: str
    comment: Optional[str] = None

    """
    def __init__(
        self,
        name: str,
        saturation: float,
        eotf: str,
        colorGamut: str,
        colorRange: str,
        comment: str = "",
        id: int = None
    ):
        self.id = id
        self.name = name
        self.comment = comment
        self.saturation = saturation
        self.eotf = eotf
        self.colorGamut = colorGamut
        self.colorRange = colorRange
    """