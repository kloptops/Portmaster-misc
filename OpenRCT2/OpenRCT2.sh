#!/bin/bash

if [ -d "/opt/system/Tools/PortMaster/" ]; then
  controlfolder="/opt/system/Tools/PortMaster"
elif [ -d "/opt/tools/PortMaster/" ]; then
  controlfolder="/opt/tools/PortMaster"
else
  controlfolder="/roms/ports/PortMaster"
fi

source $controlfolder/control.txt
if [ -z ${TASKSET+x} ]; then
  source $controlfolder/tasksetter
fi

get_controls

## TODO: Change to PortMaster/tty when Johnnyonflame merges the changes in,
CUR_TTY=/dev/tty0

PORTDIR="/$directory/ports"
GAMEDIR="$PORTDIR/openrct2"
cd $GAMEDIR

$ESUDO chmod 666 $CUR_TTY
$ESUDO touch log.txt
$ESUDO chmod 666 log.txt
export TERM=linux
printf "\033c" > $CUR_TTY

printf "\033c" > $CUR_TTY
## RUN SCRIPT HERE

# Extract the game if it exists
if [ -f "$GAMEDIR/engine.zip" ]; then
  if [ -d "$GAMEDIR/engine" ]; then
    echo "Removing old engine." > $CUR_TTY
    $ESUDO rm -fRv "$GAMEDIR/engine" > $CUR_TTY
  fi

  echo "Extracting engine files."
  # Extract the engine from the build zip.
  $ESUDO unzip "$GAMEDIR/engine.zip" > $CUR_TTY
  $ESUDO mv -fv "$GAMEDIR/engine/bin/openrct2" "$GAMEDIR/openrct2" > $CUR_TTY
  $ESUDO rm -f "$GAMEDIR/engine.zip" > $CUR_TTY
fi

if [ -f "RCT2/assets/g1.dat" ]; then
  echo "Missing game files" > $CUR_TTY
  sleep 5
  printf "\033c" > $CUR_TTY
  exit 1
fi

export TEXTINPUTPRESET="Name"
export TEXTINPUTINTERACTIVE="Y"
export TEXTINPUTNOAUTOCAPITALS="Y"
export SDL_GAMECONTROLLERCONFIG="$sdl_controllerconfig"

export LD_LIBRARY_PATH="$GAMEDIR/libs:$LD_LIBRARY_PATH"

$GPTOKEYB "openrct2" -c openrct2.gptk textinput &
$TASKSET ./openrct2 $DEBUGCMDS --user-data-path=save/ --openrct2-data-path=engine/share/openrct2 --rct2-data-path=RCT2/ $RCT1_GAME 2>&1 | $ESUDO tee -a ./log.txt

$ESUDO kill -9 $(pidof gptokeyb)
unset LD_LIBRARY_PATH
unset SDL_GAMECONTROLLERCONFIG
$ESUDO systemctl restart oga_events &

# Disable console
printf "\033c" > $CUR_TTY
