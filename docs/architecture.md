# Architecture

## Login path

```text
SDDM session selector
  ├─ Plasma (Wayland)                     stock Tumbleweed session
  └─ Evrisselle Ionis Undecima             downstream X11 session entry
       └─ startplasma-x11                 restored from Plasma workspace
            └─ kwin_x11                  compatibility link to the pinned sonic-win build
```

The selected baseline is Plasma 6.8.1. The ordinary Wayland session remains supplied by the distribution. Ionis Undecima adds a separately selectable X11 path and must not replace the Wayland files or services.

## Package set

The 6.8.1 source no longer builds an X11 login session when `WITH_X11_SESSION` is set. The option is declared but unused. `startplasma-wayland` is built directly from `startplasma.cpp`; X11 startup, the X11 login template, and the X11 systemd target were removed. Plasma Shell also lost X11-specific code, and KWin 6.8.1 builds `kwin_wayland`, not the standalone `kwin_x11` window manager.

The port therefore needs a version-matched downstream source set, not just a renamed `.desktop` file. The initial package boundary is:

- `plasma6-workspace`: restore and brand the X11 start path and its session target while keeping Wayland enabled; restore any Workspace runtime paths required for the X11 desktop.
- `kwin6-x11`: package the pinned SonicDE `sonic-win` community fork, providing `kwin_x11` plus its separate plugins and libraries alongside stock Wayland KWin.
- Additional Plasma components: include a package only when the source audit or build proves 6.8.1 removed a required X11 path from it. Do not mix 6.7.5 binaries into the 6.8.1 stack.

The Workspace patch, source checksum service, and 6.8.1 package recipe are in `packaging/opensuse/plasma68-forwardport/workspace/`. The KWin candidate source pin and package recipe are in `packaging/opensuse/plasma68-forwardport/kwin6-x11/`. SonicDE is a community fork, not an official KDE 6.8.1 release. The matched package set has passed one X11 login and one subsequent Wayland login in a disposable VM and is installed on the target. SDDM exposes both session choices; the target's first X11 login and broader compatibility checks remain. The existing 6.7.5 prototype is retained only as a fallback reference.

## Compatibility boundary

The target machine has Plasma workspace, desktop, and Wayland KWin at 6.8.1. The matched package set now supplies `kwin6-x11`, the branded session, and Workspace 6.8.1 forward-port packages. The previous 6.7.5 `libkwin-x11-6` library was replaced. Both the branded X11 session and stock Wayland session files are installed.

Every Evrisselle X11 binary and plugin must be built against the same 6.8.1 package snapshot used by the target. The system's existing Wayland session must remain selectable and pass a login check after installation and rollback.

## Branding

The login entry is named `Evrisselle Ionis Undecima`. Its description identifies it as an independently maintained Plasma session. Retain all upstream copyright and license notices; do not use KDE logos or imply KDE endorsement.
