# PortMaster - Miscellaneous

This repo is for miscellaneous ports that don't require a full port for each release. Eventually I may combine the repos to keep all my stuff together.


# General structure.

- Port Name
  - build/
    - Files that get built for this port live here, but won't be commited to the repo
  - portname/
    - files & scripts that are needed for the port to work
  - Port Name.sh
    - the file that is run to start the game.
  - build_zip.json
    - the file used to build a release zip.


# Current Ports

| Port                 | Description / Info                                                                                                                                                               | Download                      |     Status      |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|:---------------:|
| [Aquaria][AquP]      | Using [Aquaria][AquG] which is the continuation of the open sourced game Aquaria.                                                                                                | [Aquaria Download][AquD]      | :red_circle:    |
| [ArxLiberatis][ArxP] | Using [ArxLiberatis][ArxG] which is based on the publicly released Arx Fatalis source code.                                                                                      | [ArxLiberatis Download][ArxD] | :orange_circle: |
| [Augustus][AugP]     | Using [Augustus][AugG]                                                                                                                                                           | [Augustus Download][AugD]     | :green_circle:  |
| [dRally][DraP]       | Using [dRally][Drag]  a port of Death Rally (1996) running natively on Linux and BSD based operating systems.                                                                    | [dRally Download][DraD]       | :green_orange:  |
| [Fallout 1][Fo1P]    | Using [fallout1-ce][Fo1G]                                                                                                                                                        | [Fallout 1 Download][Fo1D]    | :green_circle:  |
| [FreeCiv][FrcP]      | Using [FreeCiv][FrcG] is a Free and Open Source empire-building strategy game inspired by the history of human civilization.                                                     | [FreeCiv Download][FrcD]      | :orange_circle: |
| [FreeSerf][FrsP]     | Using [FreeSerf][FrsG] which is a faithful clone of the brilliant simulation game The Settlers 1 aka Serf City.                                                                  | [FreeSerf Download][FrsD]     | :green_circle:  |
| [GemRB][GrbP]        | Using [GemRB][GrbG] the open-source reimplementation of the Infinity Engine that underpinned Baldur's Gate, Icewind Dale and Planescape: Torment.                                | [GemRB Download][GrbD]        | :green_circle:  |
| [Half-Life][HalP]    | Using [Xash3D-FWGS][HalG], a game engine, aimed to provide compatibility with Half-Life Engine, and [hlsdk-portable][HalO] for the client binaries.                              | [Half-Life Download][HalD]    | :green_circle:  |
| [Half-Life 2][Hl2P]  | Using [source-engine][Hl2G], play Half-Life 2                                                                                                                                    | [Half-Life 2 Download][Hl2D]  | :orange_circle: |
| [OpenFodder][OpfP]   | Using [OpenFodder][OpfG] is an open source version of the Cannon Fodder engine, for modern operating systems.                                                                    | [OpenFodder Download][OpfD]   | :green_circle:  |
| [OpenRCT2][OrcP]     | Using [OpenRCT2][OrcG] an open-source re-implementation of RollerCoaster Tycoon 2, a construction and management simulation video game that simulates amusement park management. | [OpenRCT2 Download][OrcD]     | :green_circle:  |
| [Rlvm][RlvP]         | Using [Rlvm][RlvG] a Free Software reimplementation of the VisualArt's KK's RealLive interpreter.                                                                                | [Rlvm Download][RlvD]         | :green_circle:  |
| [Rttr][RttP]         | [Rttr][RttG] is a Settlers II clone.                                                                                                                                             | [Rttr Download][RttD]         | :red_circle:    |
| [VanillaRA][VraP]    | Built using [VanillaConquer][VraG] is a fully portable version of the first generation C&C engine and is capable of running Red Alert on multiple platforms.                     | [VanillaRA Download][VraD]    | :green_circle:  |
| [VanillaTD][VtdP]    | Built using [VanillaConquer][VtdG] is a fully portable version of the first generation C&C engine and is capable of running Tiberian Dawn on multiple platforms.                 | [VanillaTD Download][VtdD]    | :green_circle:  |
| [VCMI][VcmP]         | Built using [VCMI][VcmG] the open source engine for Heroes of Might and Magic III                                                                                                | [VCMI Download][VcmD]         | :green_circle:  |

