# sqlalchemy-challenge

Unit 10 Homework

### Step 1 - Climate Analysis & Exploration

##### Objective:

Using Python and SQLAlchemy , complete a basic climate analysis and data exploration of the climate database (hawaii.sqlite). The following analysis is displayed in Jupyter Notebook file (climate_starter.ipynb) using SQLAlchemy ORM queries, Pandas, and Matplotlib for the analysis.

##### SQL Alchemy:

* Use SQLAlchemy `create_engine` to connect to your sqlite database.

* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

* Link Python to the database by creating an SQLAlchemy session.

* **Important** Don't forget to close out your session at the end of your notebook.

##### Precipitation Analysis

* Find the most recent date in the data set and retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. 
* Select only the `date` and `prcp` values and plot the results.

##### Station Analysis

* Design a query to calculate the total number of stations in the dataset.

* Design a query to find the most active stations (i.e., which stations have the most rows?).

  * List the stations and observation counts in descending order.

  * List the station id that has the highest number of observations.

  * Using the most active station id, calculate the lowest, highest, and average temperature.

* Design a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filter by the station with the highest number of observations.
  * Query the last 12 months of temperature observation data for this station and plot the results as a histogram.

## Step 2 - Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed (app.py)

### Routes

* `/`

  * Home page listing all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Returns the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.

  * Returns a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.



