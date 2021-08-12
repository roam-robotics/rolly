# Rolly Polly
A lightweight Rollbar client.

## Use
```python
import rolly

log = rolly.Polly(token='deadbeef', environment='development')

ok, response = log.fatal('something something danger zone...')
if not ok:
	print(f'Rollbar call failed because :: {response}', file=sys.stderr)

log.info('new arrivals',
         data={
             'movies': ['Planet Earth', 'Deadpool'],
             'paintings': ['Mona Lisa', 'Starry Night']
         })

log.log('generic message', level='warning', data={'lol': 'wut?'})
```

As of the writing of this document, response object looks like this:
```json
{
    "err":  0,
    "result":  {
        "id":  "None",
        "uuid":  "daa42187218c469e87599a8d5fa91234"
    }
}
```
