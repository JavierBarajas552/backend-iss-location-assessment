#!/usr/bin/env python

__author__ = 'Javier Barajas'

import requests
import turtle
import tkinter
import time


def people_in_space():
    r = requests.get('http://api.open-notify.org/astros.json')
    for person in r.json().get('people'):
        print(person.get('name') + ' is abord the ' + person.get('craft'))
    print('There are ' + str(r.json().get('number')) + ' people in space')
    pass


def lat_lon_iss():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    return r.json().get('iss_position')


def turtle_map(latlon):
    tr = turtle
    iss = tr.Turtle()
    tr.Screen().register_shape('iss.gif')
    tr.Screen().bgpic('map.gif')
    tr.Screen().setup(720, 360)
    tr.Screen().setworldcoordinates(-180, -90, 180, 90)
    iss.shape('iss.gif')
    iss.penup()
    iss.goto(float(latlon.get('longitude')),
             float(latlon.get('latitude')))
    tr.Screen().exitonclick()
    pass


def indi_when():
    r = requests.get(
        'http://api.open-notify.org/iss-pass.json', {'lat': '39.768', 'lon': '-86.158'})
    print('The next time the ISS will passover Indianapolis is ' +
          time.ctime(r.json().get('response')[0].get('risetime')))
    pass


def main():
    people_in_space()
    latlon = lat_lon_iss()
    turtle_map(latlon)
    indi_when()
    pass


if __name__ == '__main__':
    main()
