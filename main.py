"""news-image-20261122, builder C ('closing').

The entry image is entry.png beside this file: a one-day newspaper front
page for Sunday 22 November 2026 — COP31 ends with no deal, Democrats take
258 House seats, 30 stories across 6 regions, each labelled REPORTED /
CLAIM / DENIAL / ONGOING with its source. This program only copies it to
the output directory, standard library only, so both runs are byte-identical.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(os.path.join(here, "entry.png"),
                    os.path.join(out, "entry.png"))


if __name__ == "__main__":
    main()
