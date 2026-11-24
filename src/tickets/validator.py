import logging
from pathlib import Path
from tickets.loader import load_tickets

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


def validate_tickets(file_path: str):
    valid_tickets, invalid_tickets = load_tickets(file_path)

    for ticket in valid_tickets:
        logger.info("Valid ticket processed: %s", ticket.ticket_id)

    for ticket in invalid_tickets:
        logger.error(
            "Invalid ticket at row %s: %s",
            ticket["row"],
            ticket["error"]
        )

    logger.info("Total valid tickets: %s", len(valid_tickets))
    logger.info("Total invalid tickets: %s", len(invalid_tickets))

    return valid_tickets, invalid_tickets


if __name__ == "__main__":
    csv_path = Path("data/tickets.csv")
    validate_tickets(str(csv_path))