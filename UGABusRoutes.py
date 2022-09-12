#   Ways to Improve:
# 2) Add a Night Campus and Weekender Bus routes option
# 6) Make program more accessible (Web app or phone app)

import pyautogui

All_places = ["Aderhold","BDM Hall","Botanical Gardens","Building F","Building G","Building H","Building P",
        "Building Q","Building S","Brandon Oaks","Broad Street Studios", 
        "CCRC","Chemistry","Chicopee","Clarke Central","Conner Hall","Correll Hall","Coverdell",
        "Creswell Hall","Driftmier","East Campus Village","Food Science",
        "Gilbert Hall","Greenhouses","Health Science Campus","Henderson Ave.","I-Fields (College Station",
        "Intramural Fields","Intramural Fields Deck","Intramural Fields Lot EO1","Jamestown",
        "Joe Frank Harris","Learning & Development","Lucy Cobb","Rutherord St",
        "Main Library","Memorial Hall","Multi-Modal Center","Myers Quad","Nacoochee Ave.",
        "Newton St.","Oakland Ave.","Oglethorpe Dining","Park and Ride","Peabody St.","Physics"
        "Plant Science","Poultry Diagnostic & Rsch Center","Presbyterian Center","Psychology-Journalism",
        "Rivers Crossing","Rogers Rd","Russell Hall","Rutherford Hall","Rutherford St.",
        "School of Social Work","Science Learning Center","Snelling Dining","Soccer Softball"
        "Spring St.","Springdale St.","Stegeman Coliseum","STEM Building","Tate Center",
        "The Arch","Transit","Tucker Hall","UGA Automotive Center","UGA Human Resources",
        "University Health Center","Veterinary Medical Learning Center","Waddell St."]

CentralLoopStops = ["Memorial Hall","Tate Center","Gilbert Hall","The Arch","Arch","Main Library","Tucker Hall",
        "Joe Frank Harris","University Health Center","UHC","East Campus Village","Aderhold Hall",
        "Plant Sciences","Science Learning Center","SLC","Snelling Dining","Snelling","Physics"]

NorthSouthConnectorStops = ["Tate Center","Memorial Hall","Physics","Myers Quad","Meyers","Stegeman Coliseum","Stegeman","Science Learning Center",
        "SLC","Coverdell","Driftmier","Tucker Hall","Main Library","Psychology-Journalism","PJ"]

EastCampusStops = ["Memorial Hall","Gilbert Hall","The Arch","Arch","Main Library","Tate Center",
        "Physics","Connor Hall","STEM Building","Tucker Hall","Joe Frank Harris","JFM",
        "University Health Center","UHC","Intramural Fields Deck","Intramural Fields Lot EO1",
        "East Campus Village","Food Science","Chemistry","Conner Hall"]

WestCampusStops = ["Oglethorpe Dining","Oglethorpe","Rutherford Hall","Physics","Memorial Hall","Tate Center",
        "Gilbert Hall","The Arch","Arch","Transit","Main Library","Psychology-Journalism","PJ",
        "Correll Hall","Russell Hall","Russell"]

CrossCampusStops = ["Russell Hall","Russell","Oglethorpe Dining","Oglethorpe","Rutherford Hall","Conner Hall",
        "STEM Building","Tucker Hall","Joe Frank Harris","JFH","University Health Center","UHC",
        "East Campus Village","Tucker Hall","Food Science","Chemistry","Conner Hall","Physics","Memorial Hall","Tate Center",
        "Correll Hall"]

BulldogHousingStops = ["Building S","Building Q","Building P","Rogers Rd.","Building G","Driftmier",
        "Science Learning Center","SLC","Snelling Dining","Snelling","Physics","Memorial Hall","Tate Center","Correll Hall",
        "BDM Hall","BDM","Creswell Hall","Oglethorpe Dining","Oglethorpe","Rutherford Hall","Myers Quad","Meyers","Stegeman Coliseum",
        "Stegeman","Aderhold Hall","Joe Frank Harris","JFH","University Health Center","UHC","Building H","Brandon Oaks","Jamestown"]

ParkAndRideStops = ["Park and Ride","Intramural Fields Deck","Intramural Fields Lot EO1","East Campus Village",
        "Tucker Hall","Food Science","Chemistry","Conner Hall","Physics","Memorial Hall","Tate Center","Human Resources","Spring St.","Tucker Hall",
        "Joe Frank Harris","JFH","University Health Center","UHC"]

VetMedStops = ["Veterinary Medical Learning Center","PDRC","Park and Ride","East Campus Village","Aderhold Hall",
        "Plant Sciences","Coverdell Hall","Driftmier","Building F","Intramural Fields","Park and Ride","Rivers Crossing"]

HealthSciencesStops = ["Health Science Campus","Lucy Cobb","Clarke Central","Springdale St.","Oakland Ave.",
        "Snelling Dining","Snelling","Physics","Memorial Hall","Tate Center","Gilbert Hall","Nacoochee Ave"]

MilledgeAveStops = ["Tate Center","Memorial Hall","Physics","Myers Quad","Presbyterian Center","Rutherford Hall","Oakland Ave.","Rutherford St.",
        "Peabody St.","Henderson Ave.","Waddell St.","Newton St.","The Arch","Main Library","Psychology-Journalism","PJ"]

UGABusRoutes = {
        "CentralLoopStops": CentralLoopStops,
        "NorthSouthConnectorStops": NorthSouthConnectorStops,
        "EastCampusStops": EastCampusStops,
        "WestCampusStops": WestCampusStops,
        "CrossCampusStops": CrossCampusStops,
        "BulldogHousingStops": BulldogHousingStops,
        "ParkAndRideStops": ParkAndRideStops,
        "VetMedStops": VetMedStops,
        "HealthSciencesStops": HealthSciencesStops,
        "MilledgeAveStops": MilledgeAveStops
}

popularStops = ["Conner Hall","Correll Hall (Closest to Lipscomb/Bolton)","Joe Frank Harris (JFH)","Memorial Hall (Tate Center)", "Oglethorpe","Snelling","The Arch","University Health Center (UHC)","Science Learning Center (SLC)"]

for route in UGABusRoutes:
        UGABusRoutes[route] = [stop.lower() for stop in UGABusRoutes[route]]

while True:
        position = pyautogui.prompt(text='These are some popular stops: '+ str(popularStops), title='Where are you?',default='')
        if position == "exit" or position == "quit":
                break
        destination = pyautogui.prompt(text='These are some popular stops: '+ str(popularStops),title='Where are you going?',default='')
        if destination == "exit" or destination == "quit":
                break
        PossibleRoutes = []

        for route in UGABusRoutes:
                if position.lower().strip() in UGABusRoutes[route] and destination.lower().strip() in UGABusRoutes[route]:
                        PossibleRoutes.append(route)

        if len(PossibleRoutes) == 0:
                pyautogui.alert(text='Unfortunately, there are no routes that fufill your request.',title='Possible Routes',button='OK')
        else:     
                pyautogui.alert(text='These are the possible routes you can take: '+str(PossibleRoutes),title='Possible Routes',button='OK')

        if pyautogui.confirm(text='Do you have any more queries?',title='Would you like to continue?',buttons=['No','Yes']) == "No":
                break