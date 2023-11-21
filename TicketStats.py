class Ticket:
    ticket_counter = 2000
    open_tickets = 0
    closed_tickets = 0

    def __init__(self, creator_name, staff_id, contact_email, description):
        self.ticket_number = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.creator_name = creator_name
        self.staff_id = staff_id
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        self.comment = []  # Added for future use
        Ticket.open_tickets += 1

    def generate_password(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.close_ticket()
            return f"New password generated: {new_password}"
        return None  # Return None if no password is generated

    def resolve_ticket(self, response):
        self.response = response
        self.close_ticket()
        self.generate_auto_response()  # Call the new method for automated response

    def generate_auto_response(self):
        if self.status == "Closed":
            self.response += "\nAutomated Response: Thank you for using our help desk. Your issue has been resolved!"

    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.open_tickets += 1
        Ticket.closed_tickets -= 1

    def close_ticket(self):
        self.status = "Closed"
        Ticket.open_tickets -= 1
        Ticket.closed_tickets += 1

    @staticmethod
    def ticket_stats():
        return f"\nTickets Created: {Ticket.ticket_counter - 2000}\n" \
               f"Tickets Resolved: {Ticket.closed_tickets}\n" \
               f"Tickets To Solve: {Ticket.open_tickets}\n"

    def print_ticket_info(self):
        print(f"\nTicket Number: {self.ticket_number}\n"
              f"Ticket Creator: {self.creator_name}\n"
              f"Staff ID: {self.staff_id}\n"
              f"Email Address: {self.contact_email}\n"
              f"Description: {self.description}\n"
              f"Response: {self.response}\n"
              f"Ticket Status: {self.status}\n")
