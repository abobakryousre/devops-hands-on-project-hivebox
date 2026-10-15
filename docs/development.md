# Development

[Back to the project README](../README.md)

## Prerequisites

- Python 3.12 with `venv` for local execution.
- Docker with a running engine for container execution.
- Access to the Python package index and Docker Hub when dependencies or the
  base image are not already available locally.

Run all commands from the repository root. Examples use Bash or Zsh.

## Local setup and execution

```sh
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python src/main.py
```

Without configuration overrides, the application prints:

```text
App Version: 0.0.1
```

It exits immediately with status `0`. Run `echo $?` immediately after executing
the application to inspect the status. Use `deactivate` when finished.

See [configuration](configuration.md) for override behavior. An existing shell
variable or local `.env` setting can change the displayed version.

## Build and run with Docker

```sh
docker build -t hive:0.0.1 .
docker run --rm hive:0.0.1
```

The expected default output is the same as local execution, with exit status `0`.
No port mapping is required: the application does not start a server. `--rm`
removes the stopped container while retaining the image.

The Dockerfile uses `python:3.12-alpine`, installs the dependencies declared in
`requirements.txt`, and runs `src/main.py` as the non-root user `pythonuser`.
Dependencies are copied and installed before application files so source changes
can reuse the dependency layer.

The repository root is the build context. `.dockerignore` excludes Git metadata,
`.gitignore`, `.env*` files, and the local `venv` contents. Runtime configuration
is supplied when starting the container; see [configuration](configuration.md).

## Manual verification

Before submitting a change:

1. Install dependencies in a fresh virtual environment.
2. Run the application without configuration overrides and verify the default
   output described above and exit status `0`.
3. Build and run the image, then verify matching output and exit status `0`.
4. Exercise the override examples in [configuration](configuration.md) and
   verify that the supplied value is displayed.
5. Check the image's configured runtime user:

   ```sh
   docker run --rm --entrypoint id hive:0.0.1
   ```

   Confirm that the username is `pythonuser` and the UID is not `0`.

6. Include commands and observed results in the pull request description.

These instructions describe checks to perform, not completed test results. The
current project has no automated test suite or CI workflow.

## Contribution workflow

Track work on the fork's project board, using small issues with acceptance
criteria. Create a branch for each increment and submit a pull request against
this fork's `main` branch. Link the related issue and describe the behavior change
and verification results. Avoid direct pushes to `main`.

Maintain documentation in the same pull request as the implementation:

- Keep the README focused on purpose, quick start, and navigation.
- Update existing topic pages when behavior changes instead of appending phase
  reports. Git preserves previous versions.
- Keep configuration definitions in [configuration.md](configuration.md), and
  link to them from other guides.
- Record significant decisions in `docs/decisions/` with context, choice,
  alternatives, and consequences. If a choice changes, add a new decision and
  mark the previous one superseded with a link.
- Add deployment guides and operational runbooks when those capabilities exist.
- Record completed work and validation evidence in issues and pull requests.
