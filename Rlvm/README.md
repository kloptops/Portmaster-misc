# Portmaster-Rlvm


This is the configuration files and the required steps to build the rlvm engine for handheld emulator devices (Anbernic RG353V, etc.) using the Portmaster scripts for launching.


# Installation

Use portmaster to install rlvm, copy the desired game or games into `{PORTFOLDER}/rlvm/games/{GAMENAME}`. On launch it will ask you to choose the game if it detects multiple games.

# Controls

- L1/B: Right Click
- L2: Fast Forward
- R1/R2/A: Left Click
- Start: enter
- Select: escape
- Left Analog Stick: Move cursor
- Select + L1: display system info

## Required libs

- [Gl4es](https://github.com/ptitSeb/gl4es)
    built with: cmake .. -DNOX11=ON -DGLX_STUBS=ON -DEGL_WRAPPER=ON -DGBM=ON
- [libsdl1.2-compat](https://github.com/libsdl-org/sdl12-compat)
    built with no fancy options.
- the following libraries from Debian 11 Bullseye Aarch64
  - libboost_filesystem.so.1.74.0
  - libboost_iostreams.so.1.74.0
  - libboost_program_options.so.1.74.0
  - libboost_serialization.so.1.74.0
  - liblzma.so.5
  - libbrotlicommon.so.1
  - libbrotlidec.so.1
  - libfreetype.so.6
  - liblzma.so.5

## Building

    git clone https://github.com/kloptops/rlvm.git

    cd rlvm

    scons --puresdl --release --portmaster


At the end, the `build/rlvm` file is what you want.


# TODO:

- [x] Auto detect which games are found in the games directory, bring up a list if there is more than 1 game detected.
- [ ] Add option to add a launch script in the ports folder, for direct launching of the game, so game info can be scraped.
- [ ] Write installation instructions.
- [ ] Write better info
- [ ] Fix HD games
- [ ] Fix resolution 
- [x] Figure out controls.
- [x] Figure out why menus are crashing.
- [x] Fix save file location
- [x] Fix font searching


# Thanks

A special thanks to the excellent folks on the [AmberELEC discord](https://discord.com/invite/R9Er7hkRMe), and HyperActiv for getting the idea of this working stuck in my head, and Cebion for testing and encouragement.

Also thanks to [Christian Haitian](https://github.com/christianhaitian) for the excellent work with [PortMaster](https://github.com/christianhaitian/PortMaster) (and PortMaster.sh which I used heavily to get the dialog stuff to work!).
