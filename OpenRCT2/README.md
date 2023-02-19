# Portmaster-OpenRCT2

# Controls

**TO BE DONE**


To enter text: press **Start + Down**, then use **Up** and **Down** selects the letter, **Left** and **Right** moves forwards and backwards. **Start** or **A** to finish editing.

# Game folder structure

Install your RCT2 game files into `{PORTS}/openrct2/RCT2`, and optionally your RCT1 game files into `{PORTS}/openrct2/RCT1`

For help getting the game files for [RCT2 on macOS & Linux](https://github.com/OpenRCT2/OpenRCT2/wiki/Installation-on-Linux-and-macOS), and for help getting game files for [RCT1](https://github.com/OpenRCT2/OpenRCT2/wiki/Loading-RCT1-scenarios-and-data).

## Required libs

- the following libraries from Debian 11 Bullseye Aarch64
  - libicudata.so.67
  - libicuuc.so.67
  - libzip.so.4

 
## Building

Either my pre-patched repo:

    git clone https://github.com/kloptops/OpenRCT2.git`

or clone the latest version and apply the patch

    git clone https://github.com/kloptops/OpenRCT2.git

    git apply PATH_TO_HERE/SDL_sim_cursor.diff

then just run:

    cd openrct2

    mkdir build

    cd build

    cmake .. -DCMAKE_BUILD_TYPE=MinSizeRel -DDISABLE_GOOGLE_BENCHMARK="ON" -DDISABLE_DISCORD_RPC="ON" -DPORTABLE="ON" -DENABLE_SDL_SIM_CURSOR="ON" -DCMAKE_INSTALL_PREFIX:FILE="engine"

    make -j4

    make install

    rm -f engine.zip
    rm -f engine/bin/libopenrct2.a
    rm -f engine/bin/openrct2-cli

    zip -9r engine.zip engine/

    At the end, you want the `engine.zip`.

# TODO:

- [x] Get a map to work!
- [ ] Figure out controls
- [ ] Make text a bit more readable if possible
- [x] Test it on AmberELEC
- [x] Test it on ArkOS

# Thanks

A special thanks to the excellent folks on the [AmberELEC discord](https://discord.com/invite/R9Er7hkRMe).