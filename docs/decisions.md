# Project decisions

| Topic | Decision |
| --- | --- |
| Umbrella project | Evrisselle |
| First product | Evrisselle Ionis Undecima |
| Purpose | Explore a separately selectable Plasma X11 session for users who need X11 |
| First distribution | openSUSE Tumbleweed x86_64 |
| Target baseline | Plasma 6.8.1 source and package family |
| Target hardware | Mac Pro 5,1; no hardware validation is claimed here |
| Session model | X11 and Wayland are separate choices; preserve Wayland as the stable fallback |
| Initial implementation | Downstream forward-port of removed X11 session and runtime paths |
| KWin | Pinned SonicDE `sonic-win` community fork, packaged separately as `kwin6-x11` |
| Maintenance | Solo maintainer, best-effort updates, no SLA |
| Public release | Only after diagnosis, reproducible build evidence, licensing decisions, and acceptance checks |

## Current engineering assessment

The package source attempts to restore the X11 startup path in Plasma Workspace and uses a separate KWin X11 implementation. The maintainer reports that an earlier X11 experiment produced a black screen and empty panel. The failure is unresolved; a usable X11 desktop is not established.

Earlier repository notes report that the matched RPM set built in an isolated Tumbleweed environment and that both X11 and Wayland started in a disposable VM. The checked-in repository does not include the build logs, exact dependency snapshot, VM transcript, or resulting RPM checksums needed to reproduce those results. Treat them as historical reports, not independently verifiable acceptance evidence.

## Release and safety boundary

- Do not describe this port as a working or installable X11 session until the failure is diagnosed and acceptance evidence is reproducible.
- Do not mix the 6.7.5 fallback packages with the 6.8.1 baseline.
- Preserve the stock Wayland path throughout future work.
- Keep source archives, signatures or checksums, patches, build inputs, RPM checksums, and instructions together.
- Keep SSH and sudo credentials out of scripts and Git.
- Do not install or remove packages, restart SDDM, switch the target session, or alter target permissions as part of this work.
- Do not use KDE logos or claim official KDE support or endorsement.

## Fallback

The 6.7.5 prototype is retained only as a historical reference. Returning to it would require a separate compatibility decision and complete validation against an explicitly selected stack; it is not the active plan.
