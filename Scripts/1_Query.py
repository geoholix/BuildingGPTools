"""
Print out only "friendly" cats
"""
import os

from arcpy.da import SearchCursor

in_table = os.path.join(os.getcwd(), r"Intro_GP_Script_Tools_2018.gdb\Cat_Data")
field_names = ['OID@', 'Type']
sql = "friendly = 1"

output = '\nFriendly Cats:\n'

with SearchCursor(in_table, field_names, sql) as sc:
    for row in sc:
        output += 'OID: {0} -- {1} cat\n'.format(*row)
        
print(output)
arcpy.AddMessage(output)
