import logging
import traceback

import intersight
import credentials
import intersight.api.ntp_api
from intersight.model.ntp_policy import NtpPolicy


client = credentials.config_credentials()
ntp_policy_name = "POD11_ntp_policy"

   
        
def update_ntp_policy():
    api_instance = intersight.api.ntp_api.NtpApi(client)
    # Get the modi of the ntp policy to update
    result = api_instance.get_ntp_policy_list(filter=f"Name eq {ntp_policy_name}")
    moid = result.results[0].moid
    print(result.results[0].moid)    
    # create an instance of ntp policy object.
    ntp_policy = NtpPolicy()

    # Setting all the attributes for updating the policye.
    # Only update NTP servers
    ntp_servers = [
        "pool.ntp.org",
        "10.20.1.6"
    ]
    ntp_policy.ntp_servers = ntp_servers
    

    # update a Policy with given values
    try:
        # Update a 'ntp.Policy' resource.
        resp_ntp_policy = api_instance.update_ntp_policy(moid,ntp_policy)
        print(resp_ntp_policy)
        #return resp_ntp_policy
    except intersight.ApiException as e:
        print("Exception when calling NtpApi->create_ntp_policy: %s\n" % e)
        sys.exit(1)


def main():
 
    update_ntp_policy()

if __name__== "__main__":
    main()
