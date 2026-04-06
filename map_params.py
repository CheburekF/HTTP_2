def get_map_params(toponym, apikey):
    coords = toponym["Point"]["pos"].split()
    lon, lat = coords[0], coords[1]

    envelope = toponym["boundedBy"]["Envelope"]
    lower = envelope["lowerCorner"].split()
    upper = envelope["upperCorner"].split()

    spn_lon = abs(float(upper[0]) - float(lower[0]))
    spn_lat = abs(float(upper[1]) - float(lower[1]))

    return {
        "ll": f"{lon},{lat}",
        "spn": f"{spn_lon},{spn_lat}",
        "pt": f"{lon},{lat},pm2rdm",
        "apikey": apikey,
    }
