# Getting Started with Nucoro API v2

## Getting Started

### Introduction

No description

### Building

You must have Python `3 >=3.6, <= 3.9` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK.To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Nucoroapiv2-Python&step=installDependencies)

### Installation

The following section explains how to use the nucoroapiv2 library in a new project.

#### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Nucoroapiv2-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Nucoroapiv2-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Nucoroapiv2-Python&projectName=nucoroapiv2&step=openProject1)

#### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Nucoroapiv2-Python&projectName=nucoroapiv2&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Nucoroapiv2-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Nucoroapiv2-Python&projectName=nucoroapiv2&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Nucoroapiv2-Python&projectName=nucoroapiv2&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from nucoroapiv2.nucoroapiv_2_client import Nucoroapiv2Client
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Nucoroapiv2-Python&projectName=nucoroapiv2&libraryName=nucoroapiv2.nucoroapiv_2_client&className=Nucoroapiv2Client&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

#### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Nucoroapiv2-Python&projectName=nucoroapiv2&libraryName=nucoroapiv2.nucoroapiv_2_client&className=Nucoroapiv2Client&step=runProject)

### Initialize the API Client

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `default_host` | `string` | *Default*: `'www.example.com'` |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |

The API client can be initialized as follows:

```python
from nucoroapiv2.nucoroapiv_2_client import Nucoroapiv2Client
from nucoroapiv2.configuration import Environment

client = Nucoroapiv2Client(
    environment=Environment.PRODUCTION,
    default_host = 'www.example.com',)
```

### Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `nose` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
nosetests
```

## Client Class Documentation

### Nucoro API v2 Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

### Controllers

| Name | Description |
|  --- | --- |
| api | Gets ApiController |
| auth | Gets AuthController |
| application | Gets ApplicationController |

## API Reference

### List of APIs

* [Api](#api)
* [Auth](#auth)
* [Application](#application)

### Api

#### Overview

##### Get instance

An instance of the `ApiController` class can be accessed from the API Client.

```
api_controller = client.api
```

#### Api Schema Retrieve

OpenApi3 schema for this API. Format can be selected via content negotiation.

- YAML: application/vnd.oai.openapi
- JSON: application/vnd.oai.openapi+json

:information_source: **Note** This endpoint does not require authentication.

```python
def api_schema_retrieve(self,
                       format=None,
                       lang=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `format` | [`FormatEnum`](#format) | Query, Optional | - |
| `lang` | [`LangEnum`](#lang) | Query, Optional | - |

##### Response Type

`dict`

##### Example Usage

```python
result = api_controller.api_schema_retrieve()
```

#### Api V 2 Advice Engines Ets Categories List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_advice_engines_ets_categories_list(self,
                                              limit=None,
                                              offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedCategoryList`](#paginated-category-list)

##### Example Usage

```python
result = api_controller.api_v_2_advice_engines_ets_categories_list()
```

#### Api V 2 Advice Engines Ets Core Category Groups List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_advice_engines_ets_core_category_groups_list(self,
                                                        limit=None,
                                                        offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedCoreCategoryGroupList`](#paginated-core-category-group-list)

##### Example Usage

```python
result = api_controller.api_v_2_advice_engines_ets_core_category_groups_list()
```

#### Api V 2 Advice Engines Ets Forecast Create

The forecast positions and amounts for the time_horizon and  risk_level chosen.
Taking into account the initial_auto_deposit and the initial_amount jointly with the selected filters.

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_advice_engines_ets_forecast_create(self,
                                              time_horizon,
                                              initial_amount,
                                              risk_level,
                                              recurring_amount=None,
                                              recurring_period=None,
                                              favourite_categories=None,
                                              excluded_categories=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time_horizon` | `int` | Form, Required | **Constraints**: `>= 1`, `<= 50` |
| `initial_amount` | `float` | Form, Required | **Constraints**: `>= 1`, `<= 1000000000000` |
| `risk_level` | `int` | Form, Required | **Constraints**: `>= 1`, `<= 10` |
| `recurring_amount` | `float` | Form, Optional | **Constraints**: `>= 0`, `<= 1000000000000` |
| `recurring_period` | `int` | Form, Optional | **Constraints**: `>= 0`, `<= 12` |
| `favourite_categories` | `List of string` | Form, Optional | - |
| `excluded_categories` | `List of string` | Form, Optional | - |

##### Response Type

[`ETSForecastRequest`](#ets-forecast-request)

##### Example Usage

```python
time_horizon = 200
initial_amount = 140.36
risk_level = 66

result = api_controller.api_v_2_advice_engines_ets_forecast_create(time_horizon, initial_amount, risk_level)
```

#### Api V 2 Advice Engines Ets Preset Category Groups List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_advice_engines_ets_preset_category_groups_list(self,
                                                          limit=None,
                                                          offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedPresetCategoryGroupList`](#paginated-preset-category-group-list)

##### Example Usage

```python
result = api_controller.api_v_2_advice_engines_ets_preset_category_groups_list()
```

#### Api V 2 Advice Engines Model Portfolio Forecast Create

The forecast positions and amounts for the time_horizon chosen.
Taking into account the initial_auto_deposit and the initial_amount jointly with the selected filters.

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_advice_engines_model_portfolio_forecast_create(self,
                                                          time_horizon,
                                                          initial_amount,
                                                          model_portfolio,
                                                          recurring_amount=None,
                                                          recurring_period=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time_horizon` | `int` | Form, Required | **Constraints**: `>= 1`, `<= 50` |
| `initial_amount` | `float` | Form, Required | **Constraints**: `>= 1`, `<= 1000000000000` |
| `model_portfolio` | `string` | Form, Required | - |
| `recurring_amount` | `float` | Form, Optional | **Constraints**: `>= 0`, `<= 1000000000000` |
| `recurring_period` | `int` | Form, Optional | **Constraints**: `>= 0`, `<= 12` |

##### Response Type

[`ModelPortfolioForecastRequest`](#model-portfolio-forecast-request)

##### Example Usage

```python
time_horizon = 200
initial_amount = 140.36
model_portfolio = 'model_portfolio2'

result = api_controller.api_v_2_advice_engines_model_portfolio_forecast_create(time_horizon, initial_amount, model_portfolio)
```

#### Api V 2 Advice Engines Model Portfolio Model Portfolios List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_advice_engines_model_portfolio_model_portfolios_list(self,
                                                                extra_data=None,
                                                                limit=None,
                                                                name=None,
                                                                offset=None,
                                                                risk_higher=None,
                                                                risk_level=None,
                                                                risk_lower=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `extra_data` | `dict` | Query, Optional | Additional ModelPortfolio attributes |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `name` | `string` | Query, Optional | - |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `risk_higher` | `int` | Query, Optional | - |
| `risk_level` | `int` | Query, Optional | - |
| `risk_lower` | `int` | Query, Optional | - |

##### Response Type

[`PaginatedInvestorModelPortfolioList`](#paginated-investor-model-portfolio-list)

##### Example Usage

```python
result = api_controller.api_v_2_advice_engines_model_portfolio_model_portfolios_list()
```

#### Api V 2 Advice Engines Model Portfolio Model Portfolios Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_advice_engines_model_portfolio_model_portfolios_retrieve(self,
                                                                    uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`InvestorModelPortfolio`](#investor-model-portfolio)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_advice_engines_model_portfolio_model_portfolios_retrieve(uuid)
```

#### Api V 2 Assets List

A list of Assets filtered by category codes.
Default is an empty dict which returns the whole universe.

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_assets_list(self,
                       asset_type=None,
                       category_code=None,
                       category_type=None,
                       currency=None,
                       isin=None,
                       limit=None,
                       market=None,
                       name=None,
                       offset=None,
                       status=None,
                       ticker=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_type` | [`AssetTypeEnum`](#asset-type-enum) | Query, Optional | - |
| `category_code` | `List of string` | Query, Optional | - |
| `category_type` | `List of string` | Query, Optional | - |
| `currency` | `int` | Query, Optional | - |
| `isin` | `string` | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `market` | `int` | Query, Optional | - |
| `name` | `string` | Query, Optional | - |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `status` | [`Status6f6Enum`](#status-6-f-6-enum) | Query, Optional | - |
| `ticker` | `string` | Query, Optional | - |

##### Response Type

[`PaginatedAssetListList`](#paginated-asset-list-list)

##### Example Usage

```python
result = api_controller.api_v_2_assets_list()
```

#### Api V 2 Assets Retrieve

Allows get an asset instance by

* UUID
* ISIN
* ISIN & MARKET_CODE
* ISIN & MARKET_CODE & CURRENCY_CODE

Examples:
* assets/a66633d7-4418-4c85-9582-01c80df531d4/
* assets/IE00B579F325/
* assets/IE00B579F325_XETR_GBP/
* assets/IE00B579F325_XETR/

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_assets_retrieve(self,
                           asset_identifier)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_identifier` | `uuid\|string` | Template, Required | - |

##### Response Type

[`AssetDetail`](#asset-detail)

##### Example Usage

```python
asset_identifier = '00001b5a-0000-0000-0000-000000000000'

result = api_controller.api_v_2_assets_retrieve(asset_identifier)
```

#### Api V 2 Assets Intraday Prices List

Prices (from an Asset) list view endpoints.

GET: Prices retrieve (rest framework builtin overriding get_object)

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_assets_intraday_prices_list(self,
                                       asset_identifier,
                                       date_after=None,
                                       date_before=None,
                                       datetime_after=None,
                                       datetime_before=None,
                                       limit=None,
                                       offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_identifier` | `uuid\|string` | Template, Required | - |
| `date_after` | `date` | Query, Optional | - |
| `date_before` | `date` | Query, Optional | - |
| `datetime_after` | `datetime` | Query, Optional | - |
| `datetime_before` | `datetime` | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedIntradayPriceList`](#paginated-intraday-price-list)

##### Example Usage

```python
asset_identifier = '00001b5a-0000-0000-0000-000000000000'

result = api_controller.api_v_2_assets_intraday_prices_list(asset_identifier)
```

#### Api V 2 Assets Intraday Prices Latest Retrieve

Prices (from an Asset) list view endpoints.

GET: Prices retrieve (rest framework builtin overriding get_object)

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_assets_intraday_prices_latest_retrieve(self,
                                                  asset_identifier)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_identifier` | `uuid\|string` | Template, Required | - |

##### Response Type

[`IntradayPrice`](#intraday-price)

##### Example Usage

```python
asset_identifier = '00001b5a-0000-0000-0000-000000000000'

result = api_controller.api_v_2_assets_intraday_prices_latest_retrieve(asset_identifier)
```

#### Api V 2 Assets Performance List

Retrieve asset's yearly performance.

This View overwrites ListAPIView's 'list' method because it doesn't have
any hook that allows us to call 'get_asset_price_year_graph after the
filtering is applied.

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_assets_performance_list(self,
                                   asset_identifier,
                                   date_year_after=None,
                                   date_year_before=None,
                                   limit=None,
                                   offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_identifier` | `uuid\|string` | Template, Required | - |
| `date_year_after` | `float` | Query, Optional | - |
| `date_year_before` | `float` | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedAssetGrowthList`](#paginated-asset-growth-list)

##### Example Usage

```python
asset_identifier = '00001b5a-0000-0000-0000-000000000000'

result = api_controller.api_v_2_assets_performance_list(asset_identifier)
```

#### Api V 2 Assets Prices List

Prices (from an Asset) list view endpoints.

GET: Prices retrieve (rest framework builtin overriding get_object)

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_assets_prices_list(self,
                              asset_identifier,
                              date_after=None,
                              date_before=None,
                              datetime_after=None,
                              datetime_before=None,
                              limit=None,
                              offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_identifier` | `uuid\|string` | Template, Required | - |
| `date_after` | `date` | Query, Optional | - |
| `date_before` | `date` | Query, Optional | - |
| `datetime_after` | `datetime` | Query, Optional | - |
| `datetime_before` | `datetime` | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedPriceList`](#paginated-price-list)

##### Example Usage

```python
asset_identifier = '00001b5a-0000-0000-0000-000000000000'

result = api_controller.api_v_2_assets_prices_list(asset_identifier)
```

#### Api V 2 Assets Prices Latest Retrieve

Prices (from an Asset) list view endpoints.

GET: Prices retrieve (rest framework builtin overriding get_object)

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_assets_prices_latest_retrieve(self,
                                         asset_identifier)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_identifier` | `uuid\|string` | Template, Required | - |

##### Response Type

[`Price`](#price)

##### Example Usage

```python
asset_identifier = '00001b5a-0000-0000-0000-000000000000'

result = api_controller.api_v_2_assets_prices_latest_retrieve(asset_identifier)
```

#### Api V 2 Assets Categories List

Retrieve all asset categories

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_assets_categories_list(self,
                                  limit=None,
                                  offset=None,
                                  mtype=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `mtype` | `string` | Query, Optional | - |

##### Response Type

[`PaginatedAssetCategoryList`](#paginated-asset-category-list)

##### Example Usage

```python
result = api_controller.api_v_2_assets_categories_list()
```

#### Api V 2 Billing Invoices List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_billing_invoices_list(self,
                                 date_from=None,
                                 date_to=None,
                                 limit=None,
                                 offset=None,
                                 status=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_from` | `date` | Query, Optional | - |
| `date_to` | `date` | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `status` | [`Status260Enum`](#status-260-enum) | Query, Optional | - |

##### Response Type

[`PaginatedInvoiceListList`](#paginated-invoice-list-list)

##### Example Usage

```python
result = api_controller.api_v_2_billing_invoices_list()
```

#### Api V 2 Billing Invoices Retrieve

This mixin implements binary responses.
It supports PDF and Base64. It can be adapted to any django View that implements the retrieve method

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_billing_invoices_retrieve(self,
                                     uuid,
                                     format=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |
| `format` | [`Format1Enum`](#format-1) | Query, Optional | - |

##### Response Type

[`InvoiceDetails`](#invoice-details)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_billing_invoices_retrieve(uuid)
```

#### Api V 2 Broker Orders List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_broker_orders_list(self,
                              portfolio_uuid,
                              advice_external_id=None,
                              asset=None,
                              completed_after=None,
                              completed_before=None,
                              extra_data=None,
                              limit=None,
                              offset=None,
                              portfolio=None,
                              status=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `advice_external_id` | `string` | Query, Optional | - |
| `asset` | `string` | Query, Optional | - |
| `completed_after` | `date` | Query, Optional | - |
| `completed_before` | `date` | Query, Optional | - |
| `extra_data` | `dict` | Query, Optional | Additional order attributes for the specific portal |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `portfolio` | `string` | Query, Optional | - |
| `status` | `string` | Query, Optional | - |

##### Response Type

[`PaginatedOrderListList`](#paginated-order-list-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_broker_orders_list(portfolio_uuid)
```

#### Api V 2 Broker Orders Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_broker_orders_create(self,
                                portfolio_uuid,
                                shares,
                                asset,
                                order_type,
                                method,
                                portfolio=None,
                                limit_price=None,
                                stop_price=None,
                                duration=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `shares` | `int` | Form, Required | **Constraints**: `>= 1` |
| `asset` | [`RelatedAssetSerializerWithAssetCategories`](#related-asset-serializer-with-asset-categories) | Form, Required | Allow get asset by multiple params or UUID |
| `order_type` | [`OrderTypeEnum`](#order-type-enum) | Form, Required | - |
| `method` | [`CreateOrderMethodEnum`](#create-order-method-enum) | Form, Required | - |
| `portfolio` | `string` | Form, Optional | - |
| `limit_price` | `float` | Form, Optional | **Constraints**: `>= 0.01`, `<= 1000000000000` |
| `stop_price` | `float` | Form, Optional | **Constraints**: `>= 0.01`, `<= 1000000000000` |
| `duration` | [`DurationEnum`](#duration-enum) | Form, Optional | - |

##### Response Type

[`CreateOrder`](#create-order)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
shares = 214
asset = RelatedAssetSerializerWithAssetCategories()
asset.uuid = '000010be-0000-0000-0000-000000000000'
asset.isin = 'isin0'
asset.ticker = 'ticker2'
asset.name = 'name0'
asset.categories = ['categories2', 'categories1']
order_type = OrderTypeEnum.VERIFICATION
method = CreateOrderMethodEnum.LIMIT

result = api_controller.api_v_2_broker_orders_create(portfolio_uuid, shares, asset, order_type, method)
```

#### Api V 2 Broker Orders Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_broker_orders_retrieve(self,
                                  portfolio_uuid,
                                  uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`OrderList`](#order-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_broker_orders_retrieve(portfolio_uuid, uuid)
```

#### Api V 2 Broker Orders Destroy

Cancel or request cancellation to the broker

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_broker_orders_destroy(self,
                                 portfolio_uuid,
                                 uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_broker_orders_destroy(portfolio_uuid, uuid)
```

#### Api V 2 Clients Activities List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_activities_list(self,
                                   client_uuid,
                                   limit=None,
                                   offset=None,
                                   target=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `target` | [`List of TargetEnum`](#target) | Query, Optional | - |

##### Response Type

[`PaginatedFeedActivityListList`](#paginated-feed-activity-list-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_activities_list(client_uuid)
```

#### Api V 2 Clients Activities Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_activities_retrieve(self,
                                       client_uuid,
                                       uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`FeedActivityList`](#feed-activity-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_activities_retrieve(client_uuid, uuid)
```

#### Api V 2 Clients Advice Engines List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_advice_engines_list(self,
                                       client_uuid,
                                       uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_advice_engines_list(client_uuid, uuid)
```

#### Api V 2 Clients Advice Engines Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_advice_engines_retrieve(self,
                                           client_uuid,
                                           uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_advice_engines_retrieve(client_uuid, uuid)
```

#### Api V 2 Clients Billing Fees List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_billing_fees_list(self,
                                     client_uuid,
                                     investor_fee_uuid,
                                     limit=None,
                                     offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `investor_fee_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedInvestorFeeList`](#paginated-investor-fee-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
investor_fee_uuid = '00000cea-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_billing_fees_list(client_uuid, investor_fee_uuid)
```

#### Api V 2 Clients Billing Fees Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_billing_fees_create(self,
                                       client_uuid,
                                       investor_fee_uuid,
                                       fee_type,
                                       concept,
                                       uuid,
                                       created,
                                       updated,
                                       value=None,
                                       value_unit=None,
                                       date_from=None,
                                       date_to=None,
                                       amount_from=None,
                                       amount_to=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `investor_fee_uuid` | `uuid\|string` | Template, Required | - |
| `fee_type` | [`FeeTypeEnum`](#fee-type-enum) | Form, Required | Each choice should have a related method on fee model that contains the logic to charge the client |
| `concept` | `string` | Form, Required | Describes the concept that will be shown on invoice<br>**Constraints**: *Maximum Length*: `100` |
| `uuid` | `uuid\|string` | Form, Required | - |
| `created` | `datetime` | Form, Required | - |
| `updated` | `datetime` | Form, Required | - |
| `value` | `float` | Form, Optional | Determinates a percentage or an amount (between 0 and 1 if percentage otherwise Positive Decimal)<br>**Constraints**: `>= 0`, `<= 100` |
| `value_unit` | [`ValueUnitEnum`](#value-unit-enum) | Form, Optional | Determines the type of the value(Fixed, Percentage) |
| `date_from` | `date` | Form, Optional | Defines the end date when the percentage should be applied |
| `date_to` | `date` | Form, Optional | Defines the start date when the percentage should be applied |
| `amount_from` | `float` | Form, Optional | Defines the amount start range when the percentage should be applied<br>**Constraints**: `>= -1000000000`, `<= 1000000000` |
| `amount_to` | `float` | Form, Optional | Defines the amount end range when the percentage should be applied<br>**Constraints**: `>= -1000000000`, `<= 1000000000` |

##### Response Type

[`InvestorFee`](#investor-fee)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
investor_fee_uuid = '00000cea-0000-0000-0000-000000000000'
fee_type = FeeTypeEnum.PORTAL_SERVICE
concept = 'concept4'
uuid = '00000f7e-0000-0000-0000-000000000000'
created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
updated = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = api_controller.api_v_2_clients_billing_fees_create(client_uuid, investor_fee_uuid, fee_type, concept, uuid, created, updated)
```

#### Api V 2 Clients Billing Fees Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_billing_fees_retrieve(self,
                                         client_uuid,
                                         investor_fee_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `investor_fee_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`InvestorFee`](#investor-fee)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
investor_fee_uuid = '00000cea-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_billing_fees_retrieve(client_uuid, investor_fee_uuid)
```

#### Api V 2 Clients Billing Fees Update

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_billing_fees_update(self,
                                       client_uuid,
                                       investor_fee_uuid,
                                       fee_type,
                                       concept,
                                       uuid,
                                       created,
                                       updated,
                                       value=None,
                                       value_unit=None,
                                       date_from=None,
                                       date_to=None,
                                       amount_from=None,
                                       amount_to=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `investor_fee_uuid` | `uuid\|string` | Template, Required | - |
| `fee_type` | [`FeeTypeEnum`](#fee-type-enum) | Form, Required | Each choice should have a related method on fee model that contains the logic to charge the client |
| `concept` | `string` | Form, Required | Describes the concept that will be shown on invoice<br>**Constraints**: *Maximum Length*: `100` |
| `uuid` | `uuid\|string` | Form, Required | - |
| `created` | `datetime` | Form, Required | - |
| `updated` | `datetime` | Form, Required | - |
| `value` | `float` | Form, Optional | Determinates a percentage or an amount (between 0 and 1 if percentage otherwise Positive Decimal)<br>**Constraints**: `>= 0`, `<= 100` |
| `value_unit` | [`ValueUnitEnum`](#value-unit-enum) | Form, Optional | Determines the type of the value(Fixed, Percentage) |
| `date_from` | `date` | Form, Optional | Defines the end date when the percentage should be applied |
| `date_to` | `date` | Form, Optional | Defines the start date when the percentage should be applied |
| `amount_from` | `float` | Form, Optional | Defines the amount start range when the percentage should be applied<br>**Constraints**: `>= -1000000000`, `<= 1000000000` |
| `amount_to` | `float` | Form, Optional | Defines the amount end range when the percentage should be applied<br>**Constraints**: `>= -1000000000`, `<= 1000000000` |

##### Response Type

[`InvestorFee`](#investor-fee)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
investor_fee_uuid = '00000cea-0000-0000-0000-000000000000'
fee_type = FeeTypeEnum.PORTAL_SERVICE
concept = 'concept4'
uuid = '00000f7e-0000-0000-0000-000000000000'
created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
updated = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = api_controller.api_v_2_clients_billing_fees_update(client_uuid, investor_fee_uuid, fee_type, concept, uuid, created, updated)
```

#### Api V 2 Clients Billing Fees Partial Update

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_billing_fees_partial_update(self,
                                               client_uuid,
                                               investor_fee_uuid,
                                               value=None,
                                               value_unit=None,
                                               fee_type=None,
                                               concept=None,
                                               date_from=None,
                                               date_to=None,
                                               amount_from=None,
                                               amount_to=None,
                                               uuid=None,
                                               created=None,
                                               updated=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `investor_fee_uuid` | `uuid\|string` | Template, Required | - |
| `value` | `float` | Form, Optional | Determinates a percentage or an amount (between 0 and 1 if percentage otherwise Positive Decimal)<br>**Constraints**: `>= 0`, `<= 100` |
| `value_unit` | [`ValueUnitEnum`](#value-unit-enum) | Form, Optional | Determines the type of the value(Fixed, Percentage) |
| `fee_type` | [`FeeTypeEnum`](#fee-type-enum) | Form, Optional | Each choice should have a related method on fee model that contains the logic to charge the client |
| `concept` | `string` | Form, Optional | Describes the concept that will be shown on invoice<br>**Constraints**: *Maximum Length*: `100` |
| `date_from` | `date` | Form, Optional | Defines the end date when the percentage should be applied |
| `date_to` | `date` | Form, Optional | Defines the start date when the percentage should be applied |
| `amount_from` | `float` | Form, Optional | Defines the amount start range when the percentage should be applied<br>**Constraints**: `>= -1000000000`, `<= 1000000000` |
| `amount_to` | `float` | Form, Optional | Defines the amount end range when the percentage should be applied<br>**Constraints**: `>= -1000000000`, `<= 1000000000` |
| `uuid` | `uuid\|string` | Form, Optional | - |
| `created` | `datetime` | Form, Optional | - |
| `updated` | `datetime` | Form, Optional | - |

##### Response Type

[`InvestorFee`](#investor-fee)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
investor_fee_uuid = '00000cea-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_billing_fees_partial_update(client_uuid, investor_fee_uuid)
```

#### Api V 2 Clients Billing Fees Destroy

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_billing_fees_destroy(self,
                                        client_uuid,
                                        investor_fee_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `investor_fee_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
investor_fee_uuid = '00000cea-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_billing_fees_destroy(client_uuid, investor_fee_uuid)
```

#### Api V 2 Clients Billing Invoices List

This mixin implements binary responses.
It supports PDF and Base64. It can be adapted to any django View that implements the retrieve method

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_billing_invoices_list(self,
                                         client_uuid,
                                         format=None,
                                         limit=None,
                                         offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `format` | [`Format1Enum`](#format-1) | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedInvoiceListList`](#paginated-invoice-list-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_billing_invoices_list(client_uuid)
```

#### Api V 2 Clients Billing Invoices Retrieve

This mixin implements binary responses.
It supports PDF and Base64. It can be adapted to any django View that implements the retrieve method

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_billing_invoices_retrieve(self,
                                             client_uuid,
                                             uuid,
                                             format=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |
| `format` | [`Format1Enum`](#format-1) | Query, Optional | - |

##### Response Type

[`InvoiceList`](#invoice-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_billing_invoices_retrieve(client_uuid, uuid)
```

#### Api V 2 Clients Documents List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_documents_list(self,
                                  client_uuid,
                                  client=None,
                                  description=None,
                                  doc_type=None,
                                  extra_data=None,
                                  limit=None,
                                  name=None,
                                  offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `client` | `int` | Query, Optional | - |
| `description` | `string` | Query, Optional | - |
| `doc_type` | [`List of DocTypeEnum`](#doc-type-enum) | Query, Optional | - |
| `extra_data` | `dict` | Query, Optional | Additional document attributes for the specific portal |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `name` | `string` | Query, Optional | - |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedDocumentList`](#paginated-document-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_documents_list(client_uuid)
```

#### Api V 2 Clients Documents Create

Uploads a document for a certain user.

This call expects the files and parameters being sent as form/multipart
encoding.

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_documents_create(self,
                                    client_uuid,
                                    uuid,
                                    name,
                                    doc_type,
                                    path,
                                    description=None,
                                    extra_data=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `name` | `string` | Form, Required | - |
| `doc_type` | [`DocTypeEnum`](#doc-type-enum) | Form, Required | - |
| `path` | `string` | Form, Required | - |
| `description` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `extra_data` | `dict` | Form, Optional | Additional document attributes for the specific portal |

##### Response Type

[`Document`](#document)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
name = 'name0'
doc_type = DocTypeEnum.ID_PERSONAL
path = 'path6'

result = api_controller.api_v_2_clients_documents_create(client_uuid, uuid, name, doc_type, path)
```

#### Api V 2 Clients Documents Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_documents_retrieve(self,
                                      client_uuid,
                                      uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`Document`](#document)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_documents_retrieve(client_uuid, uuid)
```

#### Api V 2 Clients Documents Destroy

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_documents_destroy(self,
                                     client_uuid,
                                     uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_documents_destroy(client_uuid, uuid)
```

#### Api V 2 Clients Report Statements List

This mixin implements binary responses.
It supports PDF and Base64. It can be adapted to any django View that implements the retrieve method

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_report_statements_list(self,
                                          client_uuid,
                                          format=None,
                                          limit=None,
                                          offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `format` | [`Format1Enum`](#format-1) | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedStatementList`](#paginated-statement-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_report_statements_list(client_uuid)
```

#### Api V 2 Clients Report Statements Retrieve

This mixin implements binary responses.
It supports PDF and Base64. It can be adapted to any django View that implements the retrieve method

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_report_statements_retrieve(self,
                                              client_uuid,
                                              uuid,
                                              format=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |
| `format` | [`Format1Enum`](#format-1) | Query, Optional | - |

##### Response Type

[`Statement`](#statement)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_report_statements_retrieve(client_uuid, uuid)
```

#### Api V 2 Clients Report Tax Reports List

This mixin implements binary responses.
It supports PDF and Base64. It can be adapted to any django View that implements the retrieve method

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_report_tax_reports_list(self,
                                           client_uuid,
                                           format=None,
                                           limit=None,
                                           offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `format` | [`Format1Enum`](#format-1) | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedTaxReportList`](#paginated-tax-report-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_report_tax_reports_list(client_uuid)
```

#### Api V 2 Clients Report Tax Reports Retrieve

This mixin implements binary responses.
It supports PDF and Base64. It can be adapted to any django View that implements the retrieve method

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_report_tax_reports_retrieve(self,
                                               client_uuid,
                                               uuid,
                                               format=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |
| `format` | [`Format1Enum`](#format-1) | Query, Optional | - |

##### Response Type

[`TaxReport`](#tax-report)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_report_tax_reports_retrieve(client_uuid, uuid)
```

#### Api V 2 Clients Watchlists List

Applies filters without declaring them explicitly.
How? Creating those filters on the fly.

# How it works.

- Declare 'filterable_fields' in the view.
  E.g. filterable_fields = ['status', 'name']
  __all__ is allowed. It applies filters for all model attributes.

- COMMON_FILTERS: common filters configuration.
  
  - key: field name. E.g. status.
  - filter_class. filter class for the field.
  - args. Args for the filter_class __init__.  These args are taken from the queryset model
    E.g. 'args': {'choices': 'STATUS_CHOICES'} means Filter(choices=queryset.model.STATUS_CHOICES)

# How to use it:

class PortfolioListCreateView(CommonFilterMixin, InvestorAPIViewMixin, ListCreateAPIView):
filterable_fields = ['status', 'name']

# Filters priority.

1- Explicit filter declared in the filterset_class
2- Filters declared in COMMON_FILTERS
3- Filterset.FILTER_DEFAULTS

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_watchlists_list(self,
                                   client_uuid,
                                   watchlist_uuid,
                                   limit=None,
                                   offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `watchlist_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedWatchlistList`](#paginated-watchlist-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
watchlist_uuid = '00001df0-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_watchlists_list(client_uuid, watchlist_uuid)
```

#### Api V 2 Clients Watchlists Create

Applies filters without declaring them explicitly.
How? Creating those filters on the fly.

# How it works.

- Declare 'filterable_fields' in the view.
  E.g. filterable_fields = ['status', 'name']
  __all__ is allowed. It applies filters for all model attributes.

- COMMON_FILTERS: common filters configuration.
  
  - key: field name. E.g. status.
  - filter_class. filter class for the field.
  - args. Args for the filter_class __init__.  These args are taken from the queryset model
    E.g. 'args': {'choices': 'STATUS_CHOICES'} means Filter(choices=queryset.model.STATUS_CHOICES)

# How to use it:

class PortfolioListCreateView(CommonFilterMixin, InvestorAPIViewMixin, ListCreateAPIView):
filterable_fields = ['status', 'name']

# Filters priority.

1- Explicit filter declared in the filterset_class
2- Filters declared in COMMON_FILTERS
3- Filterset.FILTER_DEFAULTS

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_watchlists_create(self,
                                     client_uuid,
                                     watchlist_uuid,
                                     uuid,
                                     name,
                                     assets)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `watchlist_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `name` | `string` | Form, Required | **Constraints**: *Maximum Length*: `250` |
| `assets` | [`List of RelatedAssetSerializerWithPermission`](#related-asset-serializer-with-permission) | Form, Required | - |

##### Response Type

[`Watchlist`](#watchlist)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
watchlist_uuid = '00001df0-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
name = 'name0'
assets = []

assets.append(RelatedAssetSerializerWithPermission())
assets[0].uuid = '0000062c-0000-0000-0000-000000000000'
assets[0].isin = 'isin6'
assets[0].ticker = 'ticker6'
assets[0].name = 'name4'

assets.append(RelatedAssetSerializerWithPermission())
assets[1].uuid = '0000062d-0000-0000-0000-000000000000'
assets[1].isin = 'isin5'
assets[1].ticker = 'ticker7'
assets[1].name = 'name5'

assets.append(RelatedAssetSerializerWithPermission())
assets[2].uuid = '0000062e-0000-0000-0000-000000000000'
assets[2].isin = 'isin4'
assets[2].ticker = 'ticker8'
assets[2].name = 'name6'


result = api_controller.api_v_2_clients_watchlists_create(client_uuid, watchlist_uuid, uuid, name, assets)
```

#### Api V 2 Clients Watchlists Retrieve

Applies filters without declaring them explicitly.
How? Creating those filters on the fly.

# How it works.

- Declare 'filterable_fields' in the view.
  E.g. filterable_fields = ['status', 'name']
  __all__ is allowed. It applies filters for all model attributes.

- COMMON_FILTERS: common filters configuration.
  
  - key: field name. E.g. status.
  - filter_class. filter class for the field.
  - args. Args for the filter_class __init__.  These args are taken from the queryset model
    E.g. 'args': {'choices': 'STATUS_CHOICES'} means Filter(choices=queryset.model.STATUS_CHOICES)

# How to use it:

class PortfolioListCreateView(CommonFilterMixin, InvestorAPIViewMixin, ListCreateAPIView):
filterable_fields = ['status', 'name']

# Filters priority.

1- Explicit filter declared in the filterset_class
2- Filters declared in COMMON_FILTERS
3- Filterset.FILTER_DEFAULTS

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_watchlists_retrieve(self,
                                       client_uuid,
                                       watchlist_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `watchlist_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`Watchlist`](#watchlist)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
watchlist_uuid = '00001df0-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_watchlists_retrieve(client_uuid, watchlist_uuid)
```

#### Api V 2 Clients Watchlists Update

Applies filters without declaring them explicitly.
How? Creating those filters on the fly.

# How it works.

- Declare 'filterable_fields' in the view.
  E.g. filterable_fields = ['status', 'name']
  __all__ is allowed. It applies filters for all model attributes.

- COMMON_FILTERS: common filters configuration.
  
  - key: field name. E.g. status.
  - filter_class. filter class for the field.
  - args. Args for the filter_class __init__.  These args are taken from the queryset model
    E.g. 'args': {'choices': 'STATUS_CHOICES'} means Filter(choices=queryset.model.STATUS_CHOICES)

# How to use it:

class PortfolioListCreateView(CommonFilterMixin, InvestorAPIViewMixin, ListCreateAPIView):
filterable_fields = ['status', 'name']

# Filters priority.

1- Explicit filter declared in the filterset_class
2- Filters declared in COMMON_FILTERS
3- Filterset.FILTER_DEFAULTS

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_watchlists_update(self,
                                     client_uuid,
                                     watchlist_uuid,
                                     uuid,
                                     name,
                                     assets)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `watchlist_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `name` | `string` | Form, Required | **Constraints**: *Maximum Length*: `250` |
| `assets` | [`List of RelatedAssetSerializerWithPermission`](#related-asset-serializer-with-permission) | Form, Required | - |

##### Response Type

[`Watchlist`](#watchlist)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
watchlist_uuid = '00001df0-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
name = 'name0'
assets = []

assets.append(RelatedAssetSerializerWithPermission())
assets[0].uuid = '0000062c-0000-0000-0000-000000000000'
assets[0].isin = 'isin6'
assets[0].ticker = 'ticker6'
assets[0].name = 'name4'

assets.append(RelatedAssetSerializerWithPermission())
assets[1].uuid = '0000062d-0000-0000-0000-000000000000'
assets[1].isin = 'isin5'
assets[1].ticker = 'ticker7'
assets[1].name = 'name5'

assets.append(RelatedAssetSerializerWithPermission())
assets[2].uuid = '0000062e-0000-0000-0000-000000000000'
assets[2].isin = 'isin4'
assets[2].ticker = 'ticker8'
assets[2].name = 'name6'


result = api_controller.api_v_2_clients_watchlists_update(client_uuid, watchlist_uuid, uuid, name, assets)
```

#### Api V 2 Clients Watchlists Destroy

Applies filters without declaring them explicitly.
How? Creating those filters on the fly.

# How it works.

- Declare 'filterable_fields' in the view.
  E.g. filterable_fields = ['status', 'name']
  __all__ is allowed. It applies filters for all model attributes.

- COMMON_FILTERS: common filters configuration.
  
  - key: field name. E.g. status.
  - filter_class. filter class for the field.
  - args. Args for the filter_class __init__.  These args are taken from the queryset model
    E.g. 'args': {'choices': 'STATUS_CHOICES'} means Filter(choices=queryset.model.STATUS_CHOICES)

# How to use it:

class PortfolioListCreateView(CommonFilterMixin, InvestorAPIViewMixin, ListCreateAPIView):
filterable_fields = ['status', 'name']

# Filters priority.

1- Explicit filter declared in the filterset_class
2- Filters declared in COMMON_FILTERS
3- Filterset.FILTER_DEFAULTS

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_watchlists_destroy(self,
                                      client_uuid,
                                      watchlist_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `watchlist_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
watchlist_uuid = '00001df0-0000-0000-0000-000000000000'

result = api_controller.api_v_2_clients_watchlists_destroy(client_uuid, watchlist_uuid)
```

#### Api V 2 Clients Verify Email Update

Verify e-mail account with the given email token.

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_verify_email_update(self,
                                       uuid,
                                       token)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |
| `token` | `string` | Form, Required | - |

##### Response Type

[`EmailVerifyView`](#email-verify-view)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'
token = 'token6'

result = api_controller.api_v_2_clients_verify_email_update(uuid, token)
```

#### Api V 2 Clients Me Verify Email Create

Request e-mail account verification notification.

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_me_verify_email_create(self,
                                          email=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Form, Optional | - |

##### Response Type

[`EmailVerifyRequest`](#email-verify-request)

##### Example Usage

```python
result = api_controller.api_v_2_clients_me_verify_email_create()
```

#### Api V 2 Clients National Documents List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_national_documents_list(self,
                                           limit=None,
                                           offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedNationalDocumentList`](#paginated-national-document-list)

##### Example Usage

```python
result = api_controller.api_v_2_clients_national_documents_list()
```

#### Api V 2 Clients Referral Retrieve

Retrieves the currently logged in client referral code

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_clients_referral_retrieve(self,
                                     referral_code)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `referral_code` | `string` | Template, Required | - |

##### Response Type

[`ClientReferral`](#client-referral)

##### Example Usage

```python
referral_code = 'referral_code2'

result = api_controller.api_v_2_clients_referral_retrieve(referral_code)
```

#### Api V 2 Feeds Access Logs List

Retrieves the latest access to the client's account

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_feeds_access_logs_list(self,
                                  browser=None,
                                  browser_version=None,
                                  channel=None,
                                  city=None,
                                  country=None,
                                  device_brand=None,
                                  device_model=None,
                                  ip_address=None,
                                  limit=None,
                                  offset=None,
                                  os=None,
                                  os_version=None,
                                  user_agent=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `browser` | `string` | Query, Optional | - |
| `browser_version` | `string` | Query, Optional | - |
| `channel` | [`ChannelEnum`](#channel-enum) | Query, Optional | - |
| `city` | `string` | Query, Optional | - |
| `country` | `int` | Query, Optional | - |
| `device_brand` | `string` | Query, Optional | - |
| `device_model` | `string` | Query, Optional | - |
| `ip_address` | `string` | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `os` | `string` | Query, Optional | - |
| `os_version` | `string` | Query, Optional | - |
| `user_agent` | `string` | Query, Optional | - |

##### Response Type

[`PaginatedAccessLogList`](#paginated-access-log-list)

##### Example Usage

```python
result = api_controller.api_v_2_feeds_access_logs_list()
```

#### Api V 2 Feeds Activities List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_feeds_activities_list(self,
                                 limit=None,
                                 offset=None,
                                 target=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `target` | [`List of TargetEnum`](#target) | Query, Optional | - |

##### Response Type

[`PaginatedFeedActivityListList`](#paginated-feed-activity-list-list)

##### Example Usage

```python
result = api_controller.api_v_2_feeds_activities_list()
```

#### Api V 2 Goals List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_goals_list(self,
                      goal_uuid,
                      limit=None,
                      offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedGoalList`](#paginated-goal-list)

##### Example Usage

```python
goal_uuid = '00000028-0000-0000-0000-000000000000'

result = api_controller.api_v_2_goals_list(goal_uuid)
```

#### Api V 2 Goals Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_goals_create(self,
                        goal_uuid,
                        uuid,
                        name,
                        goal_amount,
                        deadline,
                        initial_amount,
                        risk_level,
                        created,
                        portfolio=None,
                        recurring_amount=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `name` | `string` | Form, Required | **Constraints**: *Maximum Length*: `150` |
| `goal_amount` | `float` | Form, Required | Desired amount needed to fulfill the goal<br>**Constraints**: `>= 0.1`, `<= 1000000000000` |
| `deadline` | `date` | Form, Required | Due date to reach the goal. |
| `initial_amount` | `float` | Form, Required | Initial deposit amount to start from. No sense to start by 0<br>**Constraints**: `>= 0.1`, `<= 1000000000000` |
| `risk_level` | `int` | Form, Required | **Constraints**: `>= 0`, `<= 32767` |
| `created` | `datetime` | Form, Required | - |
| `portfolio` | `string` | Form, Optional | - |
| `recurring_amount` | `float` | Form, Optional | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |

##### Response Type

[`Goal`](#goal)

##### Example Usage

```python
goal_uuid = '00000028-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
name = 'name0'
goal_amount = 140.86
deadline = dateutil.parser.parse('2016-03-13').date()
initial_amount = 140.36
risk_level = 66
created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = api_controller.api_v_2_goals_create(goal_uuid, uuid, name, goal_amount, deadline, initial_amount, risk_level, created)
```

#### Api V 2 Goals Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_goals_retrieve(self,
                          goal_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`Goal`](#goal)

##### Example Usage

```python
goal_uuid = '00000028-0000-0000-0000-000000000000'

result = api_controller.api_v_2_goals_retrieve(goal_uuid)
```

#### Api V 2 Goals Partial Update

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_goals_partial_update(self,
                                goal_uuid,
                                uuid=None,
                                name=None,
                                portfolio=None,
                                goal_amount=None,
                                deadline=None,
                                initial_amount=None,
                                recurring_amount=None,
                                risk_level=None,
                                created=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Optional | - |
| `name` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `150` |
| `portfolio` | `string` | Form, Optional | - |
| `goal_amount` | `float` | Form, Optional | Desired amount needed to fulfill the goal<br>**Constraints**: `>= 0.1`, `<= 1000000000000` |
| `deadline` | `date` | Form, Optional | Due date to reach the goal. |
| `initial_amount` | `float` | Form, Optional | Initial deposit amount to start from. No sense to start by 0<br>**Constraints**: `>= 0.1`, `<= 1000000000000` |
| `recurring_amount` | `float` | Form, Optional | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `risk_level` | `int` | Form, Optional | **Constraints**: `>= 0`, `<= 32767` |
| `created` | `datetime` | Form, Optional | - |

##### Response Type

[`Goal`](#goal)

##### Example Usage

```python
goal_uuid = '00000028-0000-0000-0000-000000000000'

result = api_controller.api_v_2_goals_partial_update(goal_uuid)
```

#### Api V 2 Goals Destroy

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_goals_destroy(self,
                         goal_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
goal_uuid = '00000028-0000-0000-0000-000000000000'

result = api_controller.api_v_2_goals_destroy(goal_uuid)
```

#### Api V 2 Goals Decumulation Create

Return a Goal Forecast Decumulation

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_goals_decumulation_create(self,
                                     initial_amount,
                                     recurring_amount,
                                     risk_level,
                                     withdrawal_amount,
                                     retirement_age,
                                     life_expectancy=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `initial_amount` | `float` | Form, Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `recurring_amount` | `float` | Form, Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `risk_level` | `int` | Form, Required | - |
| `withdrawal_amount` | `float` | Form, Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `retirement_age` | `int` | Form, Required | **Constraints**: `>= 18`, `<= 110` |
| `life_expectancy` | `int` | Form, Optional | **Constraints**: `>= 75`, `<= 110` |

##### Response Type

[`ForecastDecumulationRequest`](#forecast-decumulation-request)

##### Example Usage

```python
initial_amount = 140.36
recurring_amount = 118.5
risk_level = 66
withdrawal_amount = 38.74
retirement_age = 12

result = api_controller.api_v_2_goals_decumulation_create(initial_amount, recurring_amount, risk_level, withdrawal_amount, retirement_age)
```

#### Api V 2 Goals Forecast Create

Return a Goal Forecast

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_goals_forecast_create(self,
                                 goal_amount,
                                 deadline,
                                 initial_amount,
                                 recurring_amount,
                                 risk_level)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_amount` | `float` | Form, Required | **Constraints**: `>= 1`, `<= 1000000000000` |
| `deadline` | `date` | Form, Required | - |
| `initial_amount` | `float` | Form, Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `recurring_amount` | `float` | Form, Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `risk_level` | `int` | Form, Required | **Constraints**: `>= 1` |

##### Response Type

[`ForecastRequest`](#forecast-request)

##### Example Usage

```python
goal_amount = 140.86
deadline = dateutil.parser.parse('2016-03-13').date()
initial_amount = 140.36
recurring_amount = 118.5
risk_level = 66

result = api_controller.api_v_2_goals_forecast_create(goal_amount, deadline, initial_amount, recurring_amount, risk_level)
```

#### Api V 2 Inbox Conversations List

get:
List all conversations with last_message of a user

post:
Create new conversation with N messages (without attachments)

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_inbox_conversations_list(self,
                                    limit=None,
                                    offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedConversationListList`](#paginated-conversation-list-list)

##### Example Usage

```python
result = api_controller.api_v_2_inbox_conversations_list()
```

#### Api V 2 Inbox Conversations Create

get:
List all conversations with last_message of a user

post:
Create new conversation with N messages (without attachments)

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_inbox_conversations_create(self,
                                      uuid,
                                      portal,
                                      created,
                                      subject,
                                      messages=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Form, Required | - |
| `portal` | `int` | Form, Required | - |
| `created` | `datetime` | Form, Required | - |
| `subject` | `string` | Form, Required | **Constraints**: *Maximum Length*: `80` |
| `messages` | [`Message`](#message) | Form, Optional | - |

##### Response Type

[`ConversationCreate`](#conversation-create)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'
portal = 4
created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
subject = 'subject6'

result = api_controller.api_v_2_inbox_conversations_create(uuid, portal, created, subject)
```

#### Api V 2 Inbox Conversations List 2

List all messages from a conversation uuid

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_inbox_conversations_list_2(self,
                                      conversation,
                                      limit=None,
                                      offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conversation` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedMessageList`](#paginated-message-list)

##### Example Usage

```python
conversation = '00000124-0000-0000-0000-000000000000'

result = api_controller.api_v_2_inbox_conversations_list_2(conversation)
```

#### Api V 2 Inbox Conversations Messages Create

View for creating message on a specific conversation

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_inbox_conversations_messages_create(self,
                                               conversation,
                                               user,
                                               read_date,
                                               created,
                                               attachments,
                                               uuid,
                                               content=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conversation` | `uuid\|string` | Template, Required | - |
| `user` | `string` | Form, Required | - |
| `read_date` | `datetime` | Form, Required | - |
| `created` | `datetime` | Form, Required | - |
| `attachments` | [`List of Attachment`](#attachment) | Form, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `content` | `string` | Form, Optional | - |

##### Response Type

[`Message`](#message)

##### Example Usage

```python
conversation = '00000124-0000-0000-0000-000000000000'
user = 'user0'
read_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
attachments = []

attachments.append(Attachment())
attachments[0].attachment_extension = 'attachment_extension4'
attachments[0].attachment_filename = 'attachment_filename4'
attachments[0].uuid = '000002cc-0000-0000-0000-000000000000'

attachments.append(Attachment())
attachments[1].attachment_extension = 'attachment_extension3'
attachments[1].attachment_filename = 'attachment_filename3'
attachments[1].uuid = '000002cd-0000-0000-0000-000000000000'

attachments.append(Attachment())
attachments[2].attachment_extension = 'attachment_extension2'
attachments[2].attachment_filename = 'attachment_filename2'
attachments[2].uuid = '000002ce-0000-0000-0000-000000000000'

uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_inbox_conversations_messages_create(conversation, user, read_date, created, attachments, uuid)
```

#### Api V 2 Inbox Conversations Messages Attachments Retrieve

View to access to an attachment

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_inbox_conversations_messages_attachments_retrieve(self,
                                                             conversation,
                                                             message,
                                                             uuid,
                                                             format=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conversation` | `uuid\|string` | Template, Required | - |
| `message` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |
| `format` | [`Format1Enum`](#format-1) | Query, Optional | - |

##### Response Type

[`Attachment`](#attachment)

##### Example Usage

```python
conversation = '00000124-0000-0000-0000-000000000000'
message = '00000a00-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_inbox_conversations_messages_attachments_retrieve(conversation, message, uuid)
```

#### Api V 2 Mobile Version Retrieve

Returns the number of the last required APP Version for a platform.

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_mobile_version_retrieve(self,
                                   platform)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `platform` | `string` | Template, Required | - |

##### Response Type

[`MinimumAppVersion`](#minimum-app-version)

##### Example Usage

```python
platform = 'platform6'

result = api_controller.api_v_2_mobile_version_retrieve(platform)
```

#### Api V 2 Platform Settings List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_platform_settings_list(self)
```

##### Response Type

[`List of NucoroSetting`](#nucoro-setting)

##### Example Usage

```python
result = api_controller.api_v_2_platform_settings_list()
```

#### Api V 2 Portal Countries List

Retrieves the list of countries

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portal_countries_list(self,
                                 limit=None,
                                 offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedCountryListList`](#paginated-country-list-list)

##### Example Usage

```python
result = api_controller.api_v_2_portal_countries_list()
```

#### Api V 2 Portal Settings Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portal_settings_retrieve(self)
```

##### Response Type

[`PortalSettingValueList`](#portal-setting-value-list)

##### Example Usage

```python
result = api_controller.api_v_2_portal_settings_retrieve()
```

#### Api V 2 Portal Tos List

List all ToS for the current Portal

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portal_tos_list(self,
                           limit=None,
                           offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedTosList`](#paginated-tos-list)

##### Example Usage

```python
result = api_controller.api_v_2_portal_tos_list()
```

#### Api V 2 Portal Tos Retrieve

Retrieves a specific ToS

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portal_tos_retrieve(self,
                               uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`Tos`](#tos)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portal_tos_retrieve(uuid)
```

#### Api V 2 Portal Tos Current Retrieve

Retrieves the current ToS for the Portal

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portal_tos_current_retrieve(self)
```

##### Response Type

[`Tos`](#tos)

##### Example Usage

```python
result = api_controller.api_v_2_portal_tos_current_retrieve()
```

#### Api V 2 Portfolios List

Allow aggregate/group fields of the ModelView model or its related entities.
Query params should use dot notation.

Requires:
ListModelMixin (ListAPIView, ListCreateApiView)

Args:
* aggregatable_fields (dict): optional.
Keys: fields that allow aggregation (including related entities with "__" notation).
Values: django qs functions or aggregate_fns
Example:
aggregatable_fields = {
'allocations__balance': [Sum, Avg],
}

    * groupable_fields (list): optional. fields that allow grouping (including related entities with "__" notation).
        Example:
            groupable_fields = ['portfolio__portfolio_type']

Query Param Examples:
>>> ?group_by=portfolio.portfolio_type
>>> ?aggregate[Sum]=portfolio.allocations.balance
>>> ?group_by=valuation_date&aggregate[Sum]=portfolio.allocations.balance

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_list(self,
                           portfolio_uuid,
                           external_custodian_id=None,
                           limit=None,
                           offset=None,
                           status=None,
                           valuation_date_after=None,
                           valuation_date_before=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `external_custodian_id` | `string` | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `status` | [`List of Status2efEnum`](#status-2-ef-enum) | Query, Optional | - |
| `valuation_date_after` | `date` | Query, Optional | - |
| `valuation_date_before` | `date` | Query, Optional | - |

##### Response Type

[`PaginatedPortfolioListList`](#paginated-portfolio-list-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_list(portfolio_uuid)
```

#### Api V 2 Portfolios Create

Allow aggregate/group fields of the ModelView model or its related entities.
Query params should use dot notation.

Requires:
ListModelMixin (ListAPIView, ListCreateApiView)

Args:
* aggregatable_fields (dict): optional.
Keys: fields that allow aggregation (including related entities with "__" notation).
Values: django qs functions or aggregate_fns
Example:
aggregatable_fields = {
'allocations__balance': [Sum, Avg],
}

    * groupable_fields (list): optional. fields that allow grouping (including related entities with "__" notation).
        Example:
            groupable_fields = ['portfolio__portfolio_type']

Query Param Examples:
>>> ?group_by=portfolio.portfolio_type
>>> ?aggregate[Sum]=portfolio.allocations.balance
>>> ?group_by=valuation_date&aggregate[Sum]=portfolio.allocations.balance

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_create(self,
                             portfolio_uuid,
                             uuid,
                             name,
                             portfolio_type,
                             risk_level,
                             time_horizon,
                             status,
                             created,
                             activated,
                             advisor,
                             advice_engine,
                             currency=None,
                             extra_data=None,
                             client=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `name` | `string` | Form, Required | **Constraints**: *Maximum Length*: `150` |
| `portfolio_type` | `string` | Form, Required | - |
| `risk_level` | `int` | Form, Required | - |
| `time_horizon` | `int` | Form, Required | - |
| `status` | [`Status2efEnum`](#status-2-ef-enum) | Form, Required | - |
| `created` | `datetime` | Form, Required | - |
| `activated` | `datetime` | Form, Required | - |
| `advisor` | `string` | Form, Required | - |
| `advice_engine` | `string` | Form, Required | - |
| `currency` | `string` | Form, Optional | - |
| `extra_data` | `dict` | Form, Optional | - |
| `client` | `string` | Form, Optional | - |

##### Response Type

[`PortfolioCreate`](#portfolio-create)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
name = 'name0'
portfolio_type = 'portfolio_type4'
risk_level = 66
time_horizon = 200
status = Status2efEnum.PENDING
created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
activated = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
advisor = 'advisor6'
advice_engine = 'advice_engine6'

result = api_controller.api_v_2_portfolios_create(portfolio_uuid, uuid, name, portfolio_type, risk_level, time_horizon, status, created, activated, advisor, advice_engine)
```

#### Api V 2 Portfolios Retrieve

Allow aggregate/group fields of the ModelView model or its related entities.
Query params should use dot notation.

Requires:
ListModelMixin (ListAPIView, ListCreateApiView)

Args:
* aggregatable_fields (dict): optional.
Keys: fields that allow aggregation (including related entities with "__" notation).
Values: django qs functions or aggregate_fns
Example:
aggregatable_fields = {
'allocations__balance': [Sum, Avg],
}

    * groupable_fields (list): optional. fields that allow grouping (including related entities with "__" notation).
        Example:
            groupable_fields = ['portfolio__portfolio_type']

Query Param Examples:
>>> ?group_by=portfolio.portfolio_type
>>> ?aggregate[Sum]=portfolio.allocations.balance
>>> ?group_by=valuation_date&aggregate[Sum]=portfolio.allocations.balance

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_retrieve(self,
                               portfolio_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`PortfolioDetail`](#portfolio-detail)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_retrieve(portfolio_uuid)
```

#### Api V 2 Portfolios Update

Allow aggregate/group fields of the ModelView model or its related entities.
Query params should use dot notation.

Requires:
ListModelMixin (ListAPIView, ListCreateApiView)

Args:
* aggregatable_fields (dict): optional.
Keys: fields that allow aggregation (including related entities with "__" notation).
Values: django qs functions or aggregate_fns
Example:
aggregatable_fields = {
'allocations__balance': [Sum, Avg],
}

    * groupable_fields (list): optional. fields that allow grouping (including related entities with "__" notation).
        Example:
            groupable_fields = ['portfolio__portfolio_type']

Query Param Examples:
>>> ?group_by=portfolio.portfolio_type
>>> ?aggregate[Sum]=portfolio.allocations.balance
>>> ?group_by=valuation_date&aggregate[Sum]=portfolio.allocations.balance

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_update(self,
                             portfolio_uuid,
                             uuid,
                             name,
                             portfolio_type,
                             status,
                             created,
                             activated,
                             advisor,
                             advice_engine,
                             risk_level=None,
                             time_horizon=None,
                             currency=None,
                             extra_data=None,
                             client=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `name` | `string` | Form, Required | **Constraints**: *Maximum Length*: `150` |
| `portfolio_type` | `string` | Form, Required | - |
| `status` | [`Status2efEnum`](#status-2-ef-enum) | Form, Required | - |
| `created` | `datetime` | Form, Required | - |
| `activated` | `datetime` | Form, Required | - |
| `advisor` | `string` | Form, Required | - |
| `advice_engine` | `string` | Form, Required | - |
| `risk_level` | `int` | Form, Optional | **Constraints**: `>= 0`, `<= 32767` |
| `time_horizon` | `int` | Form, Optional | **Constraints**: `>= 0`, `<= 32767` |
| `currency` | `string` | Form, Optional | - |
| `extra_data` | `dict` | Form, Optional | - |
| `client` | `string` | Form, Optional | - |

##### Response Type

[`PortfolioUpdate`](#portfolio-update)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
name = 'name0'
portfolio_type = 'portfolio_type4'
status = Status2efEnum.PENDING
created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
activated = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
advisor = 'advisor6'
advice_engine = 'advice_engine6'

result = api_controller.api_v_2_portfolios_update(portfolio_uuid, uuid, name, portfolio_type, status, created, activated, advisor, advice_engine)
```

#### Api V 2 Portfolios Partial Update

Allow aggregate/group fields of the ModelView model or its related entities.
Query params should use dot notation.

Requires:
ListModelMixin (ListAPIView, ListCreateApiView)

Args:
* aggregatable_fields (dict): optional.
Keys: fields that allow aggregation (including related entities with "__" notation).
Values: django qs functions or aggregate_fns
Example:
aggregatable_fields = {
'allocations__balance': [Sum, Avg],
}

    * groupable_fields (list): optional. fields that allow grouping (including related entities with "__" notation).
        Example:
            groupable_fields = ['portfolio__portfolio_type']

Query Param Examples:
>>> ?group_by=portfolio.portfolio_type
>>> ?aggregate[Sum]=portfolio.allocations.balance
>>> ?group_by=valuation_date&aggregate[Sum]=portfolio.allocations.balance

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_partial_update(self,
                                     portfolio_uuid,
                                     uuid=None,
                                     name=None,
                                     portfolio_type=None,
                                     risk_level=None,
                                     time_horizon=None,
                                     status=None,
                                     currency=None,
                                     created=None,
                                     activated=None,
                                     advisor=None,
                                     advice_engine=None,
                                     extra_data=None,
                                     client=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Optional | - |
| `name` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `150` |
| `portfolio_type` | `string` | Form, Optional | - |
| `risk_level` | `int` | Form, Optional | **Constraints**: `>= 0`, `<= 32767` |
| `time_horizon` | `int` | Form, Optional | **Constraints**: `>= 0`, `<= 32767` |
| `status` | [`Status2efEnum`](#status-2-ef-enum) | Form, Optional | - |
| `currency` | `string` | Form, Optional | - |
| `created` | `datetime` | Form, Optional | - |
| `activated` | `datetime` | Form, Optional | - |
| `advisor` | `string` | Form, Optional | - |
| `advice_engine` | `string` | Form, Optional | - |
| `extra_data` | `dict` | Form, Optional | - |
| `client` | `string` | Form, Optional | - |

##### Response Type

[`PortfolioUpdate`](#portfolio-update)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_partial_update(portfolio_uuid)
```

#### Api V 2 Portfolios Destroy

Allow aggregate/group fields of the ModelView model or its related entities.
Query params should use dot notation.

Requires:
ListModelMixin (ListAPIView, ListCreateApiView)

Args:
* aggregatable_fields (dict): optional.
Keys: fields that allow aggregation (including related entities with "__" notation).
Values: django qs functions or aggregate_fns
Example:
aggregatable_fields = {
'allocations__balance': [Sum, Avg],
}

    * groupable_fields (list): optional. fields that allow grouping (including related entities with "__" notation).
        Example:
            groupable_fields = ['portfolio__portfolio_type']

Query Param Examples:
>>> ?group_by=portfolio.portfolio_type
>>> ?aggregate[Sum]=portfolio.allocations.balance
>>> ?group_by=valuation_date&aggregate[Sum]=portfolio.allocations.balance

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_destroy(self,
                              portfolio_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_destroy(portfolio_uuid)
```

#### Api V 2 Portfolios Activities List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_activities_list(self,
                                      portfolio_uuid,
                                      limit=None,
                                      offset=None,
                                      target=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `target` | [`List of TargetEnum`](#target) | Query, Optional | - |

##### Response Type

[`PaginatedFeedActivityListList`](#paginated-feed-activity-list-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_activities_list(portfolio_uuid)
```

#### Api V 2 Portfolios Activities Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_activities_retrieve(self,
                                          portfolio_uuid,
                                          uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`FeedActivityList`](#feed-activity-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_activities_retrieve(portfolio_uuid, uuid)
```

#### Api V 2 Portfolios Allocations List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_allocations_list(self,
                                       portfolio_uuid,
                                       limit=None,
                                       offset=None,
                                       valuation_date_after=None,
                                       valuation_date_before=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `valuation_date_after` | `date` | Query, Optional | - |
| `valuation_date_before` | `date` | Query, Optional | - |

##### Response Type

[`PaginatedAllocationListList`](#paginated-allocation-list-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_allocations_list(portfolio_uuid)
```

#### Api V 2 Portfolios Allocations Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_allocations_retrieve(self,
                                           id,
                                           portfolio_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | A unique integer value identifying this allocation. |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`AllocationList`](#allocation-list)

##### Example Usage

```python
id = 112
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_allocations_retrieve(id, portfolio_uuid)
```

#### Api V 2 Portfolios Allocations End Day

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_allocations_end_day(self,
                                          portfolio_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`AllocationList`](#allocation-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_allocations_end_day(portfolio_uuid)
```

#### Api V 2 Portfolios Allocations End Day by Date Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_allocations_end_day_by_date_retrieve(self,
                                                           allocation_date,
                                                           portfolio_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allocation_date` | `string` | Template, Required | - |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`AllocationDetail`](#allocation-detail)

##### Example Usage

```python
allocation_date = 'allocation_date2'
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_allocations_end_day_by_date_retrieve(allocation_date, portfolio_uuid)
```

#### Api V 2 Portfolios Allocations End Day Latest Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_allocations_end_day_latest_retrieve(self,
                                                          portfolio_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`AllocationDetail`](#allocation-detail)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_allocations_end_day_latest_retrieve(portfolio_uuid)
```

#### Api V 2 Portfolios Allocations Intraday Latest Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_allocations_intraday_latest_retrieve(self,
                                                           portfolio_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`CurrentAllocation`](#current-allocation)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_allocations_intraday_latest_retrieve(portfolio_uuid)
```

#### Api V 2 Portfolios Deposits List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_deposits_list(self,
                                    portfolio_uuid,
                                    limit=None,
                                    offset=None,
                                    status=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `status` | [`List of StatusB6aEnum`](#status-b6-a-enum) | Query, Optional | - |

##### Response Type

[`PaginatedDepositListList`](#paginated-deposit-list-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_deposits_list(portfolio_uuid)
```

#### Api V 2 Portfolios Deposits Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_deposits_create(self,
                                      portfolio_uuid,
                                      uuid,
                                      amount,
                                      provider,
                                      reference,
                                      status,
                                      reason,
                                      completed,
                                      transacted_at,
                                      deposit_type=None,
                                      extra_data=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `amount` | `float` | Form, Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `provider` | `string` | Form, Required | - |
| `reference` | `string` | Form, Required | - |
| `status` | [`StatusB6aEnum`](#status-b6-a-enum) | Form, Required | - |
| `reason` | `string` | Form, Required | Cancelled reason |
| `completed` | `datetime` | Form, Required | - |
| `transacted_at` | `datetime` | Form, Required | - |
| `deposit_type` | [`DepositTypeEnum`](#deposit-type-enum) | Form, Optional | - |
| `extra_data` | `dict` | Form, Optional | Additional deposit attributes for the specific portal |

##### Response Type

[`DepositCreate`](#deposit-create)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
amount = 56.78
provider = 'provider8'
reference = 'reference4'
status = StatusB6aEnum.PROCESSING
reason = 'reason4'
completed = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
transacted_at = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = api_controller.api_v_2_portfolios_deposits_create(portfolio_uuid, uuid, amount, provider, reference, status, reason, completed, transacted_at)
```

#### Api V 2 Portfolios Deposits Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_deposits_retrieve(self,
                                        portfolio_uuid,
                                        uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`DepositDetail`](#deposit-detail)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_deposits_retrieve(portfolio_uuid, uuid)
```

#### Api V 2 Portfolios Deposits Destroy

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_deposits_destroy(self,
                                       portfolio_uuid,
                                       uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_deposits_destroy(portfolio_uuid, uuid)
```

#### Api V 2 Portfolios Orders List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_orders_list(self,
                                  portfolio_uuid,
                                  advice_external_id=None,
                                  asset=None,
                                  completed_after=None,
                                  completed_before=None,
                                  extra_data=None,
                                  limit=None,
                                  offset=None,
                                  portfolio=None,
                                  status=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `advice_external_id` | `string` | Query, Optional | - |
| `asset` | `string` | Query, Optional | - |
| `completed_after` | `date` | Query, Optional | - |
| `completed_before` | `date` | Query, Optional | - |
| `extra_data` | `dict` | Query, Optional | Additional order attributes for the specific portal |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `portfolio` | `string` | Query, Optional | - |
| `status` | `string` | Query, Optional | - |

##### Response Type

[`PaginatedOrderListList`](#paginated-order-list-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_orders_list(portfolio_uuid)
```

#### Api V 2 Portfolios Orders Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_orders_create(self,
                                    portfolio_uuid,
                                    shares,
                                    asset,
                                    order_type,
                                    method,
                                    portfolio=None,
                                    limit_price=None,
                                    stop_price=None,
                                    duration=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `shares` | `int` | Form, Required | **Constraints**: `>= 1` |
| `asset` | [`RelatedAssetSerializerWithAssetCategories`](#related-asset-serializer-with-asset-categories) | Form, Required | Allow get asset by multiple params or UUID |
| `order_type` | [`OrderTypeEnum`](#order-type-enum) | Form, Required | - |
| `method` | [`CreateOrderMethodEnum`](#create-order-method-enum) | Form, Required | - |
| `portfolio` | `string` | Form, Optional | - |
| `limit_price` | `float` | Form, Optional | **Constraints**: `>= 0.01`, `<= 1000000000000` |
| `stop_price` | `float` | Form, Optional | **Constraints**: `>= 0.01`, `<= 1000000000000` |
| `duration` | [`DurationEnum`](#duration-enum) | Form, Optional | - |

##### Response Type

[`CreateOrder`](#create-order)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
shares = 214
asset = RelatedAssetSerializerWithAssetCategories()
asset.uuid = '000010be-0000-0000-0000-000000000000'
asset.isin = 'isin0'
asset.ticker = 'ticker2'
asset.name = 'name0'
asset.categories = ['categories2', 'categories1']
order_type = OrderTypeEnum.VERIFICATION
method = CreateOrderMethodEnum.LIMIT

result = api_controller.api_v_2_portfolios_orders_create(portfolio_uuid, shares, asset, order_type, method)
```

#### Api V 2 Portfolios Orders Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_orders_retrieve(self,
                                      portfolio_uuid,
                                      uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`OrderList`](#order-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_orders_retrieve(portfolio_uuid, uuid)
```

#### Api V 2 Portfolios Orders Destroy

Cancel or request cancellation to the broker

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_orders_destroy(self,
                                     portfolio_uuid,
                                     uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_orders_destroy(portfolio_uuid, uuid)
```

#### Api V 2 Portfolios Performance Mwrr List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_performance_mwrr_list(self,
                                            portfolio_uuid,
                                            date_after=None,
                                            date_before=None,
                                            limit=None,
                                            offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `date_after` | `date` | Query, Optional | - |
| `date_before` | `date` | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedPortfolioPerformanceList`](#paginated-portfolio-performance-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_performance_mwrr_list(portfolio_uuid)
```

#### Api V 2 Portfolios Performance Positions List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_performance_positions_list(self,
                                                 portfolio_uuid,
                                                 limit=None,
                                                 offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedPortfolioPerformancePositionsList`](#paginated-portfolio-performance-positions-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_performance_positions_list(portfolio_uuid)
```

#### Api V 2 Portfolios Performance Twrr List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_performance_twrr_list(self,
                                            portfolio_uuid,
                                            date_after=None,
                                            date_before=None,
                                            limit=None,
                                            offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `date_after` | `date` | Query, Optional | - |
| `date_before` | `date` | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedPortfolioPerformanceList`](#paginated-portfolio-performance-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_performance_twrr_list(portfolio_uuid)
```

#### Api V 2 Portfolios Rebalances List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_rebalances_list(self,
                                      portfolio_uuid,
                                      limit=None,
                                      offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedRebalanceList`](#paginated-rebalance-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_rebalances_list(portfolio_uuid)
```

#### Api V 2 Portfolios Rebalances Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_rebalances_retrieve(self,
                                          portfolio_uuid,
                                          uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`Rebalance`](#rebalance)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_rebalances_retrieve(portfolio_uuid, uuid)
```

#### Api V 2 Portfolios Restrictions Retrieve

Allow aggregate/group fields of the ModelView model or its related entities.
Query params should use dot notation.

Requires:
ListModelMixin (ListAPIView, ListCreateApiView)

Args:
* aggregatable_fields (dict): optional.
Keys: fields that allow aggregation (including related entities with "__" notation).
Values: django qs functions or aggregate_fns
Example:
aggregatable_fields = {
'allocations__balance': [Sum, Avg],
}

    * groupable_fields (list): optional. fields that allow grouping (including related entities with "__" notation).
        Example:
            groupable_fields = ['portfolio__portfolio_type']

Query Param Examples:
>>> ?group_by=portfolio.portfolio_type
>>> ?aggregate[Sum]=portfolio.allocations.balance
>>> ?group_by=valuation_date&aggregate[Sum]=portfolio.allocations.balance

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_restrictions_retrieve(self,
                                            portfolio_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`PortfolioTypeRestrictions`](#portfolio-type-restrictions)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_restrictions_retrieve(portfolio_uuid)
```

#### Api V 2 Portfolios Withdrawals List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_withdrawals_list(self,
                                       portfolio_uuid,
                                       limit=None,
                                       offset=None,
                                       status=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `status` | [`List of Status14bEnum`](#status-14-b-enum) | Query, Optional | - |

##### Response Type

[`PaginatedInvestorWithdrawalListList`](#paginated-investor-withdrawal-list-list)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_withdrawals_list(portfolio_uuid)
```

#### Api V 2 Portfolios Withdrawals Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_withdrawals_create(self,
                                         portfolio_uuid,
                                         uuid,
                                         amount,
                                         provider,
                                         status,
                                         reason,
                                         completed,
                                         withdrawal_type,
                                         purpose=None,
                                         extra_data=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `amount` | `float` | Form, Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `provider` | `string` | Form, Required | - |
| `status` | [`Status14bEnum`](#status-14-b-enum) | Form, Required | - |
| `reason` | `string` | Form, Required | Cancelled reason |
| `completed` | `datetime` | Form, Required | - |
| `withdrawal_type` | `string` | Form, Required | - |
| `purpose` | `string` | Form, Optional | Withdrawal reason<br>**Constraints**: *Maximum Length*: `250` |
| `extra_data` | `dict` | Form, Optional | Additional withdrawal attributes for the specific portal |

##### Response Type

[`InvestorWithdrawalCreate`](#investor-withdrawal-create)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
amount = 56.78
provider = 'provider8'
status = Status14bEnum.REQUESTED
reason = 'reason4'
completed = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
withdrawal_type = 'withdrawal_type4'

result = api_controller.api_v_2_portfolios_withdrawals_create(portfolio_uuid, uuid, amount, provider, status, reason, completed, withdrawal_type)
```

#### Api V 2 Portfolios Withdrawals Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_withdrawals_retrieve(self,
                                           portfolio_uuid,
                                           uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`WithdrawalDetail`](#withdrawal-detail)

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_withdrawals_retrieve(portfolio_uuid, uuid)
```

#### Api V 2 Portfolios Withdrawals Destroy

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_withdrawals_destroy(self,
                                          portfolio_uuid,
                                          uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
portfolio_uuid = '00002622-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_withdrawals_destroy(portfolio_uuid, uuid)
```

#### Api V 2 Portfolios Allocations History Retrieve

Allocations History for a given portfolio

It accepts two optional parameters, `date_to` and `date_from` to limit
the daily allocations to a certain data range. If they are not given, all the
allocations are returned.

---


## Parameters:

* **name**: `date_from`

* **description**: The initial date.

* **parameter type**: query param

* **name**: `date_from`

* **description**: The final date.

* **parameter type**: query param

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_allocations_history_retrieve(self,
                                                   portfolio)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
portfolio = '00001f44-0000-0000-0000-000000000000'

result = api_controller.api_v_2_portfolios_allocations_history_retrieve(portfolio)
```

#### Api V 2 Portfolios Portfoliotypes List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_portfoliotypes_list(self,
                                          limit=None,
                                          offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedPortfolioTypeList`](#paginated-portfolio-type-list)

##### Example Usage

```python
result = api_controller.api_v_2_portfolios_portfoliotypes_list()
```

#### Api V 2 Portfolios Portfoliotypes Restrictions List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_portfolios_portfoliotypes_restrictions_list(self,
                                                       code,
                                                       limit=None,
                                                       offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedBasePortfolioTypeRestrictionsList`](#paginated-base-portfolio-type-restrictions-list)

##### Example Usage

```python
code = 'code8'

result = api_controller.api_v_2_portfolios_portfoliotypes_restrictions_list(code)
```

#### Api V 2 Relationship Manager Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_retrieve(self,
                                         uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`RelationshipManager`](#relationship-manager)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_relationship_manager_retrieve(uuid)
```

#### Api V 2 Relationship Manager Analytics Allocations by Asset Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_analytics_allocations_by_asset_retrieve(self,
                                                                        uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`AllocationByAsset`](#allocation-by-asset)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_relationship_manager_analytics_allocations_by_asset_retrieve(uuid)
```

#### Api V 2 Relationship Manager Analytics Asset Concentration Risk Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_analytics_asset_concentration_risk_retrieve(self,
                                                                            uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`AssetConcentrationRisk`](#asset-concentration-risk)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_relationship_manager_analytics_asset_concentration_risk_retrieve(uuid)
```

#### Api V 2 Relationship Manager Analytics Aum Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_analytics_aum_retrieve(self,
                                                       uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`RelationshipManager`](#relationship-manager)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_relationship_manager_analytics_aum_retrieve(uuid)
```

#### Api V 2 Relationship Manager Analytics Aum Evolution Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_analytics_aum_evolution_retrieve(self,
                                                                 uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`AUMEvoluation`](#aum-evoluation)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_relationship_manager_analytics_aum_evolution_retrieve(uuid)
```

#### Api V 2 Relationship Manager Analytics Aum Portfolio Risk Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_analytics_aum_portfolio_risk_retrieve(self,
                                                                      uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`AUMPortfolioRisk`](#aum-portfolio-risk)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_relationship_manager_analytics_aum_portfolio_risk_retrieve(uuid)
```

#### Api V 2 Relationship Manager Analytics Client by Risk Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_analytics_client_by_risk_retrieve(self,
                                                                  uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`RelationshipManager`](#relationship-manager)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_relationship_manager_analytics_client_by_risk_retrieve(uuid)
```

#### Api V 2 Relationship Manager Analytics Client by Status Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_analytics_client_by_status_retrieve(self,
                                                                    uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`RelationshipManager`](#relationship-manager)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_relationship_manager_analytics_client_by_status_retrieve(uuid)
```

#### Api V 2 Relationship Manager Analytics Client Ranking Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_analytics_client_ranking_retrieve(self,
                                                                  uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`ClientRanking`](#client-ranking)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_relationship_manager_analytics_client_ranking_retrieve(uuid)
```

#### Api V 2 Relationship Manager Analytics Inflows Outflows Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_analytics_inflows_outflows_retrieve(self,
                                                                    uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`RelationshipManager`](#relationship-manager)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_relationship_manager_analytics_inflows_outflows_retrieve(uuid)
```

#### Api V 2 Relationship Manager Analytics Portfolio Risk Performance Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_analytics_portfolio_risk_performance_retrieve(self,
                                                                              uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`RelationshipManager`](#relationship-manager)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_relationship_manager_analytics_portfolio_risk_performance_retrieve(uuid)
```

#### Api V 2 Relationship Manager Analytics Total Active Clients Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_analytics_total_active_clients_retrieve(self,
                                                                        uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`RelationshipManager`](#relationship-manager)

##### Example Usage

```python
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_relationship_manager_analytics_total_active_clients_retrieve(uuid)
```

#### Api V 2 Relationship Manager Me Retrieve

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_relationship_manager_me_retrieve(self)
```

##### Response Type

[`RelationshipManager`](#relationship-manager)

##### Example Usage

```python
result = api_controller.api_v_2_relationship_manager_me_retrieve()
```

#### Api V 2 Report Statements List

This mixin implements binary responses.
It supports PDF and Base64. It can be adapted to any django View that implements the retrieve method

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_report_statements_list(self,
                                  client_uuid,
                                  format=None,
                                  limit=None,
                                  offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `format` | [`Format1Enum`](#format-1) | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedStatementList`](#paginated-statement-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = api_controller.api_v_2_report_statements_list(client_uuid)
```

#### Api V 2 Report Statements Retrieve

This mixin implements binary responses.
It supports PDF and Base64. It can be adapted to any django View that implements the retrieve method

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_report_statements_retrieve(self,
                                      client_uuid,
                                      uuid,
                                      format=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |
| `format` | [`Format1Enum`](#format-1) | Query, Optional | - |

##### Response Type

[`Statement`](#statement)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_report_statements_retrieve(client_uuid, uuid)
```

#### Api V 2 Report Tax Report List

This mixin implements binary responses.
It supports PDF and Base64. It can be adapted to any django View that implements the retrieve method

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_report_tax_report_list(self,
                                  client_uuid,
                                  format=None,
                                  limit=None,
                                  offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `format` | [`Format1Enum`](#format-1) | Query, Optional | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedTaxReportList`](#paginated-tax-report-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = api_controller.api_v_2_report_tax_report_list(client_uuid)
```

#### Api V 2 Report Tax Report Retrieve

This mixin implements binary responses.
It supports PDF and Base64. It can be adapted to any django View that implements the retrieve method

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_report_tax_report_retrieve(self,
                                      client_uuid,
                                      uuid,
                                      format=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Template, Required | - |
| `format` | [`Format1Enum`](#format-1) | Query, Optional | - |

##### Response Type

[`TaxReport`](#tax-report)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = api_controller.api_v_2_report_tax_report_retrieve(client_uuid, uuid)
```

#### Api V 2 Risk Questions List

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_risk_questions_list(self,
                               limit=None,
                               offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedQuestionList`](#paginated-question-list)

##### Example Usage

```python
result = api_controller.api_v_2_risk_questions_list()
```

#### Api V 2 Verifications Verifier Webhook Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_verifications_verifier_webhook_create(self,
                                                 action,
                                                 verifier)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | `string` | Template, Required | - |
| `verifier` | `string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
action = 'action2'
verifier = 'verifier2'

result = api_controller.api_v_2_verifications_verifier_webhook_create(action, verifier)
```

#### Api V 2 Websocket Authentication Ticket Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_websocket_authentication_ticket_create(self,
                                                  ticket)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ticket` | `string` | Form, Required | - |

##### Response Type

[`AuthenticationResponse`](#authentication-response)

##### Example Usage

```python
ticket = 'ticket4'

result = api_controller.api_v_2_websocket_authentication_ticket_create(ticket)
```

#### Api V 2 Websocket Authorize Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_websocket_authorize_create(self,
                                      ticket)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ticket` | `string` | Form, Required | - |

##### Response Type

[`Response`](#response)

##### Example Usage

```python
ticket = 'ticket4'

result = api_controller.api_v_2_websocket_authorize_create(ticket)
```

#### Api V 2 Websocket Authorize Asset Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_websocket_authorize_asset_create(self,
                                            ticket)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ticket` | `string` | Form, Required | - |

##### Response Type

[`Response`](#response)

##### Example Usage

```python
ticket = 'ticket4'

result = api_controller.api_v_2_websocket_authorize_asset_create(ticket)
```

#### Api V 2 Websocket Authorize Portfolio Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_websocket_authorize_portfolio_create(self,
                                                ticket)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ticket` | `string` | Form, Required | - |

##### Response Type

[`Response`](#response)

##### Example Usage

```python
ticket = 'ticket4'

result = api_controller.api_v_2_websocket_authorize_portfolio_create(ticket)
```

#### Api V 2 Websocket on Subscribe Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_websocket_on_subscribe_create(self,
                                         id,
                                         subscription)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Form, Required | - |
| `subscription` | `string` | Form, Required | - |

##### Response Type

[`Subscribe`](#subscribe)

##### Example Usage

```python
id = 'id0'
subscription = 'subscription4'

result = api_controller.api_v_2_websocket_on_subscribe_create(id, subscription)
```

#### Api V 2 Websocket on Unsubscribe Create

:information_source: **Note** This endpoint does not require authentication.

```python
def api_v_2_websocket_on_unsubscribe_create(self,
                                           id,
                                           subscription)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Form, Required | - |
| `subscription` | `string` | Form, Required | - |

##### Response Type

[`Unsubscribe`](#unsubscribe)

##### Example Usage

```python
id = 'id0'
subscription = 'subscription4'

result = api_controller.api_v_2_websocket_on_unsubscribe_create(id, subscription)
```

### Auth

#### Overview

##### Get instance

An instance of the `AuthController` class can be accessed from the API Client.

```
auth_controller = client.auth
```

#### Auth Impersonation Token

API View that receives an impersonation token and check its validity
Returns a JSON Web Token that can be used for authenticated (and restricted) requests.

:information_source: **Note** This endpoint does not require authentication.

```python
def auth_impersonation_token(self,
                            impersonator,
                            impersonated,
                            token)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `impersonator` | `string` | Form, Required | - |
| `impersonated` | `string` | Form, Required | - |
| `token` | `string` | Form, Required | - |

##### Response Type

[`ImpersionationResponse`](#impersionation-response)

##### Example Usage

```python
impersonator = 'impersonator2'
impersonated = 'impersonated4'
token = 'token6'

result = auth_controller.auth_impersonation_token(impersonator, impersonated, token)
```

#### Auth Login

API View that receives a POST with a user's username and password.

Returns a JSON Web Token that can be used for authenticated requests.

:information_source: **Note** This endpoint does not require authentication.

```python
def auth_login(self,
              username,
              password,
              captcha=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `string` | Form, Required | - |
| `password` | `string` | Form, Required | - |
| `captcha` | `string` | Form, Optional | - |

##### Response Type

[`JWTResponse`](#jwt-response)

##### Example Usage

```python
username = 'username0'
password = 'password4'

result = auth_controller.auth_login(username, password)
```

#### Auth Get Onboarding Token

API View that receives a onboarding token and check its validity

Returns a JSON Web Token that can be used for authenticated requests.

:information_source: **Note** This endpoint does not require authentication.

```python
def auth_get_onboarding_token(self,
                             email,
                             token)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Form, Required | - |
| `token` | `string` | Form, Required | - |

##### Response Type

[`OnboardingResponse`](#onboarding-response)

##### Example Usage

```python
email = 'email6'
token = 'token6'

result = auth_controller.auth_get_onboarding_token(email, token)
```

#### User Set Password

Set a new password for an user

:information_source: **Note** This endpoint does not require authentication.

```python
def user_set_password(self,
                     email,
                     token,
                     password)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Form, Required | - |
| `token` | `string` | Form, Required | - |
| `password` | `string` | Form, Required | - |

##### Response Type

[`PasswordReset`](#password-reset)

##### Example Usage

```python
email = 'email6'
token = 'token6'
password = 'password4'

result = auth_controller.user_set_password(email, token, password)
```

#### User Change Password

Change password for an user

:information_source: **Note** This endpoint does not require authentication.

```python
def user_change_password(self,
                        new_password,
                        old_password=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `new_password` | `string` | Form, Required | - |
| `old_password` | `string` | Form, Optional | - |

##### Response Type

[`PasswordUpdate`](#password-update)

##### Example Usage

```python
new_password = 'new_password6'

result = auth_controller.user_change_password(new_password)
```

#### User Request Password Reset

Request a password reset

:information_source: **Note** This endpoint does not require authentication.

```python
def user_request_password_reset(self,
                               email=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Form, Optional | - |

##### Response Type

[`PasswordResetRequest`](#password-reset-request)

##### Example Usage

```python
result = auth_controller.user_request_password_reset()
```

#### Auth Resfresh JWT Token

API View that receives a POST with a refresh token as token.

Returns a refreshed JSON Web Token that can be used for authenticated requests.

:information_source: **Note** This endpoint does not require authentication.

```python
def auth_resfresh_jwt_token(self,
                           refresh)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `refresh` | `string` | Form, Required | - |

##### Response Type

[`JWTRefreshResponse`](#jwt-refresh-response)

##### Example Usage

```python
refresh = 'refresh2'

result = auth_controller.auth_resfresh_jwt_token(refresh)
```

### Application

#### Overview

##### Get instance

An instance of the `ApplicationController` class can be accessed from the API Client.

```
application_controller = client.application
```

#### Client List

List client for a Relationship manager

:information_source: **Note** This endpoint does not require authentication.

```python
def client_list(self,
               external_custodian_id=None,
               extra_data=None,
               limit=None,
               offset=None,
               ordering=None,
               search=None,
               status=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `external_custodian_id` | `string` | Query, Optional | - |
| `extra_data` | `dict` | Query, Optional | Additional client attributes for the specific portal |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `ordering` | [`List of OrderingEnum`](#ordering) | Query, Optional | Ordering |
| `search` | `string` | Query, Optional | A search term. |
| `status` | [`StatusB65Enum`](#status-b65-enum) | Query, Optional | - |

##### Response Type

[`PaginatedClientDetailList`](#paginated-client-detail-list)

##### Example Usage

```python
result = application_controller.client_list()
```

#### Client Create

Create a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_create(self,
                 email,
                 birthdate=None,
                 title=None,
                 first_name=None,
                 last_name=None,
                 middle_name=None,
                 gender=None,
                 marital_status=None,
                 language=None,
                 employment_status=None,
                 activated=None,
                 profile=None,
                 password=None,
                 referral_code=None,
                 utm_source=None,
                 utm_medium=None,
                 utm_campaign=None,
                 utm_term=None,
                 utm_content=None,
                 tos_consent=None,
                 data_consent=None,
                 marketing_consent=None,
                 extra_data=None,
                 phone_number=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Form, Required | - |
| `birthdate` | `date` | Form, Optional | - |
| `title` | [`TitleEnum`](#title-enum) | Form, Optional | - |
| `first_name` | `string` | Form, Optional | - |
| `last_name` | `string` | Form, Optional | - |
| `middle_name` | `string` | Form, Optional | - |
| `gender` | [`GenderEnum`](#gender-enum) | Form, Optional | - |
| `marital_status` | [`MaritalStatusEnum`](#marital-status-enum) | Form, Optional | - |
| `language` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `5` |
| `employment_status` | [`EmploymentStatusEnum`](#employment-status-enum) | Form, Optional | - |
| `activated` | `datetime` | Form, Optional | - |
| `profile` | `dict` | Form, Optional | - |
| `password` | `string` | Form, Optional | - |
| `referral_code` | `string` | Form, Optional | - |
| `utm_source` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_medium` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_campaign` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_term` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_content` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `tos_consent` | `bool` | Form, Optional | - |
| `data_consent` | `bool` | Form, Optional | - |
| `marketing_consent` | `bool` | Form, Optional | - |
| `extra_data` | `dict` | Form, Optional | - |
| `phone_number` | `string` | Form, Optional | - |

##### Response Type

[`ClientCreate`](#client-create-1)

##### Example Usage

```python
email = 'email6'

result = application_controller.client_create(email)
```

#### Client Retrieve

Retrieve a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_retrieve(self,
                   client_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`ClientDetail`](#client-detail)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_retrieve(client_uuid)
```

#### Client Update

Update a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_update(self,
                 client_uuid,
                 email,
                 tos_consent_date,
                 tax_information,
                 country_birth,
                 last_login,
                 successful_referrals,
                 kyc_verified,
                 is_verified,
                 fee_segments,
                 portfolios,
                 risk_level,
                 onboarding_token,
                 uuid,
                 created,
                 updated,
                 status,
                 language,
                 marketing_consent_date,
                 data_consent_date,
                 referred_by=None,
                 birthdate=None,
                 tos_consent=None,
                 marketing_consent=None,
                 data_consent=None,
                 extra_data=None,
                 onboarded_by=None,
                 password=None,
                 email_verified_last_request=None,
                 comments=None,
                 email_verified=None,
                 email_verify_last_request=None,
                 title=None,
                 first_name=None,
                 middle_name=None,
                 last_name=None,
                 gender=None,
                 marital_status=None,
                 phone_number=None,
                 phone_number_verified=None,
                 employment_status=None,
                 profession=None,
                 referral_code=None,
                 activated=None,
                 utm_source=None,
                 utm_medium=None,
                 utm_campaign=None,
                 utm_term=None,
                 utm_content=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `email` | `string` | Form, Required | - |
| `tos_consent_date` | `date` | Form, Required | - |
| `tax_information` | `List of string` | Form, Required | - |
| `country_birth` | [`CountryField`](#country-field) | Form, Required | - |
| `last_login` | `datetime` | Form, Required | - |
| `successful_referrals` | `int` | Form, Required | - |
| `kyc_verified` | `bool` | Form, Required | - |
| `is_verified` | `bool` | Form, Required | - |
| `fee_segments` | `List of string` | Form, Required | - |
| `portfolios` | `List of string` | Form, Required | - |
| `risk_level` | `int` | Form, Required | - |
| `onboarding_token` | `string` | Form, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `created` | `datetime` | Form, Required | - |
| `updated` | `datetime` | Form, Required | - |
| `status` | [`StatusB65Enum`](#status-b65-enum) | Form, Required | - |
| `language` | `string` | Form, Required | **Constraints**: *Maximum Length*: `5` |
| `marketing_consent_date` | `date` | Form, Required | - |
| `data_consent_date` | `date` | Form, Required | - |
| `referred_by` | `string` | Form, Optional | - |
| `birthdate` | `date` | Form, Optional | - |
| `tos_consent` | `bool` | Form, Optional | - |
| `marketing_consent` | `bool` | Form, Optional | - |
| `data_consent` | `bool` | Form, Optional | - |
| `extra_data` | `dict` | Form, Optional | - |
| `onboarded_by` | `string` | Form, Optional | - |
| `password` | `string` | Form, Optional | - |
| `email_verified_last_request` | `datetime` | Form, Optional | - |
| `comments` | `string` | Form, Optional | - |
| `email_verified` | `bool` | Form, Optional | - |
| `email_verify_last_request` | `datetime` | Form, Optional | - |
| `title` | [`TitleEnum`](#title-enum) | Form, Optional | - |
| `first_name` | `string` | Form, Optional | - |
| `middle_name` | `string` | Form, Optional | - |
| `last_name` | `string` | Form, Optional | - |
| `gender` | [`GenderEnum`](#gender-enum) | Form, Optional | - |
| `marital_status` | [`MaritalStatusEnum`](#marital-status-enum) | Form, Optional | - |
| `phone_number` | `string` | Form, Optional | - |
| `phone_number_verified` | `datetime` | Form, Optional | - |
| `employment_status` | [`EmploymentStatusEnum`](#employment-status-enum) | Form, Optional | - |
| `profession` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `referral_code` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `activated` | `datetime` | Form, Optional | - |
| `utm_source` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_medium` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_campaign` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_term` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_content` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |

##### Response Type

[`ApplicationClientUpdate`](#application-client-update)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
email = 'email6'
tos_consent_date = dateutil.parser.parse('2016-03-13').date()
tax_information = ['tax_information9', 'tax_information0']
country_birth = CountryField()
country_birth.id = 58
country_birth.code = 'code4'
country_birth.iso_3 = 'iso34'
country_birth.name = 'name6'
country_birth.long_name = 'long_name6'
last_login = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
successful_referrals = 180
kyc_verified = False
is_verified = False
fee_segments = ['fee_segments8', 'fee_segments9', 'fee_segments0']
portfolios = ['portfolios4']
risk_level = 66
onboarding_token = 'onboarding_token4'
uuid = '00000f7e-0000-0000-0000-000000000000'
created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
updated = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
status = StatusB65Enum.ACTIVE
language = 'language2'
marketing_consent_date = dateutil.parser.parse('2016-03-13').date()
data_consent_date = dateutil.parser.parse('2016-03-13').date()

result = application_controller.client_update(client_uuid, email, tos_consent_date, tax_information, country_birth, last_login, successful_referrals, kyc_verified, is_verified, fee_segments, portfolios, risk_level, onboarding_token, uuid, created, updated, status, language, marketing_consent_date, data_consent_date)
```

#### Client Partial Update

Partial Update a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_partial_update(self,
                         client_uuid,
                         email=None,
                         birthdate=None,
                         tos_consent=None,
                         marketing_consent=None,
                         data_consent=None,
                         tos_consent_date=None,
                         tax_information=None,
                         country_birth=None,
                         last_login=None,
                         referred_by=None,
                         successful_referrals=None,
                         kyc_verified=None,
                         is_verified=None,
                         fee_segments=None,
                         extra_data=None,
                         portfolios=None,
                         onboarded_by=None,
                         risk_level=None,
                         onboarding_token=None,
                         password=None,
                         email_verified_last_request=None,
                         uuid=None,
                         created=None,
                         updated=None,
                         comments=None,
                         status=None,
                         email_verified=None,
                         email_verify_last_request=None,
                         title=None,
                         first_name=None,
                         middle_name=None,
                         last_name=None,
                         gender=None,
                         marital_status=None,
                         phone_number=None,
                         phone_number_verified=None,
                         language=None,
                         employment_status=None,
                         profession=None,
                         referral_code=None,
                         activated=None,
                         utm_source=None,
                         utm_medium=None,
                         utm_campaign=None,
                         utm_term=None,
                         utm_content=None,
                         marketing_consent_date=None,
                         data_consent_date=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `email` | `string` | Form, Optional | - |
| `birthdate` | `date` | Form, Optional | - |
| `tos_consent` | `bool` | Form, Optional | - |
| `marketing_consent` | `bool` | Form, Optional | - |
| `data_consent` | `bool` | Form, Optional | - |
| `tos_consent_date` | `date` | Form, Optional | - |
| `tax_information` | `List of string` | Form, Optional | - |
| `country_birth` | [`CountryField`](#country-field) | Form, Optional | - |
| `last_login` | `datetime` | Form, Optional | - |
| `referred_by` | `string` | Form, Optional | - |
| `successful_referrals` | `int` | Form, Optional | - |
| `kyc_verified` | `bool` | Form, Optional | - |
| `is_verified` | `bool` | Form, Optional | - |
| `fee_segments` | `List of string` | Form, Optional | - |
| `extra_data` | `dict` | Form, Optional | - |
| `portfolios` | `List of string` | Form, Optional | - |
| `onboarded_by` | `string` | Form, Optional | - |
| `risk_level` | `int` | Form, Optional | - |
| `onboarding_token` | `string` | Form, Optional | - |
| `password` | `string` | Form, Optional | - |
| `email_verified_last_request` | `datetime` | Form, Optional | - |
| `uuid` | `uuid\|string` | Form, Optional | - |
| `created` | `datetime` | Form, Optional | - |
| `updated` | `datetime` | Form, Optional | - |
| `comments` | `string` | Form, Optional | - |
| `status` | [`StatusB65Enum`](#status-b65-enum) | Form, Optional | - |
| `email_verified` | `bool` | Form, Optional | - |
| `email_verify_last_request` | `datetime` | Form, Optional | - |
| `title` | [`TitleEnum`](#title-enum) | Form, Optional | - |
| `first_name` | `string` | Form, Optional | - |
| `middle_name` | `string` | Form, Optional | - |
| `last_name` | `string` | Form, Optional | - |
| `gender` | [`GenderEnum`](#gender-enum) | Form, Optional | - |
| `marital_status` | [`MaritalStatusEnum`](#marital-status-enum) | Form, Optional | - |
| `phone_number` | `string` | Form, Optional | - |
| `phone_number_verified` | `datetime` | Form, Optional | - |
| `language` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `5` |
| `employment_status` | [`EmploymentStatusEnum`](#employment-status-enum) | Form, Optional | - |
| `profession` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `referral_code` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `activated` | `datetime` | Form, Optional | - |
| `utm_source` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_medium` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_campaign` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_term` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_content` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `marketing_consent_date` | `date` | Form, Optional | - |
| `data_consent_date` | `date` | Form, Optional | - |

##### Response Type

[`ApplicationClientUpdate`](#application-client-update)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_partial_update(client_uuid)
```

#### Client Addresses List

List address for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_addresses_list(self,
                         client_uuid,
                         limit=None,
                         offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedAddressListList`](#paginated-address-list-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_addresses_list(client_uuid)
```

#### Client Address Create

Create an address for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_address_create(self,
                         client_uuid,
                         uuid,
                         line_1,
                         postcode,
                         locality,
                         country,
                         line_2=None,
                         region=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `line_1` | `string` | Form, Required | - |
| `postcode` | `string` | Form, Required | - |
| `locality` | `string` | Form, Required | - |
| `country` | `string` | Form, Required | - |
| `line_2` | `string` | Form, Optional | - |
| `region` | `string` | Form, Optional | - |

##### Response Type

[`AddressCreate`](#address-create)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
line_1 = 'line12'
postcode = 'postcode4'
locality = 'locality0'
country = 'country4'

result = application_controller.client_address_create(client_uuid, uuid, line_1, postcode, locality, country)
```

#### Client Address Retrieve

Retrieve a client address

:information_source: **Note** This endpoint does not require authentication.

```python
def client_address_retrieve(self,
                           address_uuid,
                           client_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_uuid` | `uuid\|string` | Template, Required | - |
| `client_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`AddressList`](#address-list)

##### Example Usage

```python
address_uuid = '00002030-0000-0000-0000-000000000000'
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_address_retrieve(address_uuid, client_uuid)
```

#### Client Address Update

Update a client address

:information_source: **Note** This endpoint does not require authentication.

```python
def client_address_update(self,
                         address_uuid,
                         client_uuid,
                         uuid,
                         line_1,
                         postcode,
                         locality,
                         country,
                         line_2=None,
                         region=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_uuid` | `uuid\|string` | Template, Required | - |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `line_1` | `string` | Form, Required | - |
| `postcode` | `string` | Form, Required | - |
| `locality` | `string` | Form, Required | - |
| `country` | `string` | Form, Required | - |
| `line_2` | `string` | Form, Optional | - |
| `region` | `string` | Form, Optional | - |

##### Response Type

[`AddressUpdate`](#address-update)

##### Example Usage

```python
address_uuid = '00002030-0000-0000-0000-000000000000'
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
line_1 = 'line12'
postcode = 'postcode4'
locality = 'locality0'
country = 'country4'

result = application_controller.client_address_update(address_uuid, client_uuid, uuid, line_1, postcode, locality, country)
```

#### Client Address Partial Update

Partial Update a client address

:information_source: **Note** This endpoint does not require authentication.

```python
def client_address_partial_update(self,
                                 address_uuid,
                                 client_uuid,
                                 uuid=None,
                                 line_1=None,
                                 line_2=None,
                                 postcode=None,
                                 locality=None,
                                 country=None,
                                 region=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_uuid` | `uuid\|string` | Template, Required | - |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Optional | - |
| `line_1` | `string` | Form, Optional | - |
| `line_2` | `string` | Form, Optional | - |
| `postcode` | `string` | Form, Optional | - |
| `locality` | `string` | Form, Optional | - |
| `country` | `string` | Form, Optional | - |
| `region` | `string` | Form, Optional | - |

##### Response Type

[`AddressUpdate`](#address-update)

##### Example Usage

```python
address_uuid = '00002030-0000-0000-0000-000000000000'
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_address_partial_update(address_uuid, client_uuid)
```

#### Client Address Delete

Delete a client address

:information_source: **Note** This endpoint does not require authentication.

```python
def client_address_delete(self,
                         address_uuid,
                         client_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_uuid` | `uuid\|string` | Template, Required | - |
| `client_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
address_uuid = '00002030-0000-0000-0000-000000000000'
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_address_delete(address_uuid, client_uuid)
```

#### Client Bank Accounts List

List Bank Account for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_bank_accounts_list(self,
                             client_uuid,
                             limit=None,
                             offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedBankAccountListList`](#paginated-bank-account-list-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_bank_accounts_list(client_uuid)
```

#### Client Bank Account Create

Create a bank account for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_bank_account_create(self,
                              client_uuid,
                              uuid,
                              account_number=None,
                              account_sort_code=None,
                              account_holder_name=None,
                              joint=None,
                              bank_name=None,
                              iban=None,
                              swift_code=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `account_number` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `30` |
| `account_sort_code` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `6` |
| `account_holder_name` | `string` | Form, Optional | - |
| `joint` | `bool` | Form, Optional | - |
| `bank_name` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `iban` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `34` |
| `swift_code` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `11` |

##### Response Type

[`BankAccountCreateUpdate`](#bank-account-create-update)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = application_controller.client_bank_account_create(client_uuid, uuid)
```

#### Client Bank Account Retrieve

Retrieve a client bank account

:information_source: **Note** This endpoint does not require authentication.

```python
def client_bank_account_retrieve(self,
                                bank_account_uuid,
                                client_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_uuid` | `uuid\|string` | Template, Required | - |
| `client_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`BankAccountList`](#bank-account-list)

##### Example Usage

```python
bank_account_uuid = '000004bc-0000-0000-0000-000000000000'
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_bank_account_retrieve(bank_account_uuid, client_uuid)
```

#### Client Bank Account Update

Update a client bank account

:information_source: **Note** This endpoint does not require authentication.

```python
def client_bank_account_update(self,
                              bank_account_uuid,
                              client_uuid,
                              uuid,
                              account_number=None,
                              account_sort_code=None,
                              account_holder_name=None,
                              joint=None,
                              bank_name=None,
                              iban=None,
                              swift_code=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_uuid` | `uuid\|string` | Template, Required | - |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `account_number` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `30` |
| `account_sort_code` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `6` |
| `account_holder_name` | `string` | Form, Optional | - |
| `joint` | `bool` | Form, Optional | - |
| `bank_name` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `iban` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `34` |
| `swift_code` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `11` |

##### Response Type

[`BankAccountCreateUpdate`](#bank-account-create-update)

##### Example Usage

```python
bank_account_uuid = '000004bc-0000-0000-0000-000000000000'
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'

result = application_controller.client_bank_account_update(bank_account_uuid, client_uuid, uuid)
```

#### Client Bank Account Partial Update

Partial Update a client bank account

:information_source: **Note** This endpoint does not require authentication.

```python
def client_bank_account_partial_update(self,
                                      bank_account_uuid,
                                      client_uuid,
                                      uuid=None,
                                      account_number=None,
                                      account_sort_code=None,
                                      account_holder_name=None,
                                      joint=None,
                                      bank_name=None,
                                      iban=None,
                                      swift_code=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_uuid` | `uuid\|string` | Template, Required | - |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Optional | - |
| `account_number` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `30` |
| `account_sort_code` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `6` |
| `account_holder_name` | `string` | Form, Optional | - |
| `joint` | `bool` | Form, Optional | - |
| `bank_name` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `iban` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `34` |
| `swift_code` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `11` |

##### Response Type

[`BankAccountCreateUpdate`](#bank-account-create-update)

##### Example Usage

```python
bank_account_uuid = '000004bc-0000-0000-0000-000000000000'
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_bank_account_partial_update(bank_account_uuid, client_uuid)
```

#### Client Bank Account Delete

Delete a client bank account

:information_source: **Note** This endpoint does not require authentication.

```python
def client_bank_account_delete(self,
                              bank_account_uuid,
                              client_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_uuid` | `uuid\|string` | Template, Required | - |
| `client_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
bank_account_uuid = '000004bc-0000-0000-0000-000000000000'
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_bank_account_delete(bank_account_uuid, client_uuid)
```

#### Client Nationlities List

List nationlities for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_nationlities_list(self,
                            client_uuid,
                            limit=None,
                            offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedNationalityListList`](#paginated-nationality-list-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_nationlities_list(client_uuid)
```

#### Client Nationality Create

Create nationality for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_nationality_create(self,
                             client_uuid,
                             country,
                             document_number=None,
                             document_type=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `country` | `string` | Form, Required | - |
| `document_number` | `string` | Form, Optional | - |
| `document_type` | `string` | Form, Optional | - |

##### Response Type

[`NationalityCreate`](#nationality-create)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
country = 'country4'

result = application_controller.client_nationality_create(client_uuid, country)
```

#### Client Nationlity Retrieve

Retrieve a client nationality

:information_source: **Note** This endpoint does not require authentication.

```python
def client_nationlity_retrieve(self,
                              client_uuid,
                              nationality_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `nationality_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`NationalityList`](#nationality-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
nationality_uuid = '00000edc-0000-0000-0000-000000000000'

result = application_controller.client_nationlity_retrieve(client_uuid, nationality_uuid)
```

#### Client Nationlity Update

Update a client nationality

:information_source: **Note** This endpoint does not require authentication.

```python
def client_nationlity_update(self,
                            client_uuid,
                            nationality_uuid,
                            country,
                            document_number=None,
                            document_type=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `nationality_uuid` | `uuid\|string` | Template, Required | - |
| `country` | `string` | Form, Required | - |
| `document_number` | `string` | Form, Optional | - |
| `document_type` | `string` | Form, Optional | - |

##### Response Type

[`NationalityUpdate`](#nationality-update)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
nationality_uuid = '00000edc-0000-0000-0000-000000000000'
country = 'country4'

result = application_controller.client_nationlity_update(client_uuid, nationality_uuid, country)
```

#### Client Nationlity Partial Update

Partial Update a client nationality

:information_source: **Note** This endpoint does not require authentication.

```python
def client_nationlity_partial_update(self,
                                    client_uuid,
                                    nationality_uuid,
                                    country=None,
                                    document_number=None,
                                    document_type=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `nationality_uuid` | `uuid\|string` | Template, Required | - |
| `country` | `string` | Form, Optional | - |
| `document_number` | `string` | Form, Optional | - |
| `document_type` | `string` | Form, Optional | - |

##### Response Type

[`NationalityUpdate`](#nationality-update)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
nationality_uuid = '00000edc-0000-0000-0000-000000000000'

result = application_controller.client_nationlity_partial_update(client_uuid, nationality_uuid)
```

#### Client Nationlity Delete

Delete a client nationality

:information_source: **Note** This endpoint does not require authentication.

```python
def client_nationlity_delete(self,
                            client_uuid,
                            nationality_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `nationality_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
nationality_uuid = '00000edc-0000-0000-0000-000000000000'

result = application_controller.client_nationlity_delete(client_uuid, nationality_uuid)
```

#### Client Complete Onboarding

Complete onboarding for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_complete_onboarding(self,
                              client_uuid,
                              email,
                              tos_consent,
                              marketing_consent,
                              data_consent,
                              tos_consent_date,
                              tax_information,
                              country_birth,
                              last_login,
                              successful_referrals,
                              kyc_verified,
                              is_verified,
                              fee_segments,
                              extra_data,
                              portfolios,
                              risk_level,
                              onboarding_token,
                              uuid,
                              created,
                              updated,
                              status,
                              language,
                              marketing_consent_date,
                              data_consent_date,
                              referred_by=None,
                              birthdate=None,
                              onboarded_by=None,
                              comments=None,
                              email_verified=None,
                              email_verify_last_request=None,
                              title=None,
                              first_name=None,
                              middle_name=None,
                              last_name=None,
                              gender=None,
                              marital_status=None,
                              phone_number=None,
                              phone_number_verified=None,
                              employment_status=None,
                              profession=None,
                              referral_code=None,
                              activated=None,
                              utm_source=None,
                              utm_medium=None,
                              utm_campaign=None,
                              utm_term=None,
                              utm_content=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `email` | `string` | Form, Required | - |
| `tos_consent` | `bool` | Form, Required | - |
| `marketing_consent` | `bool` | Form, Required | - |
| `data_consent` | `bool` | Form, Required | - |
| `tos_consent_date` | `date` | Form, Required | - |
| `tax_information` | `List of string` | Form, Required | - |
| `country_birth` | [`CountryField`](#country-field) | Form, Required | - |
| `last_login` | `datetime` | Form, Required | - |
| `successful_referrals` | `int` | Form, Required | - |
| `kyc_verified` | `bool` | Form, Required | - |
| `is_verified` | `bool` | Form, Required | - |
| `fee_segments` | `List of string` | Form, Required | - |
| `extra_data` | `dict` | Form, Required | - |
| `portfolios` | `List of string` | Form, Required | - |
| `risk_level` | `int` | Form, Required | - |
| `onboarding_token` | `string` | Form, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `created` | `datetime` | Form, Required | - |
| `updated` | `datetime` | Form, Required | - |
| `status` | [`StatusB65Enum`](#status-b65-enum) | Form, Required | - |
| `language` | `string` | Form, Required | **Constraints**: *Maximum Length*: `5` |
| `marketing_consent_date` | `date` | Form, Required | - |
| `data_consent_date` | `date` | Form, Required | - |
| `referred_by` | `string` | Form, Optional | - |
| `birthdate` | `date` | Form, Optional | - |
| `onboarded_by` | `string` | Form, Optional | - |
| `comments` | `string` | Form, Optional | - |
| `email_verified` | `bool` | Form, Optional | - |
| `email_verify_last_request` | `datetime` | Form, Optional | - |
| `title` | [`TitleEnum`](#title-enum) | Form, Optional | - |
| `first_name` | `string` | Form, Optional | - |
| `middle_name` | `string` | Form, Optional | - |
| `last_name` | `string` | Form, Optional | - |
| `gender` | [`GenderEnum`](#gender-enum) | Form, Optional | - |
| `marital_status` | [`MaritalStatusEnum`](#marital-status-enum) | Form, Optional | - |
| `phone_number` | `string` | Form, Optional | - |
| `phone_number_verified` | `datetime` | Form, Optional | - |
| `employment_status` | [`EmploymentStatusEnum`](#employment-status-enum) | Form, Optional | - |
| `profession` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `referral_code` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `activated` | `datetime` | Form, Optional | - |
| `utm_source` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_medium` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_campaign` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_term` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_content` | `string` | Form, Optional | **Constraints**: *Maximum Length*: `250` |

##### Response Type

[`ClientDetail`](#client-detail)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
email = 'email6'
tos_consent = False
marketing_consent = False
data_consent = False
tos_consent_date = dateutil.parser.parse('2016-03-13').date()
tax_information = ['tax_information9', 'tax_information0']
country_birth = CountryField()
country_birth.id = 58
country_birth.code = 'code4'
country_birth.iso_3 = 'iso34'
country_birth.name = 'name6'
country_birth.long_name = 'long_name6'
last_login = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
successful_referrals = 180
kyc_verified = False
is_verified = False
fee_segments = ['fee_segments8', 'fee_segments9', 'fee_segments0']
extra_data = {'' : jsonpickle.decode(None), '' : jsonpickle.decode(None), '' : jsonpickle.decode(None) } 
portfolios = ['portfolios4']
risk_level = 66
onboarding_token = 'onboarding_token4'
uuid = '00000f7e-0000-0000-0000-000000000000'
created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
updated = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
status = StatusB65Enum.ACTIVE
language = 'language2'
marketing_consent_date = dateutil.parser.parse('2016-03-13').date()
data_consent_date = dateutil.parser.parse('2016-03-13').date()

result = application_controller.client_complete_onboarding(client_uuid, email, tos_consent, marketing_consent, data_consent, tos_consent_date, tax_information, country_birth, last_login, successful_referrals, kyc_verified, is_verified, fee_segments, extra_data, portfolios, risk_level, onboarding_token, uuid, created, updated, status, language, marketing_consent_date, data_consent_date)
```

#### Client TWRR Performance

Calculate TWRR Performance for client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_twrr_performance(self,
                           client_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`ClientPerformance`](#client-performance)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_twrr_performance(client_uuid)
```

#### Client Risk Assessment List

List Risk Assessment for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_risk_assessment_list(self,
                               client_uuid,
                               limit=None,
                               offset=None,
                               status=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |
| `status` | [`List of AssessmentStatusEnum`](#assessment-status-enum) | Query, Optional | - |

##### Response Type

[`PaginatedAssessmentList`](#paginated-assessment-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_risk_assessment_list(client_uuid)
```

#### Client Risk Assessment Create

Create a risk assessment for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_risk_assessment_create(self,
                                 client_uuid,
                                 uuid,
                                 choices,
                                 risk_level,
                                 created,
                                 completed=None,
                                 status=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `choices` | [`List of RiskChoiceQuestionCode`](#risk-choice-question-code) | Form, Required | - |
| `risk_level` | `int` | Form, Required | - |
| `created` | `datetime` | Form, Required | - |
| `completed` | `datetime` | Form, Optional | - |
| `status` | [`AssessmentStatusEnum`](#assessment-status-enum) | Form, Optional | - |

##### Response Type

[`Assessment`](#assessment)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
choices = []

choices.append(RiskChoiceQuestionCode())
choices[0].code = 'code5'
choices[0].created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
choices[0].question_code = 'question_code3'

choices.append(RiskChoiceQuestionCode())
choices[1].code = 'code6'
choices[1].created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
choices[1].question_code = 'question_code4'

risk_level = 66
created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = application_controller.client_risk_assessment_create(client_uuid, uuid, choices, risk_level, created)
```

#### Client Risk Assessment Retrieve

Retrieve a client risk assessment

:information_source: **Note** This endpoint does not require authentication.

```python
def client_risk_assessment_retrieve(self,
                                   assessment_uuid,
                                   client_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assessment_uuid` | `uuid\|string` | Template, Required | - |
| `client_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`Assessment`](#assessment)

##### Example Usage

```python
assessment_uuid = '00002304-0000-0000-0000-000000000000'
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_risk_assessment_retrieve(assessment_uuid, client_uuid)
```

#### Client Risk Assessment Partial Update

Partial Update a client risk assessment

:information_source: **Note** This endpoint does not require authentication.

```python
def client_risk_assessment_partial_update(self,
                                         assessment_uuid,
                                         client_uuid,
                                         uuid=None,
                                         completed=None,
                                         choices=None,
                                         status=None,
                                         risk_level=None,
                                         created=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assessment_uuid` | `uuid\|string` | Template, Required | - |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Optional | - |
| `completed` | `datetime` | Form, Optional | - |
| `choices` | [`List of RiskChoiceQuestionCode`](#risk-choice-question-code) | Form, Optional | - |
| `status` | [`AssessmentStatusEnum`](#assessment-status-enum) | Form, Optional | - |
| `risk_level` | `int` | Form, Optional | - |
| `created` | `datetime` | Form, Optional | - |

##### Response Type

[`Assessment`](#assessment)

##### Example Usage

```python
assessment_uuid = '00002304-0000-0000-0000-000000000000'
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_risk_assessment_partial_update(assessment_uuid, client_uuid)
```

#### Client Risk Assessment Delete

Delete a client risk assessment

:information_source: **Note** This endpoint does not require authentication.

```python
def client_risk_assessment_delete(self,
                                 assessment_uuid,
                                 client_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assessment_uuid` | `uuid\|string` | Template, Required | - |
| `client_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
assessment_uuid = '00002304-0000-0000-0000-000000000000'
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_risk_assessment_delete(assessment_uuid, client_uuid)
```

#### Client Tax Information List

List tax information for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_tax_information_list(self,
                               client_uuid,
                               limit=None,
                               offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedTaxInformationListList`](#paginated-tax-information-list-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'

result = application_controller.client_tax_information_list(client_uuid)
```

#### Client Tax Information Create

Create a tax inforation for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_tax_information_create(self,
                                 client_uuid,
                                 uuid,
                                 country,
                                 document_number,
                                 document_type=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `country` | `string` | Form, Required | - |
| `document_number` | `string` | Form, Required | - |
| `document_type` | `string` | Form, Optional | - |

##### Response Type

[`TaxInformationCreateUpdate`](#tax-information-create-update)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
country = 'country4'
document_number = 'document_number6'

result = application_controller.client_tax_information_create(client_uuid, uuid, country, document_number)
```

#### Client Tax Information Retrieve

Retrieve a client tax inforation

:information_source: **Note** This endpoint does not require authentication.

```python
def client_tax_information_retrieve(self,
                                   client_uuid,
                                   tax_information_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `tax_information_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

[`TaxInformationList`](#tax-information-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
tax_information_uuid = '00000900-0000-0000-0000-000000000000'

result = application_controller.client_tax_information_retrieve(client_uuid, tax_information_uuid)
```

#### Client Tax Information Update

Update a client tax inforation

:information_source: **Note** This endpoint does not require authentication.

```python
def client_tax_information_update(self,
                                 client_uuid,
                                 tax_information_uuid,
                                 uuid,
                                 country,
                                 document_number,
                                 document_type=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `tax_information_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `country` | `string` | Form, Required | - |
| `document_number` | `string` | Form, Required | - |
| `document_type` | `string` | Form, Optional | - |

##### Response Type

[`TaxInformationCreateUpdate`](#tax-information-create-update)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
tax_information_uuid = '00000900-0000-0000-0000-000000000000'
uuid = '00000f7e-0000-0000-0000-000000000000'
country = 'country4'
document_number = 'document_number6'

result = application_controller.client_tax_information_update(client_uuid, tax_information_uuid, uuid, country, document_number)
```

#### Client Tax Information Partial Update

Partial Update a client tax inforation

:information_source: **Note** This endpoint does not require authentication.

```python
def client_tax_information_partial_update(self,
                                         client_uuid,
                                         tax_information_uuid,
                                         uuid=None,
                                         country=None,
                                         document_number=None,
                                         document_type=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `tax_information_uuid` | `uuid\|string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Optional | - |
| `country` | `string` | Form, Optional | - |
| `document_number` | `string` | Form, Optional | - |
| `document_type` | `string` | Form, Optional | - |

##### Response Type

[`TaxInformationCreateUpdate`](#tax-information-create-update)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
tax_information_uuid = '00000900-0000-0000-0000-000000000000'

result = application_controller.client_tax_information_partial_update(client_uuid, tax_information_uuid)
```

#### Client Tax Information Delete

Delete a client tax inforation

:information_source: **Note** This endpoint does not require authentication.

```python
def client_tax_information_delete(self,
                                 client_uuid,
                                 tax_information_uuid)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `tax_information_uuid` | `uuid\|string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
tax_information_uuid = '00000900-0000-0000-0000-000000000000'

result = application_controller.client_tax_information_delete(client_uuid, tax_information_uuid)
```

#### Client Verification List

List Verification for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_verification_list(self,
                            client_uuid,
                            verify_type_code,
                            limit=None,
                            offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `verify_type_code` | `string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedVerificationListList`](#paginated-verification-list-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
verify_type_code = 'verify_type_code0'

result = application_controller.client_verification_list(client_uuid, verify_type_code)
```

#### Client Verification Create

Create a verification for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_verification_create(self,
                              client_uuid,
                              verify_type_code,
                              uuid,
                              verify_type,
                              created,
                              updated,
                              status=None,
                              result=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `verify_type_code` | `string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `verify_type` | [`VerifyTypeEnum`](#verify-type-enum) | Form, Required | - |
| `created` | `datetime` | Form, Required | - |
| `updated` | `datetime` | Form, Required | - |
| `status` | [`StatusBd7Enum`](#status-bd-7-enum) | Form, Optional | - |
| `result` | [`ResultEnum`](#result-enum) | Form, Optional | - |

##### Response Type

[`VerificationCreate`](#verification-create)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
verify_type_code = 'verify_type_code0'
uuid = '00000f7e-0000-0000-0000-000000000000'
verify_type = VerifyTypeEnum.IDENTITY
created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
updated = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = application_controller.client_verification_create(client_uuid, verify_type_code, uuid, verify_type, created, updated)
```

#### Client Verification Retrieve

Retrieve a client verification

:information_source: **Note** This endpoint does not require authentication.

```python
def client_verification_retrieve(self,
                                client_uuid,
                                verification_uuid,
                                verify_type_code)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `verification_uuid` | `uuid\|string` | Template, Required | - |
| `verify_type_code` | `string` | Template, Required | - |

##### Response Type

[`VerificationList`](#verification-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
verification_uuid = '00001dcc-0000-0000-0000-000000000000'
verify_type_code = 'verify_type_code0'

result = application_controller.client_verification_retrieve(client_uuid, verification_uuid, verify_type_code)
```

#### Client Verification Document List

List Verification Document for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_verification_document_list(self,
                                     client_uuid,
                                     verify_type_code,
                                     limit=None,
                                     offset=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `verify_type_code` | `string` | Template, Required | - |
| `limit` | `int` | Query, Optional | Number of results to return per page. |
| `offset` | `int` | Query, Optional | The initial index from which to return the results. |

##### Response Type

[`PaginatedVerificationDocumentList`](#paginated-verification-document-list)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
verify_type_code = 'verify_type_code0'

result = application_controller.client_verification_document_list(client_uuid, verify_type_code)
```

#### Client Verification Document Create

Create a verification Document for a client

:information_source: **Note** This endpoint does not require authentication.

```python
def client_verification_document_create(self,
                                       client_uuid,
                                       verify_type_code,
                                       uuid,
                                       verify_type,
                                       created,
                                       updated,
                                       verification_documents=None,
                                       status=None,
                                       result=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `verify_type_code` | `string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `verify_type` | [`VerifyTypeEnum`](#verify-type-enum) | Form, Required | - |
| `created` | `datetime` | Form, Required | - |
| `updated` | `datetime` | Form, Required | - |
| `verification_documents` | [`List of VerificationDocumentCreate`](#verification-document-create) | Form, Optional | - |
| `status` | [`StatusBd7Enum`](#status-bd-7-enum) | Form, Optional | - |
| `result` | [`ResultEnum`](#result-enum) | Form, Optional | - |

##### Response Type

[`VerificationWithType`](#verification-with-type)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
verify_type_code = 'verify_type_code0'
uuid = '00000f7e-0000-0000-0000-000000000000'
verify_type = VerifyTypeEnum.IDENTITY
created = dateutil.parser.parse('2016-03-13T12:52:32.123Z')
updated = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = application_controller.client_verification_document_create(client_uuid, verify_type_code, uuid, verify_type, created, updated)
```

#### Client Verification Document Retrieve

Retrieve a client verification document

:information_source: **Note** This endpoint does not require authentication.

```python
def client_verification_document_retrieve(self,
                                         client_uuid,
                                         verification_document_uuid,
                                         verify_type_code)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `verification_document_uuid` | `uuid\|string` | Template, Required | - |
| `verify_type_code` | `string` | Template, Required | - |

##### Response Type

[`VerificationDocument`](#verification-document)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
verification_document_uuid = '0000005c-0000-0000-0000-000000000000'
verify_type_code = 'verify_type_code0'

result = application_controller.client_verification_document_retrieve(client_uuid, verification_document_uuid, verify_type_code)
```

#### Client Verification Document Update

Update a client verification document

:information_source: **Note** This endpoint does not require authentication.

```python
def client_verification_document_update(self,
                                       client_uuid,
                                       verification_document_uuid,
                                       verify_type_code,
                                       uuid,
                                       document_type,
                                       document_front,
                                       document_back)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `verification_document_uuid` | `uuid\|string` | Template, Required | - |
| `verify_type_code` | `string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Required | - |
| `document_type` | [`DocumentTypeEnum`](#document-type-enum) | Form, Required | - |
| `document_front` | `string` | Form, Required | - |
| `document_back` | `string` | Form, Required | - |

##### Response Type

[`VerificationDocument`](#verification-document)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
verification_document_uuid = '0000005c-0000-0000-0000-000000000000'
verify_type_code = 'verify_type_code0'
uuid = '00000f7e-0000-0000-0000-000000000000'
document_type = DocumentTypeEnum.LOCAL_TAX_BILL
document_front = 'document_front0'
document_back = 'document_back6'

result = application_controller.client_verification_document_update(client_uuid, verification_document_uuid, verify_type_code, uuid, document_type, document_front, document_back)
```

#### Client Verification Document Partial Update

Partial Update a client verification document

:information_source: **Note** This endpoint does not require authentication.

```python
def client_verification_document_partial_update(self,
                                               client_uuid,
                                               verification_document_uuid,
                                               verify_type_code,
                                               uuid=None,
                                               document_type=None,
                                               document_front=None,
                                               document_back=None)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `verification_document_uuid` | `uuid\|string` | Template, Required | - |
| `verify_type_code` | `string` | Template, Required | - |
| `uuid` | `uuid\|string` | Form, Optional | - |
| `document_type` | [`DocumentTypeEnum`](#document-type-enum) | Form, Optional | - |
| `document_front` | `string` | Form, Optional | - |
| `document_back` | `string` | Form, Optional | - |

##### Response Type

[`VerificationDocument`](#verification-document)

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
verification_document_uuid = '0000005c-0000-0000-0000-000000000000'
verify_type_code = 'verify_type_code0'

result = application_controller.client_verification_document_partial_update(client_uuid, verification_document_uuid, verify_type_code)
```

#### Client Verification Document Delete

Delete a client verificatoin document

:information_source: **Note** This endpoint does not require authentication.

```python
def client_verification_document_delete(self,
                                       client_uuid,
                                       verification_document_uuid,
                                       verify_type_code)
```

##### Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_uuid` | `uuid\|string` | Template, Required | - |
| `verification_document_uuid` | `uuid\|string` | Template, Required | - |
| `verify_type_code` | `string` | Template, Required | - |

##### Response Type

`void`

##### Example Usage

```python
client_uuid = '00001c58-0000-0000-0000-000000000000'
verification_document_uuid = '0000005c-0000-0000-0000-000000000000'
verify_type_code = 'verify_type_code0'

result = application_controller.client_verification_document_delete(client_uuid, verification_document_uuid, verify_type_code)
```

## Model Reference

### Structures

* [AUM Evoluation](#aum-evoluation)
* [AUM Portfolio Risk](#aum-portfolio-risk)
* [Access Log](#access-log)
* [Address Create](#address-create)
* [Address List](#address-list)
* [Address Update](#address-update)
* [Allocation by Asset](#allocation-by-asset)
* [Allocation by Code](#allocation-by-code)
* [Allocation Detail](#allocation-detail)
* [Allocation List](#allocation-list)
* [App Version](#app-version)
* [Application Client Update](#application-client-update)
* [Assessment](#assessment)
* [Asset Category](#asset-category)
* [Asset Concentration Risk](#asset-concentration-risk)
* [Asset Detail](#asset-detail)
* [Asset Growth](#asset-growth)
* [Asset List](#asset-list)
* [Asset Model Portfolio](#asset-model-portfolio)
* [Attachment](#attachment)
* [Authentication Response](#authentication-response)
* [Bank Account Create Update](#bank-account-create-update)
* [Bank Account List](#bank-account-list)
* [Base Portfolio Type Restrictions](#base-portfolio-type-restrictions)
* [Category](#category)
* [Client Create](#client-create-1)
* [Client Detail](#client-detail)
* [Client Embed Ranking](#client-embed-ranking)
* [Client Performance](#client-performance)
* [Client Ranking](#client-ranking)
* [Client Referral](#client-referral)
* [Conversation Create](#conversation-create)
* [Conversation List](#conversation-list)
* [Core Category Group](#core-category-group)
* [Country Field](#country-field)
* [Country List](#country-list)
* [Create Order](#create-order)
* [Currency](#currency)
* [Current Allocation](#current-allocation)
* [Deposit Create](#deposit-create)
* [Deposit Detail](#deposit-detail)
* [Deposit List](#deposit-list)
* [Document](#document)
* [ETS Forecast Request](#ets-forecast-request)
* [Email Verify Request](#email-verify-request)
* [Email Verify View](#email-verify-view)
* [Feed Activity List](#feed-activity-list)
* [Forecast Decumulation Request](#forecast-decumulation-request)
* [Forecast Request](#forecast-request)
* [Goal](#goal)
* [Impersionation Response](#impersionation-response)
* [Impersonation Token](#impersonation-token)
* [Intraday Price](#intraday-price)
* [Investor Fee](#investor-fee)
* [Investor Model Portfolio](#investor-model-portfolio)
* [Investor Withdrawal Create](#investor-withdrawal-create)
* [Investor Withdrawal List](#investor-withdrawal-list)
* [Invoice Details](#invoice-details)
* [Invoice List](#invoice-list)
* [JSON Web Token](#json-web-token)
* [JWT Refresh Response](#jwt-refresh-response)
* [JWT Response](#jwt-response)
* [Message](#message)
* [Minimum App Version](#minimum-app-version)
* [Model Portfolio Forecast Request](#model-portfolio-forecast-request)
* [National Document](#national-document)
* [Nationality Create](#nationality-create)
* [Nationality List](#nationality-list)
* [Nationality Update](#nationality-update)
* [Nucoro Setting](#nucoro-setting)
* [Onboarding Response](#onboarding-response)
* [Onboarding Token](#onboarding-token)
* [Order List](#order-list)
* [Paginated Access Log List](#paginated-access-log-list)
* [Paginated Address List List](#paginated-address-list-list)
* [Paginated Allocation List List](#paginated-allocation-list-list)
* [Paginated Assessment List](#paginated-assessment-list)
* [Paginated Asset Category List](#paginated-asset-category-list)
* [Paginated Asset Growth List](#paginated-asset-growth-list)
* [Paginated Asset List List](#paginated-asset-list-list)
* [Paginated Bank Account List List](#paginated-bank-account-list-list)
* [Paginated Base Portfolio Type Restrictions List](#paginated-base-portfolio-type-restrictions-list)
* [Paginated Category List](#paginated-category-list)
* [Paginated Client Detail List](#paginated-client-detail-list)
* [Paginated Conversation List List](#paginated-conversation-list-list)
* [Paginated Core Category Group List](#paginated-core-category-group-list)
* [Paginated Country List List](#paginated-country-list-list)
* [Paginated Deposit List List](#paginated-deposit-list-list)
* [Paginated Document List](#paginated-document-list)
* [Paginated Feed Activity List List](#paginated-feed-activity-list-list)
* [Paginated Goal List](#paginated-goal-list)
* [Paginated Intraday Price List](#paginated-intraday-price-list)
* [Paginated Investor Fee List](#paginated-investor-fee-list)
* [Paginated Investor Model Portfolio List](#paginated-investor-model-portfolio-list)
* [Paginated Investor Withdrawal List List](#paginated-investor-withdrawal-list-list)
* [Paginated Invoice List List](#paginated-invoice-list-list)
* [Paginated Message List](#paginated-message-list)
* [Paginated National Document List](#paginated-national-document-list)
* [Paginated Nationality List List](#paginated-nationality-list-list)
* [Paginated Order List List](#paginated-order-list-list)
* [Paginated Portfolio List List](#paginated-portfolio-list-list)
* [Paginated Portfolio Performance List](#paginated-portfolio-performance-list)
* [Paginated Portfolio Performance Positions List](#paginated-portfolio-performance-positions-list)
* [Paginated Portfolio Type List](#paginated-portfolio-type-list)
* [Paginated Preset Category Group List](#paginated-preset-category-group-list)
* [Paginated Price List](#paginated-price-list)
* [Paginated Question List](#paginated-question-list)
* [Paginated Rebalance List](#paginated-rebalance-list)
* [Paginated Statement List](#paginated-statement-list)
* [Paginated Tax Information List List](#paginated-tax-information-list-list)
* [Paginated Tax Report List](#paginated-tax-report-list)
* [Paginated Tos List](#paginated-tos-list)
* [Paginated Verification Document List](#paginated-verification-document-list)
* [Paginated Verification List List](#paginated-verification-list-list)
* [Paginated Watchlist List](#paginated-watchlist-list)
* [Password Reset](#password-reset)
* [Password Reset Request](#password-reset-request)
* [Password Update](#password-update)
* [Patched Address Update](#patched-address-update)
* [Patched Application Client Update](#patched-application-client-update)
* [Patched Assessment](#patched-assessment)
* [Patched Bank Account Create Update](#patched-bank-account-create-update)
* [Patched Goal](#patched-goal)
* [Patched Investor Fee](#patched-investor-fee)
* [Patched Nationality Update](#patched-nationality-update)
* [Patched Password Reset Request](#patched-password-reset-request)
* [Patched Portfolio Update](#patched-portfolio-update)
* [Patched Tax Information Create Update](#patched-tax-information-create-update)
* [Patched Verification Document](#patched-verification-document)
* [Portal Setting Value List](#portal-setting-value-list)
* [Portfolio Create](#portfolio-create)
* [Portfolio Detail](#portfolio-detail)
* [Portfolio List](#portfolio-list)
* [Portfolio Performance](#portfolio-performance)
* [Portfolio Performance Positions](#portfolio-performance-positions)
* [Portfolio Type](#portfolio-type)
* [Portfolio Type Restrictions](#portfolio-type-restrictions)
* [Portfolio Update](#portfolio-update)
* [Position](#position)
* [Preset Category Group](#preset-category-group)
* [Price](#price)
* [Question](#question)
* [Rebalance](#rebalance)
* [Related Asset Serializer With Asset Categories](#related-asset-serializer-with-asset-categories)
* [Related Asset Serializer With Permission](#related-asset-serializer-with-permission)
* [Relationship Manager](#relationship-manager)
* [Response](#response)
* [Risk Choice](#risk-choice)
* [Risk Choice Question Code](#risk-choice-question-code)
* [Statement](#statement)
* [Subscribe](#subscribe)
* [Tax Information Create Update](#tax-information-create-update)
* [Tax Information List](#tax-information-list)
* [Tax Report](#tax-report)
* [Token Refresh](#token-refresh)
* [Tos](#tos)
* [Unsubscribe](#unsubscribe)
* [Verification Create](#verification-create)
* [Verification Document](#verification-document)
* [Verification Document Create](#verification-document-create)
* [Verification List](#verification-list)
* [Verification With Type](#verification-with-type)
* [Watchlist](#watchlist)
* [Websocket Authentication](#websocket-authentication)
* [Withdrawal Detail](#withdrawal-detail)

#### AUM Evoluation

##### Class Name

`AUMEvoluation`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `valuation_date` | `date` | Required | - |
| `balance` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |

##### Example (as JSON)

```json
{
  "valuation_date": "2016-03-13",
  "balance": 26.24
}
```

#### AUM Portfolio Risk

##### Class Name

`AUMPortfolioRisk`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `risk_level` | `int` | Required | - |
| `balance` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |

##### Example (as JSON)

```json
{
  "risk_level": 66,
  "balance": 26.24
}
```

#### Access Log

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`AccessLog`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `created` | `datetime` | Required | - |
| `user_agent` | `string` | Required | - |
| `ip_address` | `string` | Required | - |
| `browser` | `string` | Required | - |
| `browser_version` | `string` | Required | - |
| `device_brand` | `string` | Required | - |
| `device_model` | `string` | Required | - |
| `os` | `string` | Required | - |
| `os_version` | `string` | Required | - |
| `channel` | [`ChannelEnum`](#channel-enum) | Required | - |
| `country` | `string` | Required | - |
| `city` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "created": "2016-03-13T12:52:32.123Z",
  "user_agent": "user_agent2",
  "ip_address": "ip_address0",
  "browser": "browser0",
  "browser_version": "browser_version2",
  "device_brand": "device_brand4",
  "device_model": "device_model4",
  "os": "os8",
  "os_version": "os_version8",
  "channel": "IOS",
  "country": "country4",
  "city": "city0"
}
```

#### Address Create

##### Class Name

`AddressCreate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `line_1` | `string` | Required | - |
| `line_2` | `string` | Optional | - |
| `postcode` | `string` | Required | - |
| `locality` | `string` | Required | - |
| `country` | `string` | Required | - |
| `region` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "line1": "line12",
  "line2": null,
  "postcode": "postcode4",
  "locality": "locality0",
  "country": "country4",
  "region": null
}
```

#### Address List

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`AddressList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `line_1` | `string` | Required | - |
| `line_2` | `string` | Required | - |
| `postcode` | `string` | Required | - |
| `locality` | `string` | Required | - |
| `country` | `string` | Required | - |
| `region` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "line1": "line12",
  "line2": "line24",
  "postcode": "postcode4",
  "locality": "locality0",
  "country": "country4",
  "region": "region6"
}
```

#### Address Update

##### Class Name

`AddressUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `line_1` | `string` | Required | - |
| `line_2` | `string` | Optional | - |
| `postcode` | `string` | Required | - |
| `locality` | `string` | Required | - |
| `country` | `string` | Required | - |
| `region` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "line1": "line12",
  "line2": null,
  "postcode": "postcode4",
  "locality": "locality0",
  "country": "country4",
  "region": null
}
```

#### Allocation by Asset

##### Class Name

`AllocationByAsset`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category_code` | `string` | Required | - |
| `display_allocation_chart` | `bool` | Required | - |
| `display_allocation_chart_configuration_error` | `bool` | Required | - |
| `allocations_by_code` | [`List of AllocationByCode`](#allocation-by-code) | Required | - |

##### Example (as JSON)

```json
{
  "category_code": "category_code8",
  "display_allocation_chart": false,
  "display_allocation_chart_configuration_error": false,
  "allocations_by_code": [
    {
      "code": "code5",
      "name": "name7",
      "balance": 90.81,
      "weight": 128.53
    },
    {
      "code": "code6",
      "name": "name8",
      "balance": 90.82,
      "weight": 128.54
    },
    {
      "code": "code7",
      "name": "name9",
      "balance": 90.83,
      "weight": 128.55
    }
  ]
}
```

#### Allocation by Code

##### Class Name

`AllocationByCode`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Required | - |
| `name` | `string` | Required | - |
| `balance` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `weight` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |

##### Example (as JSON)

```json
{
  "code": "code8",
  "name": "name0",
  "balance": 26.24,
  "weight": 192.04
}
```

#### Allocation Detail

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`AllocationDetail`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `valuation_date` | `date` | Required | - |
| `balance` | `float` | Optional | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `invested` | `float` | Optional | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `earnings` | `float` | Optional | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `cash_active` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `trade_total` | `float` | Optional | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `performance` | `float` | Required | - |
| `positions` | `List of string` | Required | - |

##### Example (as JSON)

```json
{
  "valuation_date": "2016-03-13",
  "balance": null,
  "invested": null,
  "earnings": null,
  "cash_active": 78.52,
  "trade_total": null,
  "performance": 234.24,
  "positions": [
    "positions2"
  ]
}
```

#### Allocation List

##### Class Name

`AllocationList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `valuation_date` | `date` | Required | - |
| `balance` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `invested` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `earnings` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `cash_active` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `trade_total` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `performance` | `float` | Required | - |

##### Example (as JSON)

```json
{
  "valuation_date": "2016-03-13",
  "balance": 26.24,
  "invested": 192.52,
  "earnings": 67.32,
  "cash_active": 78.52,
  "trade_total": 45.56,
  "performance": 234.24
}
```

#### App Version

##### Class Name

`AppVersion`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `int` | Required | **Constraints**: `>= 0`, `<= 2147483647` |

##### Example (as JSON)

```json
{
  "number": 158
}
```

#### Application Client Update

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`ApplicationClientUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Required | - |
| `birthdate` | `date` | Optional | - |
| `tos_consent` | `bool` | Optional | - |
| `marketing_consent` | `bool` | Optional | - |
| `data_consent` | `bool` | Optional | - |
| `tos_consent_date` | `date` | Required | - |
| `tax_information` | `List of string` | Required | - |
| `country_birth` | [`CountryField`](#country-field) | Required | - |
| `last_login` | `datetime` | Required | - |
| `referred_by` | `string` | Optional | - |
| `successful_referrals` | `int` | Required | - |
| `kyc_verified` | `bool` | Required | - |
| `is_verified` | `bool` | Required | - |
| `fee_segments` | `List of string` | Required | - |
| `extra_data` | `dict` | Optional | - |
| `portfolios` | `List of string` | Required | - |
| `onboarded_by` | `string` | Optional | - |
| `risk_level` | `int` | Required | - |
| `onboarding_token` | `string` | Required | - |
| `password` | `string` | Optional | - |
| `email_verified_last_request` | `datetime` | Optional | - |
| `uuid` | `uuid\|string` | Required | - |
| `created` | `datetime` | Required | - |
| `updated` | `datetime` | Required | - |
| `comments` | `string` | Optional | - |
| `status` | [`StatusB65Enum`](#status-b65-enum) | Required | - |
| `email_verified` | `bool` | Optional | - |
| `email_verify_last_request` | `datetime` | Optional | - |
| `title` | [`TitleEnum`](#title-enum) | Optional | - |
| `first_name` | `string` | Optional | - |
| `middle_name` | `string` | Optional | - |
| `last_name` | `string` | Optional | - |
| `gender` | [`GenderEnum`](#gender-enum) | Optional | - |
| `marital_status` | [`MaritalStatusEnum`](#marital-status-enum) | Optional | - |
| `phone_number` | `string` | Optional | - |
| `phone_number_verified` | `datetime` | Optional | - |
| `language` | `string` | Required | **Constraints**: *Maximum Length*: `5` |
| `employment_status` | [`EmploymentStatusEnum`](#employment-status-enum) | Optional | - |
| `profession` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `referral_code` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `activated` | `datetime` | Optional | - |
| `utm_source` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_medium` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_campaign` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_term` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_content` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `marketing_consent_date` | `date` | Required | - |
| `data_consent_date` | `date` | Required | - |

##### Example (as JSON)

```json
{
  "email": "email6",
  "birthdate": null,
  "tos_consent": null,
  "marketing_consent": null,
  "data_consent": null,
  "tos_consent_date": "2016-03-13",
  "tax_information": [
    "tax_information9",
    "tax_information0"
  ],
  "country_birth": {
    "id": 58,
    "code": "code4",
    "iso3": "iso34",
    "name": "name6",
    "name_en_gb": null,
    "name_en_ch": null,
    "name_fr_ch": null,
    "long_name": "long_name6",
    "long_name_en_gb": null,
    "long_name_en_ch": null,
    "long_name_fr_ch": null,
    "eea_country": null
  },
  "last_login": "2016-03-13T12:52:32.123Z",
  "referred_by": null,
  "successful_referrals": 180,
  "kyc_verified": false,
  "is_verified": false,
  "fee_segments": [
    "fee_segments8",
    "fee_segments9",
    "fee_segments0"
  ],
  "extra_data": null,
  "portfolios": [
    "portfolios4"
  ],
  "onboarded_by": null,
  "risk_level": 66,
  "onboarding_token": "onboarding_token4",
  "password": null,
  "email_verified_last_request": null,
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "created": "2016-03-13T12:52:32.123Z",
  "updated": "2016-03-13T12:52:32.123Z",
  "comments": null,
  "status": "ACTIVE",
  "email_verified": null,
  "email_verify_last_request": null,
  "title": null,
  "first_name": null,
  "middle_name": null,
  "last_name": null,
  "gender": null,
  "marital_status": null,
  "phone_number": null,
  "phone_number_verified": null,
  "language": "language2",
  "employment_status": null,
  "profession": null,
  "referral_code": null,
  "activated": null,
  "utm_source": null,
  "utm_medium": null,
  "utm_campaign": null,
  "utm_term": null,
  "utm_content": null,
  "marketing_consent_date": "2016-03-13",
  "data_consent_date": "2016-03-13"
}
```

#### Assessment

##### Class Name

`Assessment`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `completed` | `datetime` | Optional | - |
| `choices` | [`List of RiskChoiceQuestionCode`](#risk-choice-question-code) | Required | - |
| `status` | [`AssessmentStatusEnum`](#assessment-status-enum) | Optional | - |
| `risk_level` | `int` | Required | - |
| `created` | `datetime` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "completed": null,
  "choices": [
    {
      "code": "code5",
      "order": null,
      "description": null,
      "created": "2016-03-13T12:52:32.123Z",
      "question_code": "question_code3"
    },
    {
      "code": "code6",
      "order": null,
      "description": null,
      "created": "2016-03-13T12:52:32.123Z",
      "question_code": "question_code4"
    }
  ],
  "status": null,
  "risk_level": 66,
  "created": "2016-03-13T12:52:32.123Z"
}
```

#### Asset Category

##### Class Name

`AssetCategory`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `150` |
| `code` | `string` | Required | **Constraints**: *Maximum Length*: `50` |
| `order` | `int` | Required | **Constraints**: `>= 0`, `<= 32767` |
| `mtype` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "name": "name0",
  "code": "code8",
  "order": 32,
  "type": "type0"
}
```

#### Asset Concentration Risk

##### Class Name

`AssetConcentrationRisk`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | - |
| `asset_class` | `string` | Required | - |
| `uuid` | `string` | Required | - |
| `value` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `weight` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |

##### Example (as JSON)

```json
{
  "name": "name0",
  "asset_class": "asset_class8",
  "uuid": "uuid6",
  "value": 251.52,
  "weight": 192.04
}
```

#### Asset Detail

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`AssetDetail`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `250` |
| `isin` | `string` | Required | **Constraints**: *Maximum Length*: `120` |
| `ticker` | `string` | Required | **Constraints**: *Maximum Length*: `120` |
| `status` | [`Status6f6Enum`](#status-6-f-6-enum) | Optional | - |
| `market` | `string` | Required | - |
| `currency` | `string` | Required | - |
| `extra_data` | `dict` | Optional | - |
| `categories` | [`List of AssetCategory`](#asset-category) | Required | - |
| `asset_type` | [`AssetTypeEnum`](#asset-type-enum) | Optional | - |
| `expense_ratio` | `float` | Optional | This field determines the administrative and operational costs associated to certain types of assets like ETFs or mutual funds. |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "name": "name0",
  "isin": "isin0",
  "ticker": "ticker2",
  "status": null,
  "market": "market0",
  "currency": "currency0",
  "extra_data": null,
  "categories": [
    {
      "uuid": "00000bae-0000-0000-0000-000000000000",
      "name": "name4",
      "code": "code2",
      "order": 208,
      "type": "type6"
    },
    {
      "uuid": "00000baf-0000-0000-0000-000000000000",
      "name": "name5",
      "code": "code3",
      "order": 207,
      "type": "type5"
    },
    {
      "uuid": "00000bb0-0000-0000-0000-000000000000",
      "name": "name6",
      "code": "code4",
      "order": 206,
      "type": "type4"
    }
  ],
  "asset_type": null,
  "expense_ratio": null
}
```

#### Asset Growth

##### Class Name

`AssetGrowth`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `year` | `int` | Required | - |
| `amount` | `float` | Required | **Constraints**: `>= -1000`, `<= 1000` |

##### Example (as JSON)

```json
{
  "year": 248,
  "amount": 56.78
}
```

#### Asset List

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`AssetList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `name` | `string` | Required | - |
| `isin` | `string` | Required | - |
| `ticker` | `string` | Required | - |
| `status` | [`Status6f6Enum`](#status-6-f-6-enum) | Required | - |
| `market` | `string` | Required | - |
| `currency` | `string` | Required | - |
| `extra_data` | `dict` | Required | - |
| `categories` | [`List of AssetCategory`](#asset-category) | Required | - |
| `asset_type` | [`AssetTypeEnum`](#asset-type-enum) | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "name": "name0",
  "isin": "isin0",
  "ticker": "ticker2",
  "status": "DELETED",
  "market": "market0",
  "currency": "currency0",
  "extra_data": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    },
    "key1": {
      "key1": "val1",
      "key2": "val2"
    },
    "key2": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "categories": [
    {
      "uuid": "00000bae-0000-0000-0000-000000000000",
      "name": "name4",
      "code": "code2",
      "order": 208,
      "type": "type6"
    },
    {
      "uuid": "00000baf-0000-0000-0000-000000000000",
      "name": "name5",
      "code": "code3",
      "order": 207,
      "type": "type5"
    },
    {
      "uuid": "00000bb0-0000-0000-0000-000000000000",
      "name": "name6",
      "code": "code4",
      "order": 206,
      "type": "type4"
    }
  ],
  "asset_type": "MUTUAL_FUND"
}
```

#### Asset Model Portfolio

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`AssetModelPortfolio`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset` | [`RelatedAssetSerializerWithAssetCategories`](#related-asset-serializer-with-asset-categories) | Required | Allow get asset by multiple params or UUID |
| `weight` | `float` | Required | **Constraints**: `>= 0`, `<= 1` |

##### Example (as JSON)

```json
{
  "asset": {
    "uuid": "000010be-0000-0000-0000-000000000000",
    "market": null,
    "isin": "isin0",
    "currency": null,
    "ticker": "ticker2",
    "name": "name0",
    "extra_data": null,
    "categories": [
      "categories2",
      "categories1"
    ]
  },
  "weight": 192.04
}
```

#### Attachment

##### Class Name

`Attachment`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attachment_extension` | `string` | Required | - |
| `attachment_filename` | `string` | Required | - |
| `uuid` | `uuid\|string` | Required | - |

##### Example (as JSON)

```json
{
  "attachment_extension": "attachment_extension4",
  "attachment_filename": "attachment_filename4",
  "uuid": "00000f7e-0000-0000-0000-000000000000"
}
```

#### Authentication Response

##### Class Name

`AuthenticationResponse`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `string` | Optional | **Default**: `'ok'`<br>*Default: `'ok'`* |
| `error` | `string` | Optional | - |
| `id` | `string` | Required | - |
| `email` | `string` | Required | - |
| `session_token` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "status": null,
  "error": null,
  "id": "id0",
  "email": "email6",
  "session_token": "session_token0"
}
```

#### Bank Account Create Update

##### Class Name

`BankAccountCreateUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `account_number` | `string` | Optional | **Constraints**: *Maximum Length*: `30` |
| `account_sort_code` | `string` | Optional | **Constraints**: *Maximum Length*: `6` |
| `account_holder_name` | `string` | Optional | - |
| `joint` | `bool` | Optional | - |
| `bank_name` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `iban` | `string` | Optional | **Constraints**: *Maximum Length*: `34` |
| `swift_code` | `string` | Optional | **Constraints**: *Maximum Length*: `11` |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "account_number": null,
  "account_sort_code": null,
  "account_holder_name": null,
  "joint": null,
  "bank_name": null,
  "iban": null,
  "swift_code": null
}
```

#### Bank Account List

##### Class Name

`BankAccountList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `account_number` | `string` | Required | - |
| `account_sort_code` | `string` | Required | - |
| `account_holder_name` | `string` | Required | - |
| `joint` | `bool` | Required | - |
| `bank_name` | `string` | Required | - |
| `iban` | `string` | Required | - |
| `swift_code` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "account_number": "account_number0",
  "account_sort_code": "account_sort_code8",
  "account_holder_name": "account_holder_name0",
  "joint": false,
  "bank_name": "bank_name4",
  "iban": "iban4",
  "swift_code": "swift_code0"
}
```

#### Base Portfolio Type Restrictions

##### Class Name

`BasePortfolioTypeRestrictions`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `string` | Required | - |
| `date_from` | `date` | Required | - |
| `date_to` | `date` | Required | - |
| `clean_value` | `float` | Required | - |

##### Example (as JSON)

```json
{
  "key": "key0",
  "date_from": "2016-03-13",
  "date_to": "2016-03-13",
  "clean_value": 56.22
}
```

#### Category

##### Class Name

`Category`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `code` | `string` | Required | - |
| `categories` | [`List of AssetCategory`](#asset-category) | Required | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `120` |
| `status` | [`CategoryStatusEnum`](#category-status-enum) | Optional | - |
| `extra_data` | `dict` | Optional | Additional ETSCategory attributes |
| `description` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "code": "code8",
  "categories": [
    {
      "uuid": "00000bae-0000-0000-0000-000000000000",
      "name": "name4",
      "code": "code2",
      "order": 208,
      "type": "type6"
    },
    {
      "uuid": "00000baf-0000-0000-0000-000000000000",
      "name": "name5",
      "code": "code3",
      "order": 207,
      "type": "type5"
    },
    {
      "uuid": "00000bb0-0000-0000-0000-000000000000",
      "name": "name6",
      "code": "code4",
      "order": 206,
      "type": "type4"
    }
  ],
  "name": "name0",
  "status": null,
  "extra_data": null,
  "description": null
}
```

#### Client Create

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`ClientCreate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Required | - |
| `birthdate` | `date` | Optional | - |
| `title` | [`TitleEnum`](#title-enum) | Optional | - |
| `first_name` | `string` | Optional | - |
| `last_name` | `string` | Optional | - |
| `middle_name` | `string` | Optional | - |
| `gender` | [`GenderEnum`](#gender-enum) | Optional | - |
| `marital_status` | [`MaritalStatusEnum`](#marital-status-enum) | Optional | - |
| `language` | `string` | Optional | **Constraints**: *Maximum Length*: `5` |
| `employment_status` | [`EmploymentStatusEnum`](#employment-status-enum) | Optional | - |
| `activated` | `datetime` | Optional | - |
| `profile` | `dict` | Optional | - |
| `password` | `string` | Optional | - |
| `referral_code` | `string` | Optional | - |
| `utm_source` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_medium` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_campaign` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_term` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_content` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `tos_consent` | `bool` | Optional | - |
| `data_consent` | `bool` | Optional | - |
| `marketing_consent` | `bool` | Optional | - |
| `extra_data` | `dict` | Optional | - |
| `phone_number` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "email": "email6",
  "birthdate": null,
  "title": null,
  "first_name": null,
  "last_name": null,
  "middle_name": null,
  "gender": null,
  "marital_status": null,
  "language": null,
  "employment_status": null,
  "activated": null,
  "profile": null,
  "password": null,
  "referral_code": null,
  "utm_source": null,
  "utm_medium": null,
  "utm_campaign": null,
  "utm_term": null,
  "utm_content": null,
  "tos_consent": null,
  "data_consent": null,
  "marketing_consent": null,
  "extra_data": null,
  "phone_number": null
}
```

#### Client Detail

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`ClientDetail`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Required | - |
| `birthdate` | `date` | Optional | - |
| `tos_consent` | `bool` | Required | - |
| `marketing_consent` | `bool` | Required | - |
| `data_consent` | `bool` | Required | - |
| `tos_consent_date` | `date` | Required | - |
| `tax_information` | `List of string` | Required | - |
| `country_birth` | [`CountryField`](#country-field) | Required | - |
| `last_login` | `datetime` | Required | - |
| `referred_by` | `string` | Optional | - |
| `successful_referrals` | `int` | Required | - |
| `kyc_verified` | `bool` | Required | - |
| `is_verified` | `bool` | Required | - |
| `fee_segments` | `List of string` | Required | - |
| `extra_data` | `dict` | Required | - |
| `portfolios` | `List of string` | Required | - |
| `onboarded_by` | `string` | Optional | - |
| `risk_level` | `int` | Required | - |
| `onboarding_token` | `string` | Required | - |
| `uuid` | `uuid\|string` | Required | - |
| `created` | `datetime` | Required | - |
| `updated` | `datetime` | Required | - |
| `comments` | `string` | Optional | - |
| `status` | [`StatusB65Enum`](#status-b65-enum) | Required | - |
| `email_verified` | `bool` | Optional | - |
| `email_verify_last_request` | `datetime` | Optional | - |
| `title` | [`TitleEnum`](#title-enum) | Optional | - |
| `first_name` | `string` | Optional | - |
| `middle_name` | `string` | Optional | - |
| `last_name` | `string` | Optional | - |
| `gender` | [`GenderEnum`](#gender-enum) | Optional | - |
| `marital_status` | [`MaritalStatusEnum`](#marital-status-enum) | Optional | - |
| `phone_number` | `string` | Optional | - |
| `phone_number_verified` | `datetime` | Optional | - |
| `language` | `string` | Required | **Constraints**: *Maximum Length*: `5` |
| `employment_status` | [`EmploymentStatusEnum`](#employment-status-enum) | Optional | - |
| `profession` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `referral_code` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `activated` | `datetime` | Optional | - |
| `utm_source` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_medium` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_campaign` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_term` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_content` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `marketing_consent_date` | `date` | Required | - |
| `data_consent_date` | `date` | Required | - |

##### Example (as JSON)

```json
{
  "email": "email6",
  "birthdate": null,
  "tos_consent": false,
  "marketing_consent": false,
  "data_consent": false,
  "tos_consent_date": "2016-03-13",
  "tax_information": [
    "tax_information9",
    "tax_information0"
  ],
  "country_birth": {
    "id": 58,
    "code": "code4",
    "iso3": "iso34",
    "name": "name6",
    "name_en_gb": null,
    "name_en_ch": null,
    "name_fr_ch": null,
    "long_name": "long_name6",
    "long_name_en_gb": null,
    "long_name_en_ch": null,
    "long_name_fr_ch": null,
    "eea_country": null
  },
  "last_login": "2016-03-13T12:52:32.123Z",
  "referred_by": null,
  "successful_referrals": 180,
  "kyc_verified": false,
  "is_verified": false,
  "fee_segments": [
    "fee_segments8",
    "fee_segments9",
    "fee_segments0"
  ],
  "extra_data": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    },
    "key1": {
      "key1": "val1",
      "key2": "val2"
    },
    "key2": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "portfolios": [
    "portfolios4"
  ],
  "onboarded_by": null,
  "risk_level": 66,
  "onboarding_token": "onboarding_token4",
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "created": "2016-03-13T12:52:32.123Z",
  "updated": "2016-03-13T12:52:32.123Z",
  "comments": null,
  "status": "ACTIVE",
  "email_verified": null,
  "email_verify_last_request": null,
  "title": null,
  "first_name": null,
  "middle_name": null,
  "last_name": null,
  "gender": null,
  "marital_status": null,
  "phone_number": null,
  "phone_number_verified": null,
  "language": "language2",
  "employment_status": null,
  "profession": null,
  "referral_code": null,
  "activated": null,
  "utm_source": null,
  "utm_medium": null,
  "utm_campaign": null,
  "utm_term": null,
  "utm_content": null,
  "marketing_consent_date": "2016-03-13",
  "data_consent_date": "2016-03-13"
}
```

#### Client Embed Ranking

##### Class Name

`ClientEmbedRanking`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `full_name` | `string` | Required | - |
| `balance` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `earnings` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `mwrr` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `twrr` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "full_name": "full_name6",
  "balance": 26.24,
  "earnings": 67.32,
  "mwrr": 75.74,
  "twrr": 169.02
}
```

#### Client Performance

##### Class Name

`ClientPerformance`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `valuation_date` | `date` | Required | - |
| `performance` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |

##### Example (as JSON)

```json
{
  "valuation_date": "2016-03-13",
  "performance": 234.24
}
```

#### Client Ranking

##### Class Name

`ClientRanking`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `top_performing` | [`List of ClientEmbedRanking`](#client-embed-ranking) | Required | - |
| `bottom_performing` | [`List of ClientEmbedRanking`](#client-embed-ranking) | Required | - |

##### Example (as JSON)

```json
{
  "top_performing": [
    {
      "uuid": "00001b28-0000-0000-0000-000000000000",
      "full_name": "full_name2",
      "balance": 56.1,
      "earnings": 97.18,
      "mwrr": 45.88,
      "twrr": 139.16
    },
    {
      "uuid": "00001b29-0000-0000-0000-000000000000",
      "full_name": "full_name3",
      "balance": 56.11,
      "earnings": 97.19,
      "mwrr": 45.87,
      "twrr": 139.15
    },
    {
      "uuid": "00001b2a-0000-0000-0000-000000000000",
      "full_name": "full_name4",
      "balance": 56.12,
      "earnings": 97.2,
      "mwrr": 45.86,
      "twrr": 139.14
    }
  ],
  "bottom_performing": [
    {
      "uuid": "00000a11-0000-0000-0000-000000000000",
      "full_name": "full_name7",
      "balance": 144.35,
      "earnings": 185.43,
      "mwrr": 42.37,
      "twrr": 205.09
    },
    {
      "uuid": "00000a12-0000-0000-0000-000000000000",
      "full_name": "full_name8",
      "balance": 144.36,
      "earnings": 185.44,
      "mwrr": 42.38,
      "twrr": 205.1
    }
  ]
}
```

#### Client Referral

##### Class Name

`ClientReferral`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `string` | Required | - |
| `last_name` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "first_name": "first_name0",
  "last_name": "last_name8"
}
```

#### Conversation Create

##### Class Name

`ConversationCreate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `portal` | `int` | Required | - |
| `created` | `datetime` | Required | - |
| `subject` | `string` | Required | **Constraints**: *Maximum Length*: `80` |
| `messages` | [`Message`](#message) | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "portal": 4,
  "created": "2016-03-13T12:52:32.123Z",
  "subject": "subject6",
  "messages": null
}
```

#### Conversation List

##### Class Name

`ConversationList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `created` | `datetime` | Required | - |
| `subject` | `string` | Required | - |
| `last_message` | [`Message`](#message) | Required | - |
| `unreads` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "created": "2016-03-13T12:52:32.123Z",
  "subject": "subject6",
  "last_message": {
    "user": "user4",
    "read_date": "2016-03-13T12:52:32.123Z",
    "content": null,
    "created": "2016-03-13T12:52:32.123Z",
    "attachments": [
      {
        "attachment_extension": "attachment_extension0",
        "attachment_filename": "attachment_filename0",
        "uuid": "00000fa0-0000-0000-0000-000000000000"
      }
    ],
    "uuid": "00001c52-0000-0000-0000-000000000000"
  },
  "unreads": 156
}
```

#### Core Category Group

##### Class Name

`CoreCategoryGroup`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `code` | `string` | Required | - |
| `risk_level` | `int` | Required | **Constraints**: `>= 0`, `<= 32767` |
| `categories` | [`List of Category`](#category) | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "code": "code8",
  "risk_level": 66,
  "categories": [
    {
      "uuid": "00000bae-0000-0000-0000-000000000000",
      "code": "code2",
      "categories": [
        {
          "uuid": "00000f7e-0000-0000-0000-000000000000",
          "name": "name0",
          "code": "code8",
          "order": 32,
          "type": "type0"
        },
        {
          "uuid": "00000f7f-0000-0000-0000-000000000000",
          "name": "name1",
          "code": "code9",
          "order": 31,
          "type": "type9"
        }
      ],
      "name": "name4",
      "status": null,
      "extra_data": null,
      "description": null
    },
    {
      "uuid": "00000baf-0000-0000-0000-000000000000",
      "code": "code3",
      "categories": [
        {
          "uuid": "00000f7f-0000-0000-0000-000000000000",
          "name": "name1",
          "code": "code9",
          "order": 31,
          "type": "type9"
        }
      ],
      "name": "name5",
      "status": null,
      "extra_data": null,
      "description": null
    },
    {
      "uuid": "00000bb0-0000-0000-0000-000000000000",
      "code": "code4",
      "categories": [
        {
          "uuid": "00000f80-0000-0000-0000-000000000000",
          "name": "name2",
          "code": "code0",
          "order": 30,
          "type": "type8"
        },
        {
          "uuid": "00000f7f-0000-0000-0000-000000000000",
          "name": "name1",
          "code": "code9",
          "order": 31,
          "type": "type9"
        },
        {
          "uuid": "00000f7e-0000-0000-0000-000000000000",
          "name": "name0",
          "code": "code8",
          "order": 32,
          "type": "type0"
        }
      ],
      "name": "name6",
      "status": null,
      "extra_data": null,
      "description": null
    }
  ]
}
```

#### Country Field

##### Class Name

`CountryField`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `code` | `string` | Required | **Constraints**: *Maximum Length*: `2` |
| `iso_3` | `string` | Required | **Constraints**: *Maximum Length*: `3` |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `150` |
| `name_en_gb` | `string` | Optional | **Constraints**: *Maximum Length*: `150` |
| `name_en_ch` | `string` | Optional | **Constraints**: *Maximum Length*: `150` |
| `name_fr_ch` | `string` | Optional | **Constraints**: *Maximum Length*: `150` |
| `long_name` | `string` | Required | **Constraints**: *Maximum Length*: `250` |
| `long_name_en_gb` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `long_name_en_ch` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `long_name_fr_ch` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `eea_country` | `bool` | Optional | - |

##### Example (as JSON)

```json
{
  "id": 112,
  "code": "code8",
  "iso3": "iso38",
  "name": "name0",
  "name_en_gb": null,
  "name_en_ch": null,
  "name_fr_ch": null,
  "long_name": "long_name2",
  "long_name_en_gb": null,
  "long_name_en_ch": null,
  "long_name_fr_ch": null,
  "eea_country": null
}
```

#### Country List

##### Class Name

`CountryList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Required | - |
| `iso_3` | `string` | Required | - |
| `name` | `string` | Required | - |
| `long_name` | `string` | Required | - |
| `eea_country` | `bool` | Required | - |

##### Example (as JSON)

```json
{
  "code": "code8",
  "iso3": "iso38",
  "name": "name0",
  "long_name": "long_name2",
  "eea_country": false
}
```

#### Create Order

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`CreateOrder`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `shares` | `int` | Required | **Constraints**: `>= 1` |
| `asset` | [`RelatedAssetSerializerWithAssetCategories`](#related-asset-serializer-with-asset-categories) | Required | Allow get asset by multiple params or UUID |
| `portfolio` | `string` | Optional | - |
| `order_type` | [`OrderTypeEnum`](#order-type-enum) | Required | - |
| `method` | [`CreateOrderMethodEnum`](#create-order-method-enum) | Required | - |
| `limit_price` | `float` | Optional | **Constraints**: `>= 0.01`, `<= 1000000000000` |
| `stop_price` | `float` | Optional | **Constraints**: `>= 0.01`, `<= 1000000000000` |
| `duration` | [`DurationEnum`](#duration-enum) | Optional | - |

##### Example (as JSON)

```json
{
  "shares": 214,
  "asset": {
    "uuid": "000010be-0000-0000-0000-000000000000",
    "market": null,
    "isin": "isin0",
    "currency": null,
    "ticker": "ticker2",
    "name": "name0",
    "extra_data": null,
    "categories": [
      "categories2",
      "categories1"
    ]
  },
  "portfolio": null,
  "order_type": "VERIFICATION",
  "method": "LIMIT",
  "limit_price": null,
  "stop_price": null,
  "duration": null
}
```

#### Currency

##### Class Name

`Currency`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Required | - |
| `name` | `string` | Required | - |
| `symbol` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "code": "code8",
  "name": "name0",
  "symbol": "symbol8"
}
```

#### Current Allocation

##### Class Name

`CurrentAllocation`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cash_active` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `balance` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `invested` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `earnings` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `positions` | [`List of Position`](#position) | Required | - |
| `valuation_datetime` | `datetime` | Required | - |
| `performance` | `float` | Optional | **Default**: `0`<br>**Constraints**: `>= -1000000000000`, `<= 1000000000000`<br>*Default: `0`* |
| `trade_total` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `cash_available` | `float` | Required | - |

##### Example (as JSON)

```json
{
  "cash_active": 78.52,
  "balance": 26.24,
  "invested": 192.52,
  "earnings": 67.32,
  "positions": [
    {
      "asset": {
        "uuid": "00000df0-0000-0000-0000-000000000000",
        "market": null,
        "isin": "isin2",
        "currency": null,
        "ticker": "ticker4",
        "name": "name2",
        "extra_data": null,
        "categories": [
          "categories0",
          "categories1"
        ]
      },
      "shares": 195.76,
      "price": 229.3,
      "value": 176.34,
      "weight": 244.78,
      "fx_rate_account": 126.1,
      "asset_currency_value": 234.9
    }
  ],
  "valuation_datetime": "2016-03-13T12:52:32.123Z",
  "performance": null,
  "trade_total": 45.56,
  "cash_available": 34.64
}
```

#### Deposit Create

##### Class Name

`DepositCreate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `amount` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `provider` | `string` | Required | - |
| `reference` | `string` | Required | - |
| `status` | [`StatusB6aEnum`](#status-b6-a-enum) | Required | - |
| `reason` | `string` | Required | Cancelled reason |
| `completed` | `datetime` | Required | - |
| `deposit_type` | [`DepositTypeEnum`](#deposit-type-enum) | Optional | - |
| `transacted_at` | `datetime` | Required | - |
| `extra_data` | `dict` | Optional | Additional deposit attributes for the specific portal |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "amount": 56.78,
  "provider": "provider8",
  "reference": "reference4",
  "status": "PROCESSING",
  "reason": "reason4",
  "completed": "2016-03-13T12:52:32.123Z",
  "deposit_type": null,
  "transacted_at": "2016-03-13T12:52:32.123Z",
  "extra_data": null
}
```

#### Deposit Detail

##### Class Name

`DepositDetail`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `portfolio` | `string` | Required | - |
| `amount` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `provider` | `string` | Required | - |
| `reference` | `string` | Required | - |
| `status` | [`StatusB6aEnum`](#status-b6-a-enum) | Optional | - |
| `reason` | `string` | Optional | Cancelled reason<br>**Constraints**: *Maximum Length*: `250` |
| `completed` | `datetime` | Optional | - |
| `deposit_type` | [`DepositTypeEnum`](#deposit-type-enum) | Optional | - |
| `transacted_at` | `datetime` | Optional | - |
| `extra_data` | `dict` | Optional | Additional deposit attributes for the specific portal |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "portfolio": "portfolio4",
  "amount": 56.78,
  "provider": "provider8",
  "reference": "reference4",
  "status": null,
  "reason": null,
  "completed": null,
  "deposit_type": null,
  "transacted_at": null,
  "extra_data": null
}
```

#### Deposit List

##### Class Name

`DepositList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `amount` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `reference` | `string` | Required | - |
| `status` | [`StatusB6aEnum`](#status-b6-a-enum) | Required | - |
| `deposit_type` | [`DepositTypeEnum`](#deposit-type-enum) | Required | - |
| `completed` | `datetime` | Required | - |
| `transacted_at` | `datetime` | Required | - |
| `extra_data` | `dict` | Required | Additional deposit attributes for the specific portal |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "amount": 56.78,
  "reference": "reference4",
  "status": "PROCESSING",
  "deposit_type": "CONTRIBUTION",
  "completed": "2016-03-13T12:52:32.123Z",
  "transacted_at": "2016-03-13T12:52:32.123Z",
  "extra_data": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    },
    "key1": {
      "key1": "val1",
      "key2": "val2"
    },
    "key2": {
      "key1": "val1",
      "key2": "val2"
    }
  }
}
```

#### Document

##### Class Name

`Document`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `name` | `string` | Required | - |
| `doc_type` | [`DocTypeEnum`](#doc-type-enum) | Required | - |
| `description` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `path` | `string` | Required | - |
| `extra_data` | `dict` | Optional | Additional document attributes for the specific portal |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "name": "name0",
  "doc_type": "ID_PERSONAL",
  "description": null,
  "path": "path6",
  "extra_data": null
}
```

#### ETS Forecast Request

##### Class Name

`ETSForecastRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time_horizon` | `int` | Required | **Constraints**: `>= 1`, `<= 50` |
| `initial_amount` | `float` | Required | **Constraints**: `>= 1`, `<= 1000000000000` |
| `recurring_amount` | `float` | Optional | **Constraints**: `>= 0`, `<= 1000000000000` |
| `recurring_period` | `int` | Optional | **Constraints**: `>= 0`, `<= 12` |
| `risk_level` | `int` | Required | **Constraints**: `>= 1`, `<= 10` |
| `favourite_categories` | `List of string` | Optional | - |
| `excluded_categories` | `List of string` | Optional | - |

##### Example (as JSON)

```json
{
  "time_horizon": 200,
  "initial_amount": 140.36,
  "recurring_amount": null,
  "recurring_period": null,
  "risk_level": 66,
  "favourite_categories": null,
  "excluded_categories": null
}
```

#### Email Verify Request

##### Class Name

`EmailVerifyRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "email": null
}
```

#### Email Verify View

##### Class Name

`EmailVerifyView`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `token` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "token": "token6"
}
```

#### Feed Activity List

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`FeedActivityList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `created` | `datetime` | Required | - |
| `activity_type` | [`ActivityTypeEnum`](#activity-type-enum) | Required | - |
| `activity_data` | `dict` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "created": "2016-03-13T12:52:32.123Z",
  "activity_type": "DELETED",
  "activity_data": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    }
  }
}
```

#### Forecast Decumulation Request

##### Class Name

`ForecastDecumulationRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `initial_amount` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `recurring_amount` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `risk_level` | `int` | Required | - |
| `withdrawal_amount` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `retirement_age` | `int` | Required | **Constraints**: `>= 18`, `<= 110` |
| `life_expectancy` | `int` | Optional | **Constraints**: `>= 75`, `<= 110` |

##### Example (as JSON)

```json
{
  "initial_amount": 140.36,
  "recurring_amount": 118.5,
  "risk_level": 66,
  "withdrawal_amount": 38.74,
  "retirement_age": 12,
  "life_expectancy": null
}
```

#### Forecast Request

##### Class Name

`ForecastRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `goal_amount` | `float` | Required | **Constraints**: `>= 1`, `<= 1000000000000` |
| `deadline` | `date` | Required | - |
| `initial_amount` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `recurring_amount` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `risk_level` | `int` | Required | **Constraints**: `>= 1` |

##### Example (as JSON)

```json
{
  "goal_amount": 140.86,
  "deadline": "2016-03-13",
  "initial_amount": 140.36,
  "recurring_amount": 118.5,
  "risk_level": 66
}
```

#### Goal

##### Class Name

`Goal`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `150` |
| `portfolio` | `string` | Optional | - |
| `goal_amount` | `float` | Required | Desired amount needed to fulfill the goal<br>**Constraints**: `>= 0.1`, `<= 1000000000000` |
| `deadline` | `date` | Required | Due date to reach the goal. |
| `initial_amount` | `float` | Required | Initial deposit amount to start from. No sense to start by 0<br>**Constraints**: `>= 0.1`, `<= 1000000000000` |
| `recurring_amount` | `float` | Optional | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `risk_level` | `int` | Required | **Constraints**: `>= 0`, `<= 32767` |
| `created` | `datetime` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "name": "name0",
  "portfolio": null,
  "goal_amount": 140.86,
  "deadline": "2016-03-13",
  "initial_amount": 140.36,
  "recurring_amount": null,
  "risk_level": 66,
  "created": "2016-03-13T12:52:32.123Z"
}
```

#### Impersionation Response

##### Class Name

`ImpersionationResponse`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access` | `string` | Required | - |
| `refresh` | `string` | Required | - |
| `email` | `string` | Required | - |
| `status` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "access": "access2",
  "refresh": "refresh2",
  "email": "email6",
  "status": "status8"
}
```

#### Impersonation Token

##### Class Name

`ImpersonationToken`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `impersonator` | `string` | Required | - |
| `impersonated` | `string` | Required | - |
| `token` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "impersonator": "impersonator2",
  "impersonated": "impersonated4",
  "token": "token6"
}
```

#### Intraday Price

##### Class Name

`IntradayPrice`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `datetime` | `datetime` | Required | - |
| `open_price` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `high_price` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `low_price` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `previous_close_price` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |

##### Example (as JSON)

```json
{
  "amount": 56.78,
  "datetime": "2016-03-13T12:52:32.123Z",
  "open_price": 141.9,
  "high_price": 65.54,
  "low_price": 156.04,
  "previous_close_price": 65.6
}
```

#### Investor Fee

##### Class Name

`InvestorFee`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `float` | Optional | Determinates a percentage or an amount (between 0 and 1 if percentage otherwise Positive Decimal)<br>**Constraints**: `>= 0`, `<= 100` |
| `value_unit` | [`ValueUnitEnum`](#value-unit-enum) | Optional | Determines the type of the value(Fixed, Percentage) |
| `fee_type` | [`FeeTypeEnum`](#fee-type-enum) | Required | Each choice should have a related method on fee model that contains the logic to charge the client |
| `concept` | `string` | Required | Describes the concept that will be shown on invoice<br>**Constraints**: *Maximum Length*: `100` |
| `date_from` | `date` | Optional | Defines the end date when the percentage should be applied |
| `date_to` | `date` | Optional | Defines the start date when the percentage should be applied |
| `amount_from` | `float` | Optional | Defines the amount start range when the percentage should be applied<br>**Constraints**: `>= -1000000000`, `<= 1000000000` |
| `amount_to` | `float` | Optional | Defines the amount end range when the percentage should be applied<br>**Constraints**: `>= -1000000000`, `<= 1000000000` |
| `uuid` | `uuid\|string` | Required | - |
| `created` | `datetime` | Required | - |
| `updated` | `datetime` | Required | - |

##### Example (as JSON)

```json
{
  "value": null,
  "value_unit": null,
  "fee_type": "portal_service",
  "concept": "concept4",
  "date_from": null,
  "date_to": null,
  "amount_from": null,
  "amount_to": null,
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "created": "2016-03-13T12:52:32.123Z",
  "updated": "2016-03-13T12:52:32.123Z"
}
```

#### Investor Model Portfolio

##### Class Name

`InvestorModelPortfolio`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `name` | `string` | Required | - |
| `cash_weight` | `float` | Required | Percentage on the interval 0-1.<br>**Constraints**: `>= -10`, `<= 10` |
| `risk_level` | `int` | Required | - |
| `allocation` | [`List of AssetModelPortfolio`](#asset-model-portfolio) | Required | - |
| `extra_data` | `dict` | Required | Additional ModelPortfolio attributes |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "name": "name0",
  "cash_weight": 120.24,
  "risk_level": 66,
  "allocation": [
    {
      "asset": {
        "uuid": "0000186d-0000-0000-0000-000000000000",
        "market": null,
        "isin": "isin3",
        "currency": null,
        "ticker": "ticker9",
        "name": "name7",
        "extra_data": null,
        "categories": [
          "categories5",
          "categories4"
        ]
      },
      "weight": 72.37
    },
    {
      "asset": {
        "uuid": "0000186e-0000-0000-0000-000000000000",
        "market": null,
        "isin": "isin2",
        "currency": null,
        "ticker": "ticker0",
        "name": "name8",
        "extra_data": null,
        "categories": [
          "categories4",
          "categories3",
          "categories2"
        ]
      },
      "weight": 72.36
    }
  ],
  "extra_data": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    },
    "key1": {
      "key1": "val1",
      "key2": "val2"
    },
    "key2": {
      "key1": "val1",
      "key2": "val2"
    }
  }
}
```

#### Investor Withdrawal Create

##### Class Name

`InvestorWithdrawalCreate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `amount` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `provider` | `string` | Required | - |
| `status` | [`Status14bEnum`](#status-14-b-enum) | Required | - |
| `reason` | `string` | Required | Cancelled reason |
| `completed` | `datetime` | Required | - |
| `purpose` | `string` | Optional | Withdrawal reason<br>**Constraints**: *Maximum Length*: `250` |
| `withdrawal_type` | `string` | Required | - |
| `extra_data` | `dict` | Optional | Additional withdrawal attributes for the specific portal |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "amount": 56.78,
  "provider": "provider8",
  "status": "REQUESTED",
  "reason": "reason4",
  "completed": "2016-03-13T12:52:32.123Z",
  "purpose": null,
  "withdrawal_type": "withdrawal_type4",
  "extra_data": null
}
```

#### Investor Withdrawal List

##### Class Name

`InvestorWithdrawalList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `amount` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `status` | [`Status14bEnum`](#status-14-b-enum) | Required | - |
| `withdrawal_type` | `string` | Required | - |
| `extra_data` | `dict` | Required | Additional withdrawal attributes for the specific portal |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "amount": 56.78,
  "status": "REQUESTED",
  "withdrawal_type": "withdrawal_type4",
  "extra_data": {
    "key0": {
      "key1": "val1",
      "key2": "val2"
    },
    "key1": {
      "key1": "val1",
      "key2": "val2"
    },
    "key2": {
      "key1": "val1",
      "key2": "val2"
    }
  }
}
```

#### Invoice Details

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`InvoiceDetails`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `number` | `string` | Optional | Invoice legal number<br>**Constraints**: *Maximum Length*: `50` |
| `status` | [`Status260Enum`](#status-260-enum) | Optional | - |
| `created` | `datetime` | Required | - |
| `date_from` | `date` | Optional | Beginning of charge period |
| `date_to` | `date` | Optional | End of charge period |
| `url` | `string` | Required | - |
| `amount` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `charges` | `List of string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "number": null,
  "status": null,
  "created": "2016-03-13T12:52:32.123Z",
  "date_from": null,
  "date_to": null,
  "url": "url4",
  "amount": 56.78,
  "charges": [
    "charges8",
    "charges9"
  ]
}
```

#### Invoice List

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`InvoiceList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `number` | `string` | Required | Invoice legal number |
| `status` | [`Status260Enum`](#status-260-enum) | Required | - |
| `date_from` | `date` | Required | Beginning of charge period |
| `date_to` | `date` | Required | End of charge period |
| `amount` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `charges` | `List of string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "number": "number2",
  "status": "PENDING",
  "date_from": "2016-03-13",
  "date_to": "2016-03-13",
  "amount": 56.78,
  "charges": [
    "charges8",
    "charges9"
  ]
}
```

#### JSON Web Token

##### Class Name

`JSONWebToken`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `string` | Required | - |
| `password` | `string` | Required | - |
| `captcha` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "username": "username0",
  "password": "password4",
  "captcha": null
}
```

#### JWT Refresh Response

##### Class Name

`JWTRefreshResponse`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access` | `string` | Required | - |
| `refresh` | `string` | Required | - |
| `status` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "access": "access2",
  "refresh": "refresh2",
  "status": "status8"
}
```

#### JWT Response

##### Class Name

`JWTResponse`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access` | `string` | Required | - |
| `refresh` | `string` | Required | - |
| `status` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "access": "access2",
  "refresh": "refresh2",
  "status": "status8"
}
```

#### Message

##### Class Name

`Message`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user` | `string` | Required | - |
| `read_date` | `datetime` | Required | - |
| `content` | `string` | Optional | - |
| `created` | `datetime` | Required | - |
| `attachments` | [`List of Attachment`](#attachment) | Required | - |
| `uuid` | `uuid\|string` | Required | - |

##### Example (as JSON)

```json
{
  "user": "user0",
  "read_date": "2016-03-13T12:52:32.123Z",
  "content": null,
  "created": "2016-03-13T12:52:32.123Z",
  "attachments": [
    {
      "attachment_extension": "attachment_extension4",
      "attachment_filename": "attachment_filename4",
      "uuid": "000002cc-0000-0000-0000-000000000000"
    },
    {
      "attachment_extension": "attachment_extension3",
      "attachment_filename": "attachment_filename3",
      "uuid": "000002cd-0000-0000-0000-000000000000"
    },
    {
      "attachment_extension": "attachment_extension2",
      "attachment_filename": "attachment_filename2",
      "uuid": "000002ce-0000-0000-0000-000000000000"
    }
  ],
  "uuid": "00000f7e-0000-0000-0000-000000000000"
}
```

#### Minimum App Version

##### Class Name

`MinimumAppVersion`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `required` | [`AppVersion`](#app-version) | Required | - |

##### Example (as JSON)

```json
{
  "required": {
    "number": 186
  }
}
```

#### Model Portfolio Forecast Request

##### Class Name

`ModelPortfolioForecastRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time_horizon` | `int` | Required | **Constraints**: `>= 1`, `<= 50` |
| `initial_amount` | `float` | Required | **Constraints**: `>= 1`, `<= 1000000000000` |
| `recurring_amount` | `float` | Optional | **Constraints**: `>= 0`, `<= 1000000000000` |
| `recurring_period` | `int` | Optional | **Constraints**: `>= 0`, `<= 12` |
| `model_portfolio` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "time_horizon": 200,
  "initial_amount": 140.36,
  "recurring_amount": null,
  "recurring_period": null,
  "model_portfolio": "model_portfolio2"
}
```

#### National Document

##### Class Name

`NationalDocument`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `code` | `string` | Required | **Constraints**: *Maximum Length*: `20` |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `120` |
| `countries` | `List of string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "code": "code8",
  "name": "name0",
  "countries": [
    "countries3",
    "countries4",
    "countries5"
  ]
}
```

#### Nationality Create

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`NationalityCreate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country` | `string` | Required | - |
| `document_number` | `string` | Optional | - |
| `document_type` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "country": "country4",
  "document_number": null,
  "document_type": null
}
```

#### Nationality List

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`NationalityList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `country` | `string` | Required | - |
| `document_type` | `string` | Optional | - |
| `document_number` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "country": "country4",
  "document_type": null,
  "document_number": "document_number6"
}
```

#### Nationality Update

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`NationalityUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country` | `string` | Required | - |
| `document_number` | `string` | Optional | - |
| `document_type` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "country": "country4",
  "document_number": null,
  "document_type": null
}
```

#### Nucoro Setting

##### Class Name

`NucoroSetting`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "key": "key0"
}
```

#### Onboarding Response

##### Class Name

`OnboardingResponse`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access` | `string` | Required | - |
| `refresh` | `string` | Required | - |
| `status` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "access": "access2",
  "refresh": "refresh2",
  "status": "status8"
}
```

#### Onboarding Token

##### Class Name

`OnboardingToken`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Required | - |
| `token` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "email": "email6",
  "token": "token6"
}
```

#### Order List

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`OrderList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset` | [`RelatedAssetSerializerWithAssetCategories`](#related-asset-serializer-with-asset-categories) | Required | - |
| `trade` | `string` | Required | - |
| `order_type` | [`OrderTypeEnum`](#order-type-enum) | Required | - |
| `method` | [`OrderListMethodEnum`](#order-list-method-enum) | Required | - |
| `status` | [`OrderListStatusEnum`](#order-list-status-enum) | Required | - |
| `reason` | `string` | Required | - |
| `completed` | `datetime` | Required | - |
| `rebalance` | `string` | Required | - |
| `portfolio` | `string` | Required | - |
| `shares` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `amount` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `price_avg` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `currency` | [`Currency`](#currency) | Required | - |
| `withdrawal` | `string` | Required | - |
| `created` | `datetime` | Required | - |
| `stop_price` | `float` | Optional | - |
| `limit_price` | `float` | Optional | - |
| `duration` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "asset": {
    "uuid": "000010be-0000-0000-0000-000000000000",
    "market": null,
    "isin": "isin0",
    "currency": null,
    "ticker": "ticker2",
    "name": "name0",
    "extra_data": null,
    "categories": [
      "categories2",
      "categories1"
    ]
  },
  "trade": "trade6",
  "order_type": "VERIFICATION",
  "method": "QUOTE",
  "status": "COMPLETED",
  "reason": "reason4",
  "completed": "2016-03-13T12:52:32.123Z",
  "rebalance": "rebalance8",
  "portfolio": "portfolio4",
  "shares": 14.94,
  "amount": 56.78,
  "price_avg": 3.24,
  "currency": {
    "code": "code8",
    "name": "name0",
    "symbol": "symbol8"
  },
  "withdrawal": "withdrawal6",
  "created": "2016-03-13T12:52:32.123Z",
  "stop_price": null,
  "limit_price": null,
  "duration": "duration6"
}
```

#### Paginated Access Log List

##### Class Name

`PaginatedAccessLogList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of AccessLog`](#access-log) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Address List List

##### Class Name

`PaginatedAddressListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of AddressList`](#address-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Allocation List List

##### Class Name

`PaginatedAllocationListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of AllocationList`](#allocation-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Assessment List

##### Class Name

`PaginatedAssessmentList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of Assessment`](#assessment) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Asset Category List

##### Class Name

`PaginatedAssetCategoryList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of AssetCategory`](#asset-category) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Asset Growth List

##### Class Name

`PaginatedAssetGrowthList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of AssetGrowth`](#asset-growth) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Asset List List

##### Class Name

`PaginatedAssetListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of AssetList`](#asset-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Bank Account List List

##### Class Name

`PaginatedBankAccountListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of BankAccountList`](#bank-account-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Base Portfolio Type Restrictions List

##### Class Name

`PaginatedBasePortfolioTypeRestrictionsList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of BasePortfolioTypeRestrictions`](#base-portfolio-type-restrictions) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Category List

##### Class Name

`PaginatedCategoryList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of Category`](#category) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Client Detail List

##### Class Name

`PaginatedClientDetailList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of ClientDetail`](#client-detail) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Conversation List List

##### Class Name

`PaginatedConversationListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of ConversationList`](#conversation-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Core Category Group List

##### Class Name

`PaginatedCoreCategoryGroupList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of CoreCategoryGroup`](#core-category-group) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Country List List

##### Class Name

`PaginatedCountryListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of CountryList`](#country-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Deposit List List

##### Class Name

`PaginatedDepositListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of DepositList`](#deposit-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Document List

##### Class Name

`PaginatedDocumentList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of Document`](#document) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Feed Activity List List

##### Class Name

`PaginatedFeedActivityListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of FeedActivityList`](#feed-activity-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Goal List

##### Class Name

`PaginatedGoalList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of Goal`](#goal) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Intraday Price List

##### Class Name

`PaginatedIntradayPriceList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of IntradayPrice`](#intraday-price) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Investor Fee List

##### Class Name

`PaginatedInvestorFeeList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of InvestorFee`](#investor-fee) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Investor Model Portfolio List

##### Class Name

`PaginatedInvestorModelPortfolioList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of InvestorModelPortfolio`](#investor-model-portfolio) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Investor Withdrawal List List

##### Class Name

`PaginatedInvestorWithdrawalListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of InvestorWithdrawalList`](#investor-withdrawal-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Invoice List List

##### Class Name

`PaginatedInvoiceListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of InvoiceList`](#invoice-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Message List

##### Class Name

`PaginatedMessageList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of Message`](#message) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated National Document List

##### Class Name

`PaginatedNationalDocumentList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of NationalDocument`](#national-document) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Nationality List List

##### Class Name

`PaginatedNationalityListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of NationalityList`](#nationality-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Order List List

##### Class Name

`PaginatedOrderListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of OrderList`](#order-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Portfolio List List

##### Class Name

`PaginatedPortfolioListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of PortfolioList`](#portfolio-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Portfolio Performance List

##### Class Name

`PaginatedPortfolioPerformanceList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of PortfolioPerformance`](#portfolio-performance) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Portfolio Performance Positions List

##### Class Name

`PaginatedPortfolioPerformancePositionsList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of PortfolioPerformancePositions`](#portfolio-performance-positions) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Portfolio Type List

##### Class Name

`PaginatedPortfolioTypeList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of PortfolioType`](#portfolio-type) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Preset Category Group List

##### Class Name

`PaginatedPresetCategoryGroupList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of PresetCategoryGroup`](#preset-category-group) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Price List

##### Class Name

`PaginatedPriceList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of Price`](#price) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Question List

##### Class Name

`PaginatedQuestionList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of Question`](#question) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Rebalance List

##### Class Name

`PaginatedRebalanceList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of Rebalance`](#rebalance) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Statement List

##### Class Name

`PaginatedStatementList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of Statement`](#statement) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Tax Information List List

##### Class Name

`PaginatedTaxInformationListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of TaxInformationList`](#tax-information-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Tax Report List

##### Class Name

`PaginatedTaxReportList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of TaxReport`](#tax-report) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Tos List

##### Class Name

`PaginatedTosList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of Tos`](#tos) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Verification Document List

##### Class Name

`PaginatedVerificationDocumentList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of VerificationDocument`](#verification-document) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Verification List List

##### Class Name

`PaginatedVerificationListList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of VerificationList`](#verification-list) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Paginated Watchlist List

##### Class Name

`PaginatedWatchlistList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `previous` | `string` | Optional | - |
| `results` | [`List of Watchlist`](#watchlist) | Optional | - |

##### Example (as JSON)

```json
{
  "count": null,
  "next": null,
  "previous": null,
  "results": null
}
```

#### Password Reset

##### Class Name

`PasswordReset`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Required | - |
| `token` | `string` | Required | - |
| `password` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "email": "email6",
  "token": "token6",
  "password": "password4"
}
```

#### Password Reset Request

##### Class Name

`PasswordResetRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "email": "email6"
}
```

#### Password Update

##### Class Name

`PasswordUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `old_password` | `string` | Optional | - |
| `new_password` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "old_password": null,
  "new_password": "new_password6"
}
```

#### Patched Address Update

##### Class Name

`PatchedAddressUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Optional | - |
| `line_1` | `string` | Optional | - |
| `line_2` | `string` | Optional | - |
| `postcode` | `string` | Optional | - |
| `locality` | `string` | Optional | - |
| `country` | `string` | Optional | - |
| `region` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": null,
  "line1": null,
  "line2": null,
  "postcode": null,
  "locality": null,
  "country": null,
  "region": null
}
```

#### Patched Application Client Update

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`PatchedApplicationClientUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Optional | - |
| `birthdate` | `date` | Optional | - |
| `tos_consent` | `bool` | Optional | - |
| `marketing_consent` | `bool` | Optional | - |
| `data_consent` | `bool` | Optional | - |
| `tos_consent_date` | `date` | Optional | - |
| `tax_information` | `List of string` | Optional | - |
| `country_birth` | [`CountryField`](#country-field) | Optional | - |
| `last_login` | `datetime` | Optional | - |
| `referred_by` | `string` | Optional | - |
| `successful_referrals` | `int` | Optional | - |
| `kyc_verified` | `bool` | Optional | - |
| `is_verified` | `bool` | Optional | - |
| `fee_segments` | `List of string` | Optional | - |
| `extra_data` | `dict` | Optional | - |
| `portfolios` | `List of string` | Optional | - |
| `onboarded_by` | `string` | Optional | - |
| `risk_level` | `int` | Optional | - |
| `onboarding_token` | `string` | Optional | - |
| `password` | `string` | Optional | - |
| `email_verified_last_request` | `datetime` | Optional | - |
| `uuid` | `uuid\|string` | Optional | - |
| `created` | `datetime` | Optional | - |
| `updated` | `datetime` | Optional | - |
| `comments` | `string` | Optional | - |
| `status` | [`StatusB65Enum`](#status-b65-enum) | Optional | - |
| `email_verified` | `bool` | Optional | - |
| `email_verify_last_request` | `datetime` | Optional | - |
| `title` | [`TitleEnum`](#title-enum) | Optional | - |
| `first_name` | `string` | Optional | - |
| `middle_name` | `string` | Optional | - |
| `last_name` | `string` | Optional | - |
| `gender` | [`GenderEnum`](#gender-enum) | Optional | - |
| `marital_status` | [`MaritalStatusEnum`](#marital-status-enum) | Optional | - |
| `phone_number` | `string` | Optional | - |
| `phone_number_verified` | `datetime` | Optional | - |
| `language` | `string` | Optional | **Constraints**: *Maximum Length*: `5` |
| `employment_status` | [`EmploymentStatusEnum`](#employment-status-enum) | Optional | - |
| `profession` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `referral_code` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `activated` | `datetime` | Optional | - |
| `utm_source` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_medium` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_campaign` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_term` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `utm_content` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `marketing_consent_date` | `date` | Optional | - |
| `data_consent_date` | `date` | Optional | - |

##### Example (as JSON)

```json
{
  "email": null,
  "birthdate": null,
  "tos_consent": null,
  "marketing_consent": null,
  "data_consent": null,
  "tos_consent_date": null,
  "tax_information": null,
  "country_birth": null,
  "last_login": null,
  "referred_by": null,
  "successful_referrals": null,
  "kyc_verified": null,
  "is_verified": null,
  "fee_segments": null,
  "extra_data": null,
  "portfolios": null,
  "onboarded_by": null,
  "risk_level": null,
  "onboarding_token": null,
  "password": null,
  "email_verified_last_request": null,
  "uuid": null,
  "created": null,
  "updated": null,
  "comments": null,
  "status": null,
  "email_verified": null,
  "email_verify_last_request": null,
  "title": null,
  "first_name": null,
  "middle_name": null,
  "last_name": null,
  "gender": null,
  "marital_status": null,
  "phone_number": null,
  "phone_number_verified": null,
  "language": null,
  "employment_status": null,
  "profession": null,
  "referral_code": null,
  "activated": null,
  "utm_source": null,
  "utm_medium": null,
  "utm_campaign": null,
  "utm_term": null,
  "utm_content": null,
  "marketing_consent_date": null,
  "data_consent_date": null
}
```

#### Patched Assessment

##### Class Name

`PatchedAssessment`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Optional | - |
| `completed` | `datetime` | Optional | - |
| `choices` | [`List of RiskChoiceQuestionCode`](#risk-choice-question-code) | Optional | - |
| `status` | [`AssessmentStatusEnum`](#assessment-status-enum) | Optional | - |
| `risk_level` | `int` | Optional | - |
| `created` | `datetime` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": null,
  "completed": null,
  "choices": null,
  "status": null,
  "risk_level": null,
  "created": null
}
```

#### Patched Bank Account Create Update

##### Class Name

`PatchedBankAccountCreateUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Optional | - |
| `account_number` | `string` | Optional | **Constraints**: *Maximum Length*: `30` |
| `account_sort_code` | `string` | Optional | **Constraints**: *Maximum Length*: `6` |
| `account_holder_name` | `string` | Optional | - |
| `joint` | `bool` | Optional | - |
| `bank_name` | `string` | Optional | **Constraints**: *Maximum Length*: `250` |
| `iban` | `string` | Optional | **Constraints**: *Maximum Length*: `34` |
| `swift_code` | `string` | Optional | **Constraints**: *Maximum Length*: `11` |

##### Example (as JSON)

```json
{
  "uuid": null,
  "account_number": null,
  "account_sort_code": null,
  "account_holder_name": null,
  "joint": null,
  "bank_name": null,
  "iban": null,
  "swift_code": null
}
```

#### Patched Goal

##### Class Name

`PatchedGoal`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Optional | - |
| `name` | `string` | Optional | **Constraints**: *Maximum Length*: `150` |
| `portfolio` | `string` | Optional | - |
| `goal_amount` | `float` | Optional | Desired amount needed to fulfill the goal<br>**Constraints**: `>= 0.1`, `<= 1000000000000` |
| `deadline` | `date` | Optional | Due date to reach the goal. |
| `initial_amount` | `float` | Optional | Initial deposit amount to start from. No sense to start by 0<br>**Constraints**: `>= 0.1`, `<= 1000000000000` |
| `recurring_amount` | `float` | Optional | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `risk_level` | `int` | Optional | **Constraints**: `>= 0`, `<= 32767` |
| `created` | `datetime` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": null,
  "name": null,
  "portfolio": null,
  "goal_amount": null,
  "deadline": null,
  "initial_amount": null,
  "recurring_amount": null,
  "risk_level": null,
  "created": null
}
```

#### Patched Investor Fee

##### Class Name

`PatchedInvestorFee`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `float` | Optional | Determinates a percentage or an amount (between 0 and 1 if percentage otherwise Positive Decimal)<br>**Constraints**: `>= 0`, `<= 100` |
| `value_unit` | [`ValueUnitEnum`](#value-unit-enum) | Optional | Determines the type of the value(Fixed, Percentage) |
| `fee_type` | [`FeeTypeEnum`](#fee-type-enum) | Optional | Each choice should have a related method on fee model that contains the logic to charge the client |
| `concept` | `string` | Optional | Describes the concept that will be shown on invoice<br>**Constraints**: *Maximum Length*: `100` |
| `date_from` | `date` | Optional | Defines the end date when the percentage should be applied |
| `date_to` | `date` | Optional | Defines the start date when the percentage should be applied |
| `amount_from` | `float` | Optional | Defines the amount start range when the percentage should be applied<br>**Constraints**: `>= -1000000000`, `<= 1000000000` |
| `amount_to` | `float` | Optional | Defines the amount end range when the percentage should be applied<br>**Constraints**: `>= -1000000000`, `<= 1000000000` |
| `uuid` | `uuid\|string` | Optional | - |
| `created` | `datetime` | Optional | - |
| `updated` | `datetime` | Optional | - |

##### Example (as JSON)

```json
{
  "value": null,
  "value_unit": null,
  "fee_type": null,
  "concept": null,
  "date_from": null,
  "date_to": null,
  "amount_from": null,
  "amount_to": null,
  "uuid": null,
  "created": null,
  "updated": null
}
```

#### Patched Nationality Update

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`PatchedNationalityUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country` | `string` | Optional | - |
| `document_number` | `string` | Optional | - |
| `document_type` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "country": null,
  "document_number": null,
  "document_type": null
}
```

#### Patched Password Reset Request

##### Class Name

`PatchedPasswordResetRequest`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "email": null
}
```

#### Patched Portfolio Update

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`PatchedPortfolioUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Optional | - |
| `name` | `string` | Optional | **Constraints**: *Maximum Length*: `150` |
| `portfolio_type` | `string` | Optional | - |
| `risk_level` | `int` | Optional | **Constraints**: `>= 0`, `<= 32767` |
| `time_horizon` | `int` | Optional | **Constraints**: `>= 0`, `<= 32767` |
| `status` | [`Status2efEnum`](#status-2-ef-enum) | Optional | - |
| `currency` | `string` | Optional | - |
| `created` | `datetime` | Optional | - |
| `activated` | `datetime` | Optional | - |
| `advisor` | `string` | Optional | - |
| `advice_engine` | `string` | Optional | - |
| `extra_data` | `dict` | Optional | - |
| `client` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": null,
  "name": null,
  "portfolio_type": null,
  "risk_level": null,
  "time_horizon": null,
  "status": null,
  "currency": null,
  "created": null,
  "activated": null,
  "advisor": null,
  "advice_engine": null,
  "extra_data": null,
  "client": null
}
```

#### Patched Tax Information Create Update

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`PatchedTaxInformationCreateUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Optional | - |
| `country` | `string` | Optional | - |
| `document_number` | `string` | Optional | - |
| `document_type` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": null,
  "country": null,
  "document_number": null,
  "document_type": null
}
```

#### Patched Verification Document

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`PatchedVerificationDocument`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Optional | - |
| `document_type` | [`DocumentTypeEnum`](#document-type-enum) | Optional | - |
| `document_front` | `string` | Optional | - |
| `document_back` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": null,
  "document_type": null,
  "document_front": null,
  "document_back": null
}
```

#### Portal Setting Value List

##### Class Name

`PortalSettingValueList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `uuid` | `uuid\|string` | Required | - |
| `created` | `datetime` | Required | - |
| `updated` | `datetime` | Required | - |
| `value` | `string` | Required | **Constraints**: *Maximum Length*: `250` |
| `portal` | `int` | Required | - |
| `key` | `int` | Required | - |

##### Example (as JSON)

```json
{
  "id": 112,
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "created": "2016-03-13T12:52:32.123Z",
  "updated": "2016-03-13T12:52:32.123Z",
  "value": "value2",
  "portal": 4,
  "key": 120
}
```

#### Portfolio Create

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`PortfolioCreate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `150` |
| `portfolio_type` | `string` | Required | - |
| `risk_level` | `int` | Required | - |
| `time_horizon` | `int` | Required | - |
| `status` | [`Status2efEnum`](#status-2-ef-enum) | Required | - |
| `currency` | `string` | Optional | - |
| `created` | `datetime` | Required | - |
| `activated` | `datetime` | Required | - |
| `advisor` | `string` | Required | - |
| `advice_engine` | `string` | Required | - |
| `extra_data` | `dict` | Optional | - |
| `client` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "name": "name0",
  "portfolio_type": "portfolio_type4",
  "risk_level": 66,
  "time_horizon": 200,
  "status": "PENDING",
  "currency": null,
  "created": "2016-03-13T12:52:32.123Z",
  "activated": "2016-03-13T12:52:32.123Z",
  "advisor": "advisor6",
  "advice_engine": "advice_engine6",
  "extra_data": null,
  "client": null
}
```

#### Portfolio Detail

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`PortfolioDetail`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `150` |
| `portfolio_type` | `string` | Required | - |
| `risk_level` | `int` | Optional | **Constraints**: `>= 0`, `<= 32767` |
| `time_horizon` | `int` | Optional | **Constraints**: `>= 0`, `<= 32767` |
| `status` | [`Status2efEnum`](#status-2-ef-enum) | Optional | - |
| `extra_data` | `dict` | Optional | Additional Portfolio attributes |
| `currency` | `string` | Optional | - |
| `created` | `datetime` | Required | - |
| `activated` | `datetime` | Optional | - |
| `balance` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `performance` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `deposit_reference` | `string` | Required | - |
| `advisor` | `string` | Optional | - |
| `advice_engine` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "name": "name0",
  "portfolio_type": "portfolio_type4",
  "risk_level": null,
  "time_horizon": null,
  "status": null,
  "extra_data": null,
  "currency": null,
  "created": "2016-03-13T12:52:32.123Z",
  "activated": null,
  "balance": 26.24,
  "performance": 234.24,
  "deposit_reference": "deposit_reference0",
  "advisor": null,
  "advice_engine": null
}
```

#### Portfolio List

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`PortfolioList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `name` | `string` | Required | - |
| `portfolio_type` | `string` | Required | - |
| `risk_level` | `int` | Required | - |
| `time_horizon` | `int` | Required | - |
| `status` | [`Status2efEnum`](#status-2-ef-enum) | Required | - |
| `balance` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `invested` | `float` | Required | **Constraints**: `>= 0`, `<= 1000000000000` |
| `currency` | `string` | Optional | - |
| `created` | `datetime` | Required | - |
| `advisor` | `string` | Optional | - |
| `advice_engine` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "name": "name0",
  "portfolio_type": "portfolio_type4",
  "risk_level": 66,
  "time_horizon": 200,
  "status": "PENDING",
  "balance": 26.24,
  "invested": 192.52,
  "currency": null,
  "created": "2016-03-13T12:52:32.123Z",
  "advisor": null,
  "advice_engine": null
}
```

#### Portfolio Performance

##### Class Name

`PortfolioPerformance`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `valuation_date` | `date` | Required | - |
| `percentage` | `float` | Optional | **Default**: `0`<br>**Constraints**: `>= -1000000000000`, `<= 1000000000000`<br>*Default: `0`* |
| `performance` | `float` | Optional | **Default**: `0`<br>**Constraints**: `>= -1000000000000`, `<= 1000000000000`<br>*Default: `0`* |

##### Example (as JSON)

```json
{
  "valuation_date": "2016-03-13",
  "percentage": null,
  "performance": null
}
```

#### Portfolio Performance Positions

##### Class Name

`PortfolioPerformancePositions`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `valuation_datetime` | `datetime` | Required | - |
| `last_update` | `datetime` | Required | - |
| `asset` | `string` | Required | - |
| `shares` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `price` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `currency` | `string` | Required | - |
| `weight` | `float` | Optional | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `fx_rate_account` | `float` | Optional | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `asset_currency_value` | `float` | Optional | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `value` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `position_return` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `unrealised_pl` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `realised_pl` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `earnings` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `avg_entry_price` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `daily_pl` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |

##### Example (as JSON)

```json
{
  "valuation_datetime": "2016-03-13T12:52:32.123Z",
  "last_update": "2016-03-13T12:52:32.123Z",
  "asset": "asset0",
  "shares": 14.94,
  "price": 207.52,
  "currency": "currency0",
  "weight": null,
  "fx_rate_account": null,
  "asset_currency_value": null,
  "value": 251.52,
  "position_return": 90.86,
  "unrealised_pl": 6.48,
  "realised_pl": 54.26,
  "earnings": 67.32,
  "avg_entry_price": 228.2,
  "daily_pl": 72.36
}
```

#### Portfolio Type

##### Class Name

`PortfolioType`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Required | - |
| `name` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "code": "code8",
  "name": "name0"
}
```

#### Portfolio Type Restrictions

##### Class Name

`PortfolioTypeRestrictions`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `portfolio_type` | `string` | Required | - |
| `key` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "portfolio_type": "portfolio_type4",
  "key": "key0"
}
```

#### Portfolio Update

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`PortfolioUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `150` |
| `portfolio_type` | `string` | Required | - |
| `risk_level` | `int` | Optional | **Constraints**: `>= 0`, `<= 32767` |
| `time_horizon` | `int` | Optional | **Constraints**: `>= 0`, `<= 32767` |
| `status` | [`Status2efEnum`](#status-2-ef-enum) | Required | - |
| `currency` | `string` | Optional | - |
| `created` | `datetime` | Required | - |
| `activated` | `datetime` | Required | - |
| `advisor` | `string` | Required | - |
| `advice_engine` | `string` | Required | - |
| `extra_data` | `dict` | Optional | - |
| `client` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "name": "name0",
  "portfolio_type": "portfolio_type4",
  "risk_level": null,
  "time_horizon": null,
  "status": "PENDING",
  "currency": null,
  "created": "2016-03-13T12:52:32.123Z",
  "activated": "2016-03-13T12:52:32.123Z",
  "advisor": "advisor6",
  "advice_engine": "advice_engine6",
  "extra_data": null,
  "client": null
}
```

#### Position

##### Class Name

`Position`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset` | [`RelatedAssetSerializerWithAssetCategories`](#related-asset-serializer-with-asset-categories) | Required | - |
| `shares` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `price` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `value` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `weight` | `float` | Required | - |
| `fx_rate_account` | `float` | Required | - |
| `asset_currency_value` | `float` | Required | - |

##### Example (as JSON)

```json
{
  "asset": {
    "uuid": "000010be-0000-0000-0000-000000000000",
    "market": null,
    "isin": "isin0",
    "currency": null,
    "ticker": "ticker2",
    "name": "name0",
    "extra_data": null,
    "categories": [
      "categories2",
      "categories1"
    ]
  },
  "shares": 14.94,
  "price": 207.52,
  "value": 251.52,
  "weight": 192.04,
  "fx_rate_account": 54.72,
  "asset_currency_value": 54.08
}
```

#### Preset Category Group

##### Class Name

`PresetCategoryGroup`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `code` | `string` | Required | - |
| `categories` | [`List of Category`](#category) | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "code": "code8",
  "categories": [
    {
      "uuid": "00000bae-0000-0000-0000-000000000000",
      "code": "code2",
      "categories": [
        {
          "uuid": "00000f7e-0000-0000-0000-000000000000",
          "name": "name0",
          "code": "code8",
          "order": 32,
          "type": "type0"
        },
        {
          "uuid": "00000f7f-0000-0000-0000-000000000000",
          "name": "name1",
          "code": "code9",
          "order": 31,
          "type": "type9"
        }
      ],
      "name": "name4",
      "status": null,
      "extra_data": null,
      "description": null
    },
    {
      "uuid": "00000baf-0000-0000-0000-000000000000",
      "code": "code3",
      "categories": [
        {
          "uuid": "00000f7f-0000-0000-0000-000000000000",
          "name": "name1",
          "code": "code9",
          "order": 31,
          "type": "type9"
        }
      ],
      "name": "name5",
      "status": null,
      "extra_data": null,
      "description": null
    },
    {
      "uuid": "00000bb0-0000-0000-0000-000000000000",
      "code": "code4",
      "categories": [
        {
          "uuid": "00000f80-0000-0000-0000-000000000000",
          "name": "name2",
          "code": "code0",
          "order": 30,
          "type": "type8"
        },
        {
          "uuid": "00000f7f-0000-0000-0000-000000000000",
          "name": "name1",
          "code": "code9",
          "order": 31,
          "type": "type9"
        },
        {
          "uuid": "00000f7e-0000-0000-0000-000000000000",
          "name": "name0",
          "code": "code8",
          "order": 32,
          "type": "type0"
        }
      ],
      "name": "name6",
      "status": null,
      "extra_data": null,
      "description": null
    }
  ]
}
```

#### Price

##### Class Name

`Price`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `datetime` | `datetime` | Required | - |
| `date` | `datetime` | Required | - |

##### Example (as JSON)

```json
{
  "amount": 56.78,
  "datetime": "2016-03-13T12:52:32.123Z",
  "date": "2016-03-13T12:52:32.123Z"
}
```

#### Question

##### Class Name

`Question`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Required | - |
| `order` | `int` | Required | - |
| `description` | `string` | Required | - |
| `choices` | [`List of RiskChoice`](#risk-choice) | Required | - |
| `created` | `datetime` | Required | - |

##### Example (as JSON)

```json
{
  "code": "code8",
  "order": 32,
  "description": "description0",
  "choices": [
    {
      "code": "code5",
      "order": 43,
      "description": "description3",
      "created": "2016-03-13T12:52:32.123Z"
    },
    {
      "code": "code6",
      "order": 42,
      "description": "description2",
      "created": "2016-03-13T12:52:32.123Z"
    }
  ],
  "created": "2016-03-13T12:52:32.123Z"
}
```

#### Rebalance

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`Rebalance`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `status` | [`RebalanceStatusEnum`](#rebalance-status-enum) | Required | - |
| `reason` | `string` | Required | Cancelled reason |
| `broker_orders` | `List of string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "status": "IN_PROCESS",
  "reason": "reason4",
  "broker_orders": [
    "broker_orders9"
  ]
}
```

#### Related Asset Serializer With Asset Categories

Allow get asset by multiple params or UUID

##### Class Name

`RelatedAssetSerializerWithAssetCategories`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `market` | `string` | Optional | - |
| `isin` | `string` | Required | **Constraints**: *Maximum Length*: `120` |
| `currency` | `string` | Optional | - |
| `ticker` | `string` | Required | **Constraints**: *Maximum Length*: `120` |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `250` |
| `extra_data` | `dict` | Optional | - |
| `categories` | `List of string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "market": null,
  "isin": "isin0",
  "currency": null,
  "ticker": "ticker2",
  "name": "name0",
  "extra_data": null,
  "categories": [
    "categories4",
    "categories5",
    "categories6"
  ]
}
```

#### Related Asset Serializer With Permission

Allow get asset by multiple params or UUID

##### Class Name

`RelatedAssetSerializerWithPermission`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `market` | `string` | Optional | - |
| `isin` | `string` | Required | **Constraints**: *Maximum Length*: `120` |
| `currency` | `string` | Optional | - |
| `ticker` | `string` | Required | **Constraints**: *Maximum Length*: `120` |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `250` |
| `extra_data` | `dict` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "market": null,
  "isin": "isin0",
  "currency": null,
  "ticker": "ticker2",
  "name": "name0",
  "extra_data": null
}
```

#### Relationship Manager

##### Class Name

`RelationshipManager`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `first_name` | `string` | Optional | - |
| `last_name` | `string` | Optional | - |
| `phone_number` | `string` | Optional | - |
| `email` | `string` | Required | - |
| `photo` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "first_name": null,
  "last_name": null,
  "phone_number": null,
  "email": "email6",
  "photo": null
}
```

#### Response

##### Class Name

`Response`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `string` | Optional | **Default**: `'ok'`<br>*Default: `'ok'`* |
| `error` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "status": null,
  "error": null
}
```

#### Risk Choice

##### Class Name

`RiskChoice`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Required | - |
| `order` | `int` | Required | - |
| `description` | `string` | Required | - |
| `created` | `datetime` | Required | - |

##### Example (as JSON)

```json
{
  "code": "code8",
  "order": 32,
  "description": "description0",
  "created": "2016-03-13T12:52:32.123Z"
}
```

#### Risk Choice Question Code

##### Class Name

`RiskChoiceQuestionCode`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Required | **Constraints**: *Maximum Length*: `60`, *Pattern*: `^[-a-zA-Z0-9_]+$` |
| `order` | `int` | Optional | **Constraints**: `>= 0`, `<= 32767` |
| `description` | `string` | Optional | - |
| `created` | `datetime` | Required | - |
| `question_code` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "code": "code8",
  "order": null,
  "description": null,
  "created": "2016-03-13T12:52:32.123Z",
  "question_code": "question_code6"
}
```

#### Statement

##### Class Name

`Statement`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `date_from` | `date` | Required | - |
| `date_to` | `date` | Required | - |
| `created` | `datetime` | Required | - |
| `status` | [`Status181Enum`](#status-181-enum) | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "date_from": "2016-03-13",
  "date_to": "2016-03-13",
  "created": "2016-03-13T12:52:32.123Z",
  "status": "COMPLETED"
}
```

#### Subscribe

##### Class Name

`Subscribe`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | - |
| `subscription` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "id": "id0",
  "subscription": "subscription4"
}
```

#### Tax Information Create Update

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`TaxInformationCreateUpdate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `country` | `string` | Required | - |
| `document_number` | `string` | Required | - |
| `document_type` | `string` | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "country": "country4",
  "document_number": "document_number6",
  "document_type": null
}
```

#### Tax Information List

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`TaxInformationList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `country` | `string` | Required | - |
| `document_type` | `string` | Optional | - |
| `document_number` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "country": "country4",
  "document_type": null,
  "document_number": "document_number6"
}
```

#### Tax Report

##### Class Name

`TaxReport`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `date_from` | `date` | Required | - |
| `date_to` | `date` | Required | - |
| `created` | `datetime` | Required | - |
| `status` | [`Status181Enum`](#status-181-enum) | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "date_from": "2016-03-13",
  "date_to": "2016-03-13",
  "created": "2016-03-13T12:52:32.123Z",
  "status": "COMPLETED"
}
```

#### Token Refresh

##### Class Name

`TokenRefresh`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `refresh` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "refresh": "refresh2"
}
```

#### Tos

##### Class Name

`Tos`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `version` | `string` | Required | **Constraints**: *Maximum Length*: `20` |
| `content` | `string` | Required | - |
| `published` | `date` | Optional | - |
| `previous_tos_uuid` | `string` | Required | - |
| `next_tos_uuid` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "version": "version4",
  "content": "content4",
  "published": null,
  "previous_tos_uuid": "previous_tos_uuid4",
  "next_tos_uuid": "next_tos_uuid2"
}
```

#### Unsubscribe

##### Class Name

`Unsubscribe`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | - |
| `subscription` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "id": "id0",
  "subscription": "subscription4"
}
```

#### Verification Create

##### Class Name

`VerificationCreate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `verify_type` | [`VerifyTypeEnum`](#verify-type-enum) | Required | - |
| `status` | [`StatusBd7Enum`](#status-bd-7-enum) | Optional | - |
| `result` | [`ResultEnum`](#result-enum) | Optional | - |
| `created` | `datetime` | Required | - |
| `updated` | `datetime` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "verify_type": "IDENTITY",
  "status": null,
  "result": null,
  "created": "2016-03-13T12:52:32.123Z",
  "updated": "2016-03-13T12:52:32.123Z"
}
```

#### Verification Document

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`VerificationDocument`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `document_type` | [`DocumentTypeEnum`](#document-type-enum) | Required | - |
| `document_front` | `string` | Required | - |
| `document_back` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "document_type": "local_tax_bill",
  "document_front": "document_front0",
  "document_back": "document_back6"
}
```

#### Verification Document Create

##### Class Name

`VerificationDocumentCreate`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_type` | `string` | Required | - |
| `uuid` | `uuid\|string` | Required | - |
| `document_front` | [`Document`](#document) | Required | - |
| `document_back` | [`Document`](#document) | Required | - |

##### Example (as JSON)

```json
{
  "document_type": "document_type8",
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "document_front": {
    "uuid": "00001a00-0000-0000-0000-000000000000",
    "name": "name0",
    "doc_type": "ID_PERSONAL",
    "description": null,
    "path": "path4",
    "extra_data": null
  },
  "document_back": {
    "uuid": "000014e8-0000-0000-0000-000000000000",
    "name": "name6",
    "doc_type": "TRANSFERS",
    "description": null,
    "path": "path0",
    "extra_data": null
  }
}
```

#### Verification List

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`VerificationList`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `verify_type` | [`VerifyTypeEnum`](#verify-type-enum) | Required | - |
| `status` | [`StatusBd7Enum`](#status-bd-7-enum) | Required | - |
| `result` | [`ResultEnum`](#result-enum) | Required | - |
| `created` | `datetime` | Required | - |
| `updated` | `datetime` | Required | - |
| `verification_documents` | `List of string` | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "verify_type": "IDENTITY",
  "status": "OUTDATED",
  "result": "DOUBT",
  "created": "2016-03-13T12:52:32.123Z",
  "updated": "2016-03-13T12:52:32.123Z",
  "verification_documents": [
    "verification_documents6"
  ]
}
```

#### Verification With Type

##### Class Name

`VerificationWithType`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `verify_type` | [`VerifyTypeEnum`](#verify-type-enum) | Required | - |
| `status` | [`StatusBd7Enum`](#status-bd-7-enum) | Optional | - |
| `result` | [`ResultEnum`](#result-enum) | Optional | - |
| `created` | `datetime` | Required | - |
| `updated` | `datetime` | Required | - |
| `verification_documents` | [`List of VerificationDocumentCreate`](#verification-document-create) | Optional | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "verify_type": "IDENTITY",
  "status": null,
  "result": null,
  "created": "2016-03-13T12:52:32.123Z",
  "updated": "2016-03-13T12:52:32.123Z",
  "verification_documents": null
}
```

#### Watchlist

A ModelSerializer that takes additional arguments for
"fields", "omit" and "expand" in order to
control which fields are displayed, and whether to replace simple
values with complex, nested serializations

##### Class Name

`Watchlist`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `name` | `string` | Required | **Constraints**: *Maximum Length*: `250` |
| `assets` | [`List of RelatedAssetSerializerWithPermission`](#related-asset-serializer-with-permission) | Required | - |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "name": "name0",
  "assets": [
    {
      "uuid": "0000062c-0000-0000-0000-000000000000",
      "market": null,
      "isin": "isin6",
      "currency": null,
      "ticker": "ticker6",
      "name": "name4",
      "extra_data": null
    },
    {
      "uuid": "0000062d-0000-0000-0000-000000000000",
      "market": null,
      "isin": "isin5",
      "currency": null,
      "ticker": "ticker7",
      "name": "name5",
      "extra_data": null
    },
    {
      "uuid": "0000062e-0000-0000-0000-000000000000",
      "market": null,
      "isin": "isin4",
      "currency": null,
      "ticker": "ticker8",
      "name": "name6",
      "extra_data": null
    }
  ]
}
```

#### Websocket Authentication

##### Class Name

`WebsocketAuthentication`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ticket` | `string` | Required | - |

##### Example (as JSON)

```json
{
  "ticket": "ticket4"
}
```

#### Withdrawal Detail

##### Class Name

`WithdrawalDetail`

##### Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uuid` | `uuid\|string` | Required | - |
| `portfolio` | `string` | Required | - |
| `amount` | `float` | Required | **Constraints**: `>= -1000000000000`, `<= 1000000000000` |
| `provider` | `string` | Required | - |
| `status` | [`Status14bEnum`](#status-14-b-enum) | Required | - |
| `reason` | `string` | Optional | Cancelled reason<br>**Constraints**: *Maximum Length*: `250` |
| `completed` | `datetime` | Optional | - |
| `purpose` | `string` | Optional | Withdrawal reason<br>**Constraints**: *Maximum Length*: `250` |
| `created` | `datetime` | Required | - |
| `withdrawal_type` | `string` | Required | - |
| `extra_data` | `dict` | Optional | Additional withdrawal attributes for the specific portal |

##### Example (as JSON)

```json
{
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "portfolio": "portfolio4",
  "amount": 56.78,
  "provider": "provider8",
  "status": "REQUESTED",
  "reason": null,
  "completed": null,
  "purpose": null,
  "created": "2016-03-13T12:52:32.123Z",
  "withdrawal_type": "withdrawal_type4",
  "extra_data": null
}
```

### Enumerations

* [Activity Type Enum](#activity-type-enum)
* [Assessment Status Enum](#assessment-status-enum)
* [Asset Type Enum](#asset-type-enum)
* [Category Status Enum](#category-status-enum)
* [Channel Enum](#channel-enum)
* [Create Order Method Enum](#create-order-method-enum)
* [Deposit Type Enum](#deposit-type-enum)
* [Doc Type Enum](#doc-type-enum)
* [Document Type Enum](#document-type-enum)
* [Duration Enum](#duration-enum)
* [Employment Status Enum](#employment-status-enum)
* [Fee Type Enum](#fee-type-enum)
* [Gender Enum](#gender-enum)
* [Marital Status Enum](#marital-status-enum)
* [Order List Method Enum](#order-list-method-enum)
* [Order List Status Enum](#order-list-status-enum)
* [Order Type Enum](#order-type-enum)
* [Rebalance Status Enum](#rebalance-status-enum)
* [Result Enum](#result-enum)
* [Status 14 B Enum](#status-14-b-enum)
* [Status 181 Enum](#status-181-enum)
* [Status 260 Enum](#status-260-enum)
* [Status 2 Ef Enum](#status-2-ef-enum)
* [Status 6 F 6 Enum](#status-6-f-6-enum)
* [Status B65 Enum](#status-b65-enum)
* [Status B6 a Enum](#status-b6-a-enum)
* [Status Bd 7 Enum](#status-bd-7-enum)
* [Title Enum](#title-enum)
* [Value Unit Enum](#value-unit-enum)
* [Verify Type Enum](#verify-type-enum)
* [Format](#format)
* [Format 1](#format-1)
* [Lang](#lang)
* [Ordering](#ordering)
* [Target](#target)

#### Activity Type Enum

##### Class Name

`ActivityTypeEnum`

##### Fields

| Name |
|  --- |
| `CREATED` |
| `UPDATED` |
| `DELETED` |

#### Assessment Status Enum

##### Class Name

`AssessmentStatusEnum`

##### Fields

| Name |
|  --- |
| `PENDING` |
| `COMPLETED` |
| `OUTDATED` |

#### Asset Type Enum

##### Class Name

`AssetTypeEnum`

##### Fields

| Name |
|  --- |
| `ETF` |
| `MUTUAL_FUND` |
| `STOCK` |

#### Category Status Enum

##### Class Name

`CategoryStatusEnum`

##### Fields

| Name |
|  --- |
| `ACTIVE` |
| `INACTIVE` |

#### Channel Enum

##### Class Name

`ChannelEnum`

##### Fields

| Name |
|  --- |
| `BROWSER` |
| `IOS` |
| `ANDROID` |

#### Create Order Method Enum

##### Class Name

`CreateOrderMethodEnum`

##### Fields

| Name |
|  --- |
| `MARKET` |
| `STOP` |
| `LIMIT` |

#### Deposit Type Enum

##### Class Name

`DepositTypeEnum`

##### Fields

| Name |
|  --- |
| `CONTRIBUTION` |
| `TRANSFER` |

#### Doc Type Enum

##### Class Name

`DocTypeEnum`

##### Fields

| Name |
|  --- |
| `ID_PERSONAL` |
| `BANK_DETAILS` |
| `EMPLOYMENT` |
| `MARITAL_STATUS` |
| `PENSION` |
| `LEGAL` |
| `TRANSFERS` |
| `MEDICAL` |
| `CONTRACT` |
| `OTHERS` |

#### Document Type Enum

##### Class Name

`DocumentTypeEnum`

##### Fields

| Name |
|  --- |
| `PASSPORT` |
| `DRIVING_LICENCE` |
| `NATIONAL_IDENTITY_CARD` |
| `UTILITY_BILL` |
| `LOCAL_TAX_BILL` |
| `BANK_STATEMENT` |
| `LEASE_AGREEMENT` |
| `RENT_RECEIPT` |
| `LETTER` |
| `CERTIFICATE_MARRIAGE` |
| `DECREE_ABSOLUTE` |
| `FINAL_ORDER` |
| `CLIENT_PHOTO` |

#### Duration Enum

##### Class Name

`DurationEnum`

##### Fields

| Name |
|  --- |
| `GOOD_TILL_CANCEL` |
| `DAY_ORDER` |

#### Employment Status Enum

##### Class Name

`EmploymentStatusEnum`

##### Fields

| Name |
|  --- |
| `EMPLOYED` |
| `SELF_EMPLOYED` |
| `RETIRED` |
| `UNEMPLOYED` |

#### Fee Type Enum

##### Class Name

`FeeTypeEnum`

##### Fields

| Name |
|  --- |
| `PORTAL_SERVICE` |
| `SELLER_FEE` |

#### Gender Enum

##### Class Name

`GenderEnum`

##### Fields

| Name |
|  --- |
| `M` |
| `F` |
| `U` |

#### Marital Status Enum

##### Class Name

`MaritalStatusEnum`

##### Fields

| Name |
|  --- |
| `NOT_DISCLOSED` |
| `SINGLE` |
| `MARRIED_CIVIL_PARTNER` |
| `CIVIL_PARTNER` |
| `DIVORCED_DISSOLVED_CIVIL_PARTNERSHIP` |
| `WIDOWED_SURVIVING_CIVIL_PARTNER` |
| `SEPARATED` |

#### Order List Method Enum

##### Class Name

`OrderListMethodEnum`

##### Fields

| Name |
|  --- |
| `MARKET` |
| `QUOTE` |
| `INTERNAL` |
| `LIMIT` |
| `STOP` |

#### Order List Status Enum

##### Class Name

`OrderListStatusEnum`

##### Fields

| Name |
|  --- |
| `PENDING` |
| `WAITING_FOR_PRICE` |
| `PROCESSING` |
| `QUOTED` |
| `COMPLETED` |
| `VERIFIED` |
| `ERROR` |
| `CANCELLED` |

#### Order Type Enum

##### Class Name

`OrderTypeEnum`

##### Fields

| Name |
|  --- |
| `BUY` |
| `SELL` |
| `VERIFICATION` |

#### Rebalance Status Enum

##### Class Name

`RebalanceStatusEnum`

##### Fields

| Name |
|  --- |
| `PENDING` |
| `CREATED` |
| `ADVICE_REQUESTED` |
| `ADVICE_COMPLETED` |
| `IN_PROCESS` |
| `PROCESSING` |
| `ORDERS_GENERATED` |
| `ORDERS_FILLED` |
| `SELL_TRADES_GENERATED` |
| `BUY_TRADES_GENERATED` |
| `POSITIONS_SOLD` |
| `COMPLETED` |
| `CANCELLED` |
| `ERROR` |

#### Result Enum

##### Class Name

`ResultEnum`

##### Fields

| Name |
|  --- |
| `ACCEPTED` |
| `REJECTED` |
| `DOUBT` |

#### Status 14 B Enum

##### Class Name

`Status14bEnum`

##### Fields

| Name |
|  --- |
| `DRAFT` |
| `PENDING` |
| `PROCESSING` |
| `POSITIONS_SOLD` |
| `REQUESTED` |
| `COMPLETED` |
| `ERROR` |
| `CANCELLED` |

#### Status 181 Enum

##### Class Name

`Status181Enum`

##### Fields

| Name |
|  --- |
| `GENERATING` |
| `ERROR` |
| `COMPLETED` |

#### Status 260 Enum

##### Class Name

`Status260Enum`

##### Fields

| Name |
|  --- |
| `PENDING` |
| `CHARGED` |

#### Status 2 Ef Enum

##### Class Name

`Status2efEnum`

##### Fields

| Name |
|  --- |
| `PENDING` |
| `ACTIVE` |
| `DELETING` |
| `DELETED` |

#### Status 6 F 6 Enum

##### Class Name

`Status6f6Enum`

##### Fields

| Name |
|  --- |
| `ACTIVE` |
| `INACTIVE` |
| `DELETED` |

#### Status B65 Enum

##### Class Name

`StatusB65Enum`

##### Fields

| Name |
|  --- |
| `ONBOARDING` |
| `PENDING` |
| `ACTIVE` |
| `INACTIVE` |
| `CUSTODIAN_PENDING` |
| `KYC_PENDING` |

#### Status B6 a Enum

##### Class Name

`StatusB6aEnum`

##### Fields

| Name |
|  --- |
| `PENDING` |
| `REQUESTED` |
| `PROCESSING` |
| `COMPLETED` |
| `ERROR` |
| `CANCELLED` |

#### Status Bd 7 Enum

##### Class Name

`StatusBd7Enum`

##### Fields

| Name |
|  --- |
| `PENDING` |
| `PROCESSING` |
| `COMPLETED` |
| `PAUSED` |
| `REOPENED` |
| `OTHER` |
| `ERROR` |
| `CANCELLED` |
| `OUTDATED` |

#### Title Enum

##### Class Name

`TitleEnum`

##### Fields

| Name |
|  --- |
| `MR` |
| `MS` |
| `MX` |

#### Value Unit Enum

##### Class Name

`ValueUnitEnum`

##### Fields

| Name |
|  --- |
| `FIXED_AMOUNT` |
| `PERCENTAGE` |

#### Verify Type Enum

##### Class Name

`VerifyTypeEnum`

##### Fields

| Name |
|  --- |
| `IDENTITY` |
| `BANKING` |

#### Format

##### Class Name

`FormatEnum`

##### Fields

| Name |
|  --- |
| `JSON` |
| `YAML` |

#### Format 1

##### Class Name

`Format1Enum`

##### Fields

| Name |
|  --- |
| `BASE64` |
| `JSON` |
| `PDF` |

#### Lang

##### Class Name

`LangEnum`

##### Fields

| Name |
|  --- |
| `ENCH` |
| `ENGB` |
| `FRCH` |

#### Ordering

##### Class Name

`OrderingEnum`

##### Fields

| Name |
|  --- |
| `ENUM_ACTIVATED` |
| `ENUM_CREATED` |
| `ENUM_FIRST_NAME` |
| `ENUM_LAST_NAME` |
| `ENUM_RISK_LEVEL` |
| `ENUM_STATUS` |
| `ACTIVATED` |
| `CREATED` |
| `FIRST_NAME` |
| `LAST_NAME` |
| `RISK_LEVEL` |
| `STATUS` |

#### Target

##### Class Name

`TargetEnum`

##### Fields

| Name |
|  --- |
| `ENUM_1` |
| `ENUM_2` |
| `ENUM_3` |
| `ENUM_4` |
| `ENUM_5` |
| `ENUM_6` |
| `ENUM_7` |

## Utility Classes Documentation

### ApiHelper

A utility class for processing API Calls. Also contains classes for supporting standard datetime formats.

#### Methods

| Name | Description |
|  --- | --- |
| json_deserialize | Deserializes a JSON string to a Python dictionary. |

#### Classes

| Name | Description |
|  --- | --- |
| HttpDateTime | A wrapper for datetime to support HTTP date format. |
| UnixDateTime | A wrapper for datetime to support Unix date format. |
| RFC3339DateTime | A wrapper for datetime to support RFC3339 format. |

## Common Code Documentation

### HttpResponse

Http response received.

#### Parameters

| Name | Type | Description |
|  --- | --- | --- |
| status_code | int | The status code returned by the server. |
| reason_phrase | str | The reason phrase returned by the server. |
| headers | dict | Response headers. |
| text | str | Response body. |
| request | HttpRequest | The request that resulted in this response. |

### HttpRequest

Represents a single Http Request.

#### Parameters

| Name | Type | Tag | Description |
|  --- | --- | --- | --- |
| http_method | HttpMethodEnum |  | The HTTP method of the request. |
| query_url | str |  | The endpoint URL for the API request. |
| headers | dict | optional | Request headers. |
| query_parameters | dict | optional | Query parameters to add in the URL. |
| parameters | dict &#124; str | optional | Request body, either as a serialized string or else a list of parameters to form encode. |
| files | dict | optional | Files to be sent with the request. |

