# datachain-from-git-demo

A throwaway repo for trying out Studio's "From Git" job type, where a job stores a path
inside a repository instead of a copy of the code.

## Use it

In the Studio query editor, `+` → **From Git**, then:

| Field | Value |
|---|---|
| Repository | `https://github.com/amritghimire/datachain-from-git-demo@main` |
| File to run | `src/daily.py` |
| Requirements.txt | leave empty |

Run it. The worker clones this repo into the job working directory and runs `src/daily.py`
out of the clone, so every run picks up whatever is on `main`. Push a change here and the
next run uses it, with nothing to re-paste in Studio.

`src/daily.py` builds a five-row dataset called `from_git_demo` and shows it, so a
successful run is easy to spot.

## Things worth knowing

- **`@main` moves, a tag does not.** `...repo@main` follows the branch. `...repo@v1.0.0`
  pins to that tag's commit forever and looks identical in the UI. Commit SHAs are not
  supported.
- **Imports resolve from the repo root, not the file's directory.** A script in `src/`
  importing a sibling needs `from src.helpers import x`, not `from helpers import x`.
- **A `requirements.txt` in this repo is not read automatically.** Dependencies come from
  the Requirements.txt field on the job. This script only needs `datachain` itself, which
  the worker already has.
