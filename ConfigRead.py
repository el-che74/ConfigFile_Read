#Read through a config file: Config.ini
#Review items on: NAPriority_Report
#Append to usecol_list 

import configparser as cp


config = cp.ConfigParser()

#Read configuration file
config.read('Config.ini', encoding ='utf-8')

usecol_list = []
for col in config.items('NAPriority_Report'):
    usecol_list.append(col[1])
print(usecol_list)
