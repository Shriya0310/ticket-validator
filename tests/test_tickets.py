from tickets.loader import load_tickets


def create_csv(tmp_path, content):
    file_path = tmp_path / "test_tickets.csv"
    file_path.write_text(content)
    return str(file_path)


# Test 1: Valid ticket
def test_valid_ticket(tmp_path):
    content = """ticket_id,customer_name,equipment,issue_description,priority,status,created_at
101,Rahul,Printer,Paper jam,High,Open,2026-11-20"""

    file_path = create_csv(tmp_path, content)
    valid, invalid = load_tickets(file_path)

    assert len(valid) == 1
    assert len(invalid) == 0


# Test 2: Missing required field
def test_missing_field(tmp_path):
    content = """ticket_id,customer_name,equipment,issue_description,priority,status,created_at
101,Rahul,Printer,Paper jam,High,Open,"""

    file_path = create_csv(tmp_path, content)
    valid, invalid = load_tickets(file_path)

    assert len(valid) == 0
    assert len(invalid) == 1


# Test 3: Invalid date
def test_invalid_date(tmp_path):
    content = """ticket_id,customer_name,equipment,issue_description,priority,status,created_at
101,Rahul,Printer,Paper jam,High,Open,not-a-date"""

    file_path = create_csv(tmp_path, content)
    valid, invalid = load_tickets(file_path)

    assert len(valid) == 0
    assert len(invalid) == 1


# Test 4: Invalid enum value
def test_invalid_enum(tmp_path):
    content = """ticket_id,customer_name,equipment,issue_description,priority,status,created_at
101,Rahul,Printer,Paper jam,Urgent,Open,2026-11-20"""

    file_path = create_csv(tmp_path, content)
    valid, invalid = load_tickets(file_path)

    assert len(valid) == 0
    assert len(invalid) == 1


# Test 5: Empty CSV
def test_empty_csv(tmp_path):
    content = ""

    file_path = create_csv(tmp_path, content)
    valid, invalid = load_tickets(file_path)

    assert len(valid) == 0
    assert len(invalid) == 0