# Add automatic location detection and map integration

**Summary**
Detect the user's location via browser geolocation (with permission) and show a small interactive map (e.g., Leaflet) on the weather page to choose or confirm the location.

**Why**
Convenience: users get weather for their current location without typing a city. A map improves discovery and accuracy.

**Acceptance criteria**
- Browser prompts for geolocation; when permitted, page auto-fills the location and fetches weather.
- A map component appears on `weather.html` allowing users to pick a point; clicking the map updates the displayed weather.
- Graceful fallback to manual city input when geolocation is denied or unavailable.
- Add any required dependency notes to `README.md` and `requirements.txt` (e.g., `leaflet` via CDN; no Python dependency required unless using a server-side maps API).

**Implementation notes**
- Use JavaScript `navigator.geolocation` and a lightweight client-side map (Leaflet + OpenStreetMap tiles).
- Update templates and `static/js` as needed; keep external libs loaded via CDN for simplicity.

**Tasks**
- [ ] Add frontend geolocation and map UI
- [ ] Wire map selections to backend API calls
- [ ] Update docs and tests (where applicable)

**Labels**: enhancement, frontend, UX
