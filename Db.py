import json

from models.Finance import Finance
class Db:
    def __init__(self):
        self.db = 'data.json'
        self.finances = []
        self.load()

    def load(self):
        try:
            f = open(self.db)
        except:
            return

        data = json.load(f)
        self.finances = [Finance(x['datetime'], x['category'], x['money'], x['type'], x['note']) for x in data]
        f.close()

    def save(self):
        json_string = json.dumps([finance.__dict__ for finance in self.finances], indent=2)
        f = open(self.db, "w")
        f.write(json_string)
        f.close()

    def addFinance(self, finance):
        self.finances.append(finance)
        self.save()
