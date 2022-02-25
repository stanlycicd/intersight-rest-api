import logging
import traceback

import intersight
import credentials
import intersight.api.ntp_api
import intersight.api.organization_api
from intersight.model.ntp_policy import NtpPolicy
from intersight.model.organization_organization_relationship import OrganizationOrganizationRelationship

client = credentials.config_credentials()
# Enter the Organization Name, Replace X with POD Number
org_name = "POD11"
#NTP Policy will create with a name PODX_ntp_policy

def get_organization():
    # get moid of organization
    try:
        api_instance = intersight.api.organization_api.OrganizationApi(client)
        result = api_instance.get_organization_organization_list(filter=f"Name eq {org_name}")
        print(result.results[0].moid)
        #Create a Organization instance with specified moid
        organization = OrganizationOrganizationRelationship(class_id="mo.MoRef",
                                                        object_type="organization.Organization",moid=result.results[0].moid)
        print(organization)
        return organization

    
    except intersight.OpenApiException as e:
        logger.error("Exception when calling API: %s\n" % e)
        #traceback.print_exc()
        
def create_ntp_policy():
    api_instance = intersight.api.ntp_api.NtpApi(client)
    
    # get organization.
    organization = get_organization()
    
    # NtpPolicy instance to create.
    ntp_policy = NtpPolicy()

    # Setting all the attributes for ntp policy instance.
    ntp_policy.name = org_name+"_ntp_policy"
    ntp_policy.description = "sample ntp policy from Python"
    ntp_policy.organization = organization
    ntp_servers = [
        "pool.ntp.org"
    ]
    ntp_policy.ntp_servers = ntp_servers
    

    # create ntp policy
    try:
        # Create a 'ntp.Policy' resource.
        resp_ntp_policy = api_instance.create_ntp_policy(ntp_policy)
        print(resp_ntp_policy)
        
    except intersight.ApiException as e:
        print("Exception when calling NtpApi->create_ntp_policy: %s\n" % e)
        sys.exit(1)


def main():
 
    create_ntp_policy()

if __name__== "__main__":
    main()
