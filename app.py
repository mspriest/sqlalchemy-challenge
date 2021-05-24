import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


################################################
# Flask Routes
################################################


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Convert the query results to a dictionary using `date` as the key and `prcp` as the value"""
    # Query all Precipitation
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= '2016-08-23').\
    all()
    
    session.close()

    # Convert list of tuples into normal list
    all_prcp = []
    for date,prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp

        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)


@app.route("/api/v1.0/stations")
def stations():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of stations from the dataset"""
     # Query stations in the data set
    results = session.query(Station.station).all()

    session.close()

     # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of temperature observations (TOBS) for the previous year."""
     # Query the dates and temperature observations of the most active station for the last year of data.
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= "2016-08-24").\
        filter(Measurement.station == 'USC00519281').all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs = []
    for date,tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs

        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def Start(start):

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of temperature observations (TOBS) for the previous year."""
     # Query min, max and avg temperature observations based on given start date.
    results = session.query(func.min(Measurement.tobs),
              func.max(Measurement.tobs),
              func.avg(Measurement.tobs)).\
              filter(Measurement.date >= start).all()

    session.close()

    # Convert list of tuples into normal list
    start_tobs = []
    for min, max, avg in results:
        start_tobs_dict = {}
        start_tobs_dict["min_tobs"] = min
        start_tobs_dict["max_tobs"] = max
        start_tobs_dict["avg_tobs"] = avg

        start_tobs.append(start_tobs_dict)
    print (start_tobs)
    return jsonify(start_tobs)

@app.route("/api/v1.0/<start>/<end>")
def Start_End(start,end):

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of temperature observations (TOBS) for the previous year."""
     # Query the dates and temperature observations of the most active station for the last year of data.
    results = session.query(func.min(Measurement.tobs),
              func.max(Measurement.tobs),
              func.avg(Measurement.tobs)).\
              filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()

    # Convert list of tuples into normal list
    start_end_tobs = []
    for min, max, avg in results:
        start_end_tobs_dict = {}
        start_end_tobs_dict["min_tobs"] = min
        start_end_tobs_dict["max_tobs"] = max
        start_end_tobs_dict["avg_tobs"] = avg

        start_end_tobs.append(start_end_tobs_dict)

    return jsonify(start_end_tobs)

if __name__ == '__main__':
    app.run(debug=True)