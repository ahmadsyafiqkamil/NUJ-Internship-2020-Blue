#!/usr/bin/env python
# coding: utf-8

# ### WARNING
# ### SETELAH RUN, SILAHKAN **HAPUS OUTPUT DARI NOTEBOOK** (BAGI YANG AKAN GIT)

# In[ ]:


import csv
import json
from io import BytesIO
from zipfile import ZipFile

import pandas as pd
import requests


# In[ ]:


# Authorization
def odk_auth(authfile):
    with open(authfile, "r") as f:
        ak = f.readlines()
    f.close()
    return ak[0].replace("\n", ""), ak[1].replace("\n", "")


authfile = "./auth.k"

central_email, central_password = odk_auth(authfile)
central_url = "https://odk.genolife.org"


# In[ ]:


get_ipython().system('pip install nbstripout')
get_ipython().system('nbstripout --install')


# In[ ]:


def get_email_token():
    email_token_response = requests.post(
        central_url + "/v1/sessions",
        data=json.dumps({"email": central_email, "password": central_password}),
        headers={"Content-Type": "application/json"},
    )
    if email_token_response.status_code == 200:
        return email_token_response.json()["token"]


def list_app_users(email_token, central_project_id):
    app_users_response = requests.get(
        central_url + "/v1/projects/" + str(central_project_id) + "/app-users",
        headers={"Authorization": "Bearer " + email_token},
    )
    app_users = {}
    for app_user in app_users_response.json():
        app_users[app_user["id"]] = app_user["displayName"]
    return app_users


def list_projects(email_token):
    projects_response = requests.get(
        central_url + "/v1/projects/",
        headers={"Authorization": "Bearer " + email_token},
    )
    projects = {}
    for project in projects_response.json():
        projects[project["id"]] = project["name"]
    return projects


# In[ ]:


def odk_form(authfile):
    with open(authfile, "r") as f:
        ak = f.readlines()
    f.close()
    return (
        ak[2].replace("\n", ""),
        ak[3].replace("\n", ""),
        ak[4].replace("\n", ""),
        ak[5].replace("\n", ""),
    )


form = odk_form(authfile)


# In[ ]:


email_token = get_email_token()

dataRaw = pd.DataFrame(None)
for i in form:
    request = requests.get(
        url=i, headers={"Authorization": "Bearer " + str(email_token)}
    )
    dataODK = pd.read_csv(BytesIO(request.content), compression="zip")
    dataRaw = dataRaw.append(dataODK)

