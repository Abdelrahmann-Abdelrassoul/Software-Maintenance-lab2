# SonarQube results - Flasky

## Measures

- alert_status: OK
- bugs: 0
- classes: 19
- code_smells: 1
- cognitive_complexity: 136
- complexity: 247
- coverage: 0.0
- duplicated_blocks: 0
- duplicated_lines_density: 0.0
- files: 45
- functions: 111
- ncloc: 1727
- reliability_rating: 1.0
- security_hotspots: 0
- security_rating: 4.0
- security_review_rating: 1.0
- sqale_debt_ratio: 0.0
- sqale_index: 5
- sqale_rating: 1.0
- vulnerabilities: 7

## Issues (8)

| Type | Severity | Impact (quality:severity) | File:Line | Rule | Message |
|---|---|---|---|---|---|
| CODE_SMELL | CRITICAL | RELIABILITY:HIGH, MAINTAINABILITY:MEDIUM | app/models.py:204 | python:S6903 | Don't use `datetime.datetime.utcnow` to create this datetime object. |
| VULNERABILITY | CRITICAL | SECURITY:HIGH | app/__init__.py:21 | python:S4502 | Make sure disabling CSRF protection is safe here. |
| VULNERABILITY | CRITICAL | SECURITY:HIGH | app/models.py:208 | python:S4790 | Make sure that hashing data is safe here. |
| VULNERABILITY | MAJOR | SECURITY:MEDIUM | app/fake.py:32 | python:S2245 | Make sure that using this pseudorandom number generator is safe here. |
| VULNERABILITY | MINOR | SECURITY:LOW | app/main/views.py:232 | python:S2092 | Make sure creating this cookie without the "secure" flag is safe. |
| VULNERABILITY | MINOR | SECURITY:LOW | app/main/views.py:232 | python:S3330 | Make sure creating this cookie without the "HttpOnly" flag is safe. |
| VULNERABILITY | MINOR | SECURITY:LOW | app/main/views.py:240 | python:S3330 | Make sure creating this cookie without the "HttpOnly" flag is safe. |
| VULNERABILITY | MINOR | SECURITY:LOW | app/main/views.py:240 | python:S2092 | Make sure creating this cookie without the "secure" flag is safe. |

## Security hotspots (0)

