from bitdeli import profile_events
from bitdeli.protocol import params, done
from bitdeli.chunkedlist import ChunkedList
from datetime import datetime, timedelta
import json

PARAMS = params()
PROFILE_RETENTION = 365
TFORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

def get_element_label(props):
    if not 'tag_name' in props:
        return 'document'
    name = props['tag_name']
    if 'id' in props:
        name = '%s#%s' % (name, props['id'])
    if 'class_name' in props:
        name = '%s.%s' % (name, props['class_name'].replace(" ", "."))
    return name

def format_dom_event(props):
    props['$element_label'] = get_element_label(props)
    if 'type' in props:
        props['$event_label'] = 'DOM: %s on %s' %\
            (props['type'], props['$element_label'])
    return props

for profile, events in profile_events():
    for event in events:
        props = json.loads(event.object.data)
        name = props['$event_name']
        if name == '$dom_event':
            event.object.data = json.dumps(format_dom_event(props))
        key = name if name[0] == '$' else 'events'
        c = profile.get(key)
        if c == None:
            c = profile[key] = ChunkedList()
        c.push([(event.timestamp, event.groupkey, event.ip, event.object)])
    too_old = datetime.strftime(datetime.strptime(event.timestamp, TFORMAT) -\
                                timedelta(days=PROFILE_RETENTION), TFORMAT)
    for key, lst in profile.iteritems():
        if key[0] != '!':
            lst.drop_chunks(lambda x: x[0] > too_old)
    #profile.set_expire(PROFILE_RETENTION)

done()
