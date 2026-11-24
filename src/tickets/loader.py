import csv
from pathlib import Path
from pydantic import ValidationError
from tickets.models import Ticket


def load_tickets(file_path: str):
    valid_tickets = []
    invalid_tickets = []

    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):
            try:
                ticket = Ticket.model_validate(row)
                valid_tickets.append(ticket)

            except ValidationError as error:
                invalid_tickets.append({
                    "row": row_number,
                    "error": str(error)
                })

    return valid_tickets, invalid_tickets