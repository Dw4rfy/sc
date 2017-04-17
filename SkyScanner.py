import sqlite3
from skyscanner.skyscanner import FlightsCache

conn = sqlite3.connect('SkyScanner.db')
c = conn.cursor()

flights_cache_service = FlightsCache('ch692474677590339114824644982131')
result = flights_cache_service.get_cheapest_quotes(
    market='NO',
    currency='NOK',
    locale='nb-NO',
    originplace='OSL-sky',
    destinationplace='KRS-sky',
    outbounddate='2017-04-17',
    inbounddate='2017-04-24').parsed

# Find out how to retrieve airline and from/to values
# c.execute('CREATE TABLE IF NOT EXISTS ' + tbnavn + 'Dato TEXT, From TEXT, To TEXT, Flyselskap TEXT, Direkte TEXT, Pris REAL')
tblLogging = 'DataForPriser'
def create_table(tbnavn):
    c.execute('CREATE TABLE IF NOT EXISTS ' + tbnavn + '(Dato TEXT, Direkte TEXT, Pris TEXT)')

def log_prices(tbnavn):
    for i in result:
        for b in result['Quotes']:
            # for id in b['OutboundLeg']:
            #     print(id)
            if b['Direct']:
                s = "Ja"
            else:
                s = "Nei"
            dato = str(b["QuoteDateTime"])
            pris = str(b['MinPrice'])
            c.execute("INSERT INTO " + tbnavn + " (Dato, Direkte, Pris) VALUES (?, ? ,?)",(dato, s, pris))
            conn.commit()


create_table(tblLogging)
log_prices(tblLogging)
c.close()
conn.close()


