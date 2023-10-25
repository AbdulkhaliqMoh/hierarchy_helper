import random
from django.db import transaction
from faker import Faker
from org_tree.models import OrganizationUnit

# Initialize a Faker generator.
# Faker is a library that allows you to create fake data, which is especially useful for testing.
fake = Faker()

# This decorator ensures that all database operations within the function are atomic.
# This means that if an error occurs, all changes made within the function will be rolled back,
# leaving the database in a consistent state.
@transaction.atomic
def create_random_organization_units(num_units):
    # This list will store the created OrganizationUnit instances.
    units = []
    
    # Loop to create the specified number of OrganizationUnit instances.
    for _ in range(num_units):
        # Dictionary to store the data for the new OrganizationUnit instance.
        unit_data = {
            'name': fake.company(),
            'manager_email': fake.email(),
            'manager_name': fake.name(),
            'manager_title': fake.job(),
            'manager_level': fake.word(),
            'manager_level_desc': fake.sentence(),
            'parent': None  # Default to None, will be set later if there are other units.
        }
        
        # If there are already units created, randomly assign a parent from those units.
        if units:
            unit_data['parent'] = random.choice(units + [None])
        
        # Create a new OrganizationUnit instance and add it to the units list.
        unit = OrganizationUnit.objects.create(**unit_data)
        units.append(unit)
        
    # Return the list of created OrganizationUnit instances.
    return units
