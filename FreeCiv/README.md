# FreeCiv

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


    git clone https://github.com/freeciv/freeciv

    git apply JANKY_STUFF.diff

    mkdir build

    cd build

    CFLAGS="-DALWAYS_ROOT" ../configure --enable-client=sdl2 --enable-fcmp=no --prefix="$PWD/engine"

edit gen_headers/fc_config.h, comment out `FREECIV_STORAGE_DIR`

edit gen_headers/freeciv_config.h, modify the line with `FREECIV_STORAGE_DIR` to:

    #undef BINDIR
    #define BINDIR "bin"

    /* Location for freeciv to store its information */
    #define FREECIV_STORAGE_DIR "saves"

then you can continue making:

    make -j4

    make install

    cd engine

    mv shared/freeciv data
    strip bin/*

the files you want are `bin/` and `data/`


# TODO:

- [x] Get game to work.
- [ ] Figure out controls
- [ ] Test it on AmberELEC
- [ ] Test it on ArkOS

# Thanks

A special thanks to the excellent folks on the [AmberELEC discord](https://discord.com/invite/R9Er7hkRMe), especially Cebion for all the testing.