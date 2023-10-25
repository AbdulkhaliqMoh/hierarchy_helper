from django.shortcuts import render
from django.template.loader import get_template

from .models import OrganizationUnit
from .utiles import create_random_organization_units

def construct_units_list_children_html(children):
    # Construct an HTML ordered list for the child units.
    html = '<ol>'
    html += construct_units_list_html(children)
    html += '</ol>'
    return html

def construct_units_list_html(units):
    # Initialize an empty string to hold the HTML content.
    html = ''
    
    # Loop through each organization unit.
    for unit in units:
        # Retrieve the child units of the current unit, ordered by ID in descending order.
        children = unit.children.order_by('-id').all()
        # Check if the current unit has any child units.
        has_children = children.exists()
        
        # Render the HTML for the current unit and append it to the HTML string.
        # The context includes the unit itself and a flag indicating if it has children.
        html += get_template('organization_unit_item.html').render(
            {'unit': unit, 'has_children': has_children})
        
        # If the unit has children, recursively construct their HTML and append it.
        if has_children:
            html += construct_units_list_children_html(children)

    # Return the constructed HTML string.
    return html

def units_list(request):
    # Uncomment the line below to create 20 random organization units.
    # This should generally be done through a management command or script, not in a view.
    # create_random_organization_units(20)
    
    # Retrieve all organization units, ordered by ID, and prefetch their child units.
    units = OrganizationUnit.objects.order_by('id').all().prefetch_related('children')
    # Construct the HTML for the list of units.
    list_html = construct_units_list_html(units)
    
    # Render the units_list template, passing the constructed HTML as context.
    return render(request, 'units_list.html', {'unit_list_html': list_html})
