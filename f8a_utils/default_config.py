"""Default Configurations."""
import os

SNYK_API_TOKEN_VALIDATION_URL = os.getenv('SNYK_API_TOKEN_VALIDATION_URL',
                                          'https://snyk.io/api/v1/verify/token')
ENCRYPTION_KEY_FOR_SNYK_TOKEN = 'UMF9rhYIcaUKRdWfcAoUK1FQCXi_ENURjX1bGDgkljA='
