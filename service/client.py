""" Class representing a client
    """
class Client():

    def __init__(self, name, last_name, doc_id):
        self.name = name
        self.last_name = last_name
        self.doc_id = doc_id
        self.preexistence = []

        ******* adds preexitence cliente  
        ***
        
    def add_preexistence(self, nPreexistence):
        self.preexistence.append(nPreexistence)
        return len(self.preexistence) - 1
        
        ******* adds preexitence cliente  
        ***

    def get_preexistence(self, pIndex):
        if pIndex >= len(self.preexistence):
            return 'There is no such preexistence'
        else:
            return self.preexistence[pIndex]

    def get_all_preexistence(self):
        return self.preexistence

    def remove_preexistence(self, n_preexistence):
        self.preexistence.pop(n_preexistence)
        return len(self.preexistence) - 1

    def get_formatted_name(self):
        return self.name + ' ' + self.last_name


if __name__ == '__main__':
    client_instance = Client('uno', 'dos', '113565')
    print('User Abbas has been added with id ', client_instance.get_formatted_name())
