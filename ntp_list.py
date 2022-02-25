import logging
import traceback

import intersight
import credentials
import intersight.api.ntp_api

def main():
  
    client = credentials.config_credentials()

    try:
        #* Start main code here
        #* Get condition class instance
        api_instance = intersight.api.ntp_api.NtpApi(client)
        #* Only include Name and Description in results
        query_select = "Name,Description"

        results = api_instance.get_ntp_policy_list(select=query_select)
        print(results)
 
    except intersight.OpenApiException as e:
        logger.error("Exception when calling API: %s\n" % e)
        #traceback.print_exc()

if __name__== "__main__":
    main()
