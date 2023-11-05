# dRally

# Controls

| Button            | Command                    |
|-------------------|----------------------------|
| **A**             | Accelerate                 |
| **B**             | Brake 			 |
| **D-Pad left**    | steer left		 | 
| **D-Pad right**   | steer right 		 |
| **Left Analog**   | steer right/left           |
| **R1**            | Machine Gun                |
| **R2**            | Turbo Boost                |
| **L1**            | Drop Mine                  |
| **L2**            | Horn                       |
| **Start**         | Enter                      |
| **Select**        | Back                       |
| **Select R2**     | Quick Save                 |
| **Left Analog**   | Quick Load                 |
| **Start up/down** | Text input                 |
| **R1 Select**     | tab               |

# Game folder structure

## Installation - needs original game assets

* [Death Rally registered free windows version CHIP](https://www.chip.de/downloads/Death-Rally-Vollversion_38550689.html)

```sh
7z e -o drally DeathRallyWin_10.exe
cd drally && mkdir CINEM && mv ENDANI* CINEM && mv SANIM* CINEM
echo "./CINEM" &> CDROM.INI
```

Only versions including the DR.IDF file are able to use the `FLAGS += -DDR_CDCHECK`

    dRally
    |--CINEM
    |  |--DR.IDF
    |  |--ENDANI.HAF
    |  |--ENDANI0.HAF
    |  |--SANIM.HAF
    |--CDROM.INI        [1]
    |--ENGINE.BPA
    |--IBFILES.BPA
    |--MENU.BPA
    |--MUSICS.BPA
    |--TR[0-9].BPA

    Make sure these file/dir names in dRally directory are in uppercase.

    [1] CDROM.INI contains relative location of CINEM directory (./CINEM)

## Building

    git clone https://github.com/urxp/dRally.git

    make -j4

The file is named "drally_linux"

# TODO:

- [x] Get game to work.
- [ ] Figure out controls
- [ ] Test it on AmberELEC
- [ ] Test it on ArkOS

# Thanks

A special thanks to the excellent folks on the [PortMaster discord](https://discord.gg/m2QcSkMh).
