from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

api = Connection(config_file='ebay.yaml',siteid='EBAY-US', appid = 'GabeJuli-P-SBX-7f78bdb77-bf291bb1')

request = {'keyword': 'baseball cards',
        'paginationInput': {
            'entriesPerPage': 10,
            'pageNumber': 1
        },
        'sortOrder': 'PricePlusShippingLowest'
        }
response = api.execute('findItemsByKeywords', request)

for item in response.reply.searchResult.item:
	print("Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}")