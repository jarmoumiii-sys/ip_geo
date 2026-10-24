
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#0b1020">
<title>TracePoint | IP Intelligence</title>

<style>
:root {
    --bg: #0b1020;
    --panel: #111a2e;
    --panel2: #16213a;
    --border: #283651;
    --text: #edf3ff;
    --muted: #92a2bd;
    --blue: #65a8ff;
    --green: #42dfad;
    --red: #ff7777;
    --yellow: #f7c96b;
}

* { box-sizing: border-box; }

body {
    margin: 0;
    background:
        radial-gradient(ellipse at top left, #172b4a 0, transparent 40%),
        var(--bg);
    color: var(--text);
    font-family: Inter, "Segoe UI", Arial, sans-serif;
    min-height: 100vh;
}

button, input { font: inherit; }

button {
    cursor: pointer;
    transition: .2s ease;
}

button:disabled {
    opacity: .55;
    cursor: wait;
}

button:focus-visible, input:focus-visible, a:focus-visible {
    outline: 2px solid var(--blue);
    outline-offset: 3px;
}

header {
    border-bottom: 1px solid var(--border);
    background: #0b1020dd;
}

.nav {
    max-width: 1200px;
    margin: auto;
    padding: 20px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 20px;
    font-weight: 800;
    letter-spacing: -.5px;
}

.logo {
    display: grid;
    place-items: center;
    width: 42px;
    height: 42px;
    border-radius: 12px;
    background: #19345a;
    color: var(--blue);
    font-size: 23px;
}

.tag {
    font-size: 11px;
    padding: 6px 9px;
    border-radius: 20px;
    color: var(--green);
    background: #12372f;
    border: 1px solid #245548;
}

main {
    max-width: 1200px;
    margin: auto;
    padding: 38px 24px 60px;
}

.eyebrow {
    color: var(--blue);
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 800;
    text-transform: uppercase;
}

h1 {
    font-size: clamp(30px, 5vw, 46px);
    letter-spacing: -1.8px;
    margin: 12px 0;
}

.subtitle {
    color: var(--muted);
    max-width: 650px;
    line-height: 1.7;
}

.panel {
    margin-top: 28px;
    padding: 24px;
    background: #111a2eee;
    border: 1px solid var(--border);
    border-radius: 18px;
    box-shadow: 0 20px 70px #0002;
}

.panel-title {
    font-weight: 750;
    font-size: 17px;
    margin-bottom: 8px;
}

.help {
    color: var(--muted);
    font-size: 13px;
    line-height: 1.6;
}

.search-row {
    display: flex;
    gap: 10px;
    margin-top: 20px;
}

input {
    width: 100%;
    min-width: 0;
    padding: 14px 16px;
    color: var(--text);
    background: #090f1d;
    border: 1px solid #354664;
    border-radius: 10px;
    outline: none;
}

input:focus { border-color: var(--blue); }

.btn {
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
    font-weight: 700;
    white-space: nowrap;
}

.btn-primary {
    background: var(--blue);
    color: #081529;
    border-color: var(--blue);
}

.btn-secondary {
    background: #1a2943;
    color: var(--text);
}

.btn:hover { filter: brightness(1.12); }

.actions {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    margin-top: 15px;
}

#status {
    color: var(--muted);
    margin-top: 16px;
    font-size: 14px;
    line-height: 1.6;
    overflow-wrap: anywhere;
}

#status.error { color: var(--red); }
#status.success { color: var(--green); }

.spinner {
    display: inline-block;
    width: 14px;
    height: 14px;
    margin-right: 8px;
    border: 2px solid #455777;
    border-top-color: var(--blue);
    border-radius: 50%;
    animation: spin .7s linear infinite;
    vertical-align: -2px;
}

@keyframes spin { to { transform: rotate(360deg); } }

#results { margin-top: 28px; }

.section-heading {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
    margin: 30px 0 14px;
}

.section-heading h2 {
    font-size: 19px;
    margin: 0;
}

