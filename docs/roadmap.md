# Roadmap

## MVP acceptance

The MVP is ready for a private test when a clean OBS build succeeds for the target Tumbleweed repository and, in an isolated VM:

1. The existing Plasma Wayland choice remains available.
2. `Evrisselle Ionis Undecima` appears as a separate X11 choice in the login manager.
3. The X11 session starts, opens a Plasma desktop, and survives logout/login cycles.
4. Basic input, display changes, locking, logout, suspend/resume, and X11 application launch work.
5. Removing the session package leaves the ordinary Wayland session usable.
6. The published package source, patch, spec, and required notices are available together.

## Milestones

| Milestone | State | Output |
| --- | --- | --- |
| Confirm Tumbleweed package/source state | Done | `docs/technical-audit.md` |
| Restore and brand the 6.7.5 X11 session in packaging | Prepared, unbuilt | OBS RPM spec and patch |
| Produce a clean OBS build | Not started | Successful Tumbleweed build result |
| Install and exercise in an isolated VM | Not started | Recorded acceptance results |
| Publish the MVP source and packages | Not started | Public repository after acceptance |
| Track 6.7.x fixes and security issues | Not started | Best-effort update cadence |
| Decide how to handle Plasma 6.8+ | Later | Compatible package-set pin or tested X11 forward-port |

## Release rule

Do not label the prototype a supported release until the clean build and VM acceptance checks pass. Do not install the rebuilt package set onto the maintainer's daily system as the first test.

