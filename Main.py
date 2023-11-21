from TicketStats import Ticket

class HelpDeskSystem:
    @staticmethod
    def main():
        print("IT5016D Helpdesk Ticket System\n")

        # List of instances for testing
        ticket1 = Ticket("Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working")
        ticket2 = Ticket("Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
        ticket3 = Ticket("John", "JOHNS", "john@whitecliffe.co.nz", "Password Change")

        # Close ticket test
        ticket4_close = Ticket("George", "GEORGEH", "george@whitecliffe.co.nz", "Router Internet")
        ticket4_close.status = "Closed"
        ticket4_close.resolve_ticket("The router issue has been resolved. Please check your internet connection.")
        ticket4_close.comment = ['Test comment to close ticket']

        tickets = [ticket1, ticket2, ticket3, ticket4_close]

        while True:
            print('--------------------------------')
            print('SELECT OPTION:')
            print('1: Submit a new ticket')
            print('2: Resolve a ticket')
            print('3: Reopen a ticket')
            print('4: Display ticket information')
            print('5: Display ticket statistics')
            print('6: Exit')
            print('--------------------------------')

            choice = input("Enter your choice: ")

            if choice == "1":
                # Submit a new ticket
                ticket_creator = input('Enter your name: ')
                staff_id = input('Enter your Staff ID: ')
                contact_email = input('Enter your email: ')
                description = input('Describe your issue or type "Change Password" to reset your password: ')

                if description.lower() == "change password":
                    new_ticket = Ticket(ticket_creator, staff_id, contact_email, "Password Change")
                    new_password = new_ticket.generate_password()
                    print(f"New password generated: {new_password}")
                    new_ticket.response = f"New password generated and sent to {contact_email}."
                    tickets.append(new_ticket)
                else:
                    new_ticket = Ticket(ticket_creator, staff_id, contact_email, description)
                    tickets.append(new_ticket)

                print("New ticket submitted.")

            elif choice == "2":
                # Resolve a ticket
                if tickets:
                    tickets[0].resolve_ticket("Issue resolved. Please check your email for details.")
                    print("Ticket resolved.")
                else:
                    print("No open tickets to resolve.")

            elif choice == "3":
                # Reopen a ticket
                if tickets and tickets[0].status == "Closed":
                    tickets[0].reopen_ticket()
                    print("Ticket reopened.")
                else:
                    print("No closed tickets to reopen.")

            elif choice == "4":
                # Display ticket information
                if tickets:
                    tickets[0].print_ticket_info()
                else:
                    print("No tickets to display.")

            elif choice == "5":
                # Display ticket statistics
                print(Ticket.ticket_stats())

            elif choice == "6":
                print("Exiting the Help Desk System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    HelpDeskSystem.main()
