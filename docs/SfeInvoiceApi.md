# swagger_client.SfeInvoiceApi

All URIs are relative to *https://developper.impots.bj/sygmef-emcf*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_invoice_get**](SfeInvoiceApi.md#api_invoice_get) | **GET** /api/invoice | 
[**api_invoice_post**](SfeInvoiceApi.md#api_invoice_post) | **POST** /api/invoice | 
[**api_invoice_uid_cancel_put**](SfeInvoiceApi.md#api_invoice_uid_cancel_put) | **PUT** /api/invoice/{uid}/cancel | 
[**api_invoice_uid_confirm_put**](SfeInvoiceApi.md#api_invoice_uid_confirm_put) | **PUT** /api/invoice/{uid}/confirm | 
[**api_invoice_uid_get**](SfeInvoiceApi.md#api_invoice_uid_get) | **GET** /api/invoice/{uid} | 

# **api_invoice_get**
> StatusResponseDto api_invoice_get()



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
api_instance = swagger_client.SfeInvoiceApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.api_invoice_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfeInvoiceApi->api_invoice_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponseDto**](StatusResponseDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_invoice_post**
> InvoiceResponseDto api_invoice_post(body=body)



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
api_instance = swagger_client.SfeInvoiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.InvoiceRequestDataDto() # InvoiceRequestDataDto |  (optional)

try:
    api_response = api_instance.api_invoice_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfeInvoiceApi->api_invoice_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoiceRequestDataDto**](InvoiceRequestDataDto.md)|  | [optional] 

### Return type

[**InvoiceResponseDto**](InvoiceResponseDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_invoice_uid_cancel_put**
> SecurityElementsDto api_invoice_uid_cancel_put(uid)



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
api_instance = swagger_client.SfeInvoiceApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    api_response = api_instance.api_invoice_uid_cancel_put(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfeInvoiceApi->api_invoice_uid_cancel_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**SecurityElementsDto**](SecurityElementsDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_invoice_uid_confirm_put**
> SecurityElementsDto api_invoice_uid_confirm_put(uid)



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
api_instance = swagger_client.SfeInvoiceApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    api_response = api_instance.api_invoice_uid_confirm_put(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfeInvoiceApi->api_invoice_uid_confirm_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**SecurityElementsDto**](SecurityElementsDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_invoice_uid_get**
> InvoiceDetailsDto api_invoice_uid_get(uid)



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
api_instance = swagger_client.SfeInvoiceApi(swagger_client.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    api_response = api_instance.api_invoice_uid_get(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SfeInvoiceApi->api_invoice_uid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**InvoiceDetailsDto**](InvoiceDetailsDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

