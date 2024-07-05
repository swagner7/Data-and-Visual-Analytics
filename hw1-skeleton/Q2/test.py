import fastf1
import pandas as pd
import time
fastf1.Cache.enable_cache('cache')

race = fastf1.get_session(2021, 1, 'R')
race.load()
tire_data = pd.DataFrame(race.laps.pick_driver('LEC'))[['Driver', 'LapNumber', 'LapTime', 'Compound', 'TyreLife']]
print(tire_data, '\n')