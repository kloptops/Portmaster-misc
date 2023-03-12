# VanillaRA

# Controls

| Button            | Command                    |
|-------------------|----------------------------|
| **A**             | Mouse Left                 |
| **B**             | Mouse Right                |
| **X**             | Stop                       |
| **Y**             | Repair                     |
| **Select + A**    | Force Attack               |
| **Select + B**    | Guard                      |
| **Select + X**    | Scatte                     |
| **Select + Y**    | Sell                       |
| **R1**            | Slow down mouse            |
| **Start**         | Enter                      |
| **Select**        | Menu                       |
| **D-Pad**         | Move Screen                |
| **Left Analog**   | Mouse Movement             |


# Game folder structure

You will need to place at least `MAIN.MIX` & `READALERT.MIX` into `ports/vanillara/data/vanillara`.

For multiple cd's you need to do:

- `ports/vanillara/data/vanillara`
  - `READALERT.MIX`
  - `soviet` -- CD1
    - `MAIN.MIX`
  - `allied` -- CD2
    - `MAIN.MIX`
  - `counterstrike` -- First Expansion
    - `MAIN.MIX`
  - `aftermath` -- Second Expansion
    - `MAIN.MIX`

You can get the game files from [here](https://github.com/TheAssemblyArmada/Vanilla-Conquer#vanillatd-and-vanillara)

## Building

    git clone https://github.com/TheAssemblyArmada/Vanilla-Conquer.git

    git apply DATA_PATHS.diff

    mkdir build

    cd build

    cmake .. -DCMAKE_BUILD_TYPE=Debug

    make -j4

    strip vanilla*

You will then have `vanillara` & `vanillatd`

# TODO:

- [x] Get game to work.
- [ ] Figure out controls
- [ ] Test it on AmberELEC
- [ ] Test it on ArkOS

# Thanks

A special thanks to the excellent folks on the [AmberELEC discord](https://discord.com/invite/R9Er7hkRMe), especially Cebion for all the testing.