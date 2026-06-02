# Add 7-day forecast endpoint and UI

**Summary**
Add a backend API endpoint that fetches a 7-day weather forecast from the upstream provider and a UI page/section that displays the multi-day forecast for the selected location.

**Why**
Users currently only see current weather. A 7-day forecast increases utility and engagement for planning.

**Acceptance criteria**
- New endpoint at `/api/forecast` returning a 7-day forecast JSON for a given location.
- Frontend `weather.html` displays day-by-day summary (date, icon, high/low temps, short description).
- Mobile and desktop layouts are readable.
- Unit tests cover the endpoint and template rendering.

**Implementation notes**
- Extend `weather/api.py` to add a `get_forecast(location)` function and route.
- Reuse existing API key handling and error flows used for current weather.
- Consider caching responses (see separate caching issue) to avoid hitting upstream limits.

**Tasks**
- [ ] Design API response schema
- [ ] Implement backend endpoint and service function
- [ ] Add template UI and CSS
- [ ] Add tests in `tests/test_api.py`

**Labels**: enhancement, backend, frontend
