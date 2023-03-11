# Rttr

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


    git clone https://github.com/Return-To-The-Roots/s25client

    git apply path_to/GLES_fixes.diff

    mkdir build

    cd build

    cmake .. -DBUILD_TESTING=OFF -DCMAKE_BUILD_TYPE=Release -DFETCHCONTENT_FULLY_DISCONNECTED=ON -DRTTR_USE_SYSTEM_LIBS=ON -DRTTR_INCLUDE_DEVTOOLS=OFF -DRTTR_OPENGL=GLES2.0Compat -DRTTR_DATADIR="." -DRTTR_DRIVERDIR="libs" -DRTTR_LIBDIR="libs" -DRTTR_GAMEDIR="S2" -DCMAKE_INSTALL_PREFIX:FILE="engine"

    make -j4

    make install


the files you want are in `build/engine`


# TODO:

- [ ] Get game to work.
- [ ] Figure out controls
- [ ] Make text a bit more readable if possible
- [ ] Test it on AmberELEC
- [ ] Test it on ArkOS

# Thanks

A special thanks to the excellent folks on the [AmberELEC discord](https://discord.com/invite/R9Er7hkRMe), especially Cebion for all the testing.