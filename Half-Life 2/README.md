# Half-Life 2

# Installation

# Controls



## Building

    git clone --recursive --depth 1 https://github.com/nillerusr/source-engine.git

    # Build source-engine
    cd source-engine

    ## 
    ./waf configure -T release --64bits --togles
    ./waf clean
    ./waf build
    ./waf install --destdir=../build2

At the end all the binary stuff is in `../build2/usr/local`.

# TODO:

- [ ] game runs
