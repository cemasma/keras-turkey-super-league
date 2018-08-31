import pandas as pd

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

usefull_columns = ["Date", "Team 1", "Team 2", "FT", "HT"]

def getdatalist():
    datalist = []
    for inner_path in inner_paths:
        data = pd.read_csv(path + "\\" + inner_path + "\\" + filename)
        data = data.replace("?", "-1")
        datalist.append(data)
    print(datalist[0][usefull_columns])
    return datalist


getdatalist()
