from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

db = "sasquatch_schema"
class Sighting:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.description = data['description']
        self.date_made = data['date_made']
        self.num_sasquatch = data['num_sasquatch']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None

    @staticmethod
    def validate_sighting(form_data):
        is_valid = True

        if len(form_data['name']) < 3:
            flash("Names need to be at least 3 characters long.")
            is_valid = False
        if len(form_data['location']) < 3:
            flash("Locations need to be at least 3 characters long.")
            is_valid = False
        if len(form_data['description']) < 3:
            flash("Descriptions need to be at least 3 characters long.")
            is_valid = False
        if form_data['date_made'] == '':
            flash("Please select a sighted date.")
            is_valid = False
        if 'num_sasquatch' not in form_data:
            flash("Please select a number of sasquatch")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sightings JOIN users on sightings.user_id = users.id;"
                
        results = connectToMySQL(db).query_db(query)
        sightings = []
        for result in results:
            this_sighting = cls(result)
            this_sighting.creator = user.User.get_by_id({'id': result['user_id']})
            sightings.append(this_sighting)
            
        return sightings

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM sightings JOIN users on sightings.user_id = users.id WHERE sightings.id = %(id)s;"

        result = connectToMySQL(db).query_db(query,data)
        if not result:
            return False
        this_sighting = cls(result[0])
        this_sighting.creator = user.User.get_by_id({'id': result[0]['user_id']})
        
        return this_sighting

    @classmethod
    def save_sighting(cls, form_data):
        query = "INSERT INTO sightings (name,location,description,date_made,num_sasquatch,user_id) VALUES (%(name)s,%(location)s,%(description)s,%(date_made)s,%(num_sasquatch)s,%(user_id)s);" 
        
        return connectToMySQL(db).query_db(query,form_data)

    @classmethod
    def update_sighting(cls,form_data):
        query = "UPDATE sightings SET name = %(name)s, location = %(location)s, description = %(description)s , date_made = %(date_made)s, num_sasquatch = %(num_sasquatch)s WHERE id = %(id)s;"
        
        return connectToMySQL(db).query_db(query,form_data)
    
    @classmethod
    def delete_sighting(cls,data):
        query = "DELETE FROM sightings WHERE id = %(id)s"
        
        return connectToMySQL(db).query_db(query,data)
