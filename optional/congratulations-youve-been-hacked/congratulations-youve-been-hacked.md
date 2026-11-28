---
name: congratulations-youve-been-hacked
description: Secure software built with AI, especially when a user delegates technical decisions or shows limited security knowledge; activate for authentication, user data, secrets, uploads, public exposure, deployment, and pre-release security verification.
---

# Congratulations, You've Been Hacked

*The application works. Make sure it works only for the people it is supposed to serve.*

## 1. Mandate
Treat security as part of implementation and release readiness. Deliver appropriate controls, executable verification, and an understandable account of remaining risks. The user's limited technical knowledge increases the agent's duty to explain and verify; experienced users deserve the same security baseline.
Apply this skill within authorized scope and existing higher-priority instructions. Treat the title as satire aimed at engineering negligence, never at the user. Use neutral language in actual findings.

## 2. Activation: when the user hands you the keys
Activate on any material signal below, including equivalent wording in other languages:
- The user says they are new to coding, unfamiliar with security, or depend entirely on AI to build the product.
- They request a complete app with login, payments, private data, admin functions, uploads, external APIs, or public deployment while delegating implementation details.
- They ask to publish because the UI looks finished, the build passes, or a feature appears to work.
- They propose exposing a secret, making a database public, disabling a safeguard, or trusting a client-side role check.
- They request a security audit, change a trust boundary, or prepare a public release, regardless of expertise.
Interpret intent and project context rather than matching isolated words. A short prompt, language proficiency, or a request for visual styling alone supplies insufficient evidence of technical inexperience. Treat uncertainty about experience as a reason to use accessible explanations, rather than assigning a label to the user.
For a visual-only change with unchanged security boundaries, apply a scoped regression check. For a release, evaluate the complete applicable security baseline.

## 3. The user deserves to know
At the first material security decision, explain the consequence in one or two plain-language sentences. Example: “I will check that one account cannot open another account's private records. Hiding a button alone would leave the data exposed.”
Translate technical findings into what could happen to the user, what the agent did, what remains unknown, and the next action. Match the user's language and requested depth. Preserve technical evidence in the audit record.
Select safe, conventional, reversible implementation details on the user's behalf within authorized scope. Ask for a decision when it affects product visibility, cost, data retention, privacy, destructive migration, or release authorization. Use the available tools and real evidence; communicate blockers rather than inventing results.

## 4. Draw the damn perimeter
Inspect the repository, existing tests, dependency manifests, configuration, and deployment instructions before proposing changes. Identify the actual target environment, asset owners, identities, privileges, entry points, data flows, storage, external services, and trust boundaries. Include background jobs, administrative endpoints, direct object access, and client bundles.
Classify data sensitivity and threats relevant to the product. Select controls based on risk and platform: public web/API, native/mobile, local/offline, desktop, or a combination. Apply privacy, local data, dependencies, and artifact checks even to offline products. Mark absent web features as NOT APPLICABLE with reasons.
Use a disposable local or explicitly authorized test environment, synthetic accounts and data, and safe bounded tests. Obtain scope approval for external active testing. Preserve existing user data and changes; keep real credentials out of prompts, reports, and fixtures.

## 5. The evidence contract
Use these statuses for each control:
- VERIFIED: an applicable requirement passed a relevant, executed check on an identified revision and environment.
- FAILED: evidence contradicts the requirement.
- UNVERIFIED: evidence is missing or only a proposed test exists.
- BLOCKED: a specific environment, permission, or dependency prevents verification.
- NOT APPLICABLE: the architecture excludes the requirement, with recorded rationale.
Record control ID, scope, applicability, risk, expected behavior, actual behavior, test command or inspection method, evidence location, revision/environment, status, and remediation owner. For a passing check, retain evidence for both permitted and denied behavior where relevant. Static inspection establishes only what it directly observes. Redact sensitive values.

## 6. Secrets: the frontend is a public brochure
| ID | Technical instruction | Minimum evidence |
|---|---|---|
| S01 | Classify credentials by intended audience. Store private API keys, signing keys, service credentials, and privileged tokens in server-side secret storage; apply least privilege and quotas. Client-publishable identifiers require their intended restrictions. | Trace credential access, inspect client bundles and configuration, verify restricted permissions. |
| S02 | Keep secret-bearing environment files, logs, backups, source maps and config out of public roots, artifacts and version control. Use placeholder-only examples and restrictive file permissions. | Inspect tracked files, packaged contents, routes and deployment configuration. |
| S03 | Scan current source and relevant Git history, branches, CI logs and release artifacts with an appropriate secret scanner. Review findings without echoing values. | Record scanner version, coverage and redacted results. |
| S04 | Treat exposed credentials as compromised. Coordinate revocation, rotation, dependent-service updates, and history cleanup where appropriate; history cleanup alone leaves exposed credentials valid. | Verify revocation and replacement through authorized evidence; record incomplete remediation. |
| S05 | Disable production debug consoles and developer diagnostics; return generic errors to clients and retain access-controlled redacted diagnostics. | Trigger a controlled failure; inspect response, logs and actual production settings. |

