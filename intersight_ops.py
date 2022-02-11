"""
    intersight_ops.py - shows how to use intersight REST API

    author: John McDonough (jomcdono@cisco.com)
"""
import json
import requests

from intersight_auth import IntersightAuth
############ Users Need to Update following Code ##################################
# Create an AUTH object
AUTH = IntersightAuth(
    secret_key_filename='C:\\Users\\sabraham\\Downloads\\SecretKey.txt',
    api_key_id='61e075b87564612d33952212/61e5a7597564612d30792700/62044df27564612d3019dab1'
    )
## Replace X with POD Number ####
PODno='POD11'
## This script assume your Organization Name same as PODX
MyOrg=PODno 
## Change the value to True for only the Required REST Operation, others should be False ##
rest_get=False
rest_post=False
rest_patch=False
rest_delete=True
############ Do not Edit Code below this ###########################################
# Intersight REST API Base URL
BURL = 'https://www.intersight.com/api/v1/'

if __name__ == "__main__":

    # intersight operations, GET, POST, PATCH, DELETE
    OPERATIONS = [
        {
            "request_process":rest_get,
            "resource_path":"ntp/Policies",
            "request_method":"GET"
        },
        {
            "request_process":rest_post,
            "resource_path":"ntp/Policies",
            "request_method":"POST",
            "request_body":{
                "Enabled":True,
                "Name":PODno+"-ntp-policy",
                "Organization":"MyOrgid",
                "Description":"NTP Policy for ntp.org",
                "NtpServers":[
                    "pool.ntp.org"
                    ],
                "Tags":[]
            }
        },
        {
            "request_process":rest_patch,
            "resource_name":PODno+"-ntp-policy",
            "resource_path":"ntp/Policies",
            "request_method":"PATCH",
            "request_body":{
                "NtpServers":[
                    "pool.ntp.org",
                    "10.20.1.6"
                    ]
                }
        },
        {
            "request_process":rest_delete,
            "resource_name":PODno+"-ntp-policy",
            "resource_path":"ntp/Policies",
            "request_method":"DELETE"
        }
    ]


    for operation in OPERATIONS:

        if operation['request_process']:

            response = None
            print(operation['request_method'])

            # GET
            if operation['request_method'] == "GET":
                response = requests.get(
                    BURL + operation['resource_path'],
                    auth=AUTH
                    )

            # POST
            if operation['request_method'] == "POST":
                
                #GET the Moid of the Organization to Create Policy
                response = requests.get(
                    (
                        BURL + 'organization/Organizations' +
                        "?$filter=Name eq '" + MyOrg + "'"
                        ),
                    auth=AUTH
                    )

                # Extract the Moid from the Results
                json_result = json.loads(response.text)
                moid = json_result["Results"][0]["Moid"]
                
                response = requests.post(
                    BURL + operation['resource_path'],
                    data=json.dumps(operation['request_body']).replace('MyOrgid',moid),
                    auth=AUTH
                    )

            # PATCH
            if operation['request_method'] == "PATCH":

                # GET the Moid of the MO to PATCH
                response = requests.get(
                    (
                        BURL + operation['resource_path'] +
                        "?$filter=Name eq '" + operation['resource_name'] + "'"
                        ),
                    auth=AUTH
                    )

                # Extract the Moid from the Results
                json_result = json.loads(response.text)
                moid = json_result["Results"][0]["Moid"]

                response = requests.patch(
                    BURL + operation['resource_path'] + "/" + moid,
                    data=json.dumps(operation['request_body']),
                    auth=AUTH
                    )

            # DELETE
            if operation['request_method'] == "DELETE":

                # GET the Moid of the MO to DELETE
                response = requests.get(
                    (
                        BURL + operation['resource_path'] +
                        "?$filter=Name eq '" + operation['resource_name'] + "'"
                        ),
                    auth=AUTH
                    )

                # Extract the Moid from the Results
                json_result = json.loads(response.text)
                moid = json_result["Results"][0]["Moid"]

                response = requests.delete(
                    BURL + operation['resource_path'] + "/" + moid,
                    auth=AUTH
                    )

            print(response)
            print(response.text)
