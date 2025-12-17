# Copyright 2025 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Common utilities used by the MCP server."""

from typing import Any, Dict

from google.analytics import admin_v1beta, data_v1beta, admin_v1alpha
from google.api_core.gapic_v1.client_info import ClientInfo
from importlib import metadata
import google.auth
import proto
from google.oauth2 import service_account


def _get_package_version_with_fallback():
    """Returns the version of the package.

    Falls back to 'unknown' if the version can't be resolved.
    """
    try:
        return metadata.version("analytics-mcp")
    except:
        return "unknown"


# Client information that adds a custom user agent to all API requests.
_CLIENT_INFO = ClientInfo(
    user_agent=f"analytics-mcp/{_get_package_version_with_fallback()}"
)

# Read-only scope for Analytics Admin API and Analytics Data API.
_READ_ONLY_ANALYTICS_SCOPE = (
    "https://www.googleapis.com/auth/analytics.readonly"
)
_CREDENTIALS_PATH = {
  "type": "service_account",
  "project_id": "gen-lang-client-0711968883",
  "private_key_id": "7526aa836c74e2dccd9885312cadca5c970f830f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC93Pi1UsEuWAwj\nwiyg5vrX9lWDBlHZ73Rcnhv4MpKOeTYdl3IfOrb9uvFPB4kvPKbR9/bJExRLHNc1\n+QcT0pc4UdzJrSt89UhrHTYwIV6AbvnolaE7ErOEXySvtKY9PF64uSw+uyswPJJF\n7Nr+QQPdwRwNiNHu7d3/pselVZCMLNJZnLqre/FSkKCZyCfrYFU0+OtMA+Tb656/\nVTkpgPEH1soIHWwWc7Dll9EY4SfRZOgPN1RgMDs4tzjqeirSeNKSC1gV2R4uE8O2\nah7VhbRZO1m1kBR9BtHZLHCHgRoKFyNXw24ziqnJArKAZVaPKUE75XT1300vyKP/\njLKjalMjAgMBAAECggEAMB2OV+FbfKOqm+tLBRHUMyPFwvk4iArzib815l3mnz2f\nlbs6HCj0k/Oq0LTfsr1jp2V4QLfZljl+Xrq37PGbChZQ5jlBAp9klWSnRWZHfTPi\nmGtHG2HfZaX49aBJ2s3wUU74JAOp68UF6rueOf3+/VVBhzqLvUnBz1aUVNWM1sDb\nEpzsTpnJ040NWiDBnUosUgsS7DnsDyqDINbHmjI6B0xt2hjzqlMESKL6JEM65EQ3\nXbLfzaMV+0k2rDUI8+VTXi6VW6C7XXJbkb/MDoDE9+HIhntFsJVBBD0HKG6l8MUX\ny6YinVfR/rdDCR9eKPSdnGMwVCkhMbOAisrgACePeQKBgQDt7drLV0LYu5xcKXDg\nKdYDcVYIBBI2GtxyVcXY4BLUehBJ97K3z41ISgi2aSzDlwHpB2KFDGgFVY7DeJ63\n49LN4GpFoZDGV999QfB+r/k9+gn0CTjS39YyQDGcpcRdswp2jEn2p9Sbh1k+0C1b\nQDsa8opRlnJ0oPMBQ96lWgrkWQKBgQDMSI1xxouxJnFrz4MBaCDPbfXYatnbMNTP\n9Hpx8ZbsfkMWbthA8lpBzRJhFczGFSUzRO2Il9vagjXA+Tu+gdKlGO7lTdDqygIq\nK0TzsUj9K7zivo4sSpCuP54dg5uyvQ63X2bX0hV2PMWUBUQJ4oFhj2wozPywj89t\niRvHNw1z2wKBgC0YCIDDgBrdq+vXutnxc+thHqIUS3NPsfpFgWLyTP9SRyYNuSSX\nRLqvtWkFFAPZ6fXFfYmj6U8hgRZRFRvbJQf6AYpC7dJ5sxTlW3RXW9DARASpfsiQ\nveL2QbDjxgzQMyp2uknyUxxLEcIS6JXD3a/kygxejEDIhGX3/AmwwCG5AoGBAJwd\nhhrBBNho7JzbhN56WTisbAjr/3mHI9uYlkqluhUZmON36kQX8en/cmBHbKqkVj2M\nG4sboqSmhbXnwkSgqf4Jw+fxRAtqPaVEU/l4LrNrzXnq7nPiuBax/3/GqCI8YRa6\nDbo5jrVBVCz+qTR0qTOJi7rSjPnRrU+kTFo+NEWpAoGBAN1I6w+Y7zQgz0gT6ors\n2HysfgxTGm3kOrN0CQO7U/WChelMMi9dZQDw0C7J7FAswiBO8bOvqyOer+VFZomu\nNpwPAQkupm0Tx5DFVF9v3ulzSRCNwYMdhAiAa6isizpQtng30SEjiM0540rg28p3\n5t6I8m8uZ3HYD7lVdjg2PbEd\n-----END PRIVATE KEY-----\n",
  "client_email": "ga4-admin-api-service-account@gen-lang-client-0711968883.iam.gserviceaccount.com",
  "client_id": "113269687256414758284",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ga4-admin-api-service-account%40gen-lang-client-0711968883.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

def _create_credentials():
    """Returns Service Account credentials with read-only scope (HARDCODED)."""
    if not _CREDENTIALS_PATH:
        raise RuntimeError("Service account credentials path is not set")

    return service_account.Credentials.from_service_account_info(
        _CREDENTIALS_PATH,
        scopes=[_READ_ONLY_ANALYTICS_SCOPE],
    )

# def _create_credentials() -> google.auth.credentials.Credentials:
#     """Returns Application Default Credentials with read-only scope."""
#     (credentials, _) = google.auth.default(scopes=[_READ_ONLY_ANALYTICS_SCOPE])
#     return credentials


def create_admin_api_client() -> admin_v1beta.AnalyticsAdminServiceAsyncClient:
    """Returns a properly configured Google Analytics Admin API async client.

    Uses Application Default Credentials with read-only scope.
    """
    return admin_v1beta.AnalyticsAdminServiceAsyncClient(
        client_info=_CLIENT_INFO, credentials=_create_credentials()
    )


def create_data_api_client() -> data_v1beta.BetaAnalyticsDataAsyncClient:
    """Returns a properly configured Google Analytics Data API async client.

    Uses Application Default Credentials with read-only scope.
    """
    return data_v1beta.BetaAnalyticsDataAsyncClient(
        client_info=_CLIENT_INFO, credentials=_create_credentials()
    )


def create_admin_alpha_api_client() -> (
    admin_v1alpha.AnalyticsAdminServiceAsyncClient
):
    """Returns a properly configured Google Analytics Admin API (alpha) async client.
    Uses Application Default Credentials with read-only scope.
    """
    return admin_v1alpha.AnalyticsAdminServiceAsyncClient(
        client_info=_CLIENT_INFO, credentials=_create_credentials()
    )


def construct_property_rn(property_value: int | str) -> str:
    """Returns a property resource name in the format required by APIs."""
    property_num = None
    if isinstance(property_value, int):
        property_num = property_value
    elif isinstance(property_value, str):
        property_value = property_value.strip()
        if property_value.isdigit():
            property_num = int(property_value)
        elif property_value.startswith("properties/"):
            numeric_part = property_value.split("/")[-1]
            if numeric_part.isdigit():
                property_num = int(numeric_part)
    if property_num is None:
        raise ValueError(
            (
                f"Invalid property ID: {property_value}. "
                "A valid property value is either a number or a string starting "
                "with 'properties/' and followed by a number."
            )
        )

    return f"properties/{property_num}"


def proto_to_dict(obj: proto.Message) -> Dict[str, Any]:
    """Converts a proto message to a dictionary."""
    return type(obj).to_dict(
        obj, use_integers_for_enums=False, preserving_proto_field_name=True
    )


def proto_to_json(obj: proto.Message) -> str:
    """Converts a proto message to a JSON string."""
    return type(obj).to_json(obj, indent=None, preserving_proto_field_name=True)
