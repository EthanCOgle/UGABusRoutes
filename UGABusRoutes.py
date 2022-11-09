#   Ways to Improve:
# 2) Add a Night Campus and Weekender Bus routes option
# 6) Make program more accessible (Web app or phone app)

from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/', methods=["GET","POST"])
def home():
        if request.method == "POST":
                position = (str)(request.form["position"])
                destination = (str)(request.form["destination"])
                PossibleRoutes = []
                for route in UGABusRoutes:
                        if position.lower().strip() in UGABusRoutes[route] and destination.lower().strip() in UGABusRoutes[route]:
                                PossibleRoutes.append(route)
                
                return render_template("base.html", PossibleRoutes=PossibleRoutes)
        if request.method == "GET":
                return render_template("base.html", PossibleRoutes=[])

if __name__ == "__main__":
        app.run(debug=True)
