#!/bin/bash

clang -dynamiclib -std=gnu99 iohid_wrap.m -current_version 1.0 -compatibility_version 1.0 -lobjc -framework Foundation -framework AppKit -framework CoreFoundation -o iohid_wrap.dylib
