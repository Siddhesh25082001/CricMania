# ----------------------------------------------------------------------------------------------------------------------

#                                   ESD PROJECT : LIVE CRICKET SCOREBOARD 

# ----------------------------------------------------------------------------------------------------------------------

#                                           1. Setup for the Project

# importing flask module and other requirements
from flask import Flask, render_template, url_for
import cricapi
import json
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import urllib.request

# Creating an instance of the Flask (Flask constructor)
app = Flask(__name__)   # Placeholder for current module  

# Secret API KEY
apikey = "yMCxusKUnRVwUsKoM179MIoQ2tD3"

# Calling the API via authorized API KEY credentials
criapi = cricapi.Cricapi(apikey)

# ----------------------------------------------------------------------------------------------------------------------

#                                      2. Code of the Project

# A. Fetching the live score of all the intenational as well as domestic matches

lscore = json.dumps(criapi.cricket(), indent = 4)    # Storing the JSON response in the form of a string
live_score = json.loads(lscore)                      # Loading the JSON string
dict_ls = live_score['data']                         # Making a python list 

#                                 --------------------------------------

# B. Fetching the Upcoming Schedule of both international and domestic matches

uschedule = json.dumps(criapi.matches(), indent = 4) # Storing the JSON response in the form of a string
Upcoming_schedule = json.loads(uschedule)            # Loading the JSON string
schedule = Upcoming_schedule['matches']              # Making a python list 

# Declaring 3 empty lists each for name of team-1, team-2 and for date-time of their match
team_1 = []
team_2 = []
dateTimeGMT = []
matchStarted = []
squad = []
type_match = []
match_id = []

# Looping through the list of dictionaries (schedule) and storing the required data
for s in schedule:
        team_1.append(s['team-1'])
        team_2.append(s['team-2'])
        dateTimeGMT.append(s['dateTimeGMT'])
        matchStarted.append(s['matchStarted'])
        squad.append(s['squad'])
        type_match.append(s['squad'])
        match_id.append(s['unique_id'])
        
detail_schedule = list(zip(match_id, team_1, team_2, dateTimeGMT, matchStarted, squad, type_match, match_id))
upcoming_schedule = list(zip(team_1, team_2, dateTimeGMT))

#                                 --------------------------------------

# Home Page Route
@app.route('/')
def index():
    return render_template('index.html', dict_ls = dict_ls, upcoming_schedule = upcoming_schedule)

# Schedule Page Route
@app.route('/schedule')
def schedule():
    return render_template('schedule.html', detail_schedule = detail_schedule)


#                                --------------------------------------

# Batting Page Route
@app.route('/batting')
def batting():
    
    # Extracting batting information from cricbuzz website and then parsing it
    url = "https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')
        
    # Three sample lists for storing Tests, Odi, t20 players names, country and ratings (including all 3 formats)    
    Name = []
    Country = []
    Rating = []

    title = soup.find('h1', class_='cb-nav-hdr cb-font-24 line-ht30').text

    # Extracting Names of the Cricketers
    for names in soup.find_all('a', class_='text-hvr-underline text-bold cb-font-16'):
        Name.append(names.text)

    # Extracting Country's of the Cricketers
    for countrys in soup.find_all('div', class_='cb-font-12 text-gray'):
        Country.append(countrys.text)

    # # Extracting Rating of the Cricketers
    for rates in soup.find_all('div', class_='cb-col cb-col-17 cb-rank-tbl pull-right'):
        Rating.append(rates.text)


    # Creating three lists each for each formats to store their individual content

    # Three lists for tests
    Name_test = []
    Country_test = []
    Rating_test = []

    # Three lists for odi
    Name_odi = []
    Country_odi = []
    Rating_odi = []

    # Three lists for t20
    Name_t20 = []
    Country_t20 = []
    Rating_t20 = []

    # Appending in separate lists based on the count
    for i in range(len(Name)):
        if(i < 99):
            Name_test.append(Name[i])
            Country_test.append(Country[i])
            Rating_test.append(Rating[i])

        elif(i >= 99 and i < 199):
            Name_odi.append(Name[i])
            Country_odi.append(Country[i])
            Rating_odi.append(Rating[i])

        elif(i >= 199):
            Name_t20.append(Name[i])
            Country_t20.append(Country[i])
            Rating_t20.append(Rating[i])

    # Creating a Mega list of tuples for Batting-test, Batting-odi, Batting-t20
    answer_batting_test = list(zip(Name_test, Country_test, Rating_test))
    answer_batting_odi = list(zip(Name_odi, Country_odi, Rating_odi))
    answer_batting_t20 = list(zip(Name_t20, Country_t20, Rating_t20))

    return render_template('batting.html', answer_batting_test = answer_batting_test, answer_batting_odi = answer_batting_odi, answer_batting_t20 = answer_batting_t20)


