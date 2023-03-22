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
GAMEDIR="$PORTDIR/vanillatd"
cd $GAMEDIR

$ESUDO chmod 666 $CUR_TTY
$ESUDO touch log.txt
$ESUDO chmod 666 log.txt
export TERM=linux
printf "\033c" > $CUR_TTY

printf "\033c" > $CUR_TTY

## CHECK FOR GAME FILES
shopt -s nocaseglob

for file in "CONQUER.MIX" "DESERT.MIX" "TEMPERAT.MIX" "WINTER.MIX" "SOUNDS.MIX" "CCLOCAL.MIX" "TRANSIT.MIX" "SPEECH.MIX" "UPDATE.MIX" "UPDATEC.MIX" "DESEICNH.MIX" "TEMPICNH.MIX" "WINTICNH.MIX"; do
  if [[ ! -f "${GAMEDIR}/data/vanillatd/${file}" ]]; then
    echo "Missing game files, see README for help installing game files." > $CUR_TTY
    sleep 5
    printf "\033c" >> $CUR_TTY
    exit 1
  fi
done

ALL_FOUND="N"
for path in "gdi" "nod" "."; do
  FiLES_FOUND="Y"

  for file in "GENERAL.MIX" "MOVIES.MIX" "SCORES.MIX"; do
    if [[ ! -f "${GAMEDIR}/data/vanillatd/${path}/${file}" ]]; then
      echo "Missing: ${GAMEDIR}/data/vanillatd/${path}/${file}"
      FiLES_FOUND="N"
      break
    fi
  done

  if [[ "${FiLES_FOUND}" == "Y" ]]; then
    ALL_FOUND="Y"
    break
  fi
done

if [[ "${ALL_FOUND}" == "N" ]]; then
  echo "Missing game files, see README for help installing game files." > $CUR_TTY
  sleep 5
  printf "\033c" >> $CUR_TTY
  exit 1
fi

## RUN SCRIPT HERE

echo "Starting game." > $CUR_TTY

export PORTMASTER_HOME="$GAMEDIR"

$GPTOKEYB "vanillatd" -c vanillatd.gptk &
$TASKSET ./vanillatd 2>&1 | $ESUDO tee -a ./log.txt

$ESUDO kill -9 $(pidof gptokeyb)
unset LD_LIBRARY_PATH
unset SDL_GAMECONTROLLERCONFIG
$ESUDO systemctl restart oga_events &

# Disable console
printf "\033c" > $CUR_TTY
