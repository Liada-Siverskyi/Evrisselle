# Deployment and validation plan

## Goal

Explore a separately selectable Plasma X11 session on openSUSE Tumbleweed x86_64 for a Mac Pro 5,1, while preserving Plasma Wayland as the stable fallback. The X11 attempt has been reported to show a black screen and empty panel. This plan does not authorize or perform changes on the target machine.

## Selected source baseline

The package source targets Plasma 6.8.1. KDE removed the X11 login path and several X11 runtime paths in Plasma 6.8, so the project carries downstream changes in Workspace and packages a separate KWin X11 community fork. Source inputs are pinned in the OBS services. A complete, reproducible build environment and RPM provenance record are not yet in the public repository.

## Work sequence

1. Keep the forward-port audit current, with upstream references and exact source revisions.
2. Diagnose the black screen and empty panel in an isolated, disposable environment. Capture logs and the test setup; do not infer cause from package installation alone.
3. Publish the build environment definition, dependency snapshot, exact build commands, complete logs, and output RPM checksums.
4. Build the matched package set in a disposable openSUSE environment against the documented snapshot.
5. In a disposable VM, validate X11 startup, panel interaction, logout/login, input, display changes, lock/unlock, suspend/resume, X11 applications, Wayland startup, and rollback.
6. Review package transactions and rollback instructions for a future hardware test only after the isolated acceptance checks pass. Do not run that test as part of this source work.
7. Resolve licensing for original Evrisselle materials and publish source, notices, checksums, instructions, and acceptance evidence together.

## Existing reports and evidence limits

Older project notes record a Tumbleweed container build, a disposable-VM X11 login followed by a Wayland login, and a target package transaction on 2026-10-26. The source repository does not include logs or artifacts sufficient to reproduce those reports. The maintainer's later black-screen / empty-panel report means the X11 result cannot be considered accepted. This plan does not claim the current machine state or rely on a current remote inspection.

## Constraints

- No package install, removal, or replacement on the Mac Pro.
- No SDDM restart or session change.
- No permission or access-control change.
- Preserve Wayland and an independently documented recovery route for any future validation.
- Do not claim release readiness based only on a successful build.
