# swagger_client.SfeInfoApi

All URIs are relative to *https://developper.impots.bj/sygmef-emcf*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_info_invoice_types_get**](SfeInfoApi.md#api_info_invoice_types_get) | **GET** /api/info/invoiceTypes | 
[**api_info_payment_types_get**](SfeInfoApi.md#api_info_payment_types_get) | **GET** /api/info/paymentTypes | 
[**api_info_status_get**](SfeInfoApi.md#api_info_status_get) | **GET** /api/info/status | 
[**api_info_tax_groups_get**](SfeInfoApi.md#api_info_tax_groups_get) | **GET** /api/info/taxGroups | 

# **api_info_invoice_types_get**
> list[InvoiceTypeDto] api_info_invoice_types_get()



### Example
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
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InvoiceTypeDto]**](InvoiceTypeDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_info_payment_types_get**
> list[PaymentTypeDto] api_info_payment_types_get()



### Example
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
    api_response = api_instance.api_info_payment_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfeInfoApi->api_info_payment_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PaymentTypeDto]**](PaymentTypeDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_info_status_get**
> InfoResponseDto api_info_status_get()



### Example
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
    api_response = api_instance.api_info_status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfeInfoApi->api_info_status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InfoResponseDto**](InfoResponseDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_info_tax_groups_get**
> TaxGroupsDto api_info_tax_groups_get()



### Example
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
    api_response = api_instance.api_info_tax_groups_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfeInfoApi->api_info_tax_groups_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TaxGroupsDto**](TaxGroupsDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

