#!/usr/bin/env bash
set -euo pipefail

root=${1:-/}
session="$root/usr/share/xsessions/evrisselle-ionis-undecima.desktop"
wayland="$root/usr/share/wayland-sessions/plasmawayland.desktop"

fail() {
    printf 'FAIL: %s\n' "$1" >&2
    exit 1
}

test -f "$session" || fail "missing Evrisselle X11 session entry: $session"
test -x "$root/usr/bin/startplasma-x11" || fail "missing startplasma-x11"
test -x "$root/usr/bin/kwin_x11" || fail "missing kwin_x11 (install kwin6-x11)"
test -f "$wayland" || fail "missing existing Plasma Wayland session entry: $wayland"

grep -Eq '^Name=Evrisselle Ionis Undecima \(X11\)$' "$session" || fail "X11 entry has the wrong product name"
grep -Eq '^Exec=/usr/bin/startplasma-x11$' "$session" || fail "X11 entry has the wrong Exec path"
grep -Eq '^TryExec=/usr/bin/startplasma-x11$' "$session" || fail "X11 entry has the wrong TryExec path"
grep -Eq '^DesktopNames=KDE$' "$session" || fail "X11 entry does not identify the KDE desktop"

printf 'PASS: Evrisselle X11 session and Plasma Wayland entry are both present.\n'
