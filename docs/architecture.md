# Architecture

## Intended login path

```text
SDDM session selector
  ├─ Plasma (Wayland)                   openSUSE-provided session; preserve as fallback
  └─ Evrisselle Ionis Undecima         downstream X11 session entry
       └─ startplasma-x11               restored by the Workspace patch series
            └─ kwin_x11                compatibility link to the pinned SonicDE build
```

The selected package baseline is Plasma 6.8.1. This diagram describes the intended design, not a validated target configuration. The maintainer reported a black screen and empty panel in an earlier X11 experiment. The reason is unresolved. Wayland remains the required working session during any future diagnosis.

## Package boundaries

- `plasma6-workspace` restores the X11 startup path and Workspace runtime paths while retaining the distribution's Wayland path.
- `kwin6-x11` packages a pinned SonicDE `sonic-win` community fork with a separate executable, plugins, and libraries.
- Additional Plasma packages should be changed only when source review or reproducible build evidence shows that they are required.

The active package specs, source services, and patch series are under `packaging/opensuse/plasma68-forwardport/`. Their source identities are pinned, but the repository does not yet contain enough environment and artifact records to reproduce the previously reported RPM build. SonicDE is a community fork, not an official KDE release.

## Compatibility and safety boundary

Every downstream binary and plugin must be built against one documented Tumbleweed snapshot and matched to the target ABI. Preserve the ordinary Wayland package files and session entry. Do not install or remove packages, restart SDDM, change sessions, or alter permissions on the Mac Pro as part of this work. Hardware validation is open and requires a separate plan after the black-screen failure is understood.

## Branding

The session entry is branded `Evrisselle Ionis Undecima` and identifies its relationship to Plasma. Retain upstream copyright and license notices. Do not use KDE logos or imply KDE support or endorsement.
