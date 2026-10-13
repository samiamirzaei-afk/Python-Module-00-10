from pydantic import BaseModel, Field, model_validator
import datetime as dt
import enum
import sys

class ContactType(enum.Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: dt.date
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_o_matic(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with \"AC\"")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact is not verified!")
        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("telepathic contact needs 3 witness min!")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("strong signals need a message!")
        return(self)


def main() -> int:

    
    try:
        result = AlienContact(
                contact_id = "AC.obama",
                timestamp = dt.date.today(),
                location = "obama_land",
                contact_type = ContactType.RADIO,
                signal_strength = 8.0,
                duration_minutes = 67,
                witness_count = 12,
                message_received = "Obama invites you to Obamium"
                )
    except ValueError as e:
        for info in e.errors():
            print(info["msg"])
        return(1)
    for stuff in result:
        print(stuff)
    print("=" * 32)
    try:
        result = AlienContact(
                contact_id = "AC.Osama",
                timestamp = dt.date.today(),
                location = "Osama_land",
                contact_type = ContactType.TELEPATHIC,
                signal_strength = 8.0,
                duration_minutes = 67,
                witness_count = 2,
                message_received = "Osama invites you to Osamuim"
                )
    except ValueError as e:
        for info in e.errors():
            print(info["msg"])
        return(1)
    for stuff in result:
        print(stuff)

if __name__ == "__main__":
    exit_result = main()
    if exit_result == 1:
        print("bad exit...")
        sys.exit(1)
    print("\nclean exiting...")


    """
    try:
        result = AlienContact(
                contact_id = "obama",
                timestamp = dt.date.today(),
                location = "obama_land",
                contact_type = ContactType.VISUAL,
                signal_strength = 1.0,
                duration_minutes = 67,
                witness_count = 12,
                )
    except ValueError as e:
        for info in e.errors():
            print(info["msg"])
        return(1)
    for stuff in result:
        print(stuff)
    return(0)
    """