#                                  --------------------------------------

# Bowling Page Route
@app.route('/bowling')
def bowling():
    
    # Extracting bowling information from cricbuzz website and then parsing it
    url = "https://www.cricbuzz.com/cricket-stats/icc-rankings/men/bowling"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')
        
    # Three sample lists for storing Tests, Odi, t20 players names, country and ratings (including all 3 formats)    
    Name = []
    Country = []
    Rating = []

    title = soup.find('h1', class_='cb-nav-hdr cb-font-24 line-ht30').text

    # Extracting Names of the Cricketers
    for names in soup.find_all('a', class_='text-hvr-underline text-bold cb-font-16'):
        Name.append(names.text)

    # Extracting Country's of the Cricketers
    for countrys in soup.find_all('div', class_='cb-font-12 text-gray'):
        Country.append(countrys.text)

    # # Extracting Rating of the Cricketers
    for rates in soup.find_all('div', class_='cb-col cb-col-17 cb-rank-tbl pull-right'):
        Rating.append(rates.text)

     # Creating three lists each for each formats to store their individual content

    # Three lists for tests
    Name_test = []
    Country_test = []
    Rating_test = []

    # Three lists for odi
    Name_odi = []
    Country_odi = []
    Rating_odi = []

    # Three lists for t20
    Name_t20 = []
    Country_t20 = []
    Rating_t20 = []

    # Appending in separate lists based on the count
    for i in range(len(Name)):
        if(i < 100):
            Name_test.append(Name[i])
            Country_test.append(Country[i])
            Rating_test.append(Rating[i])

        elif(i >= 100 and i < 200):
            Name_odi.append(Name[i])
            Country_odi.append(Country[i])
            Rating_odi.append(Rating[i])

        elif(i >= 200):
            Name_t20.append(Name[i])
            Country_t20.append(Country[i])
            Rating_t20.append(Rating[i])

    # Creating a Mega list of tuples for Bowling-test, Bowling-odi, Bowling-t20
    answer_bowling_test = list(zip(Name_test, Country_test, Rating_test))
    answer_bowling_odi = list(zip(Name_odi, Country_odi, Rating_odi))
    answer_bowling_t20 = list(zip(Name_t20, Country_t20, Rating_t20))

    return render_template('bowling.html', answer_bowling_test = answer_bowling_test, answer_bowling_odi = answer_bowling_odi, answer_bowling_t20 = answer_bowling_t20)

#                                  --------------------------------------

