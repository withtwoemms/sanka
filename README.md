# sanka
> a function decorator for surfacing dead code

[![tests](https://github.com/withtwoemms/sanka/workflows/tests/badge.svg)](https://github.com/withtwoemms/sanka/actions?query=workflow%3Atests)
[![publish](https://github.com/withtwoemms/sanka/workflows/publish/badge.svg)](https://github.com/withtwoemms/sanka/actions?query=workflow%3Apublish)
[![codecov](https://codecov.io/gh/withtwoemms/sanka/branch/main/graph/badge.svg?token=95KK3WG5QW)](https://codecov.io/gh/withtwoemms/sanka)

# Quick start

The "examples/" directory is home to `sanka` use cases.
```
examples/
├── actionpack/
│   ├── example.py
│   └── requirements.txt
└── ...
```
A docker image capable of running an example can be built using a `nox` command:
```
EXAMPLE=actionpack nox -s image
```
where the example referenced in the image can be specified using the "EXAMPLE" environment variable.
To run a container, execute something like the following:
```
docker run -e RUN_DURATION_SECONDS=10 -e CALL_DELAY_SECONDS=5 sanka:0.3.0
```

# Setup

Ensure `nox` is installed.
```
pip install nox
```
Run `nox` to install `sanka` and run tests.

# Usage

### the basics

Decorate any funciton with `@sanka`.
```python
@sanka
def function():
    pass
```
The decorator instance tracks function calls so the call count can be gotten as follows:
```
function(YaDead)  #=> returns number of times `function` was called
```

### callbacks

One can also pass a callback argument to the `@sanka` decorator:
```python
from string import Template

report = Template('Called $f called $this_many times')

callback: Callable[[int], None] = lambda tally: print(
    "Ya, mon."
    if tally == 0
    else report.substitute(f=str(function), this_many=tally)
)

@sanka(callback=callback)
def function():
    pass
```
The callback is expected to be a single-parameter function that accepts an `int`.
This `int` is the latest tally for the number of times the decorated function has been called.
To access the call count for the docorated function, just ask `@sanka` if it's "dead":
```python
function(YaDead)
```
and as per the example you'd get this response if the function had never been called:
```
Ya, mon.
```

### callback control

By default, callbacks are only executed when `YaDead` is passed.
The callback can be executed _on every function call_ if desired.
```python
@sanka(callback=callback, only_callback_when_dead=False)
def function():
    pass
```
Now, every time `function` is called, the `callback` will also be called.

