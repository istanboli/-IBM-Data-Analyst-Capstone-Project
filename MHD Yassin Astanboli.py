#!/usr/bin/env python
# coding: utf-8

# In[103]:


import requests

api_url = "http://api.open-notify.org/astros.json" 

response = requests.get(api_url)

if response.ok:
    data = response.json()


# In[88]:



{'people': [{'name': 'Mark Vande Hei', 'craft': 'ISS'},
  {'name': 'Oleg Novitskiy', 'craft': 'ISS'},
  {'name': 'Pyotr Dubrov', 'craft': 'ISS'},
  {'name': 'Thomas Pesquet', 'craft': 'ISS'},
  {'name': 'Megan McArthur', 'craft': 'ISS'},
  {'name': 'Shane Kimbrough', 'craft': 'ISS'},
  {'name': 'Akihiko Hoshide', 'craft': 'ISS'},
  {'name': 'Nie Haisheng', 'craft': 'Tiangong'},
  {'name': 'Liu Boming', 'craft': 'Tiangong'},
  {'name': 'Tang Hongbo', 'craft': 'Tiangong'}],
 'number': 10,
 'message': 'success'}


# In[89]:


data["number"]


# In[90]:


astronauts = data.get("people")
for astro in astronauts:
    print(astro["name"])


# In[91]:


import careerjet_api #Import the libraries
import pandas as pd


# In[92]:


get_number_jobs("Python")


# In[93]:


technologies = [
    "C#",
    "C++",
    "Java",
    "JavaScript",
    "Python",
    "Scala",
    "Oracle",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Excel"
]

tec_dict = {}
counts = []
TECHS = []


# In[94]:


for tech in technologies:
    tecnologia, conteo = get_number_jobs(tech)
    counts.append(conteo)
    TECHS.append(tecnologia)
    tec_dict["Technologies"] = TECHS
    tec_dict["Number_jobs"] = counts


# In[95]:


tec_dict


# In[100]:


df_job=pd.DataFrame(tec_dict)
df_job


# In[102]:


df_job.to_excel("Careerjet_posting.xlsx")


# In[ ]:





# In[ ]:




