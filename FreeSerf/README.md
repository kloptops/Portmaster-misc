# FreeSerf

# Controls

| Button            | Command                    |
|-------------------|----------------------------|
| **A**             | Mouse Left                 |
| **B**             | Mouse Right                |
| **X**             | Messages                   |
| **L1**            | Toggle overlay             |
| **L2**            | Zoom Out                   |
| **R1**            | Slow down mouse            |
| **R2**            | Zoom In                    |
| **Start**         | Pause                      |
| **D-Pad + Up**    | Button 1                   |
| **D-Pad + Right** | Button 2                   |
| **D-Pad + Down**  | Button 3                   |
| **D-Pad + Left**  | Button 4                   |
| **Select**        | Button 5                   |
| **Left Analog**   | Mouse Movement             |
| **Right Analog**  | Move Screen                |

# Game folder structure

Copy the game files into the `ports/freeserf` folder, depending on whether you have the DOS or Amiga files:

- **DOS**: data file is dependent on the language installed: `SPAE.PA`, `SPAD.PA`, `SPAF.PA`, or `SPAU.PA`. This file has to be from the installed version of the game, use DosBox to install the game to get the file.
- **Amiga**: copy the following files: `gfxheader`, `gfxfast`, `gfxchip`, `gfxpics`, `sounds`, and `music`.

 
## Building


    git clone https://github.com/freeserf/freeserf

    git apply Ports_Patch.diff

    mkdir build

    cd build

    cmake ..

    make -j4

Then copy `FreeSerf` from the `build/src` directory.

# TODO:

- [x] Get game to work.
- [x] Figure out controls
- [x] Make text a bit more readable if possible
- [ ] Test it on AmberELEC
- [ ] Test it on ArkOS

# Thanks

A special thanks to the excellent folks on the [AmberELEC discord](https://discord.com/invite/R9Er7hkRMe), especially Cebion for all the testing.