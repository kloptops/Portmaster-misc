# Open Roller Coaster Tycoon 2

# Controls

| Button            | Command                    |
|-------------------|----------------------------|
| **A**             | Mouse Left                 |
| **B**             | Mouse Right                |
| **R1**            | Slow down mouse            |
| **Start**         | ?????                      |
| **Select**        | ??????                     |
| **D-Pad**         | Mouse Movement             |
| **Left Analog**   | Mouse Movement             |


# Game folder structure

 
## Building

Either my pre-patched repo:

    git clone https://github.com/Keriew/augustus.git

    cd augustus

    git apply Force_Software_Cursor.diff

    mkdir build

    cd build

    cmake .. -DCMAKE_BUILD_TYPE=Release

    make -j4

You'll need to copy `build/augustus` and `res/assets`

# TODO:

- [ ] Get a map to work!
- [ ] Figure out controls
- [ ] Make text a bit more readable if possible
- [ ] Test it on AmberELEC
- [ ] Test it on ArkOS

# Thanks

A special thanks to the excellent folks on the [AmberELEC discord](https://discord.com/invite/R9Er7hkRMe), especially Cebion for all the testing.
