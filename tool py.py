
#!/usr/bin/env python3
import argparse
import ipaddress
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

VERSION = "1.0.0"
PROVIDERS = {
    "ipapi": "https://ipapi.co/{ip}/json/",
    "ipwho": "https://ipwho.is/{ip}",
}


def get_location(provider, ip, timeout):
    response = requests.get(
        PROVIDERS[provider].format(ip=ip),
        timeout=timeout,
        headers={"User-Agent": f"TracePoint/{VERSION}"},
    )
    response.raise_for_status()
    data = response.json()

    if data.get("error") or data.get("success") is False:
        raise RuntimeError(data.get("reason") or data.get("message") or "API error")

    if provider == "ipapi":
        return {
            "provider": "ipapi.co",
            "ip": data.get("ip", ip),
            "country": data.get("country_name"),
            "country_code": data.get("country_code"),
            "region": data.get("region"),
            "city": data.get("city"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "timezone": data.get("timezone"),
            "organization": data.get("org"),
            "postal_code": data.get("postal"),
        }

    connection = data.get("connection") or {}
    timezone_data = data.get("timezone") or {}
    return {
        "provider": "ipwho.is",
        "ip": data.get("ip", ip),
        "country": data.get("country"),
        "country_code": data.get("country_code"),
        "region": data.get("region"),
        "city": data.get("city"),
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "timezone": timezone_data.get("id"),
        "organization": connection.get("org"),
        "isp": connection.get("isp"),
        "postal_code": data.get("postal"),
    }


def show_result(data):
    print(f"\n--- {data['provider']} ---")
    for key, value in data.items():
        if value not in (None, ""):
            print(f"{key.replace('_', ' ').title():20}: {value}")

    lat, lon = data.get("latitude"), data.get("longitude")
    if lat is not None and lon is not None:
        print(f"{'Map':20}: https://www.google.com/maps?q={lat},{lon}")


def main():
    parser = argparse.ArgumentParser(
        description="TracePoint - Kali Linux IP geolocation CLI"
    )
    parser.add_argument("ip", help="Public IPv4 address to look up")
    parser.add_argument(
        "--compare",
        action="store_true",
        help="Compare both geolocation providers",
    )
    parser.add_argument(
        "--provider",
        choices=PROVIDERS,
        default="ipapi",
        help="Provider to use (default: ipapi)",
    )
    parser.add_argument("--json", metavar="FILE", help="Save a JSON report")
    parser.add_argument("--timeout", type=int, default=10)
    parser.add_argument("--no-color", action="store_true",
                        help="Accepted for compatibility; output is plain text")
    parser.add_argument("--version", action="version",
                        version=f"TracePoint {VERSION}")
    args = parser.parse_args()

    try:
        address = ipaddress.ip_address(args.ip)
    except ValueError:
        parser.error("Invalid IP address")

    if address.version != 4 or not address.is_global:
        parser.error("Provide a public, globally routable IPv4 address")
    if not 1 <= args.timeout <= 120:
        parser.error("--timeout must be between 1 and 120 seconds")

    print("=" * 42)
    print(f" TRACEPOINT v{VERSION} | KALI LINUX")
    print("=" * 42)
    print(f"Target: {address}")
    print("Note: geolocation is approximate.")

    providers = list(PROVIDERS) if args.compare else [args.provider]
    results = []

    for provider in providers:
        print(f"\n[*] Querying {provider}...")
        try:
            result = get_location(provider, str(address), args.timeout)
            results.append({"ok": True, "data": result, "error": None})
            show_result(result)
        except (requests.RequestException, ValueError, RuntimeError) as exc:
            print(f"[!] {provider} failed: {exc}")
            results.append({
                "ok": False,
                "provider": provider,
                "data": None,
                "error": str(exc),
            })

    comparison = None
    if args.compare and all(item["ok"] for item in results):
        first, second = [item["data"] for item in results]
        fields = ("country_code", "region", "city", "organization")
        comparison = {}
        for field in fields:
            a, b = first.get(field), second.get(field)
            if a and b and str(a).casefold() != str(b).casefold():
                comparison[field] = {
                    first["provider"]: a,
                    second["provider"]: b,
                }

        print("\n--- Provider comparison ---")
        if comparison:
            for field, values in comparison.items():
                print(f"{field}: {values}")
        else:
            print("No differences found in comparable fields.")

    if args.json:
        report = {
            "tool": "TracePoint",
            "version": VERSION,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "target_ip": str(address),
            "results": results,
            "comparison": comparison,
            "notice": "IP geolocation is approximate.",
        }
        try:
            output = Path(args.json).expanduser()
            output.write_text(
                json.dumps(report, indent=2) + "\n",
                encoding="utf-8",
            )
            print(f"\n[+] JSON report saved: {output}")
        except OSError as exc:
            print(f"[!] Could not save report: {exc}")
            return 1

    return 0 if any(item["ok"] for item in results) else 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n[!] Interrupted.")
        sys.exit(130)