.badge {
    border-radius: 30px;
    padding: 6px 10px;
    font-size: 11px;
    font-weight: 800;
    background: #1c2d48;
    color: var(--blue);
}

.metrics {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 14px;
}

.metric, .card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px;
    min-width: 0;
}

.metric-label {
    color: var(--muted);
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.metric-value {
    font-size: 20px;
    font-weight: 750;
    margin-top: 10px;
    overflow-wrap: anywhere;
}

.metric-sub {
    color: var(--muted);
    font-size: 12px;
    margin-top: 6px;
}

.provider-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
}

.card h3 {
    font-size: 16px;
    margin: 0 0 16px;
}

.field {
    padding: 11px 0;
    border-bottom: 1px solid #26334a;
    overflow-wrap: anywhere;
}

.field:last-child { border-bottom: 0; }

.field-label {
    display: block;
    color: var(--muted);
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: .8px;
    margin-bottom: 5px;
}

.field-value {
    font-size: 14px;
    line-height: 1.5;
}

.map-link {
    display: inline-block;
    color: var(--green);
    margin-top: 14px;
    text-decoration: none;
    font-size: 13px;
}

.map-link:hover { text-decoration: underline; }

.notice {
    padding: 15px;
    border: 1px solid #4d4326;
    border-radius: 12px;
    background: #30281766;
    color: #e7d5a3;
    font-size: 13px;
    line-height: 1.7;
    margin-top: 20px;
}

.history-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid var(--border);
}

.history-item:last-child { border-bottom: 0; }

.history-ip { font-weight: 700; }
.history-location {
    color: var(--muted);
    font-size: 12px;
    margin-top: 4px;
}

.history-open {
    color: var(--blue);
    background: transparent;
    border: 0;
    padding: 8px;
}

.empty {
    color: var(--muted);
    font-size: 13px;
    padding: 10px 0;
}

footer {
    text-align: center;
    padding: 25px;
    color: var(--muted);
    font-size: 12px;
    border-top: 1px solid var(--border);
    line-height: 1.8;
}

[hidden] { display: none !important; }

@media (max-width: 750px) {
    .metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .provider-grid { grid-template-columns: 1fr; }
}

@media (max-width: 520px) {
    main { padding: 28px 14px 40px; }
    .nav { padding: 15px; }
    .panel { padding: 17px; }
    .search-row { flex-direction: column; }
    .metrics { grid-template-columns: 1fr 1fr; }
    .metric { padding: 13px; }
    .metric-value { font-size: 16px; }
    .tag { display: none; }
}
</style>
</head>

<body>

<header>
    <div class="nav">
        <div class="brand">
            <div class="logo">⌖</div>
            <div>TracePoint <span style="color:#65a8ff">.</span></div>
        </div>
        <div class="tag">OSINT TOOLKIT</div>
    </div>
</header>

