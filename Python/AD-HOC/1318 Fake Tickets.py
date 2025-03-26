ticket_filter = []
fake_ticket_filter = []

original_tickets, present_people = map(int, input().split())
while original_tickets != 0 and present_people != 0:

    ticket_sequence = list(map(int, input().split()))
    for ticket in ticket_sequence:
        if ticket in ticket_filter:
            fake_ticket_filter.append(ticket)
        else:
            ticket_filter.append(ticket)

    fake_tickets = set(fake_ticket_filter)
    print(len(fake_tickets))

    ticket_filter.clear()
    fake_ticket_filter.clear()

    original_tickets, present_people = map(int, input().split())