#!/usr/bin/env python
def trigger():
    import pypd
    integration_key = 'YOUR_INTEGRATION_KEY'
    pypd.EventV2.create(data={
        'routing_key': integration_key,
        'event_action': 'trigger',
        'payload': {
            'summary': 'test',
            'severity': 'error',
            'source': 'test',
        }
     })

datalist = [1, 2, 4, 5, "a", 6, 7]
for d in datalist:
    if d != "a":
        print("Ok")
    else:
        trigger()
