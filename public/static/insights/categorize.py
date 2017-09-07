import requests
import csv
import time
import sys
import json

def geoclassify(lat, lng):
    """
    Check the GPS coordinates of a place to find a nice match
    """
    # zone1boundingpoints = [ [x, y], [x, y] ] # top left and bottom right
    # if is_contained(lat, lng, zone1boudningpoints)
    #     assign to zone 1

    # etc

def categorize(street):
    """
    First, check for a direct match of known names of dorms and academic buildings
    If nothing found then use the geoclassifier
    """
    # South campus dorms
    SCD = [
        "CRAIGE",
        "EHRINGHAUS", 
        "HINTON JAMES",
        "MORRISON",
        "KOURY",
        "CRAIGE NORTH",
        "HORTON",
        "HARDIN",
        "RAMS VILLAGE",
        "VILLAGE"
    ] # Freshman dorms
    
    # Main campus dorms
    MCD = ["MANLY",
        "RUFFIN",
        "AYCOCK",
        "MANGUM",
        "MANLY",
        "GRAHAM",
        "OLD EAST",
        "OLD WEST",
        "COBB",
        "JOYNER",
        "ALEXANDER",
        "CONNOR",
        "WINSTON",
        "GRAHAM",
        "EVERETT",
        "LEWIS",
        "MCIVER",
        "STACY",
        "ALDERMAN",
        "SPENCER",
        "GRIMES",
        "CARMICHAEL",
        "PARKER",
        "TEAGUE"
    ]
    
    # On campus
    ACB = [ 
        "LENOIR", 
        "GENOME", 
        "STONE CENTER", 
        "HOUSE LIBRARY", 
        "DAVIS",
        "STUDENT UNION",
        "PEABODY",
        "MCCOLL",
        "MCCOLL BUSINESS",
        "DENTAL",
        "BONDURANT",
        "MEDICAL SCHOOL",
        "VAN HECKE",
        "MCGAVRAN",
        "GREENBERG", 
        "HILL",
        "MED SCH",
        "FETZER GYM",
        "GARDNER",
        "GRAHAM STUDENT UNION",
        "GREENLAW", 
        "DEY",
        "BINGHAM",
        "MURPHEY",
        "HANES ART",
        "HANES",
        "MITCHELL",
        "MURRAY",
        "VENABLE",
        "CARROLL",
        "SAUNDERS",
        "CAROLINA HALL",
        "STUDENT HEALTH",
        "CAMPUS HEALTH",
        "ARBORETUM",
        "PLANETARIUM",
        "MOREHEAD",
        "BELL TOWER",
        "HAMILTON",
        "KNAPP",
        "CALDWELL",
        "CHAPMAN",
        "PHILLIPS",
        "SITTERSON",
        "BROOKS",
        "SWAIN",
        "COKER",
        "WILSON",
        "FORDHAM",
        "WHITEHEAD",
        "FEDEX GLOBAL",
        "CARR",
        "DAVIE",
        "STEELE",
        "BYNUM",
        "PLAYMAKERS",
        "PLAY-MAKERS",
        "STUDENT STORE",
        "DANIELS STUDENT STORE",
        "STUDENT STORE",
        "HOWELL",
        "WOOLLEN",
        "POLK PLACE",
        "BRAUER",
        "BIOINFORMATICS",
        "RECREATION",
        "BENNETT",
        "BOWLES",
        "BOSHAMER",
        "BERRYHILL",
        "BEARD",
        "HOOKER",
        "LOUDERMILK",
        "PUBLIC SAFETY"
    ]

    # B School
    BUS = [
        "BUSINESS"
        ]
    # Hospitals
    HSP = [
        "HOSPITAL",
        "CARE CENTER",
        "EMERGENCY",
        "AMBULATORY"
    ]

    # Arbitrary streets including parking lots
    ARS = [
        " RD",
        " DR",
        " AVE",
        " BLVD",
        "PARKING",
        " ST",
        "ROAD",
        "STREET",
        "AVENUE",
        "BOULEVARD",
        "DRIVE"
    ]
    # Northside
    # Academic Building

    street = street.upper()

    for i in BUS:
        if i in street:
            return "BUS"
    for i in SCD:
        if i in street:
            return "SCD"
    for i in MCD:
        if i in street:
            return "MCD"
    for i in ACB:
        if i in street:
            return "ACB"

    for i in ARS:
        if i in street:
            return "ARS"
    
    for i in HSP:
        if i in street:
            return "HSP"

    return "NAN"


input_file = sys.argv[1]
output_file = "categorized.csv"


### READ THE ORIGINAL CSV ###
reader = csv.DictReader(open(input_file))
num_rows = reader.line_num

result = {}
for row in reader:
    for column, value in row.items():
        result.setdefault(column, []).append(value)

num_rows = reader.line_num

### MAKE A NEW CSV INCLUDING GEOCODED LAT AND LONG ###
business = [["inci_id", "offense", "date_rept", "street", "zone", "date_occu", "csstatus"]]# [[id, offense, date_rep, street, date_occu, csstatus], ...]

# Track the count for these categories outlined above
nan = 0
scd = 0
mcd = 0
acb = 0
ars = 0
hsp = 0
bus = 0
unc_count = 0

# For every incident ID, ie number of rows
for i in range(1, num_rows - 1):
    inci_id = result['inci_id'][i]
    offense = result['offense'][i]
    date_rept = result['date_rept'][i]
    street = result['street'][i]
    date_occu = result['date_occu'][i]
    csstatus = result['csstatus'][i]
    zone = categorize(street)

    if "AIRPORT" in street.upper():
        print(street.upper())
        print(" RD" in street.upper())

    if "UNC" in street.upper():
        unc_count += 1

    if zone == "SCD":
        scd += 1
    elif zone == "MCD":
        mcd += 1
    elif zone == "ACB":
        acb += 1
    elif zone == "ARS":
        ars += 1
    elif zone == "HSP":
        hsp += 1
    elif zone == "NAN":
        pass


    if inci_id is None:
        inci_id = "None"
    if offense is None:
        offense = "None"
    if date_rept is None:
        date_rept = "None"
    if street is None:
        street = "None"
    if date_occu is None:
        date_occu = "None"
    if csstatus is None:
        csstatus = "None"
    
    business.append([
        inci_id,
        offense,
        date_rept,
        street,
        zone,
        date_occu,
        csstatus])

# This writes a list of lists
with open(output_file, "wt") as f:
    writer = csv.writer(f)
    writer.writerows(business)

#                UNCOMMENT THIS TO WRITE RESULTS TO A JSON FILE          #
# Write json
data = {
    "SCD": scd,
    "MCD": mcd,
    "ACB": acb,
    "UNC": unc_count,
    "HSP": hsp,
    "ARS": ars
    }

with open("counts.json", "wt") as f:
    json.dump(data, f)











def analyze(data):
    pass

print()
print()
print("*** *** *** *** *** *** *** *** ***")
print(json.dumps(data))
print()
print("Failures: %s" % (num_rows + unc_count - sum(data.values())))
print("*** *** *** *** ***")
print()
print()