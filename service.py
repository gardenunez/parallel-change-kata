import dao

class SuperHero():
    def __init__(self):
        self.data = list(dao.load_data())
        
    def get_name_by_id(self, record_id):
        for row in self.data:
            if row['id'] == record_id:
                return row['name']
        return None

    def get_lenght(self):
        return len(self.data)
