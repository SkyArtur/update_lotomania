#!/bin/bash

: "${LOTOMANIA_ORIGIN_FILE:=$HOME/Projetos/Python/update_lotomania/src/update_lotomania/files/Lotomania.xlsx}"

: "${LOTOMANIA_DESTINATION_FILE:=$HOME/Projetos/GitHub/API-Lotomania/core/data/file/lotomania.csv}"

export LOTOMANIA_ORIGIN_FILE LOTOMANIA_DESTINATION_FILE

# shellcheck disable=SC2164
cd "$HOME"/Projetos/Python/update_lotomania/

uv run update-lotomania
