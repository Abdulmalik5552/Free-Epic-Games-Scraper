#!/bin/bash
# wait-for-grid.sh

set -e
cd /
set -a # automatically export all variables
source .dockerenv
set +a
cmd="$@"
while ! curl -sSL "http://$SELENIUM_GRID_HOST:4444/wd/hub/status" 2>&1 \
        | jq -r '.value.ready' 2>&1 | grep "true" >/dev/null; do
    echo 'Waiting for the Grid'
    sleep 1
done

cd usr/src/app
>&2 echo "Selenium Grid is up - executing tests"
exec $cmd
