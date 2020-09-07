import pandas as pd 
import json
import matplotlib.pyplot as plt
import utils

data_portal = pd.read_csv("covid_19_data_portal.csv")

personal_finances = data_portal[data_portal["indicator_name"] == "Effects of COVID-19 on work and income"][["parameter","value"]]
personal_finances["value"] = pd.to_numeric(personal_finances["value"])
no_effect_row = {'parameter':'No response', 'value':100-sum(personal_finances["value"])}
personal_finances = personal_finances.append(no_effect_row, ignore_index=True)

household_finances =  data_portal[data_portal["indicator_name"] == "Change in income"][["parameter","value"]]

household_finances_pie = utils.plot_pie(household_finances["value"], household_finances["parameter"],'Change in income - Household finances', "household")
personal_finances_pie = utils.plot_pie(personal_finances["value"], personal_finances["parameter"],'Effects of COVID-19 on work and income - Personal finances', "personal")

covid19_scam = data_portal[data_portal["indicator_name"] == "COVID-19 related scams"][["parameter","value"]]
covid19_scam["value"] = pd.to_numeric(covid19_scam["value"])
covid19_scam_plot = utils.plot_time_series_no_ref(covid19_scam["parameter"],covid19_scam["value"],"COVID-19 related scams","scam")

monthly_jobs = data_portal[data_portal["indicator_name"] == "Monthly filled jobs"][["parameter","value","series_name"]]
monthly_jobs = monthly_jobs[monthly_jobs["series_name"] == "All industries (actual)"][["parameter","value"]]
monthly_jobs["value"] = pd.to_numeric(monthly_jobs["value"])
monthly_jobs["parameter"] = pd.to_datetime(monthly_jobs["parameter"])
monthly_jobs = monthly_jobs.tail(20)
monthly_jobs_plot = utils.plot_time_series(monthly_jobs["parameter"],monthly_jobs["value"],"Monthly filled jobs", "jobs")

economic_sentiment = data_portal[data_portal["indicator_name"] == "Economic sentiment"][["parameter","value"]]
economic_sentiment["value"] = pd.to_numeric(economic_sentiment["value"])
economic_sentiment["parameter"] = pd.to_datetime(economic_sentiment["parameter"])
economic_sentiment = economic_sentiment.tail(30)
economic_sentiment_plot = utils.plot_time_series(economic_sentiment["parameter"],economic_sentiment["value"],"Weekly Economic Sentiment", "econ")
