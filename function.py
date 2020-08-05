import pandas as pd
import numpy as np

def my_function(df, team) :
    df2 = df[df['OffenseTeam'] == team] 
    df3 = df2[df2.Down != 0] 
    df4 = df3[df3.Down != 4]
    df5 = df4[(df4['PlayType'] == "PASS") | (df4['PlayType'] == "RUSH")]
    return df5

saints2019 = pd.read_csv("pbp-2019.csv")
saints2018 = pd.read_csv("pbp-2018.csv")

saints2018 = my_function(saints2018, "NO")
saints2019 = my_function(saints2019, "NO")

saints = saints2018.append(saints2019, ignore_index = True)
saints.to_csv("saints.csv", index=False)