<main>
    <div class="eyebrow">Network intelligence / 01</div>
    <h1>IP Geolocation</h1>
    <p class="subtitle">
        Investigate public IPv4 addresses, compare geolocation providers,
        and inspect available network metadata from one dashboard.
    </p>

    <section class="panel">
        <div class="panel-title">Target address</div>
        <div class="help">
            Enter an IPv4 address in the format xxx.xxx.xxx.xxx.
            Example: 8.8.8.8
        </div>

        <form id="lookupForm">
            <div class="search-row">
                <input
                    id="ipInput"
                    type="text"
                    placeholder="8.8.8.8"
                    maxlength="15"
                    inputmode="numeric"
                    autocomplete="off"
                    spellcheck="false"
                    aria-label="IPv4 address"
                    required
                >
                <button class="btn btn-primary" id="searchButton" type="submit">
                    Analyze IP →
                </button>
            </div>
        </form>

        <div class="actions">
            <button class="btn btn-secondary" id="myIpButton" type="button">
                Find my public IP
            </button>
            <button class="btn btn-secondary" id="clearButton" type="button">
                Clear
            </button>
        </div>

        <div id="status" role="status" aria-live="polite">
            Ready. Enter an IPv4 address to begin.
        </div>
    </section>

    <section id="results" hidden>
        <div class="section-heading">
            <h2>Intelligence overview</h2>
            <span class="badge" id="resultBadge">LOOKUP COMPLETE</span>
        </div>

        <div class="metrics">
            <div class="metric">
                <div class="metric-label">Target IP</div>
                <div class="metric-value" id="metricIP">—</div>
                <div class="metric-sub">Public IPv4</div>
            </div>
            <div class="metric">
                <div class="metric-label">Country</div>
                <div class="metric-value" id="metricCountry">—</div>
                <div class="metric-sub" id="metricCountryCode">Country code</div>
            </div>
            <div class="metric">
                <div class="metric-label">City / Region</div>
                <div class="metric-value" id="metricLocation">—</div>
                <div class="metric-sub">Approximate location</div>
            </div>
            <div class="metric">
                <div class="metric-label">Coordinates</div>
                <div class="metric-value" id="metricCoordinates">—</div>
                <div class="metric-sub">Latitude / longitude</div>
            </div>
            <div class="metric">
                <div class="metric-label">Network / ISP</div>
                <div class="metric-value" id="metricISP">—</div>
                <div class="metric-sub">Reported organization</div>
            </div>
            <div class="metric">
                <div class="metric-label">Timezone</div>
                <div class="metric-value" id="metricTimezone">—</div>
                <div class="metric-sub">Reported timezone</div>
            </div>
        </div>

        <div class="section-heading">
            <h2>Provider comparison</h2>
            <span class="badge">CROSS-CHECK</span>
        </div>

        <div class="provider-grid" id="providerGrid"></div>

        <div class="actions">
            <button class="btn btn-primary" id="copyButton" type="button">
                Copy report
            </button>
            <button class="btn btn-secondary" id="exportButton" type="button">
                Export JSON
            </button>
            <a class="btn btn-secondary" id="mapsButton"
               href="#" target="_blank" rel="noopener noreferrer" hidden>
                Open map ↗
            </a>
        </div>

        <div class="notice">
            <strong>Interpretation:</strong>
            A provider reports an estimated IP location, not GPS coordinates
            from the device. Provider agreement does not prove the location
            is correct. VPNs, proxies, carrier networks and outdated databases
            can cause inaccurate results.
        </div>
    </section>

    <section class="panel">
        <div class="section-heading" style="margin-top:0">
            <h2>Session history</h2>
            <button class="btn btn-secondary" id="clearHistoryButton" type="button">
                Clear history
            </button>
        </div>
        <div class="help">
            Recent lookups are kept only while this page remains open.
        </div>
        <div id="historyList" style="margin-top:12px">
            <div class="empty">No lookups yet.</div>
        </div>
    </section>
</main>

<footer>
    TRACEPOINT · IP INTELLIGENCE DASHBOARD<br>
    For education and authorized OSINT research. Geolocation is approximate.
    External providers receive the IP address submitted for lookup.
</footer>

<script>
"use strict";

const $ = id => document.getElementById(id);

const form = $("lookupForm");
const input = $("ipInput");
const button = $("searchButton");
const myIpButton = $("myIpButton");
const clearButton = $("clearButton");
const statusBox = $("status");
const results = $("results");
const providerGrid = $("providerGrid");
const historyList = $("historyList");
const copyButton = $("copyButton");
const exportButton = $("exportButton");
const mapsButton = $("mapsButton");

let latestReport = null;
let history = [];
let activeController = null;

// Only digits and dots are allowed. The actual IP is validated on submit.
input.addEventListener("input", () => {
    let value = input.value.replace(/[^0-9.]/g, "").slice(0, 15);

    // Keep at most four octets and at most three digits per octet.
    const parts = value.split(".").slice(0, 4).map(p => p.slice(0, 3));
    input.value = parts.join(".").slice(0, 15);
});

