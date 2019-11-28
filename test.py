#!/usr/bin/env python3
import os
from leakless import AutoFD, spawn

t = [
  AutoFD.open('/dev/null'),
  AutoFD.open('/dev/null'),
  AutoFD.open('/dev/null'),
  AutoFD.open('/dev/null'),
  AutoFD.open('/dev/null'),
]

del t
assert AutoFD.open('/dev/null').fd < 5

print("my pid", os.getpid())
pid = spawn('/bin/bash', ['/bin/bash', '-c', """
echo outer $PPID $$
( echo l1 $PPID $$; (
  echo l2 $PPID $$
  ls -l /proc/$$/fd
  echo $$
  sleep 10
  echo $$
) & ) &
echo slep
sleep 1
"""], None)

print(os.waitpid(pid))
print("done")
