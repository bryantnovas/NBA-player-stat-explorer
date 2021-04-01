# NBA Player Stats Explorer

![logo](https://media.tenor.com/images/426aa93de195958c7bb2407c29af2209/tenor.gif) 

This app performs simple webscraping and api serving of NBA player stats data!
* **Python libraries:** base64, pandas, streamlit, flask, sqlalchemy
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/)


## About:

This app is served on [heroku](https://nba-player-stats-explorer.herokuapp.com/) but do to the constrians of streamlit currently being unable to serve REST APIs and not being able to easily integrate with other REST libraries such as Flask, Django or FastApi, I decided to host my API as it's own dyno on heroku as well [here](https://nba-stat-api.herokuapp.com/api?year=2020)


## Usage:

The functionality of the streamlit app is pretty straight forward, you select a team based on year from 1950 to 2020, then you can further filter by removing teams and or positions. Finally at the bottom of the page by selecting a specific chart you will get some visual representations.


the API [https://nba-stat-api.herokuapp.com/api](https://nba-stat-api.herokuapp.com/api) has to be provided at least the year you want to return, also there's a default limit of 10 entries since it would be unnecessary and unpractical to send the whole 2600+ entries in one json object.

**example:**
 ```
    https://nba-stat-api.herokuapp.com/api?year=2020&limit=15
    
  ```

## Contact
---------------------
Bryant Novas - [Linkedin](https://www.linkedin.com/in/bryantnovas/)