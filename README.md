# sanka
a function decorator for surfacing dead code

# Setup
Ensure `nox` is installed.
```
pip install nox
```
Run `nox` to install `sanka` and run tests.

# Usage
Decorate any funciton with `@Sanka`.
```python
@Sanka
def function():
    pass
```
The decorator instance tracks function calls so the call count can be gotten as follows:
```
function(Sanka.YaDead)
```
