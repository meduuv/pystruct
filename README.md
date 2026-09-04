# pystruct

Dependency-free helpers for turning Python values into predictable structured representations.

## Features

- Recursive normalization of mappings and sequences
- Dataclass conversion
- JSON-safe primitive conversion
- Stable output for inspection and serialization

## Usage

```python
from pystruct import normalize

print(normalize({"name": "medu", "items": {1, 2}}))
```

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

https://guns.lol/meduu
