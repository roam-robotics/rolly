# Rolly Polly
A lightweight Rollbar client.

## Use
```python
import rolly

log = rolly.Polly(token='deadbeef', environment='development')

log.fatal('something something danger zone...')

log.info('new arrivals',
         data={
             'movies': ['Planet Earth', 'Deadpool'],
             'paintings': ['Mona Lisa', 'Starry Night']
         })

log.log('generic message', level='warning', data={'lol': 'wut?'})
```
