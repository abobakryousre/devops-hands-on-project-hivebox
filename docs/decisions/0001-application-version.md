# 0001: Application version default with a runtime override

Status: Accepted — records the current implementation.

## Context

The initial application must print its version and exit. Both local execution
and an unconfigured container need a useful default. The current implementation
also supports supplying a version through an environment variable or `.env`.

## Decision

Keep the default version in the application source and retain the optional
`APP_VERSION` override. Load dotenv settings before reading the variable.
The supported default and configuration precedence are documented in
[configuration](../configuration.md).

This document records implemented behavior; it does not prescribe a build-time
versioning system for future releases.

## Alternatives

- A source or package version with no override would tie the displayed identity
  more closely to the code being executed.
- Build-generated version metadata could tie the version to a release or commit,
  but requires a build and release process beyond the current increment.

## Consequences

- The application runs without external configuration.
- Runtime configuration can demonstrate environment-variable handling.
- An override can misrepresent the code's actual version. Do not use the
  displayed value alone as evidence of artifact provenance.
- Image tags and the displayed version remain independent.
- Revisit the override when implementing release automation. If this approach
  changes, add a superseding decision and link it here.
