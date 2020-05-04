#!/usr/bin/python3
import sys
import requests
from lxml import html
import re
import MySQLdb
import uuid


def add_states_with_cities(number_states=1, number_cities=0):
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    res = {}
    for i in range(number_states):
        state_id = str(uuid.uuid4())
        
        cur.execute("INSERT INTO `states` (id, created_at, updated_at, name) VALUES ('{}','2016-03-25 19:42:40','2016-03-25 19:42:40','state{}');".format(state_id, i))
        cities = []
        for j in range(number_cities):
            city_id = str(uuid.uuid4())
            cities.append(city_id)
            cur.execute("INSERT INTO `cities` (id, state_id, created_at, updated_at, name) VALUES ('{}', '{}','2016-03-25 19:42:40','2016-03-25 19:42:40','city{}{}');".format(city_id, state_id, i, j))

        res[state_id] = len(cities)

    conn.commit()
    cur.close()
    conn.close()
    
    return res


def add_cities_to_state(state_id, number_cities=0):
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    
    for j in range(number_cities):
        city_id = str(uuid.uuid4())
        cur.execute("INSERT INTO `cities` (id, state_id, created_at, updated_at, name) VALUES ('{}', '{}','2016-03-25 19:42:40','2016-03-25 19:42:40','city{}');".format(city_id, state_id, j))

    conn.commit()
    cur.close()
    conn.close()


def validate_number_state(number):
    
    NO_PROXY = {
        'no': 'pass',
    }

    ## Request
    page = requests.get('http://0.0.0.0:5000/states', proxies=NO_PROXY)
    if int(page.status_code) != 200:
        return False, "Status fail: {}".format(page.status_code)

    ## Parsing
    tree = html.fromstring(page.content)
    if tree is None:
        return False, "Can't parse page"

    # LI tags
    li_tags = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/text()')]))
    if li_tags is None or len(li_tags) != number:
        return False, "Doesn't find {} LI tags (found {})".format(number, len(li_tags))

    return True, None


def validate_number_cities(state_id, number):
    NO_PROXY = {
        'no': 'pass',
    }

    ## Request
    page = requests.get("http://0.0.0.0:5000/states/{}".format(state_id), proxies=NO_PROXY)
    if int(page.status_code) != 200:
        return False, "Status fail: {}".format(page.status_code)

    ## Parsing
    tree = html.fromstring(page.content)
    if tree is None:
        return False, "Can't parse page"

    li_tags_el_cities = tree.xpath('//body/ul/li')
    if li_tags_el_cities is None or len(li_tags_el_cities) != number:
        return False, "Doesn't find {} LI City tags (found {})".format(number, len(li_tags_el_cities))
        
    return True, None


# Test initial state
res, msg = validate_number_state(2)
if not res:
    print("ERROR: {}".format(msg))

initial_states = { "f2ab504a-503d-4216-b4e3-d6ee676d0f16": 3, "d2ab504a-503d-4216-b4e3-d6ee676d0f16": 2 }    
for state_id in initial_states.keys():
    res, msg = validate_number_cities(state_id, initial_states[state_id])
    if not res:
        print("ERROR: {}".format(msg))


# Add 1 new state with 2 cities
new_map = add_states_with_cities(1, 2)

res, msg = validate_number_state(3)
if not res:
    print("ERROR: {}".format(msg))

for state_id in initial_states.keys():
    res, msg = validate_number_cities(state_id, initial_states[state_id])
    if not res:
        print("ERROR: {}".format(msg))

state_id = list(new_map.keys())[0]
res, msg = validate_number_cities(state_id, new_map[state_id])
if not res:
    print("ERROR: {}".format(msg))


# Add 1 city to the new state
add_cities_to_state(state_id, 1)

res, msg = validate_number_cities(state_id, new_map[state_id] + 1)
if not res:
    print("ERROR: {}".format(msg))


print("OK", end="")