# All Rounder Page Route
@app.route('/all_rounder')
def all_rounder():
    
    # Extracting all-rounder information from cricbuzz website and then parsing it
    url = "https://www.cricbuzz.com/cricket-stats/icc-rankings/men/all-rounder"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')
        
    # Three sample lists for storing Tests, Odi, t20 players names, country and ratings (including all 3 formats)    
    Name = []
    Country = []
    Rating = []

    title = soup.find('h1', class_='cb-nav-hdr cb-font-24 line-ht30').text

    # Extracting Names of the Cricketers
    for names in soup.find_all('a', class_='text-hvr-underline text-bold cb-font-16'):
        Name.append(names.text)

    # Extracting Country's of the Cricketers
    for countrys in soup.find_all('div', class_='cb-font-12 text-gray'):
        Country.append(countrys.text)

    # # Extracting Rating of the Cricketers
    for rates in soup.find_all('div', class_='cb-col cb-col-17 cb-rank-tbl pull-right'):
        Rating.append(rates.text)

     # Creating three lists each for each formats to store their individual content

    # Three lists for tests
    Name_test = []
    Country_test = []
    Rating_test = []

    # Three lists for odi
    Name_odi = []
    Country_odi = []
    Rating_odi = []

    # Three lists for t20
    Name_t20 = []
    Country_t20 = []
    Rating_t20 = []

    # Appending in separate lists based on the count
    for i in range(len(Name)):
        if(i < 10):
            Name_test.append(Name[i])
            Country_test.append(Country[i])
            Rating_test.append(Rating[i])

        elif(i >= 10 and i < 20):
            Name_odi.append(Name[i])
            Country_odi.append(Country[i])
            Rating_odi.append(Rating[i])

        elif(i >= 20):
            Name_t20.append(Name[i])
            Country_t20.append(Country[i])
            Rating_t20.append(Rating[i])

    # Creating a Mega list of tuples for All-rounder-test, All-rounder-odi, All-rounder-t20
    answer_allrounder_test = list(zip(Name_test, Country_test, Rating_test))
    answer_allrounder_odi = list(zip(Name_odi, Country_odi, Rating_odi))
    answer_allrounder_t20 = list(zip(Name_t20, Country_t20, Rating_t20))

    return render_template('all-rounder.html', answer_allrounder_test = answer_allrounder_test, answer_allrounder_odi = answer_allrounder_odi, answer_allrounder_t20 = answer_allrounder_t20)

#                                  --------------------------------------

# Teams Page Route
@app.route('/teams')
def teams():

    # Extracting teams information from cricbuzz website and then parsing it
    url = "https://www.cricbuzz.com/cricket-stats/icc-rankings/men/teams"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')

    title = soup.find('h1', class_='cb-nav-hdr cb-font-24 line-ht30').text

    # Three sample lists for storing Tests, Odi, t20 Country names, ratings and points (including all 3 formats) 
    Country = []
    Rating = []
    Points = []

    score = [] # temporary for collecting all the ratings and points
        
    # Extracting Country's info 
    for names in soup.find_all('div', class_='cb-col cb-col-50 cb-lst-itm-sm text-left'):
        Country.append(names.text)

    # Extracting Rating and Points info together (due to same class-name)
    for rates in soup.find_all('div', class_='cb-col cb-col-14 cb-lst-itm-sm'):
        score.append(rates.text)

    # Segregating Ratings and Points in separate lists
    for i in range(len(score)):
        if (i % 2 == 0):
            Rating.append(score[i])
        else:
            Points.append(score[i])

    # Mega list for teams
    answer = list(zip(Country, Rating, Points))


    # Three lists for tests
    Country_test = []
    Rating_test = []
    Points_test = []

    # Three lists foor odi
    Country_odi = []
    Rating_odi = []
    Points_odi = []

    # Three lists for t20
    Country_t20 = []
    Rating_t20 = []
    Points_t20 = []

    # Appending to separate lists according to the count 
    for i in range(len(answer)):
        if(i < 10):
            Country_test.append(Country[i])
            Rating_test.append(Rating[i])
            Points_test.append(Points[i])

        elif(i >= 10 and i < 30):
            Country_odi.append(Country[i])
            Rating_odi.append(Rating[i])
            Points_odi.append(Points[i])
            
        elif(i >= 30):
            Country_t20.append(Country[i])
            Rating_t20.append(Rating[i])
            Points_t20.append(Points[i])

    # Creating a mega list for teams-test, teams-odi, teams-t20
    answer_Country_test = list(zip(Country_test, Rating_test, Points_test))
    answer_Country_odi = list(zip(Country_odi, Rating_odi, Points_odi))
    answer_Country_t20 = list(zip(Country_t20, Rating_t20, Points_t20))

    return render_template('teams.html', answer_Country_test = answer_Country_test, answer_Country_odi = answer_Country_odi, answer_Country_t20 = answer_Country_t20)

#                                  --------------------------------------

# Running the App
if __name__ == '__main__':
    app.run(debug = True) 

# ----------------------------------------------------------------------------------------------------------------------