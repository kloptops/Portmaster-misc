# VanillaTD

# Controls

| Button            | Command                    |
|-------------------|----------------------------|
| **A**             | Mouse Left                 |
| **B**             | Mouse Right                |
| **R1**            | Slow down mouse            |
| **Start**         | ?????                      |
| **Select**        | ??????                     |
| **D-Pad**         | Move Screen                |
| **Left Analog**   | Mouse Movement             |


# Game folder structure

You will need to place GAME_FILES into `ports/vanillatd/data/vanillatd`.

You can get the game files from [here](https://github.com/TheAssemblyArmada/Vanilla-Conquer#vanillatd-and-vanillara)

## Building

    git clone https://github.com/TheAssemblyArmada/Vanilla-Conquer.git

    git apply DATA_PATHS.diff

    mkdir build

    cd build

    cmake .. -DCMAKE_BUILD_TYPE=Release

    make -j4

You will then have `vanillara` & `vanillatd`

# TODO:

- [x] Get game to work.
- [ ] Figure out controls
- [ ] Test it on AmberELEC
- [ ] Test it on ArkOS

# Thanks

A special thanks to the excellent folks on the [AmberELEC discord](https://discord.com/invite/R9Er7hkRMe), especially Cebion for all the testing.