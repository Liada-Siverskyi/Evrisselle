# Licensing and attribution

This repository combines downstream packaging with source from KDE, openSUSE, and the SonicDE `sonic-win` project. There is no single license for the combined Plasma stack. The license expression in each RPM recipe describes that package's sources; it is not a license grant for every file in this repository.

## Repository inventory

| Material | License / status | Evidence and handling |
| --- | --- | --- |
| Plasma Workspace package | The spec declares `GPL-2.0-or-later` | This is the recipe's RPM metadata, not a complete repository-wide license grant. Preserve the upstream source notices in source and binary packages. |
| KWin X11 candidate | As declared in `kwin6-x11.spec` (`GPL-2.0-or-later AND GPL-3.0-or-later`) | Source is pinned to the SonicDE commit in the spec and `_service`; preserve the source tree's license files. Verify that the recipe expression matches the pinned tree before publishing binaries. |
| openSUSE spec additions and included packaging files | Per-file origin/license is not fully catalogued here | Retain the matching OBS source and its notices; identify modifications as downstream changes. |
| Downstream patches | Inherit or modify the license of the affected upstream files unless the patch explicitly states otherwise | Keep upstream copyright notices and make downstream authorship clear. Do not treat patches as a new license for upstream code. |
| Original Evrisselle documentation, scripts, and project metadata | No repository-wide license has been selected | Reuse and redistribution rights for these original materials are not granted by this file. A maintainer decision and explicit license notices are needed before representing them as openly licensed. |

## Source and build records

For every package release, publish the exact spec, patch series, source URL or immutable revision, archive checksum, source license files, and build instructions used. Record generated RPM checksums and build logs alongside a release; no such release evidence is currently included in this repository. A pinned hash establishes byte identity, not authorship, trust, license compliance, or runtime correctness.

Keep KDE and openSUSE attribution, copyright notices, and license texts. Use KDE and Plasma names only to identify upstream software accurately. Do not use KDE logos or imply KDE publication, support, or endorsement. Review each newly copied file and dependency on its own terms.
