# Add caching and rate-limit handling for external weather API

**Summary**
Implement a caching layer for upstream weather API responses and add basic rate-limit/backoff handling to prevent hitting provider limits and improve performance.

**Why**
Reducing redundant external requests lowers API costs, improves response times, and prevents outages when rate limits are exceeded.

**Acceptance criteria**
- Backend caches weather responses (in-memory or file-based) for a configurable TTL (e.g., 10 minutes).
- On HTTP 429 or provider errors, app returns a sensible cached fallback or a clear error message.
- Configuration options added to `config` or environment variables for TTL and cache type.
- Tests simulate cached responses and rate-limit behavior.

**Implementation notes**
- Add a small cache utility (LRU or TTL) to `weather/` or use `cachetools` if adding dependency.
- Wrap upstream calls in a retry/backoff policy and check cache before calling.

**Tasks**
- [ ] Add cache utility and config
- [ ] Integrate cache into `weather/api.py`
- [ ] Implement rate-limit/backoff handling
- [ ] Add tests

**Labels**: enhancement, backend, reliability
