## Leakless

Leakless is a Python 3 library for manipulating low-level UNIX calls, in such a way that you're less likely to leak external resources.

#### AutoFD

The `AutoFD` class wraps an integer file descriptor and will automatically `close()` it when garbage collected.

You could imagine doing the same thing with `__del__()` methods, or judicious use of `try: ... finally: ...` and context managers, but this goes further that what's possible from pure Python.

#### Subreaper

Provides something like `os.spawnve`, except that it wraps the child process such that grandchild processes are killed when the primary child process exits.

This feature is Linux-only. It's based on PR_SET_CHILD_SUBREAPER.

Processes killed by the subreaper wrapper are given a few seconds to respond to a `SIGTERM` before being `SIGKILL`ed.

### Notes

Leakless makes no attempt at thread-safety. Its classes are not threadsafe, and some of its guarantees (namely, always setting `CLOEXEC`) can race with a `fork()` call happening in another thread. That said, it's probably fine for most threaded python use-cases.

This library is currently highly untested, and I'm not even using it for real yet, so... don't trust it.
