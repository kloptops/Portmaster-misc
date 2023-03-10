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
GAMEDIR="$PORTDIR/rttr"
cd $GAMEDIR

$ESUDO chmod 666 $CUR_TTY
$ESUDO touch log.txt
$ESUDO chmod 666 log.txt
export TERM=linux
printf "\033c" > $CUR_TTY

printf "\033c" > $CUR_TTY
## CHECK FOR GAME FILES

if [[ ! -f S2/GFX/PALETTE/PAL5.BBM ]]; then
  echo "Missing game files." > /dev/tty1
  sleep 5
  printf "\033c" >> /dev/tty1
  exit 1
fi


## RUN SCRIPT HERE

echo "Starting game." > $CUR_TTY

export LIBGL_ES=2
export LIBGL_GL=21
export LIBGL_FB=4
export LD_LIBRARY_PATH="$GAMEDIR/libs:"

$GPTOKEYB "s25client" -c rttr.gptk &
$TASKSET bin/s25client 2>&1 | $ESUDO tee -a ./log.txt

$ESUDO kill -9 $(pidof gptokeyb)
unset LD_LIBRARY_PATH
unset SDL_GAMECONTROLLERCONFIG
$ESUDO systemctl restart oga_events &

# Disable console
printf "\033c" > $CUR_TTY
