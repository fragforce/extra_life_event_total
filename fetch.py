#!/usr/bin/env python3
import datetime
import json
import pytz
import requests

utc = pytz.UTC
START_DATE=utc.localize(datetime.datetime(2020, 10, 2, 13, 0, 0))
END_DATE=utc.localize(datetime.datetime(2020, 10, 5, 19, 0, 0))
TEAMID=50229

DONATION_URL='https://extra-life.org/api/teams/' + str(TEAMID) + '/donations'

def fetch_single_donation(offset=1):
  payload = {'offset': offset}
  data = []
  r = requests.get(DONATION_URL, params=payload)
  if r.status_code == requests.codes.ok:
    data = r.json()
    headers = r.headers
    return data, headers

def fetch_all_donations():
  total_donations = 0
  donation_list = []
  data, headers = fetch_single_donation()
  donation_list.append(parse_json_donations(data))
  total_donations = int(headers['Num-Records'])
  print("Total Donations: " + str(total_donations))
  current_offset = 100
  while total_donations > current_offset:
    data, headers = fetch_single_donation(current_offset)
    current_offset += 100
    donation_list.append(parse_json_donations(data))
  return donation_list

def parse_json_donations(json_data):
  donation_list = []
  for item in json_data:
    donation_data = {"amount": None, "date": None}
    if 'amount' in item:
      donation_data['amount'] = item['amount']
    donation_data['date'] = datetime.datetime.strptime(item['createdDateUTC'], "%Y-%m-%dT%H:%M:%S.%f%z")
    donation_list.append(donation_data)
  return donation_list

donation_list = fetch_all_donations()
#with open('data.json') as f:
#  data = json.load(f)

donation_sum = 0
donations_in_range = []

for item in donation_list[0]:
  if START_DATE < item['date'] < END_DATE: 
    donations_in_range.append(item)
    if 'amount' in item:
      donation_sum += item['amount']

print("Total donations between date endpoints: " + str(donation_sum))
#print(donation_list)
