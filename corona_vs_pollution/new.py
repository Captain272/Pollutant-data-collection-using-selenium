from selenium import webdriver
import pandas as pd
from time import sleep


home={"Bihar":["Gaya"," Patna"],
"Chandigarh":["Chandigarh"],
"Delhi":["Delhi"],
"Gujarat":["Ahmedabad ","Gandhinagar"],
"Haryana":["Ambala","Charkhi Dadri ","Faridabad","Gurugram","Hisar","Jind","Kaithal","Karnal","Kurukshetra","Plwal","Panchakula","Panipat","Rohtak","Sirsa","Sonipat","Yamunanagar"],
"Jammu and Kashmir":["Srinagar"],
"Karnataka":["Bagalkot","Benguluru","Bidar","Chikkaballapur"," Davanagere","Gadag","Kalaburagi","Mysuru","Udupi"],
"Kearala":["Ernakulam"," Kollam","Kozhikode","Thiruvananthapuram","Thrissur"],
"Madhya Pradesh":["Bhopal ","Dewas","Gwalior","Indore","Jabalpur","Ratlam","Sagar"," Ujjain.Maharashtra:Aurangabad","Chandrapur"," Mumbai","Nagpur","Nashik"," Mumbai","Pune","Solapur","Thane"],
"Mizoram":["Aizawl"],
"Nagaland":["Kohima"],
"Puducherry":["Puducherry"],
"Punjab":["Amritsar","Bathinda","Jalandhar","Khanna","Ludhiana"," Patiala","Rupnagar"],
"Rajasthan":["Ajmer","Alwar","Jaipur","Jodhpur","Kota","Pali","Udaipur"],
"Tamil Nadu":["Chennai","Coimbatore"," Thoothukudi"],
"Telangana":["Hyderabad"],
"Uttar Pradesh":["Agra","Baghpat","Bulandhshahr","GhaziabadHapur","Kanpur","Lucknow","Meerut","Moradabad","Muzaffarnagar","Varanasi"]}
states=["Uttar Pradesh","Telangana","Tamil Nadu","Rajasthan","Punjab","Puducherry","Nagaland","Mizoram","Madhya Pradesh","Kearala","Karnataka","Jammu and Kashmir","Haryana","Gujarat","Delhi","Chandigarh","Bihar"]

total_data=[]    