function validIPv4(ip) {
    const parts = ip.split(".");
    if (parts.length !== 4) return false;

    return parts.every(part =>
        /^\d{1,3}$/.test(part) &&
        Number(part) >= 0 &&
        Number(part) <= 255
    );
}

function isPublicIPv4(ip) {
    const [a, b, c] = ip.split(".").map(Number);

    if (a === 0 || a === 10 || a === 127 || a >= 224) return false;
    if (a === 100 && b >= 64 && b <= 127) return false;
    if (a === 169 && b === 254) return false;
    if (a === 172 && b >= 16 && b <= 31) return false;
    if (a === 192 && b === 168) return false;
    if (a === 192 && b === 0 && c === 0) return false;
    if (a === 192 && b === 0 && c === 2) return false;
    if (a === 198 && (b === 18 || b === 19)) return false;
    if (a === 198 && b === 51 && c === 100) return false;
    if (a === 203 && b === 0 && c === 113) return false;
    if (a === 255 && b === 255 && c === 255) return false;

    return true;
}

function setStatus(message, type = "") {
    statusBox.className = type;
    statusBox.replaceChildren();

    if (type === "loading") {
        const spinner = document.createElement("span");
        spinner.className = "spinner";
        statusBox.appendChild(spinner);
    }

    statusBox.appendChild(document.createTextNode(message));
}

function addField(card, label, value) {
    const field = document.createElement("div");
    field.className = "field";

    const title = document.createElement("span");
    title.className = "field-label";
    title.textContent = label;

    const content = document.createElement("span");
    content.className = "field-value";
    content.textContent =
        value === null || value === undefined || value === ""
            ? "Unavailable"
            : String(value);

    field.append(title, content);
    card.appendChild(field);
}

function normalizeProvider(name, raw, error = null) {
    if (error || !raw) return { name, data: null, error: error || "No data" };

    const failed = raw.error === true ||
                   raw.success === false ||
                   !raw.ip;

    if (failed) {
        return {
            name,
            data: null,
            error: raw.reason || raw.message || "Provider returned no data"
        };
    }

    const timezone = typeof raw.timezone === "object"
        ? raw.timezone?.id
        : raw.timezone;

    return {
        name,
        error: null,
        data: {
            ip: raw.ip,
            city: raw.city || "",
            region: raw.region || raw.region_name || "",
            country: raw.country_name || raw.country || "",
            countryCode: raw.country_code || "",
            latitude: raw.latitude ?? null,
            longitude: raw.longitude ?? null,
            org: raw.org || raw.connection?.isp || raw.connection?.org || "",
            asn: raw.asn || raw.connection?.asn || "",
            timezone: timezone || "",
            postal: raw.postal || ""
        }
    };
}

async function fetchProvider(name, url, signal) {
    try {
        const response = await fetch(url, {
            signal,
            headers: { "Accept": "application/json" }
        });

        if (!response.ok) {
            throw new Error("HTTP " + response.status);
        }

        const raw = await response.json();
        return normalizeProvider(name, raw);
    } catch (error) {
        return normalizeProvider(name, null, error.name === "AbortError"
            ? "Request timed out or was cancelled"
            : error.message);
    }
}

function renderProvider(provider) {
    const card = document.createElement("article");
    card.className = "card";

    const heading = document.createElement("h3");
    heading.textContent = provider.name;
    card.appendChild(heading);

    if (!provider.data) {
        addField(card, "Status", "Lookup failed");
        addField(card, "Details", provider.error);
        return card;
    }

    const d = provider.data;
    addField(card, "IP address", d.ip);
    addField(card, "City", d.city);
    addField(card, "Region", d.region);
    addField(card, "Country", d.country);
    addField(card, "Country code", d.countryCode);
    addField(card, "Latitude", d.latitude);
    addField(card, "Longitude", d.longitude);
    addField(card, "Organization / ISP", d.org);
    addField(card, "ASN", d.asn);
    addField(card, "Timezone", d.timezone);
    addField(card, "Postal code", d.postal);

    if (d.latitude != null && d.longitude != null) {
        const link = document.createElement("a");
        link.className = "map-link";
        link.href = mapURL(d.latitude, d.longitude);
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        link.textContent = "View approximate coordinates ↗";
        card.appendChild(link);
    }

    return card;
}

