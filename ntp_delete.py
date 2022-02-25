import logging
import traceback

import intersight
import credentials
import intersight.api.ntp_api
from intersight.model.ntp_policy import NtpPolicy


client = credentials.config_credentials()
ntp_policy_name = "POD11_ntp_policy"

   
        
def delete_ntp_policy():
    api_instance = intersight.api.ntp_api.NtpApi(client)
    #Get the moid of the ntp policy to delete
    result = api_instance.get_ntp_policy_list(filter=f"Name eq {ntp_policy_name}")
    moid = result.results[0].moid
    print(result.results[0].moid)    
        

    # example passing only required values which don't have defaults set
    try:
        # delete 'ntp.Policy' resource with the specified moid.
        resp_ntp_policy = api_instance.delete_ntp_policy(moid)
        print(resp_ntp_policy)
        #return resp_ntp_policy
    except intersight.ApiException as e:
        print("Exception when calling NtpApi->create_ntp_policy: %s\n" % e)
        sys.exit(1)


def main():
 
    delete_ntp_policy()

if __name__== "__main__":
    main()
