import sys
from pydantic import BaseModel, Field, ValidationError
import datetime as dt


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: dt.date
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def ft_print(result: SpaceStation) -> None:
    print("=" * 30)
    print(f"{result.station_id=}")
    print(f"{result.name=}")
    print(f"{result.crew_size=}")
    print(f"{result.power_level=}")
    print(f"{result.oxygen_level=}")
    print(f"{result.last_maintenance=}")
    print(f"{result.is_operational=}")
    print(f"{result.notes=}")
    print("=" * 30)


def main() -> int:
    try:
        result = SpaceStation(
                station_id="Obama",
                name="Obama_ship",
                crew_size=12,
                power_level=67.69,
                oxygen_level=12.12,
                last_maintenance=dt.date.today()
                )
    except ValidationError as e:
        print("CRASHED WEWOO\n")
        print(e)
        return(1)
    ft_print(result)
    try:
        result = SpaceStation(
                station_id="Obama",
                name="Obama_ship",
                crew_size=500,
                power_level=67.69,
                oxygen_level=12.12,
                last_maintenance=dt.date.today()
                )
    except ValidationError as e:
        print("CRASHED WEWOO\n")
        for info in e.errors():
            print(info["msg"])
        return(1)
    return(0)


if __name__ == "__main__":
    sys.exit(main())
