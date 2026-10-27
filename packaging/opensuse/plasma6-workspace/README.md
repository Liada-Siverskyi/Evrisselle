# Plasma 6.7.5 fallback prototype

This package set is retained as a reference for the 6.7.5 X11 session path. It is not the selected implementation and must not be mixed with the selected Plasma 6.8.1 package baseline. The active plan is the 6.8.1 forward-port documented in `docs/deployment-plan.md` and `docs/forward-port-audit.md`.

This OBS source package prototype rebuilds `plasma6-workspace` from the KDE 6.7.5 release with `WITH_X11_SESSION=ON`. It adds the `evrisselle-ionis-undecima-session` RPM, containing `startplasma-x11` and a distinct product-branded X11 session entry. The regular Wayland session remains in `plasma6-session`.

The package spec is based on the openSUSE packaging snapshot used by the community Plasma X11 build, with unrelated optional downstream patches removed. It is not linked to that OBS project at build time. The source tarball and detached KDE signature are downloaded from the official KDE release directory; `_service` checks the tarball SHA-256 before a package build.

## Contents

- `plasma6-workspace.spec` — Workspace RPM recipe and session subpackage.
- `0001-Evrisselle-session-branding.patch` — changes only the X11 login entry name and description.
- `_service` — downloads Source/Source1 and checks the official tarball checksum.
- `plasma.keyring` — KDE release signing keys used by the OBS package source convention.
- `sddm.conf`, `waitforkded.conf` — openSUSE packaging inputs retained from the base spec.

The source archive is not stored in Git. `download_files` fetches it from `download.kde.org`; the signature can be checked manually with:

```sh
gpgv --keyring plasma.keyring plasma-workspace-6.7.5.tar.xz.sig plasma-workspace-6.7.5.tar.xz
```

The recorded SHA-256 is `94ab21e2243b7876f65c315f1e545081c6437f5bd0a041ca4fb6c2533ae874c9`.

## Build and installation status

The source spec is an old prototype and is not part of the active implementation. Do not use its historical build-status notes as a report of current tools or system state. Any future use would require a matching Tumbleweed dependency set and disposable-VM validation. The session package intentionally requires the workspace and Wayland-session packages from the same build release.

The X11 window manager is provided separately by openSUSE's `kwin6-x11` package; it is not built from this recipe.

After building and installing into a staging root or disposable VM, run `scripts/check-session-root.sh <root>` to confirm the X11 executable, KWin/X11 dependency, branded session entry, and existing Wayland entry are all present.
