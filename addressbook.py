from collections import defaultdict
class AddressBook:
    def __init__(self):
        self.city_map = defaultdict(list)
        self.state_map = defaultdict(list)
        self.contacts = []

    def is_duplicate(self, first_name, last_name):
        return any(contact.first_name == first_name and contact.last_name == last_name for contact in self.contacts)

    def add_contact(self, contact):
        if self.is_duplicate(contact.first_name, contact.last_name):
            print(f"Duplicate entry: {contact.first_name} {contact.last_name} already exists.")
            return False
        self.contacts.append(contact)
        self.city_map[contact.city].append(contact)
        self.state_map[contact.state].append(contact)
        print(f"Contact added successfully: {contact}")
        return True
        
    def edit_contact(self, first_name, updated_contact):
        for index, contact in enumerate(self.contacts):
            if contact.first_name == first_name:
                self.contacts[index] = updated_contact
                old_city = contact.city
                old_state = contact.state
                self.contacts[index] = updated_contact
                self.city_map[old_city].remove(contact)
                self.state_map[old_state].remove(contact)
                self.city_map[updated_contact.city].append(updated_contact)
                self.state_map[updated_contact.state].append(updated_contact)
                return True
        return False
    
    def delete_contact(self, first_name):
        for contact in self.contacts:
            if contact.first_name == first_name:
                self.contacts.remove(contact)
                return True
        return False
    
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)
    
    def search_by_city_or_state(self, city=None, state=None):
        results = []
        city_count = 0
        state_count = 0

        if city:
            city_contacts = self.city_map.get(city, [])
            results.extend(city_contacts)
            city_count = len(city_contacts)
        
        if state:
            state_contacts = self.state_map.get(state, [])
            results.extend(state_contacts)
            state_count = len(state_contacts)
        
        return results, city_count, state_count

