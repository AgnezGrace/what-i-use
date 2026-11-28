# Foundation test report — v0.1.0

Executed locally with Python 3.13.5, standard library only.

- `python scripts/validate.py`: PASS — required files, metadata, registry validation and local Markdown links.
- `python scripts/validate.py --lookup attention`: PASS — unlisted, no matches (the shipped catalog is intentionally empty).
- `python -m unittest discover -s tests -v`: PASS — 11 test methods, including subtests for invalid profiles, unsafe paths, duplicate categories and manifestations, broken references, ambiguous aliases, future module registration, and invalid adapter metadata.

Future module and adapter fixtures were created in temporary directories, not shipped as registered catalog content. Empty registry tests use fixtures so they remain valid after catalog expansion. The tests establish structural extensibility and reject selected malformed inputs. They do not assess real-world psychology, actual agent routing obedience, semantic personality composition, external platform compatibility, model output quality, or token savings. Sixteen behavioral evaluation scenarios are supplied but have not been executed against a model. No external service was called.
