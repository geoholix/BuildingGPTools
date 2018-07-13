"""
Reports friendly cats and uses parameters from the user
"""

from arcpy import AddMessage
from arcpy import GetParameterAsText
from arcpy.da import SearchCursor

in_table = GetParameterAsText(0)  # Feature Layer  -- What happens here? Is a tuple returned from parameters in Pro?
friendly_field = GetParameterAsText(1)  # Integer

where_clause = '{0} = 1'.format(friendly_field)
field_names = ['OID@', 'Type']

output = ''

with SearchCursor(in_table, field_names, where_clause) as sc:
    output += '\nFriendly Cats:\n'
    for row in sc:
        output += '    OID: {0} -- {1} cat\n'.format(*row)
        
AddMessage(output)
