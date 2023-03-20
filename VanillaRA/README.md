# VanillaRA

# Controls

| Button            | Command                    |
|-------------------|----------------------------|
| **A**             | Mouse Left                 |
| **B**             | Mouse Right                |
| **X**             | Stop                       |
| **Y**             | Guard                      |
| **Select + R1**   | Select next unit           |
| **Select + L1**   | Select all units on screen |
| **L1**            | Slow down mouse            |
| **L2**            | Add to selection           |
| **R1**            | Slow down mouse            |
| **R2**            | Force move                 |
| **Start**         | Enter                      |
| **Select**        | Menu                       |
| **D-Pad Up**      | Group 1                    |
| **D-Pad Right**   | Group 2                    |
| **D-Pad Down**    | Group 3                    |
| **D-Pad Left**    | Group 4                    |
| **Left Analog**   | Mouse Movement             |
| **Right Analog**  | Move screen                |


# Game folder structure

You will need to place at least `MAIN.MIX` & `READALERT.MIX` into `ports/vanillara/data/vanillara`.

You can get the game files from [here](https://github.com/TheAssemblyArmada/Vanilla-Conquer#vanillatd-and-vanillara).

For multiple cd's for the campaigns & expansions it is a little more complex.

Follow the installation instructions from [here](https://github.com/TheAssemblyArmada/Vanilla-Conquer/wiki/Installing-VanillaRA).

If you want to use the expansions you will need the files from the patch 3.03, [available here](https://www.moddb.com/games/cc-red-alert/downloads/red-alert-303-beta-english-patch).

For multiple cd's and expansions you need the data folder laid out like this:

```
ports/vanillara/data/vanillara
  ├─ REDALERT.MIX             # From CD1 or CD2
  ├─ soviet/                  # From CD1
  │  ├─ MAIN.MIX
  ├─ allied/                  # From CD2
  │  ├─ MAIN.MIX
  ├─ counterstrike/           # From CD3 -- 1st Expansion
  │  ├─ MAIN.MIX
  ├─ aftermath/               # From CD4 -- 2nd Expansion
  │  ├─ MAIN.MIX
  ├─ EXPAND.MIX               # From Patch 3.03
  ├─ EXPAND2.MIX
  ├─ HIRES1.MIX
  ├─ LORES1.MIX
```

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
- [x] Get expansions to work.
- [ ] Figure out controls
- [x] Test it on AmberELEC
- [x] Test it on ArkOS

# Thanks

A special thanks to the excellent folks on the [AmberELEC discord](https://discord.com/invite/R9Er7hkRMe), especially Cebion for all the testing.