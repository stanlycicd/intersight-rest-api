import os
import datetime

import intersight


def config_credentials(description=None):
    iURL='https://intersight.com'
    configuration = intersight.Configuration(
        host=iURL,
        signing_info=intersight.HttpSigningConfiguration(
            #API Key ID from Cisco Intersight
            key_id="61e075b87564612d33952212/30792496/620562087564612d301e72fc",
            #API SecretKey.txt file location, downloaded from Cisco Intersight
            private_key_path="c:\\users\\PODX\downloads\SecretKey.txt",
            signing_scheme=intersight.signing.SCHEME_RSA_SHA256,
            signing_algorithm=intersight.signing.ALGORITHM_RSASSA_PKCS1v15,
            hash_algorithm=intersight.signing.HASH_SHA256,
            signed_headers=[intersight.signing.HEADER_REQUEST_TARGET,
                            intersight.signing.HEADER_CREATED,
                            intersight.signing.HEADER_EXPIRES,
                            intersight.signing.HEADER_HOST,
                            intersight.signing.HEADER_DATE,
                            intersight.signing.HEADER_DIGEST,
                            'Content-Type',
                            'User-Agent'
                            ],
            signature_max_validity=datetime.timedelta(minutes=5)
        )
    )
    configuration.verify_ssl = True
    configuration.proxy = os.getenv('https_proxy')
    api_client = intersight.ApiClient(configuration)
    api_client.set_default_header('referer', iURL)
    api_client.set_default_header('x-requested-with', 'XMLHttpRequest')
    api_client.set_default_header('Content-Type', 'application/json')
    return api_client

if __name__ == "__main__":
    config_credentials()