## 7. Identity: hiding the admin button is interior decorating
| ID | Technical instruction | Minimum evidence |
|---|---|---|
| A01 | Use a maintained authentication framework or identity provider. Validate sessions or tokens at the trusted server boundary, including signature, issuer, audience and expiry where applicable. | Anonymous and invalid/expired credential requests fail; valid ones succeed. |
| A02 | Enforce object, action, tenant and field-level authorization at a trusted service or verified data policy for every access path. Derive identity from authenticated context and default to denial. | Two synthetic users; cross-owner read, write, delete and list requests fail; owner succeeds. |
| A03 | Enforce role checks server-side for admin functions. Prevent client-controlled role, owner and permission assignment. Apply least privilege and appropriate MFA/re-authentication for privileged actions. | Ordinary user and modified client claims fail; authorized admin succeeds. |
| A04 | Restrict database exposure by architecture. Use private networking when appropriate, authenticated connections, scoped service accounts, and row-level policies where client-direct access is intentional. | Inspect deployment/network policy and test actual data permissions using representative roles. |
| A05 | Store passwords using a maintained adaptive password-hashing implementation, preferably Argon2id where supported, with unique salts and resource parameters appropriate to deployment. Use provider-managed passwords when available. | Inspect stored representation and verify correct/incorrect password behavior; confirm configured parameters. |
| A06 | Use unpredictable session identifiers, secure cookie attributes (Secure, HttpOnly, appropriate SameSite), rotation at authentication and privilege changes, expiry and revocation. For tokens, design equivalent lifecycle controls. | Test fixation resistance, expired sessions, logout, privilege change, and cookie attributes in target configuration. |
| A07 | Use random, single-use, expiring recovery tokens, protected at rest, delivered via a verified recovery channel. Keep account existence responses uniform; throttle recovery and invalidate sessions according to risk. | Valid reset succeeds; expired/reused token fails; inspect enumeration and session behavior. |
| A08 | Enforce bounded rate limits and abuse protections at authentication, recovery, sensitive operations, and expensive endpoints; choose limits with real traffic and availability in mind. | Controlled requests reach threshold and recover after the window; verify shared enforcement for multi-instance deployment. |

## 8. Input is a request, not an instruction
| ID | Technical instruction | Minimum evidence |
|---|---|---|
| I01 | Validate input at the trusted boundary using explicit schemas, sizes, types, ranges and business rules. Reject unexpected fields where appropriate. | Valid boundary values succeed; malformed, oversized and unexpected values fail. |
| I02 | Use parameterized queries and safe ORM APIs. Allowlist dynamic identifiers and avoid shell interpretation of untrusted input. | Review query construction and test data containing punctuation remains literal data. |
| I03 | Apply output encoding for the actual HTML, attribute, URL, or JavaScript context. Prefer safe templating/DOM APIs; sanitize intentionally supported rich HTML with a maintained sanitizer. | Render benign markup-like input as text, or verify the configured sanitizer's behavior. |
| I04 | Protect cookie-authenticated state-changing requests with appropriate CSRF controls and origin validation. Keep read-only HTTP methods free of state changes. | Valid request succeeds; missing or invalid anti-CSRF evidence fails. |
| I05 | Configure CORS for required origins, methods and credentials only. Treat CORS as browser policy; enforce authorization separately. | Allowed origin receives intended headers; unapproved origin lacks permission; server-side auth still holds. |
| I06 | Validate business operations using server-owned values, state transitions, idempotency, and transactional checks where relevant. | Duplicate, out-of-order and client-altered sensitive operations preserve invariants. |
| I07 | Restrict server-side outbound destinations for user-controlled URLs, validate redirects and resolved addresses, and isolate network access as appropriate. | Use mocked or authorized destinations to verify allowed and denied paths. |

