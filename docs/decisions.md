# Project decisions

| Topic | Decision |
| --- | --- |
| Umbrella project | Evrisselle |
| First product | Evrisselle Ionis Undecima |
| Purpose | Keep a usable Plasma X11 desktop available to people who need X11 |
| First distribution | openSUSE Tumbleweed |
| Session model | X11 and Wayland are distinct choices in the same login manager |
| First implementation | Downstream RPM packaging of upstream Plasma 6.7.5 X11 paths |
| KWin | Use the separately packaged `kwin6-x11`; do not fork it for the first prototype |
| Maintenance | Solo maintainer, best-effort updates and compatibility fixes, no SLA |
| Public release | After the MVP passes clean-build and isolated-session checks |
| Long-term scope | Aim for feature parity with the supported Plasma release; assess forward-ports when upstream removes X11 code |

## Scope of the first prototype

The prototype rebuilds `plasma6-workspace` with `WITH_X11_SESSION=ON` and adds a product-branded X11 session entry. The stock Wayland session remains in the same build and is still selectable. It depends on the openSUSE `kwin6-x11` package and does not yet maintain a private KWin fork.

The initial source baseline is Plasma 6.7.5 because that source still contains the complete X11 startup path. This is a starting snapshot, not a promise to stay on 6.7.5 indefinitely. A rolling-distribution update can change the ABI or remove dependencies; each update must be built and tested as a compatible set before being advertised.

## Not part of the first prototype

- A separate operating system or a Wayland replacement.
- New desktop features or a promise to match upstream on every release.
- A public package repository before the MVP passes its acceptance checks.
- KDE logos or any claim that KDE officially supports or endorses Ionis Undecima.

