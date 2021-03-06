import pandas as pd
from sklearn.preprocessing import Imputer
import numpy as np
import pandas as pd

import re

filename = "1-superlig.csv"
path = "tr-turkey-master"
inner_paths = [
    "1994-95",
    "1995-96",
    "1996-97",
    "1997-98",
    "1998-99",
    "1999-00",
    "2000-01",
    "2001-02",
    "2002-03",
    "2003-04",
    "2004-05",
    "2005-06",
    "2006-07",
    "2007-08",
    "2008-09",
    "2009-10",
    "2010-11",
    "2011-12",
    "2012-13",
    "2013-14",
    "2014-15",
    "2015-16",
    "2016-17",
    "2017-18"
]

usefull_columns = ["Team 1", "Team 2", "FT"]

team_codes = {}


def getdatalist():
    """Collects all the data into an array and returns it"""
    datalist = []
    for inner_path in inner_paths:
        data = pd.read_csv(path + "\\" + inner_path + "\\" + filename)
        data = data.replace("?", "-99999")
        datalist.append(data[usefull_columns])
    return datalist


def teams_to_numbers(data):
    """Refers the team names as numbers"""
    team_array = get_team_array(data)
    for x in range(1, 3):
        j = 0
        for data_part in data:
            i = 0
            for team in data_part["Team " + str(x)]:
                # It use index numbers for converting team names to numbers
                team_number = team_array.index(get_team_name(team))
                data_part.set_value(i, "Team " + str(x), team_number)
                team_codes[get_team_name(team)] = team_number
                i = i + 1
            data[j] = data_part
            j = j + 1
    return data


def ft_to_numbers(data):
    """Refers the match results as numbers"""
    j = 0
    for data_part in data:
        i = 0
        for ft in data_part["FT"]:
            result = ft.split("-")
            score = int(result[0]) - int(result[1])
            # If first team is lose the match then value will be 1
            if score < 0:
                data_part.set_value(i, "FT", 1)
            # If first team is winner then value will be 2
            elif score > 0:
                data_part.set_value(i, "FT", 2)
            # If the match result is equal then value will be 0
            else:
                data_part.set_value(i, "FT", 0)

            i = i + 1
        data[j] = data_part
        j = j + 1
    return data


def get_team_array(data):
    """Collects all the matches into an array"""
    team_array = []
    for data_part in data:
        for team in data_part["Team 1"]:
            team_name = get_team_name(team)
            try:
                team_array.index(team_name)
            except:
                team_array.append(team_name)
    return team_array


def transform_data(data):
    """Fills the missing numbers using mean values"""
    imp = Imputer(missing_values=-99999, strategy="mean", axis=0)
    return imp.fit_transform(data)


def get_team_name(name):
    """Parses team names in sended value"""
    # Gençlerbirliği Ankara SK (4) -> Gençlerbirliği Ankara SK
    return re.sub(r"\ \((\w+)\)", "", name)


def get_data_as_matrix(data):
    """Turns data array to the matrix"""
    matrix = []
    for data_part in data:
        data_arr = []
        i = 0
        for j in range(0, len(data_part)):
            for column in data_part:    
                data_arr.append(data_part[column][j])
                i = i + 1
                if i % 3 == 0:
                    matrix.append(data_arr)
                    data_arr = []
    return matrix