Legend:
- :green_circle: - Working, available on Portmaster
- :orange_circle: - Runs, but not complete, not available on Portmaster yet
- :red_circle: - Work in progress

[AquP]: https://github.com/kloptops/Portmaster-misc/tree/main/Aquaria
[AquG]: https://github.com/AquariaOSE/Aquaria
[AquD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/Aquaria.zip

[ArxP]: https://github.com/kloptops/Portmaster-misc/tree/main/ArxLiberatis
[ArxG]: https://github.com/arx/ArxLibertatis
[ArxD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/ArxLiberatis.zip

[AugP]: https://github.com/kloptops/Portmaster-misc/tree/main/Augustus
[AugG]: https://github.com/Keriew/augustus
[AugD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/Augustus.zip

[DraP]: https://github.com/kloptops/Portmaster-misc/tree/main/dRally
[DraG]: https://github.com/urxp/dRally
[DraD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/dRally.zip

[Fo1P]: https://github.com/kloptops/Portmaster-misc/tree/main/Fallout%201
[Fo1G]: https://github.com/alexbatalov/fallout1-ce
[Fo1D]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/Fallout1.zip

[FrcP]: https://github.com/kloptops/Portmaster-misc/tree/main/FreeCiv
[FrcG]: https://github.com/freeciv/freeciv
[FrcD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/FreeCiv.zip

[FrsP]: https://github.com/kloptops/Portmaster-misc/tree/main/FreeSerf
[FrsG]: https://github.com/freeserf/freeserf
[FrsD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/FreeSerf.zip

[GrbP]: https://github.com/kloptops/Portmaster-misc/tree/main/GemRB
[GrbG]: https://github.com/gemrb/gemrb
[GrbD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/GemRB.zip

[HalP]: https://github.com/kloptops/Portmaster-misc/tree/main/Half-Life
[HalG]: https://github.com/FWGS/xash3d-fwgs
[HalO]: https://github.com/FWGS/hlsdk-portable
[HalD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/Half-Life.zip

[Hl2P]: https://github.com/kloptops/Portmaster-misc/tree/main/Half-Life%202
[Hl2G]: https://github.com/nillerusr/source-engine
[Hl2D]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/Half-Life2.zip

[OpfP]: https://github.com/kloptops/Portmaster-misc/tree/main/OpenFodder
[OpfG]: https://github.com/OpenFodder/openfodder
[OpfD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/OpenFodder.zip

[OrcP]: https://github.com/kloptops/Portmaster-misc/tree/main/OpenRCT2
[OrcG]: https://github.com/kloptops/OpenRCT2
[OrcD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/OpenRCT2.zip

[RlvP]: https://github.com/kloptops/Portmaster-misc/tree/main/Rlvm
[RlvG]: https://github.com/kloptops/rlvm
[RlvD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/Rlvm.zip

[RttP]: https://github.com/kloptops/Portmaster-misc/tree/main/Rttr
[RttG]: https://github.com/Return-To-The-Roots/s25client
[RttD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/Rttr.zip

[VraP]: https://github.com/kloptops/Portmaster-misc/tree/main/VanillaRA
[VraG]: https://github.com/TheAssemblyArmada/Vanilla-Conquer
[VraD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/VanillaRA.zip

[VtdP]: https://github.com/kloptops/Portmaster-misc/tree/main/VanillaTD
[VtdG]: https://github.com/TheAssemblyArmada/Vanilla-Conquer
[VtdD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/VanillaTD.zip

[VcmP]: https://github.com/kloptops/Portmaster-misc/tree/main/VCMI
[VcmG]: https://vcmi.eu
[VcmD]: https://github.com/kloptops/Portmaster-misc/raw/main/releases/VCMI.zip
