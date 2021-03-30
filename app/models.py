class Preset:
    def __init__(
        self,
        id: int,
        name: str,
        comment: str = "",
        saturation: float,
        eotf: str,
        colorGamut: str,
        colorRange: str
    ):
        self.id = id
        self.name = name
        self.comment = comment
        self.saturation = saturation
        self.eotf = eotf
        self.colorGamut = colorGamut
        self.colorRange = colorRange
