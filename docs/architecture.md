# Architecture

## Login path

```text
SDDM session selector
  ├─ Plasma (Wayland)                    existing plasma6-session entry
  └─ Evrisselle Ionis Undecima (X11)       xsessions desktop entry
       └─ startplasma-x11                 built by plasma6-workspace
            └─ kwin_x11                   provided by kwin6-x11
```

Both choices live on one installed system. Ionis Undecima adds an X11 session entry; it does not change the existing Wayland entry.

## Package shape

The RPM spec is based on openSUSE's `plasma6-workspace` packaging for Plasma 6.7.5. It is configured to rebuild the workspace with `-DWITH_X11_SESSION=ON`. That option causes the upstream build to include X11 startup code, the X11 session target, and X11-only workspace paths which the stock package build does not ship.

The build is configured to emit:

- `plasma6-workspace`, rebuilt from the matching source and retaining its Wayland files;
- `plasma6-session`, retaining the ordinary Plasma Wayland login entry;
- `evrisselle-ionis-undecima-session`, containing `startplasma-x11` and the branded X11 `.desktop` entry.

The session package requires `kwin6-x11`, `plasma6-session`, the Xorg server, and the Xorg libinput driver. KWin/X11 is a separate upstream source/package; the prototype uses openSUSE's package instead of duplicating it.

## Version compatibility

The first spec pins its source to Plasma 6.7.5 and raises the package release so Tumbleweed can install the rebuilt workspace package over the stock build of the same source version. Workspace, session, KWin/X11, and the relevant Plasma libraries must be treated as a versioned set.

Plasma 6.8 removed the upstream X11 session startup files. Upgrading only the session package cannot restore the removed code. The update process must either keep a compatible 6.7.x package set temporarily or forward-port the X11 path and its dependencies, then validate the combined stack. The prototype does not silently claim compatibility with Plasma 6.8.

## Branding

The login entry is named `Evrisselle Ionis Undecima (X11)`. Its description identifies it as a Plasma X11 session maintained by Evrisselle. The package retains upstream KDE copyright and license notices and uses no KDE logo.