class data_collection:
    def __init__(self,st):
        self.driver = webdriver.Chrome()
        self.username=username
        # self.driver.get("https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-view-data-report/%2522%257B%255C%2522state%255C%2522%253A%255C%2522Maharashtra%255C%2522%252C%255C%2522city%255C%2522%253A%255C%2522Aurangabad%255C%2522%252C%255C%2522station%255C%2522%253A%255C%2522site_198%255C%2522%252C%255C%2522parameter_list%255C%2522%253A%255B%257B%255C%2522id%255C%2522%253A0%252C%255C%2522itemName%255C%2522%253A%255C%2522PM2.5%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_193%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A1%252C%255C%2522itemName%255C%2522%253A%255C%2522PM10%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_215%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A2%252C%255C%2522itemName%255C%2522%253A%255C%2522NO%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_226%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A3%252C%255C%2522itemName%255C%2522%253A%255C%2522NO2%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_194%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A4%252C%255C%2522itemName%255C%2522%253A%255C%2522NOx%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_225%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A5%252C%255C%2522itemName%255C%2522%253A%255C%2522NH3%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_311%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A6%252C%255C%2522itemName%255C%2522%253A%255C%2522SO2%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_312%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A7%252C%255C%2522itemName%255C%2522%253A%255C%2522CO%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_203%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A8%252C%255C%2522itemName%255C%2522%253A%255C%2522Ozone%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_222%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A9%252C%255C%2522itemName%255C%2522%253A%255C%2522Benzene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_202%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A10%252C%255C%2522itemName%255C%2522%253A%255C%2522Toluene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_232%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A11%252C%255C%2522itemName%255C%2522%253A%255C%2522Eth-Benzene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_216%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A12%252C%255C%2522itemName%255C%2522%253A%255C%2522MP-Xylene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_240%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A13%252C%255C%2522itemName%255C%2522%253A%255C%2522O%2520Xylene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_241%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A14%252C%255C%2522itemName%255C%2522%253A%255C%2522Temp%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_198%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A15%252C%255C%2522itemName%255C%2522%253A%255C%2522RH%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_235%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A16%252C%255C%2522itemName%255C%2522%253A%255C%2522WS%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_233%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A17%252C%255C%2522itemName%255C%2522%253A%255C%2522WD%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_234%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A18%252C%255C%2522itemName%255C%2522%253A%255C%2522SR%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_237%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A19%252C%255C%2522itemName%255C%2522%253A%255C%2522Xylene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_223%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A20%252C%255C%2522itemName%255C%2522%253A%255C%2522RF%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_236%255C%2522%257D%255D%252C%255C%2522criteria%255C%2522%253A%255C%252224%2520Hours%255C%2522%252C%255C%2522reportFormat%255C%2522%253A%255C%2522Tabular%255C%2522%252C%255C%2522fromDate%255C%2522%253A%255C%252221-04-2020%2520T00%253A00%253A00Z%255C%2522%252C%255C%2522toDate%255C%2522%253A%255C%252222-04-2021%2520T00%253A00%253A59Z%255C%2522%252C%255C%2522parameter%255C%2522%253A%255B%255C%2522parameter_193%255C%2522%252C%255C%2522parameter_215%255C%2522%252C%255C%2522parameter_226%255C%2522%252C%255C%2522parameter_194%255C%2522%252C%255C%2522parameter_225%255C%2522%252C%255C%2522parameter_311%255C%2522%252C%255C%2522parameter_312%255C%2522%252C%255C%2522parameter_203%255C%2522%252C%255C%2522parameter_222%255C%2522%252C%255C%2522parameter_202%255C%2522%252C%255C%2522parameter_232%255C%2522%252C%255C%2522parameter_216%255C%2522%252C%255C%2522parameter_240%255C%2522%252C%255C%2522parameter_241%255C%2522%252C%255C%2522parameter_198%255C%2522%252C%255C%2522parameter_235%255C%2522%252C%255C%2522parameter_233%255C%2522%252C%255C%2522parameter_234%255C%2522%252C%255C%2522parameter_237%255C%2522%252C%255C%2522parameter_223%255C%2522%252C%255C%2522parameter_236%255C%2522%255D%252C%255C%2522parameterNames%255C%2522%253A%255B%255C%2522PM2.5%255C%2522%252C%255C%2522PM10%255C%2522%252C%255C%2522NO%255C%2522%252C%255C%2522NO2%255C%2522%252C%255C%2522NOx%255C%2522%252C%255C%2522NH3%255C%2522%252C%255C%2522SO2%255C%2522%252C%255C%2522CO%255C%2522%252C%255C%2522Ozone%255C%2522%252C%255C%2522Benzene%255C%2522%252C%255C%2522Toluene%255C%2522%252C%255C%2522Eth-Benzene%255C%2522%252C%255C%2522MP-Xylene%255C%2522%252C%255C%2522O%2520Xylene%255C%2522%252C%255C%2522Temp%255C%2522%252C%255C%2522RH%255C%2522%252C%255C%2522WS%255C%2522%252C%255C%2522WD%255C%2522%252C%255C%2522SR%255C%2522%252C%255C%2522RF%255C%2522%255D%257D%2522")
        # sleep(20)
        

        
        # self.driver.get("https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing/data/%2522%257B%255C%2522state%255C%2522%253A%255C%2522Jammu%2520and%2520Kashmir%255C%2522%252C%255C%2522city%255C%2522%253A%255C%2522Srinagar%255C%2522%252C%255C%2522station%255C%2522%253A%255C%2522site_5424%255C%2522%252C%255C%2522parameter_list%255C%2522%253A%255B%257B%255C%2522id%255C%2522%253A0%252C%255C%2522itemName%255C%2522%253A%255C%2522PM2.5%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_193%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A1%252C%255C%2522itemName%255C%2522%253A%255C%2522PM10%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_215%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A2%252C%255C%2522itemName%255C%2522%253A%255C%2522NO%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_226%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A3%252C%255C%2522itemName%255C%2522%253A%255C%2522NO2%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_194%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A4%252C%255C%2522itemName%255C%2522%253A%255C%2522NOx%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_225%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A5%252C%255C%2522itemName%255C%2522%253A%255C%2522NH3%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_311%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A6%252C%255C%2522itemName%255C%2522%253A%255C%2522SO2%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_312%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A7%252C%255C%2522itemName%255C%2522%253A%255C%2522CO%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_203%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A8%252C%255C%2522itemName%255C%2522%253A%255C%2522Ozone%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_222%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A9%252C%255C%2522itemName%255C%2522%253A%255C%2522Benzene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_202%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A10%252C%255C%2522itemName%255C%2522%253A%255C%2522Toluene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_232%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A11%252C%255C%2522itemName%255C%2522%253A%255C%2522Eth-Benzene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_216%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A12%252C%255C%2522itemName%255C%2522%253A%255C%2522MP-Xylene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_240%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A13%252C%255C%2522itemName%255C%2522%253A%255C%2522O%2520Xylene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_241%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A14%252C%255C%2522itemName%255C%2522%253A%255C%2522Temp%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_198%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A15%252C%255C%2522itemName%255C%2522%253A%255C%2522RH%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_235%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A16%252C%255C%2522itemName%255C%2522%253A%255C%2522WS%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_233%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A17%252C%255C%2522itemName%255C%2522%253A%255C%2522WD%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_234%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A18%252C%255C%2522itemName%255C%2522%253A%255C%2522SR%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_237%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A19%252C%255C%2522itemName%255C%2522%253A%255C%2522Xylene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_223%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A20%252C%255C%2522itemName%255C%2522%253A%255C%2522RF%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_236%255C%2522%257D%255D%252C%255C%2522criteria%255C%2522%253A%255C%252224%2520Hours%255C%2522%252C%255C%2522reportFormat%255C%2522%253A%255C%2522Tabular%255C%2522%252C%255C%2522fromDate%255C%2522%253A%255C%252221-04-2020%2520T00%253A00%253A00Z%255C%2522%252C%255C%2522toDate%255C%2522%253A%255C%252222-04-2021%2520T20%253A39%253A59Z%255C%2522%252C%255C%2522parameter%255C%2522%253A%255B%255C%2522parameter_193%255C%2522%252C%255C%2522parameter_215%255C%2522%252C%255C%2522parameter_226%255C%2522%252C%255C%2522parameter_194%255C%2522%252C%255C%2522parameter_225%255C%2522%252C%255C%2522parameter_311%255C%2522%252C%255C%2522parameter_312%255C%2522%252C%255C%2522parameter_203%255C%2522%252C%255C%2522parameter_222%255C%2522%252C%255C%2522parameter_202%255C%2522%252C%255C%2522parameter_232%255C%2522%252C%255C%2522parameter_216%255C%2522%252C%255C%2522parameter_240%255C%2522%252C%255C%2522parameter_241%255C%2522%252C%255C%2522parameter_198%255C%2522%252C%255C%2522parameter_235%255C%2522%252C%255C%2522parameter_233%255C%2522%252C%255C%2522parameter_234%255C%2522%252C%255C%2522parameter_237%255C%2522%252C%255C%2522parameter_223%255C%2522%252C%255C%2522parameter_236%255C%2522%255D%252C%255C%2522parameterNames%255C%2522%253A%255B%255C%2522PM2.5%255C%2522%252C%255C%2522PM10%255C%2522%252C%255C%2522NO%255C%2522%252C%255C%2522NO2%255C%2522%252C%255C%2522NOx%255C%2522%252C%255C%2522NH3%255C%2522%252C%255C%2522SO2%255C%2522%252C%255C%2522CO%255C%2522%252C%255C%2522Ozone%255C%2522%252C%255C%2522Benzene%255C%2522%252C%255C%2522Toluene%255C%2522%252C%255C%2522Eth-Benzene%255C%2522%252C%255C%2522MP-Xylene%255C%2522%252C%255C%2522O%2520Xylene%255C%2522%252C%255C%2522Temp%255C%2522%252C%255C%2522RH%255C%2522%252C%255C%2522WS%255C%2522%252C%255C%2522WD%255C%2522%252C%255C%2522SR%255C%2522%252C%255C%2522Xylene%255C%2522%252C%255C%2522RF%255C%2522%255D%257D%2522")
        # sleep(7)
        for state in st:
            for city in home[state]:
                # State
                # body = driver.find_element_by_tag_name("body")
                # body.send_keys(Keys.CONTROL + 't')
                self.driver.get("https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing/data/%2522%257B%255C%2522state%255C%2522%253A%255C%2522Jammu%2520and%2520Kashmir%255C%2522%252C%255C%2522city%255C%2522%253A%255C%2522Srinagar%255C%2522%252C%255C%2522station%255C%2522%253A%255C%2522site_5424%255C%2522%252C%255C%2522parameter_list%255C%2522%253A%255B%257B%255C%2522id%255C%2522%253A0%252C%255C%2522itemName%255C%2522%253A%255C%2522PM2.5%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_193%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A1%252C%255C%2522itemName%255C%2522%253A%255C%2522PM10%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_215%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A2%252C%255C%2522itemName%255C%2522%253A%255C%2522NO%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_226%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A3%252C%255C%2522itemName%255C%2522%253A%255C%2522NO2%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_194%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A4%252C%255C%2522itemName%255C%2522%253A%255C%2522NOx%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_225%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A5%252C%255C%2522itemName%255C%2522%253A%255C%2522NH3%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_311%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A6%252C%255C%2522itemName%255C%2522%253A%255C%2522SO2%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_312%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A7%252C%255C%2522itemName%255C%2522%253A%255C%2522CO%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_203%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A8%252C%255C%2522itemName%255C%2522%253A%255C%2522Ozone%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_222%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A9%252C%255C%2522itemName%255C%2522%253A%255C%2522Benzene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_202%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A10%252C%255C%2522itemName%255C%2522%253A%255C%2522Toluene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_232%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A11%252C%255C%2522itemName%255C%2522%253A%255C%2522Eth-Benzene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_216%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A12%252C%255C%2522itemName%255C%2522%253A%255C%2522MP-Xylene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_240%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A13%252C%255C%2522itemName%255C%2522%253A%255C%2522O%2520Xylene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_241%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A14%252C%255C%2522itemName%255C%2522%253A%255C%2522Temp%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_198%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A15%252C%255C%2522itemName%255C%2522%253A%255C%2522RH%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_235%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A16%252C%255C%2522itemName%255C%2522%253A%255C%2522WS%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_233%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A17%252C%255C%2522itemName%255C%2522%253A%255C%2522WD%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_234%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A18%252C%255C%2522itemName%255C%2522%253A%255C%2522SR%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_237%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A19%252C%255C%2522itemName%255C%2522%253A%255C%2522Xylene%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_223%255C%2522%257D%252C%257B%255C%2522id%255C%2522%253A20%252C%255C%2522itemName%255C%2522%253A%255C%2522RF%255C%2522%252C%255C%2522itemValue%255C%2522%253A%255C%2522parameter_236%255C%2522%257D%255D%252C%255C%2522criteria%255C%2522%253A%255C%252224%2520Hours%255C%2522%252C%255C%2522reportFormat%255C%2522%253A%255C%2522Tabular%255C%2522%252C%255C%2522fromDate%255C%2522%253A%255C%25221-1-2010%2520T00%253A00%253A00Z%255C%2522%252C%255C%2522toDate%255C%2522%253A%255C%252231-12-2020%2520T20%253A39%253A59Z%255C%2522%252C%255C%2522parameter%255C%2522%253A%255B%255C%2522parameter_193%255C%2522%252C%255C%2522parameter_215%255C%2522%252C%255C%2522parameter_226%255C%2522%252C%255C%2522parameter_194%255C%2522%252C%255C%2522parameter_225%255C%2522%252C%255C%2522parameter_311%255C%2522%252C%255C%2522parameter_312%255C%2522%252C%255C%2522parameter_203%255C%2522%252C%255C%2522parameter_222%255C%2522%252C%255C%2522parameter_202%255C%2522%252C%255C%2522parameter_232%255C%2522%252C%255C%2522parameter_216%255C%2522%252C%255C%2522parameter_240%255C%2522%252C%255C%2522parameter_241%255C%2522%252C%255C%2522parameter_198%255C%2522%252C%255C%2522parameter_235%255C%2522%252C%255C%2522parameter_233%255C%2522%252C%255C%2522parameter_234%255C%2522%252C%255C%2522parameter_237%255C%2522%252C%255C%2522parameter_223%255C%2522%252C%255C%2522parameter_236%255C%2522%255D%252C%255C%2522parameterNames%255C%2522%253A%255B%255C%2522PM2.5%255C%2522%252C%255C%2522PM10%255C%2522%252C%255C%2522NO%255C%2522%252C%255C%2522NO2%255C%2522%252C%255C%2522NOx%255C%2522%252C%255C%2522NH3%255C%2522%252C%255C%2522SO2%255C%2522%252C%255C%2522CO%255C%2522%252C%255C%2522Ozone%255C%2522%252C%255C%2522Benzene%255C%2522%252C%255C%2522Toluene%255C%2522%252C%255C%2522Eth-Benzene%255C%2522%252C%255C%2522MP-Xylene%255C%2522%252C%255C%2522O%2520Xylene%255C%2522%252C%255C%2522Temp%255C%2522%252C%255C%2522RH%255C%2522%252C%255C%2522WS%255C%2522%252C%255C%2522WD%255C%2522%252C%255C%2522SR%255C%2522%252C%255C%2522Xylene%255C%2522%252C%255C%2522RF%255C%2522%255D%257D%2522")
                sleep(12)
                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[1]/div[1]/div/ng-select/div/div/div[3]")\
                .click()
                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[1]/div[1]/div/ng-select/select-dropdown/div/div[1]/input")\
                .send_keys(state)
                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[1]/div[1]/div/ng-select/select-dropdown/div/div[1]/input")\
                .click()
                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[1]/div[1]/div/ng-select/select-dropdown/div/div[2]/ul/li")\
                .click()



                city
               
                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[1]/div[2]/div/ng-select/div/div/div[2]")\
                .click()
                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[1]/div[2]/div/ng-select/select-dropdown/div/div[1]/input")\
                .send_keys(city)
                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[1]/div[2]/div/ng-select/select-dropdown/div/div[1]/input")\
                .click()
                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[1]/div[2]/div/ng-select/select-dropdown/div/div[2]/ul/li[1]")\
                .click()
                # self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[1]/div[1]/div/ng-select/select-dropdown/div/div[2]/ul/li")\
                # .click()

                # Station
                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[2]/div[1]/div/ng-select/div/div/div[2]")\
                .click()
                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[2]/div[1]/div/ng-select/select-dropdown/div/div[2]/ul/li")\
                .click()
                sleep(2)


                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[5]/button")\
                .click()

                sleep(20)
                
                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data-report/div[2]/div[2]/div[1]/label/select")\
                .click()

                sleep(2)



                label=[]

        
                head = self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data-report/div[2]/div[2]/table/thead/tr")
                heading = head.find_elements_by_tag_name('th')
                for name in heading:
                    label.append(name.text);
                lab=label[1:]

                keep={}
                for i in lab:
                    keep[i]=""

                for i in lab:
                    keep[i]=[]
                    
                print(keep)
                
                self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data-report/div[2]/div[2]/div[1]/label/select/option[4]")\
                .click()
            
                names1=[]

            


                for k in range(4):
                
                
                    sleep(60)
                    scroll_box1 = self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data-report/div[2]/div[2]/table/tbody")
                    links = scroll_box1.find_elements_by_tag_name('span')
                    for name in links:
                        names1.append(name.text);
                    # names1 = [name.text for name in links]
                    # names1.append(state)
                    # print (scroll_box1)
                #    for i in range(0, len(names1)):
                #        print(names1[i])
                #        print('\n')
                    # print(names1)
                    # for i in names1:
                    #     print(i);
                    # total_data.append(names1)
                    # self.driver.get("")
                    element = self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data-report/div[2]/div[2]/div[4]/a[3]")
                    self.driver.execute_script("arguments[0].click();", element)
                    # element = self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data-report/div[2]/div[2]/div[4]/a[3]")
                    # self.driver.execute_script("arguments[0].click();", element)
            # self.driver.find_element_by_xpath("/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data-report/div[2]/div[2]/div[4]/span/a[2]")\
            # .click()
                names1.append(state)

            

                print(len(names1))
                # print(df)
                i=0
                tt=[]
                for j in range(len(lab)):
                    i=j
                    lt=[]
                    k=0
                    while(i<len(names1)-1):
                        # print(data[0][i])
                        lt.append(names1[i])
                        i=i+len(lab)
                        k=k+1
                    tt.append(lt)
                    print(len(lt))
                    # print("->j\n")


                num=range(len(tt))
                doe=zip(lab,num)
                for i,j in doe:
                    keep[i]=tt[j]

                print(keep["From Date"])




                df=pd.DataFrame(keep)
                print(df)
                df.to_csv(state+city+".csv")


            total_data.append(names1)
            #print(total_data)




data=data_collection(states)
print(data)
# instabot.followers()

# instabot.viewpost()


# instabot.logout()
# abhi=input("username")
# cap=input("pass")  
#instabot.logout()

# instabott(abhi,cap)

