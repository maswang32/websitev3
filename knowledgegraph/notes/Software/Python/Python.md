# Python Projects
## pyproject.toml
This tells us the package metadata, like the package name and version.

toml projects are headers like [project], beneath which are key-value pairs.

Minimal example:

```
[project]
name = "soundmaker"
version = "0.1.0"
```

You run `pip install -e .` in the same directory as pyproject.toml.


## Structure

Usually, you have
```
soundmaker/
--pyproject.toml
--src/
----soundmaker/
------__init__.py
--tests/
```

The actual package, which is importated with `import soundmaker`, is the soundmaker folder in the src folder. The repo is the outer folder called soundmaker.



Last Reviewed 10/12/2026