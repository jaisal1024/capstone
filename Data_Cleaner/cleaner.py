all = ["computeDays", "computeDateFunc", "getLatLong", "getElevation"]

# Add year on-market, month on-market and year sold, month sold
def computeDateFunc(date, month_not_year):
    date_format = "%m/%d/%y"
    a = datetime.strptime(date, date_format)
    if month_not_year:
        return a.month
    else:
        return a.year


def computeDays(date1, date2):
    date_format = "%m/%d/%y"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = b - a
    return delta.days  # that's it


def getLatLong(x):
    g = geocoder.google(x["full_address"], key=google_api_key)
    x["longitude"] = g.latlng[1]
    x["latitude"] = g.latlng[0]
    return x


def getElevation(lat, lng):
    l = []
    for i in range(len(lat) - 1):
        l.append(str(lat[i]) + "," + str(lng[i]) + "|")
    l.append(str(lat[len(lat) - 1]) + "," + str(lng[len(lat) - 1]))
    locations = "".join(l)
    url_ = "https://maps.googleapis.com/maps/api/elevation/json"
    payload = {"locations": locations, "key": google_api_key}
    r = requests.get(url=url_, params=payload)
    try:
        results = r.json()
        if 0 < len(results):
            return results["results"]
        else:
            print("HTTP GET Request failed.")
    except ValueError:
        print("JSON decode failed: " + str(r))
