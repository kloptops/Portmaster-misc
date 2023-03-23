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
GAMEDIR="$PORTDIR/vanillara"
cd $GAMEDIR

$ESUDO chmod 666 $CUR_TTY
$ESUDO touch log.txt
$ESUDO chmod 666 log.txt
export TERM=linux
printf "\033c" > $CUR_TTY

printf "\033c" > $CUR_TTY

## CHECK FOR GAME FILES
CHECK_REDALERT="N"
CHECK_MAIN="N"
shopt -s nocaseglob

for path in "soviet" "allied" "."; do 
  if [[ "$CHECK_REDALERT" == "N" ]] && [[ -f "${GAMEDIR}/data/vanillara/${path}/REDALERT.MIX" ]]; then
    CHECK_REDALERT="Y"
  fi

  if [[ "$CHECK_MAIN" == "N" ]] && [[ -f "${GAMEDIR}/data/vanillara/${path}/MAIN.MIX" ]]; then
    CHECK_MAIN="Y"
  fi

  if [[ "${CHECK_REDALERT}" == "Y" ]] && [[ "${CHECK_MAIN}" == "Y" ]]; then
    break
  fi
done

if [[ "${CHECK_REDALERT}" == "N" ]] || [[ "${CHECK_MAIN}" == "N" ]]; then
  echo "Missing game files, see README for help installing game files." > $CUR_TTY
  if [[ "${CHECK_REDALERT}" == "N" ]]; then
    echo "Unable to find REDALERT.MIX." > $CUR_TTY
  fi

  if [[ "${CHECK_MAIN}" == "N" ]]; then
    echo "Unable to find MAIN.MIX." > $CUR_TTY
  fi

  sleep 5
  printf "\033c" >> $CUR_TTY
  exit 1
fi

## RUN SCRIPT HERE
echo "Starting demo." > $CUR_TTY

export PORTMASTER_HOME="$GAMEDIR"

$GPTOKEYB "vanillara" -c vanillara.gptk &
$TASKSET ./vanillara 2>&1 | $ESUDO tee -a ./log.txt

$ESUDO kill -9 $(pidof gptokeyb)
unset LD_LIBRARY_PATH
unset SDL_GAMECONTROLLERCONFIG
$ESUDO systemctl restart oga_events &

# Disable console
printf "\033c" > $CUR_TTY
