import boto
from boto.mws import connection
from boto.mws.connection import MWSConnection
from boto.mws.response import ResponseFactory, ResponseElement
from boto.handler import XmlHandler
import boto.mws.response
import itertools
import xml.etree.cElementTree as et
import time

start_time = time.time()

ACCOUNT_TYPE = "Merchant"

MWS_ACCESS_KEY = 'xxxxx'
MWS_SECRET_KEY = 'xxxxx'
MERCHANT_ID = 'xxxxx'
MARKETPLACE_ID = 'xxxxx'

# Replace file name with xml file to parse
tree = et.parse('file_name.xml')
root = tree.getroot()
# Replace xml namespace. This is the header to parse through demandware xml
xmlns = {'catalog':'{http://www.demandware.com/xml/impex/catalog/2006-10-31}'}
product = root.find('.//{catalog}product'.format(**xmlns))

# List of SKUs
IdList = []
for product in root:
    product_id = product.get('product-id')
    IdList.append(product_id)

IdType = 'SellerSKU'

# Request can only contain 5 IDs, so list needs to be split into chunks of
# 5 IDs.
def chunk(l ,n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

conn = connection.MWSConnection(aws_access_key_id=MWS_ACCESS_KEY,
            aws_secret_access_key=MWS_SECRET_KEY, Merchant=MERCHANT_ID)


for ids in chunk(IdList, 5):
        response = MWSConnection._parse_response = lambda s,x,y,z: z
        skus = conn.get_matching_product_for_id(MarketplaceId=MARKETPLACE_ID, IdList=ids,
            IdType=IdType)
        print skus

print("----%s seconds ----" % (time.time() - start_time))