function mapURL(lat, lon) {
    return "https://www.google.com/maps?q=" +
        encodeURIComponent(`${lat},${lon}`);
}

function updateOverview(providers, targetIP) {
    const good = providers.filter(p => p.data);
    if (!good.length) return;

    const d = good[0].data;

    $("metricIP").textContent = targetIP;
    $("metricCountry").textContent = d.country || "Unknown";
    $("metricCountryCode").textContent = d.countryCode || "Country code unavailable";
    $("metricLocation").textContent =
        [d.city, d.region].filter(Boolean).join(", ") || "Unknown";
    $("metricCoordinates").textContent =
        d.latitude != null && d.longitude != null
            ? `${d.latitude}, ${d.longitude}`
            : "Unavailable";
    $("metricISP").textContent = d.org || "Unavailable";
    $("metricTimezone").textContent = d.timezone || "Unavailable";

    if (d.latitude != null && d.longitude != null) {
        mapsButton.href = mapURL(d.latitude, d.longitude);
        mapsButton.hidden = false;
    } else {
        mapsButton.hidden = true;
    }
}

function compareProviders(providers) {
    const good = providers.filter(p => p.data);

    if (good.length < 2) {
        $("resultBadge").textContent =
            good.length === 1 ? "PARTIAL DATA" : "LOOKUP FAILED";
        return "Only one provider returned data, or both failed.";
    }

    const a = good[0].data;
    const b = good[1].data;

    const sameCountry = a.countryCode && b.countryCode &&
        a.countryCode.toUpperCase() === b.countryCode.toUpperCase();

    const sameCity = a.city && b.city &&
        a.city.toLowerCase() === b.city.toLowerCase();

    if (sameCountry && sameCity) {
        $("resultBadge").textContent = "CITY + COUNTRY AGREE";
        return "Both providers report the same city and country. This does not guarantee accuracy.";
    }

    if (sameCountry) {
        $("resultBadge").textContent = "COUNTRY AGREES";
        return "The country matches, but the city or region differs.";
    }

    $("resultBadge").textContent = "RESULTS DIFFER";
    return "Providers disagree. Compare the returned data; neither result is guaranteed correct.";
}

function addHistory(ip, location) {
    history = history.filter(item => item.ip !== ip);
    history.unshift({
        ip,
        location: location || "Location unavailable",
        time: new Date().toLocaleTimeString()
    });

    history = history.slice(0, 8);
    renderHistory();
}

function renderHistory() {
    historyList.replaceChildren();

    if (!history.length) {
        const empty = document.createElement("div");
        empty.className = "empty";
        empty.textContent = "No lookups yet.";
        historyList.appendChild(empty);
        return;
    }

    history.forEach(item => {
        const row = document.createElement("div");
        row.className = "history-item";

        const info = document.createElement("div");

        const ip = document.createElement("div");
        ip.className = "history-ip";
        ip.textContent = item.ip;

        const loc = document.createElement("div");
        loc.className = "history-location";
        loc.textContent = item.location + " · " + item.time;

        info.append(ip, loc);

        const open = document.createElement("button");
        open.className = "history-open";
        open.type = "button";
        open.textContent = "Analyze ↗";
        open.addEventListener("click", () => {
            input.value = item.ip;
            performLookup(item.ip);
        });

        row.append(info, open);
        historyList.appendChild(row);
    });
}

