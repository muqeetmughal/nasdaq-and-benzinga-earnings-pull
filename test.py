import csv
csv_columns = ['No','Name','Country']

csv_columns = ['No','Name','Country']


dict_data = [
{'No': 1, 'Name': 'Alex', 'Country': 'India'},
{'No': 2, 'Name': 'Ben', 'Country': 'USA'},
{'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
{'No': 4, 'Name': 'Smith', 'Country': 'USA'},
{'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
]

dict_data = [
    {
        "lastYearRptDt": "07/16/2020",
        "lastYearEPS": "$0.54",
        "time": "time-pre-market",
        "symbol": "SCHW",
        "name": "The Charles Schwab Corporation",
        "marketCap": "$135,477,393,707",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "$0.71",
        "noOfEsts": "7"
    },
    {
        "lastYearRptDt": "07/20/2020",
        "lastYearEPS": "$0.48",
        "time": "time-not-supplied",
        "symbol": "HDB",
        "name": "HDFC Bank Limited",
        "marketCap": "$134,667,721,996",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "$0.59",
        "noOfEsts": "1"
    },
    {
        "lastYearRptDt": "07/17/2020",
        "lastYearEPS": "$0.10",
        "time": "time-pre-market",
        "symbol": "ERIC",
        "name": "Ericsson",
        "marketCap": "$44,310,876,558",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "$0.14",
        "noOfEsts": "3"
    },
    {
        "lastYearRptDt": "07/17/2020",
        "lastYearEPS": "$1.88",
        "time": "time-pre-market",
        "symbol": "STT",
        "name": "State Street Corporation",
        "marketCap": "$29,073,427,539",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "$1.77",
        "noOfEsts": "7"
    },
    {
        "lastYearRptDt": "07/17/2020",
        "lastYearEPS": "$1.15",
        "time": "time-pre-market",
        "symbol": "KSU",
        "name": "Kansas City Southern",
        "marketCap": "$24,482,772,410",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "$2.19",
        "noOfEsts": "2"
    },
    {
        "lastYearRptDt": "07/17/2020",
        "lastYearEPS": "$0.20",
        "time": "time-pre-market",
        "symbol": "FHN",
        "name": "First Horizon Corporation",
        "marketCap": "$9,097,607,833",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "$0.43",
        "noOfEsts": "7"
    },
    {
        "lastYearRptDt": "07/17/2020",
        "lastYearEPS": "($1.40)",
        "time": "time-pre-market",
        "symbol": "ALV",
        "name": "Autoliv, Inc.",
        "marketCap": "$8,329,601,508",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "$1.44",
        "noOfEsts": "3"
    },
    {
        "lastYearRptDt": "NA",
        "lastYearEPS": "$0.76",
        "time": "time-not-supplied",
        "symbol": "RBCAA",
        "name": "Republic Bancorp, Inc.",
        "marketCap": "$960,760,289",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "",
        "noOfEsts": "3"
    },
    {
        "lastYearRptDt": "07/17/2020",
        "lastYearEPS": "$0.18",
        "time": "time-not-supplied",
        "symbol": "PVBC",
        "name": "Provident Bancorp, Inc.",
        "marketCap": "$293,362,272",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "$0.23",
        "noOfEsts": "1"
    },
    {
        "lastYearRptDt": "07/17/2020",
        "lastYearEPS": "$0.23",
        "time": "time-not-supplied",
        "symbol": "BOCH",
        "name": "Bank of Commerce Holdings (CA)",
        "marketCap": "$231,541,999",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "$0.31",
        "noOfEsts": "2"
    },
    {
        "lastYearRptDt": "NA",
        "lastYearEPS": "$0.49",
        "time": "time-not-supplied",
        "symbol": "ATLO",
        "name": "Ames National Corporation",
        "marketCap": "$215,844,194",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "",
        "noOfEsts": "3"
    },
    {
        "lastYearRptDt": "NA",
        "lastYearEPS": "$0.92",
        "time": "time-not-supplied",
        "symbol": "ACU",
        "name": "Acme United Corporation.",
        "marketCap": "$147,318,356",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "",
        "noOfEsts": "3"
    },
    {
        "lastYearRptDt": "NA",
        "lastYearEPS": "$0.05",
        "time": "time-not-supplied",
        "symbol": "BRID",
        "name": "Bridgford Foods Corporation",
        "marketCap": "$118,906,499",
        "fiscalQuarterEnding": "Apr/2021",
        "epsForecast": "",
        "noOfEsts": "3"
    },
    {
        "lastYearRptDt": "NA",
        "lastYearEPS": "$0.44",
        "time": "time-not-supplied",
        "symbol": "EMCF",
        "name": "Emclaire Financial Corp",
        "marketCap": "$81,337,026",
        "fiscalQuarterEnding": "Jun/2021",
        "epsForecast": "",
        "noOfEsts": "3"
    }
]
csv_file = "Names.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")