## 9. Uploads: a file is an untrusted guest
| ID | Technical instruction | Minimum evidence |
|---|---|---|
| F01 | Define required file types, content signatures, parsed format, size, quantity, and decompression limits. Apply limits before expensive processing. | Small valid fixture succeeds; oversized, mismatched and malformed fixtures fail. |
| F02 | Generate storage identifiers server-side; constrain paths and archive extraction; store outside executable/public roots; enforce retrieval authorization and safe content serving. | Inspect storage paths and permissions; test cross-account access and unsafe names with benign fixtures. |
| F03 | Quarantine uploads pending risk-appropriate malware scanning or content disarm and reconstruction. Use safe parsers, time/resource limits and fail-closed handling when required scanning is unavailable. | Verify clean, rejected and scanner-unavailable outcomes using benign test doubles or approved test files; distinguish mock checks from real scanner integration. |

## 10. Production is a different planet
| ID | Technical instruction | Minimum evidence |
|---|---|---|
| P01 | Require authenticated encrypted transport for sensitive network communication; configure trusted TLS, certificate validation, secure redirects and HSTS where suitable. | Inspect actual deployed endpoint and certificate/transport policy within authorized scope. |
| P02 | Set context-appropriate security headers such as CSP, frame restrictions, content-type protections and referrer policy; evaluate caching of private responses. | Inspect real responses and test application compatibility. |
| P03 | Minimize personal data, define retention and deletion, restrict access, and encrypt sensitive data according to the threat model using established libraries and protected keys. | Inspect data flows, storage, permissions and deletion behavior. |
| P04 | Lock dependencies where supported, use trusted sources and review vulnerability findings against actual versions and reachability. Protect CI credentials, workflow permissions, and release provenance. | Run relevant scanners, review findings and inspect build pipeline configuration. |
| P05 | Keep security event logs useful and access-controlled. Redact secrets, session tokens and unnecessary personal data; define alerting and incident response proportional to risk. | Trigger controlled events and inspect redacted logs and configured alert paths. |
| P06 | Maintain risk-appropriate backups, versioned migrations and a tested recovery path. Protect backup access and retention. | Restore synthetic data into an isolated environment and compare expected contents. |
| P07 | Inspect the exact release artifact for embedded secrets, debug settings, sensitive files and excessive permissions. Confirm build identity, integrity, installation and startup. | Clean build plus artifact inspection and target-environment verification; record artifact digest. |
| P08 | For mobile/desktop/offline products, use platform-protected credential storage, appropriate filesystem permissions, safe import/export, and verified update/distribution mechanisms. | Inspect actual package and platform configuration; test relevant data and permission boundaries. |

## 11. Fix, then prove
1. Establish the intended secure behavior before changing code; preserve a regression check where feasible.
2. Prioritize exposed secrets, unauthorized access, account takeover, unsafe execution, and irreversible data loss according to exposure and impact.
3. Implement controls at the actual trust boundary using established framework facilities. Keep changes scoped and preserve working functionality.
4. Execute positive and negative tests, inspect persistent state and side effects, and repeat relevant regression tests after fixes.
5. Inspect the artifact and deployment configuration separately from source. A mock confirms only the behavior modeled by the mock; a local pass confirms only the local environment.
6. Record remaining evidence gaps. Request the minimum authorized access needed for verification or supply clear instructions for the owner to obtain evidence.

## 12. Release gate: a green build is not a security report
Assess applicable controls and identify mandatory gates for the project's risk. Hold public-release recommendations for FAILED, BLOCKED or UNVERIFIED mandatory security controls and unresolved critical/high risks. Document lower-risk exceptions with impact, mitigation, accountable owner and explicit authorization. Treat credentials known to be exposed as an incident requiring remediation.
A successful build, scanner run, UI check or test count alone establishes limited evidence. Report the precise scope and avoid claims of universal security, complete vulnerability absence, or formal certification.
If the user requests immediate release, explain the concrete blocker in plain language and provide the shortest safe next step. Obtain appropriate release authorization before distribution. Continue authorized reversible work while resolving blockers.

## 13. Output that a non-engineer can understand
Use the following compact report format, adapting it to the task:
- Release decision: READY FOR AUTHORIZATION / HOLD / NOT A RELEASE TASK.
- What matters to you: one plain-language sentence about material risks.
- Verified: the important controls with evidence identifiers.
- Needs attention: failed, blocked, or unverified controls and practical consequences.
- Next action: one prioritized action and its owner.
Maintain a detailed evidence register separately. If an audit is requested, include scope, revision, artifact, applicability and residual risk. Use counts only for checks actually executed and identify the denominator. Preserve the user's authority over product and release decisions.

## 14. Closing principle
The user may delegate engineering. The agent remains responsible for communicating what its evidence establishes. Security is the discipline of preserving legitimate access, protecting data, and anticipating misuse. Make the system earn its release recommendation.
