import json
from regex_utils import is_valid_email,is_valid_phone


FILENAME = 'tickets.json'

class Tickets():
    def __init__(self,ticket_id,event_name,event_date,venue,buyer_name,buyer_email,buyer_phone,seat_number,price):
        if not is_valid_email(buyer_email):
            exit('Invalid Email, Please Enter a Valid one...')
        if not is_valid_phone(buyer_phone):
            exit('Invalid phone number, Please Enter a Valid one...')
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.event_date = event_date
        self.venue = venue
        self.buyer_name = buyer_name
        self.buyer_email = buyer_email
        self.buyer_phone = buyer_phone
        self.seat_number = seat_number
        self.price = price

    def to_dict(self):
        return {
            "ticket_id" : self.ticket_id,
            "event_name" : self.event_name,
            "event_date" : self.event_date,
            "venue" : self.venue,
            "buyer_name" : self.buyer_name,
            "buyer_email" : self.buyer_email,
            "buyer_phone" : self.buyer_phone,
            "seat_number" : self.seat_number,
            "price" : self.price
        }

def create_ticket(ticket_id,event_name,event_date,venue,buyer_name,buyer_email,buyer_phone,seat_number,price):
    try:
        with open(FILENAME,'r') as f:
            data = json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        data = []

    t = Tickets(ticket_id,event_name,event_date,venue,buyer_name,buyer_email,buyer_phone,seat_number,price)
    data.append(t.to_dict())

    with open(FILENAME,'w') as f:
        json.dump(data,f,indent=4)

    print('Ticket Created Successfully...')

def update_ticket(id_to_update,n_ticket_id,n_event_name,n_event_date,n_venue,n_buyer_name,n_buyer_email,n_buyer_phone,n_seat_number,n_price):
    if not is_valid_email(n_buyer_email):
        exit('Invalid Email, Please Enter a Valid one...')
    if not is_valid_phone(n_buyer_phone):
        exit('Invalid phone number, Please Enter a Valid one...')
    try:
        with open(FILENAME,'r') as f:
            data = json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        data = []

    UPDATED = False

    for tkt in data:
        if tkt['ticket_id'] == id_to_update:
            tkt['ticket_id'] = n_ticket_id
            tkt['event_name'] = n_event_name
            tkt['event_date'] = n_event_date
            tkt['venue'] = n_venue
            tkt['buyer_name'] = n_buyer_name
            tkt['buyer_email'] = n_buyer_email
            tkt['buyer_phone'] = n_buyer_phone
            tkt['seat_number'] = n_seat_number
            tkt['price'] = n_price
            UPDATED = True

    if UPDATED:
        with open(FILENAME,'w') as f:
            json.dump(data,f,indent=4)
        print('Ticket Updated Successfully....')
    else:
        print('Invalid Ticket Id...')
    
def delete_ticket(id_to__delete):
    try:
        with open(FILENAME,'r') as f:
            data = json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        data = []

    DELETED = False

    for tkt in data:
        if tkt['ticket_id'] == id_to__delete:
            data.remove(tkt)
            DELETED = True

    if DELETED:
        with open(FILENAME,'w') as f:
            json.dump(data,f,indent=4)
        print('Deleted Ticket Successfully...')
    else:
        print('Inavalid Ticket Id....')

def read_tickets():
    with open(FILENAME,'r') as f:
        print(json.load(f))

def search_tickets(n_event_name):
    try:
        with open(FILENAME,'r') as f:
            data = json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        data = []

    for tkt in data:
        if tkt['event_name'] == n_event_name:
            print(tkt)

def main():
    print('Welcome to the Event Ticket Booking System...')
    print('Press 1 to Create the Ticket.')
    print('Press 2 to Update the Ticket..')
    print('Press 3 to Delete the Ticket...')
    print('Press 4 to Read all the Tickets....')
    print('Press 5 to Search tickets based on Event name.....')
    choice = int(input('Enter the Choice:\n'))
    if choice == 1:
        ticket_id = int(input('Enter the Ticket Id:\n'))
        event_name = input('Enter the Event Name:\n')
        event_date = input('Enter the Event date:\n')
        venue = input('Enter the Venue:\n')
        buyer_name = input('Enter the Buyers Name:\n')
        buyer_email = input('Enter the Buyers Email:\n')
        buyer_phone = input('Enter the Buyers Phone:\n')
        seat_number = input('Enter the Seat number:\n')
        price = input('Enter the Price of the Ticket:\n')
        create_ticket(ticket_id,event_name,event_date,venue,buyer_name,buyer_email,buyer_phone,seat_number,price)
    elif choice == 2:
        id_to_update = int(input('Enter the id to be updated:\n'))
        n_ticket_id = int(input('Enter the new Ticket Id:\n'))
        n_event_name = input('Enter the new Event Name:\n')
        n_event_date = input('Enter the new Event date:\n')
        n_venue = input('Enter the new Venue:\n')
        n_buyer_name = input('Enter the new Buyers Name:\n')
        n_buyer_email = input('Enter the new Buyers Email:\n')
        n_buyer_phone = input('Enter the new Buyers Phone:\n')
        n_seat_number = input('Enter the new Seat number:\n')
        n_price = input('Enter the new Price of the Ticket:\n')
        update_ticket(id_to_update,n_ticket_id,n_event_name,n_event_date,n_venue,n_buyer_name,n_buyer_email,n_buyer_phone,n_seat_number,n_price)
    elif choice == 3:
        id_to_delete = int(input('Enter the Id to be Deleted:\n'))
        delete_ticket(id_to_delete)
    elif choice == 4:
        read_tickets()
    elif choice == 5:
        n_event_name = input('Enter the event name to search:\n')
        search_tickets(n_event_name)
    else:
        print('Invalid Choice......')

if __name__ == '__main__':
    main()