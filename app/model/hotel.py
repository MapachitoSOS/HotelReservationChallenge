from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from typing import ClassVar

from app.services.util import (generate_unique_id, date_lower_than_today_error,
    reservation_not_found_error, guest_not_found_error, room_not_available_error,
    room_not_found_error, room_already_exists_error)


class Guest:
    VIP:str = 'vip'
    REGULAR:str = 'regular'

    def __init__(self, name: str, email: str, type_: REGULAR):
        self.name = name
        self.email = email
        self.type_ = type_
    def __str__(self) -> str:
        return f"Guest {self.name} ({self.email}) of type {self.type_}"

dataclass(Guest)
@dataclass
class Reservation:

    def __init__(self, guest_name: str, description: str, check_in: date, check_out: date):
        self.guest_name = guest_name
        self.guest_email = guest_name
        self.description = description
        self.check_in = check_in
        self.check_out = check_out
        self.guests: list[Guest] = field(default_factory=list)
        self.id: str = field(default_factory=generate_unique_id)

    def add_guest(self, name: str, email: str, type_: str = Guest.REGULAR):
        guest = Guest(name=name, email=email, type_=type_)
        self.guests.append(guest)

    def delete_guest(self, guest_index: int):
        if 0 <= guest_index < len(self.guests):
            del self.guests[guest_index]
        else:
            guest_not_found_error()

    def __len__(self) -> int:
        return len(self.guests)

    def __str__(self) -> str:
        return f"Guest: {self.guest_name}\nDescription: {self.description}\nDates: {self.check_in} - {self.check_out}"
