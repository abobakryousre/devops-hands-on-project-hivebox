[![Dynamic DevOps Roadmap](https://img.shields.io/badge/Dynamic_DevOps_Roadmap-559e11?style=for-the-badge&logo=Vercel&logoColor=white)](https://devopsroadmap.io/getting-started/)
[![Community](https://img.shields.io/badge/Join_Community-%23FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://newsletter.devopsroadmap.io/subscribe)
[![Telegram Group](https://img.shields.io/badge/Telegram_Group-%232ca5e0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DevOpsHive/985)
[![Fork on GitHub](https://img.shields.io/badge/Fork_On_GitHub-%2336465D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)

# HiveBox - DevOps End-to-End Hands-On Project

<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox" style="display: block; padding: .5em 0; text-align: center;">
    <img alt="HiveBox - DevOps End-to-End Hands-On Project" border="0" width="90%" src="https://devopsroadmap.io/img/projects/hivebox-devops-end-to-end-project.png" />
  </a>
</p>

> [!CAUTION]
> **[Fork](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)** this repo, and create PRs in your fork, **NOT** in this repo!

> [!TIP]
> If you are looking for the full roadmap, including this project, go back to the [getting started](https://devopsroadmap.io/getting-started) page.

This repository is the starting point for [HiveBox](https://devopsroadmap.io/projects/hivebox/), the end-to-end hands-on project.

You can fork this repository and start implementing the [HiveBox](https://devopsroadmap.io/projects/hivebox/) project. HiveBox project follows the same Dynamic MVP-style mindset used in the [roadmap](https://devopsroadmap.io/).

The project aims to cover the whole Software Development Life Cycle (SDLC). That means each phase will cover all aspects of DevOps, such as planning, coding, containers, testing, continuous integration, continuous delivery, infrastructure, etc.

Happy DevOpsing ♾️

## Before you start

Here is a pre-start checklist:

- ⭐ <a target="_blank" href="https://github.com/DevOpsHiveHQ/dynamic-devops-roadmap">Star the **roadmap** repo</a> on GitHub for better visibility.
- ✉️ <a target="_blank" href="https://newsletter.devopsroadmap.io/subscribe">Join the community</a> for the project community activities, which include mentorship, job posting, online meetings, workshops, career tips and tricks, and more.
- 🌐 <a target="_blank" href="https://t.me/DevOpsHive/985">Join the Telegram group</a> for interactive communication.

## Preparation

- [Create GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) (if you don't have one), then [fork this repository](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork) and start from there.
- [Create GitHub project board](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project) for this repository (use `Kanban` template).
- Each phase should be presented as a pull request against the `main` branch. Don’t push directly to the main branch!
- Document as you go. Always assume that someone else will read your project at any phase.
- You can get senseBox IDs by checking the [openSenseMap](https://opensensemap.org/) website. Use 3 senseBox IDs close to each other (you can use the following [5eba5fbad46fb8001b799786](https://opensensemap.org/explore/5eba5fbad46fb8001b799786), [5c21ff8f919bf8001adf2488](https://opensensemap.org/explore/5c21ff8f919bf8001adf2488), and [5ade1acf223bd80019a1011c](https://opensensemap.org/explore/5ade1acf223bd80019a1011c)). Just copy the IDs, you will need them in the next steps.

<br/>
<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox/" imageanchor="1">
    <img src="https://img.shields.io/badge/Get_Started_Now-559e11?style=for-the-badge&logo=Vercel&logoColor=white" />
  </a><br/>
</p>

---

## Implementation

## Module 1

- Done

## Module 2 — DevOps Core

This phase introduces a Python application and a Docker image. The application
prints its configured version once and exits. It does not start an HTTP server,
so no port mapping is required.

### Prerequisites

- Python 3.12 and `venv` for local execution.
- Docker with a running engine for container execution.
- Access to the Python package index to install dependencies and to Docker Hub
  to pull the base image, unless they are already available locally.

Run the following commands from the repository root. Examples use a POSIX shell
such as Bash or Zsh.

### Run locally

Create and activate a virtual environment, then install the declared dependencies:

```sh
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Run the application with the Phase 2 version:

```sh
APP_VERSION=0.0.1 python src/main.py
```

Expected output:

```text
App Version: 0.0.1
```

The process should exit with status `0`. Run `echo $?` immediately afterward to
inspect its exit status. When finished, leave the virtual environment:

```sh
deactivate
```

### Configuration

| Variable | Purpose | Default |
| --- | --- | --- |
| `APP_VERSION` | Version displayed by the application | `0.0.0` |

The current implementation loads `.env` values using `python-dotenv`; an existing
process environment variable takes precedence. `.env.example` documents the
example version setting. These instructions pass the value through the process
environment explicitly.

The configured Phase 2 output is `App Version: 0.0.1`. With neither an environment
variable nor a `.env` setting, the current application prints `App Version: 0.0.0`.
The image tag and `APP_VERSION` are independent: tagging an image does not set the
application's displayed version.

### Build the Docker image

```sh
docker build -t hivebox:0.0.1 .
```

The Dockerfile uses `python:3.12-alpine`, installs dependencies from
`requirements.txt`, copies the application, and runs it as `pythonuser`.

The build context is the repository root. Check `.dockerignore` before building:
the current exclusions omit the Git directory, the local `venv`, and
`.env.example`, but do not exclude `.env`. If a local `.env` exists, the current
`COPY . .` instruction includes it in the image. Add an exclusion before using
local configuration files that must remain outside the image.

### Run the container

```sh
docker run --rm -e APP_VERSION=0.0.1 hivebox:0.0.1
```

Expected output:

```text
App Version: 0.0.1
```

The container should exit with status `0`; check with `echo $?` immediately after
the command. `--rm` removes the stopped container while keeping the image for
subsequent runs. Immediate termination is expected for this application.

### Manual verification

Before opening the Phase 2 pull request:

1. Install dependencies in a fresh virtual environment.
2. Run the local application with `APP_VERSION=0.0.1` and confirm the expected
   output and exit status `0`.
3. Build the image using the command above.
4. Run the container with the same configuration and confirm matching output
   and exit status `0`.
5. Include the commands and observed results in the pull request description.

These are verification instructions, not a record of completed checks. No
application test suite or CI workflow is included in this phase.
