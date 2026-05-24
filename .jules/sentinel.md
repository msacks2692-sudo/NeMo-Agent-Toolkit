## 2024-05-24 - [CRITICAL] Fix HTTP Basic Auth Header Scheme
**Vulnerability:** The console HTTP Basic authentication flow incorrectly generated an Authorization header using the `Bearer` scheme instead of the required `Basic` scheme.
**Learning:** Basic HTTP auth credentials (base64-encoded username:password) were mistakenly prefixed with `Bearer`. This misalignment with RFC 7617 could cause widespread authentication rejections by compliant servers.
**Prevention:** Ensure tests cover strict compliance with expected protocol structures, not just internal function returns. Validate generated headers against known HTTP standard formats.
