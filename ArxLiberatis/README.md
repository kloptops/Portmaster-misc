# ArxLiberatis

# Controls

| Button            | Command                    |
|-------------------|----------------------------|
| **A**             | Mouse Left                 |
| **B**             | Mouse Right                |
| **Start**         | ?????                      |
| **Select**        | ??????                     |
| **D-Pad**         | Mouse Movement             |
| **Left Analog**   | Up/Down/Left/Right         |
| **Right Analog**  | Mouse Movement             |


# Game folder structure

 
## Building

    git clone BLAH BLAH

    mkdir build

    cd build

    cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_TOOLS="OFF" -DBUILD_PROFILER_INSTRUMENT="OFF" -DBUILD_CRASHHANDLER="OFF"

    make -j4

    strip arx

At the end you want the `arx` file

# TODO:

- [x] Get game to work.
- [ ] Figure out controls
- [ ] Fix the text
- [ ] Test it on AmberELEC
- [ ] Test it on ArkOS

# Thanks

A special thanks to the excellent folks on the [AmberELEC discord](https://discord.com/invite/R9Er7hkRMe), especially Cebion for all the testing.