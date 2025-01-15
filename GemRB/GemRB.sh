#!/bin/bash

XDG_DATA_HOME=${XDG_DATA_HOME:-$HOME/.local/share}

if [ -d "/opt/system/Tools/PortMaster/" ]; then
  controlfolder="/opt/system/Tools/PortMaster"
elif [ -d "/opt/tools/PortMaster/" ]; then
  controlfolder="/opt/tools/PortMaster"
elif [ -d "$XDG_DATA_HOME/PortMaster/" ]; then
  controlfolder="$XDG_DATA_HOME/PortMaster"
else
  controlfolder="/roms/ports/PortMaster"
fi

source $controlfolder/control.txt
[ -f "${controlfolder}/mod_${CFW_NAME}.txt" ] && source "${controlfolder}/mod_${CFW_NAME}.txt"
get_controls

GAMEDIR="/$directory/ports/gemrb"
cd $GAMEDIR

> "$GAMEDIR/log.txt" && exec > >(tee "$GAMEDIR/log.txt") 2>&1

## Converts path names to game codes
PROPER_GAME_ID() {
  GAMENAME=$(echo "$1" | tr '[:upper:]' '[:lower:]')

  case $GAMENAME in
    bg2|baldur*gate\ 2|baldur*gate\ ii)
      echo "bg2"
      ;;
    bg1|baldur*gate)
      echo "bg1"
      ;;
    bg2ee)
      echo "bg2ee"
      ;;
    pst|planescape*)
      echo "pst"
      ;;
    how|*how*|*totl*)
      echo "how"
      ;;
    iwd|icewind\ dale)
      echo "iwd"
      ;;
    iwd2|icewind\ dale\ 2)
      echo "iwd2"
      ;;
    demo)
      echo "demo"
      ;;
    *)
      echo $GAMENAME
      ;;
  esac
}

## Converts path name to proper name
PROPER_GAME_NAME() {
  GAMEID=$(PROPER_GAME_ID "$1")
  case $GAMEID in
    bg1)
      echo "Baldurs Gate"
      ;;
    bg2)
      echo "Baldurs Gate II"
      ;;
    bg2ee)
      echo "Baldurs Gate II EE"
      ;;
    pst)
      echo "Planescape Torment"
      ;;
    how)
      echo "Icewind Dale - HoW or ToTL"
      ;;
    iwd)
      echo "Icewind Dale"
      ;;
    iwd2)
      echo "Icewind Dale 2"
      ;;
    demo)
      echo "Demo Game"
      ;;
    *)
      echo "$1"
      ;;
  esac
}

# Extract the game if it exists
if [ -f "$GAMEDIR/engine.zip" ]; then
  if [ -d "$GAMEDIR/engine" ]; then
    $ESUDO echo "Removing old engine."
    $ESUDO rm -fRv "$GAMEDIR/engine"
  fi
  # Extract the engine from the build zip.
  $ESUDO unzip "$GAMEDIR/engine.zip"
  $ESUDO mv -fv "$GAMEDIR/engine/gemrb" "$GAMEDIR/gemrb"
  $ESUDO rm -f "$GAMEDIR/engine.zip"
fi

# Copy over the demo game
if [ -d "$GAMEDIR/engine/demo" ]; then
  # Copy demo over, but dont overwrite just incase it has been modified.
  if [ -d "$GAMEDIR/games/demo" ]; then
    $ESUDO rm -fRv "$GAMEDIR/engine/demo"
  else
    $ESUDO mv -fv "$GAMEDIR/engine/demo" "$GAMEDIR/games/demo"
  fi
fi

## TODO: add a new game selector, lmao.
## CHANGE THIS TO WHATEVER GAME YOU WANT
GAME="demo"

# Install appropriate GemRB.cfg
GAMEID=$(PROPER_GAME_ID "$GAME")

if [ ! -f "${GAMEDIR}/games/${GAME}/GemRB.cfg" ]; then
  if [ -f "${GAMEDIR}/configs/GemRB.cfg.${GAMEID}" ]; then
    # Does one for this game exist?
    $ESUDO cp -v "${GAMEDIR}/configs/GemRB.cfg.${GAMEID}" "${GAMEDIR}/games/${GAME}/GemRB.cfg"
  else
    # Otherwise use the default one
    $ESUDO cp -v "${GAMEDIR}/configs/GemRB.cfg.default" "${GAMEDIR}/games/${GAME}/GemRB.cfg"
  fi
fi

# Use game specific controller config if it exists.
if [ -f "${GAMEDIR}/gemrb-${GAMEID}.gptk" ]; then
  GPTOKEYB_CFG="${GAMEDIR}/gemrb-${GAMEID}.gptk"
else
  GPTOKEYB_CFG="${GAMEDIR}/gemrb.gptk"
fi

export TEXTINPUTPRESET="Name"
export TEXTINPUTINTERACTIVE="Y"
export TEXTINPUTNOAUTOCAPITALS="Y"
export SDL_GAMECONTROLLERCONFIG="$sdl_controllerconfig"

export PYTHONHOME="$GAMEDIR"
export LD_LIBRARY_PATH="$GAMEDIR/lib:$GAMEDIR/engine:$LD_LIBRARY_PATH"

$GPTOKEYB "gemrb" -c "${GPTOKEYB_CFG}" textinput &
pm_platform_helper "$GAMEDIR/gemrb"
$ESUDO $GAMEDIR/gemrb -c "${GAMEDIR}/games/${GAME}/GemRB.cfg" "${GAMEDIR}/games/${GAME}/"

pm_finish
