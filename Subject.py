from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sqlite3
import sys


class subject():
    def __init__(self, name, time_required):
        self.current_time = 0
        self.name = name
        self.time_required = time_required

    def get_time_required(self):
        return self.time_required

    def get_name(self):
        return self.name

    def get_current_time(self):
        return self.current_time

    def convert_hours_to_seconds(self, inputted_time):
        return inputted_time * 3600

    def update_time_spent(self, time_spent):
        self.current_time = self.convert_hours_to_seconds(self.time_required) - self.convert_hours_to_seconds(
            time_spent)

    def serialize(self):
        return {
            "Name" : self.name,
            "Hours" : self.time_required
        }



