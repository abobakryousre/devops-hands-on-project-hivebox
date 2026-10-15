[![Dynamic DevOps Roadmap](https://img.shields.io/badge/Dynamic_DevOps_Roadmap-559e11?style=for-the-badge&logo=Vercel&logoColor=white)](https://devopsroadmap.io/getting-started/)
[![Community](https://img.shields.io/badge/Join_Community-%23FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://newsletter.devopsroadmap.io/subscribe)
[![Telegram Group](https://img.shields.io/badge/Telegram_Group-%232ca5e0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DevOpsHive/985)
[![Fork on GitHub](https://img.shields.io/badge/Fork_On_GitHub-%2336465D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)

# HiveBox

A hands-on DevOps project based on the [Dynamic DevOps Roadmap](https://devopsroadmap.io/)
and its [HiveBox project](https://devopsroadmap.io/projects/hivebox/), developed
incrementally from application code to infrastructure and operations.

The current application prints its version once and exits. Its default version
is `0.0.1`. It does not yet expose an API or retrieve sensor data.

## Quick start

With Docker installed and its engine running, execute these commands from the
repository root:

```sh
docker build -t hive:0.0.1 .
docker run --rm hive:0.0.1
```

Expected output, with exit status `0`:

```text
App Version: 0.0.1
```

## Documentation

- [Development](docs/development.md): local setup, container execution, manual
  verification, and contribution workflow.
- [Configuration](docs/configuration.md): supported settings, defaults, and
  environment-variable examples.
- [Application version decision](docs/decisions/0001-application-version.md):
  reasoning and consequences of the current version configuration.

Update the relevant documentation in the same pull request as a behavior change.
Keep these pages aligned with the current implementation; use issues and pull
requests to record phase completion and verification evidence.

## Project origins

This fork follows the incremental learning approach of
[DevOps Hive](https://devopshive.com/). The planned application will provide an
API around environmental sensor data from [openSenseMap](https://opensensemap.org/).
See the [upstream starter repository](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox)
and [roadmap instructions](https://devopsroadmap.io/projects/hivebox/) for the
full learning scope. Submit implementation pull requests to this fork.