async function performLookup(ip) {
    if (!validIPv4(ip)) {
        results.hidden = true;
        setStatus("Invalid IPv4. Use four numbers from 0 to 255, e.g. 8.8.8.8.", "error");
        input.focus();
        return;
    }

    if (!isPublicIPv4(ip)) {
        results.hidden = true;
        setStatus("This address is private or reserved. Enter a public IPv4 address.", "error");
        return;
    }

    if (activeController) activeController.abort();
    activeController = new AbortController();

    const controller = activeController;
    const timeout = setTimeout(() => controller.abort(), 12000);

    button.disabled = true;
    myIpButton.disabled = true;
    button.textContent = "Analyzing...";
    results.hidden = true;
    setStatus("Querying geolocation providers...", "loading");

    try {
        const encoded = encodeURIComponent(ip);

        const providers = await Promise.all([
            fetchProvider(
                "ipapi.co",
                `https://ipapi.co/${encoded}/json/`,
                controller.signal
            ),
            fetchProvider(
                "ipwho.is",
                `https://ipwho.is/${encoded}`,
                controller.signal
            )
        ]);

        if (controller.signal.aborted && activeController !== controller) return;

        providerGrid.replaceChildren();
        providers.forEach(p => providerGrid.appendChild(renderProvider(p)));

        const good = providers.filter(p => p.data && p.data.ip);

        if (!good.length) {
            results.hidden = true;
            setStatus("Both providers failed. Check your connection or try again later.", "error");
            return;
        }

        updateOverview(providers, ip);

        const comparison = compareProviders(providers);
        latestReport = {
            targetIP: ip,
            checkedAt: new Date().toISOString(),
            comparison,
            providers: providers.map(p => ({
                provider: p.name,
                error: p.error,
                data: p.data
            }))
        };

        results.hidden = false;

        const first = good[0].data;
        addHistory(ip, [first.city, first.country].filter(Boolean).join(", "));

        setStatus(comparison, "success");

    } catch (error) {
        results.hidden = true;
        setStatus("Lookup error: " + error.message, "error");
    } finally {
        clearTimeout(timeout);

        if (activeController === controller) {
            activeController = null;
            button.disabled = false;
            myIpButton.disabled = false;
            button.textContent = "Analyze IP →";
        }
    }
}

form.addEventListener("submit", event => {
    event.preventDefault();
    performLookup(input.value.trim());
});

myIpButton.addEventListener("click", async () => {
    myIpButton.disabled = true;
    setStatus("Discovering your public IP...", "loading");

    try {
        const response = await fetch("https://api.ipify.org?format=json");

        if (!response.ok) throw new Error("Could not discover public IP");

        const data = await response.json();

        if (!validIPv4(data.ip) || !isPublicIPv4(data.ip)) {
            throw new Error("The service did not return a public IPv4 address");
        }

        input.value = data.ip;
        await performLookup(data.ip);

    } catch (error) {
        setStatus("Could not discover your public IP: " + error.message, "error");
    } finally {
        myIpButton.disabled = false;
    }
});

clearButton.addEventListener("click", () => {
    if (activeController) activeController.abort();

    input.value = "";
    results.hidden = true;
    latestReport = null;
    providerGrid.replaceChildren();
    mapsButton.hidden = true;

    setStatus("Ready. Enter an IPv4 address to begin.");
    input.focus();
});

$("clearHistoryButton").addEventListener("click", () => {
    history = [];
    renderHistory();
});

copyButton.addEventListener("click", async () => {
    if (!latestReport) return;

    try {
        await navigator.clipboard.writeText(
            JSON.stringify(latestReport, null, 2)
        );
        setStatus("JSON report copied to clipboard.", "success");
    } catch {
        setStatus("Clipboard unavailable. Use Export JSON instead.", "error");
    }
});

exportButton.addEventListener("click", () => {
    if (!latestReport) return;

    const blob = new Blob(
        [JSON.stringify(latestReport, null, 2)],
        { type: "application/json" }
    );

    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `ip-report-${latestReport.targetIP}.json`;
    link.click();
    URL.revokeObjectURL(url);

    setStatus("JSON report exported.", "success");
});
</script>

</body>
</html>


