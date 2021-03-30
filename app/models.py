class Preset:
    def __init__(
        self,
        id: int,
        name: str,
        saturation: float,
        eotf: str,
        colorGamut: str,
        colorRange: str,
        comment: str = ""
    ):
        self.id = id
        self.name = name
        self.comment = comment
        self.saturation = saturation
        self.eotf = eotf
        self.colorGamut = colorGamut
        self.colorRange = colorRange
