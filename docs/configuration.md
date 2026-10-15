# Configuration

[Back to the project README](../README.md) · [Development guide](development.md)

## Supported settings

| Variable | Purpose | Required | Default |
| --- | --- | --- | --- |
| `APP_VERSION` | Version string printed by the application | No | `0.0.1` |

The application loads `.env` settings using `python-dotenv` before reading
`APP_VERSION`. Values follow this precedence:

1. Existing process environment variable.
2. Value loaded from a local `.env` file.
3. Default in the application source when the variable is absent.

An explicitly empty value is treated as an override; it does not select the
default. The current implementation does not validate version syntax.

## Local execution

After completing the [local setup](development.md#local-setup-and-execution):

```sh
APP_VERSION=0.0.2 python src/main.py
```

Expected output:

```text
App Version: 0.0.2
```

Alternatively, copy `.env.example` to `.env` in the repository root and edit the
local values. `.env` is ignored by Git and excluded from the Docker build context.
An exported `APP_VERSION` in your shell takes precedence over the file.

## Container execution

Supply a variable when starting the container:

```sh
docker run --rm -e APP_VERSION=0.0.2 hive:0.0.1
```

Or supply a local environment file without copying it into the image:

```sh
docker run --rm --env-file .env hive:0.0.1
```

For Docker's `--env-file` option, use entries in this form:

```text
APP_VERSION=0.0.2
```

Docker reads the host file and supplies its variables to the container. The file
itself remains outside the image. `.env.example` uses dotenv formatting; normalize
entries to the form above when preparing a Docker environment file.

## Image tags and application versions

An image tag identifies an image reference. It does not automatically set
`APP_VERSION`. Runtime overrides change the displayed string, not the code in
the image. See the [version decision](decisions/0001-application-version.md) for
the consequences of this approach.
