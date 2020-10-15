# Extra Life Event TOtal
Quick tool to parse all donations for an Extra Life team and add up all donations during a date range

# Howto:
* Install pipenv and python 3 to your system first
* Create a pipenv for the project ```pipenv --python <path to python3 binary>```
* run ```pipenv install``` to install all dependencies
* Edit fetch.py and change the required variables
    1. TEAMID = The teamid of the Extra Life team you want to parse
    2. START_DATE = The UTC datetime that you want to mark as the start of your event
    3. END_DATE = The UTC datetime that you want to mark as the end of your event
* Enable the pipenv shell ```pipenv shell```
* Run the code ```python fetch.py```
