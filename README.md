# swagger-client
DGI Bénin - Tous droits réservés

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://www.impots.finances.gouv.bj](https://www.impots.finances.gouv.bj)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SfeInfoApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.api_info_invoice_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfeInfoApi->api_info_invoice_types_get: %s\n" % e)

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SfeInfoApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.api_info_payment_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfeInfoApi->api_info_payment_types_get: %s\n" % e)

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SfeInfoApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.api_info_status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfeInfoApi->api_info_status_get: %s\n" % e)

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SfeInfoApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.api_info_tax_groups_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfeInfoApi->api_info_tax_groups_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://developper.impots.bj/sygmef-emcf*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SfeInfoApi* | [**api_info_invoice_types_get**](docs/SfeInfoApi.md#api_info_invoice_types_get) | **GET** /api/info/invoiceTypes | 
*SfeInfoApi* | [**api_info_payment_types_get**](docs/SfeInfoApi.md#api_info_payment_types_get) | **GET** /api/info/paymentTypes | 
*SfeInfoApi* | [**api_info_status_get**](docs/SfeInfoApi.md#api_info_status_get) | **GET** /api/info/status | 
*SfeInfoApi* | [**api_info_tax_groups_get**](docs/SfeInfoApi.md#api_info_tax_groups_get) | **GET** /api/info/taxGroups | 
*SfeInvoiceApi* | [**api_invoice_get**](docs/SfeInvoiceApi.md#api_invoice_get) | **GET** /api/invoice | 
*SfeInvoiceApi* | [**api_invoice_post**](docs/SfeInvoiceApi.md#api_invoice_post) | **POST** /api/invoice | 
*SfeInvoiceApi* | [**api_invoice_uid_cancel_put**](docs/SfeInvoiceApi.md#api_invoice_uid_cancel_put) | **PUT** /api/invoice/{uid}/cancel | 
*SfeInvoiceApi* | [**api_invoice_uid_confirm_put**](docs/SfeInvoiceApi.md#api_invoice_uid_confirm_put) | **PUT** /api/invoice/{uid}/confirm | 
*SfeInvoiceApi* | [**api_invoice_uid_get**](docs/SfeInvoiceApi.md#api_invoice_uid_get) | **GET** /api/invoice/{uid} | 

## Documentation For Models

 - [AibGroupTypeEnum](docs/AibGroupTypeEnum.md)
 - [ClientDto](docs/ClientDto.md)
 - [EmcfInfoDto](docs/EmcfInfoDto.md)
 - [InfoResponseDto](docs/InfoResponseDto.md)
 - [InvoiceDetailsDto](docs/InvoiceDetailsDto.md)
 - [InvoiceRequestDataDto](docs/InvoiceRequestDataDto.md)
 - [InvoiceResponseDto](docs/InvoiceResponseDto.md)
 - [InvoiceTypeDto](docs/InvoiceTypeDto.md)
 - [InvoiceTypeEnum](docs/InvoiceTypeEnum.md)
 - [ItemDto](docs/ItemDto.md)
 - [OperatorDto](docs/OperatorDto.md)
 - [PaymentDto](docs/PaymentDto.md)
 - [PaymentTypeDto](docs/PaymentTypeDto.md)
 - [PaymentTypeEnum](docs/PaymentTypeEnum.md)
 - [PendingRequestDto](docs/PendingRequestDto.md)
 - [SecurityElementsDto](docs/SecurityElementsDto.md)
 - [StatusResponseDto](docs/StatusResponseDto.md)
 - [TaxGroupTypeEnum](docs/TaxGroupTypeEnum.md)
 - [TaxGroupsDto](docs/TaxGroupsDto.md)

## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


