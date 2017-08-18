import json
from json2html import json2html

data = json.loads('{"entity":{"entity_type":"DOMAIN","entity_id":"ucenterdress.com"},"requests":[{"request_id":4878088,"request_date_ms":1501214633243,"reporting_org":{"entity_type":"REPORTING_ORG","entity_id":"51966","entity_name":"Counterfeit.Technology"},"urls_in_request":15,"urls_removed_in_request":15,"copyright_owner":{"entity_type":"COPYRIGHT_OWNER","entity_id":"205347","entity_name":"House of Mooshki"}},{"request_id":4879018,"request_date_ms":1501210311382,"reporting_org":{"entity_type":"REPORTING_ORG","entity_id":"51966","entity_name":"Counterfeit.Technology"},"urls_in_request":10,"urls_removed_in_request":10,"copyright_owner":{"entity_type":"COPYRIGHT_OWNER","entity_id":"205347","entity_name":"House of Mooshki"}},{"request_id":4880859,"request_date_ms":1501210192149,"reporting_org":{"entity_type":"REPORTING_ORG","entity_id":"51966","entity_name":"Counterfeit.Technology"},"urls_in_request":22,"urls_removed_in_request":22,"copyright_owner":{"entity_type":"COPYRIGHT_OWNER","entity_id":"205347","entity_name":"House of Mooshki"}},{"request_id":4880303,"request_date_ms":1501210072270,"reporting_org":{"entity_type":"REPORTING_ORG","entity_id":"51966","entity_name":"Counterfeit.Technology"},"urls_in_request":16,"urls_removed_in_request":16,"copyright_owner":{"entity_type":"COPYRIGHT_OWNER","entity_id":"205347","entity_name":"House of Mooshki"}},{"request_id":4880127,"request_date_ms":1501209835763,"reporting_org":{"entity_type":"REPORTING_ORG","entity_id":"51966","entity_name":"Counterfeit.Technology"},"urls_in_request":10,"urls_removed_in_request":10,"copyright_owner":{"entity_type":"COPYRIGHT_OWNER","entity_id":"205347","entity_name":"House of Mooshki"}},{"request_id":4638985,"request_date_ms":1495262847869,"reporting_org":{"entity_type":"REPORTING_ORG","entity_id":"51966","entity_name":"Counterfeit.Technology"},"urls_in_request":11,"urls_removed_in_request":11,"copyright_owner":{"entity_type":"COPYRIGHT_OWNER","entity_id":"190399","entity_name":"Terani Couture"}},{"request_id":4636186,"request_date_ms":1495226365958,"reporting_org":{"entity_type":"REPORTING_ORG","entity_id":"51966","entity_name":"Counterfeit.Technology"},"urls_in_request":37,"urls_removed_in_request":37,"copyright_owner":{"entity_type":"COPYRIGHT_OWNER","entity_id":"190399","entity_name":"Terani Couture"}},{"request_id":4253966,"request_date_ms":1484051738090,"reporting_org":{"entity_type":"REPORTING_ORG","entity_id":"51966","entity_name":"Counterfeit.Technology"},"urls_in_request":47,"urls_removed_in_request":47,"copyright_owner":{"entity_type":"COPYRIGHT_OWNER","entity_id":"58388","entity_name":"PromGirl, llc"}},{"request_id":4251196,"request_date_ms":1484030655108,"reporting_org":{"entity_type":"REPORTING_ORG","entity_id":"51966","entity_name":"Counterfeit.Technology"},"urls_in_request":17,"urls_removed_in_request":17,"copyright_owner":{"entity_type":"COPYRIGHT_OWNER","entity_id":"65545","entity_name":"Mon Cheri LLC"}}],"requests_overall_count":9}')
print json2html.convert(json=data)

