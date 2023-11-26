# Widelands

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


    git clone https://github.com/widelands/widelands.git

    git apply GL_fixes.diff

    cmake .. -DCMAKE_BUILD_TYPE=Release -DOPTION_TSAN="OFF" -DOPTION_USE_GLBINDING="ON" -DCMAKE_INSTALL_PREFIX:FILE="engine"

    make -j4


# TODO:

- [ ] Get game to work.
- [ ] Figure out controls
- [ ] Make text a bit more readable if possible
- [ ] Test it on AmberELEC
- [ ] Test it on ArkOS

# Thanks

A special thanks to the excellent folks on the [AmberELEC discord](https://discord.com/invite/R9Er7hkRMe), especially Cebion for all the testing.