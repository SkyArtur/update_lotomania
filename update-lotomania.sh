#!/usr/bin/env bash

set -euo pipefail

: "${LOTOMANIA_ORIGIN_FILE:=$HOME/Projetos/Python/update_lotomania/src/update_lotomania/files/Lotomania.xlsx}"

: "${LOTOMANIA_DESTINATION_FILE:=$HOME/Projetos/GitHub/API-Lotomania/core/data/file/lotomania.csv}"

export LOTOMANIA_ORIGIN_FILE LOTOMANIA_DESTINATION_FILE


SCRIPT_PATH="$(readlink -f "$0")"
PROJECT_DIR="$(cd "$(dirname "$SCRIPT_PATH")/" && pwd)"
API_DIR="$(cd "$(dirname "$LOTOMANIA_DESTINATION_FILE")/../../../" && pwd)"

# shellcheck disable=SC2164
cd "$PROJECT_DIR"
uv run update-lotomania

cd "$API_DIR"

docker compose -f "$API_DIR/docker/docker-compose.yml" exec api python manage.py atualizar_sorteios
