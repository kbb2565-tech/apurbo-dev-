# ═══════════════════════════════════════════════════════════════════════════
#   AGS PKG — Protected Build v3
#   Credit: AGS (obfuscated)
# ═══════════════════════════════════════════════════════════════════════════
import subprocess
import sys
import os
import time
import shutil
import platform
import threading
import base64
import hashlib
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed

# ── rich auto-install ──
try:
    from rich.console import Console, Group
    from rich.live import Live
    from rich.panel import Panel
    from rich.progress import (
        Progress, BarColumn, TextColumn, TaskProgressColumn,
        TimeElapsedColumn, TimeRemainingColumn, SpinnerColumn,
    )
    from rich.table import Table
    from rich.text import Text
    from rich.align import Align
    from rich.box import ROUNDED, DOUBLE
except ImportError:
    print("Installing rich...")
    subprocess.run([sys.executable, "-m", "pip", "install", "rich"], check=False)
    from rich.console import Console, Group
    from rich.live import Live
    from rich.panel import Panel
    from rich.progress import (
        Progress, BarColumn, TextColumn, TaskProgressColumn,
        TimeElapsedColumn, TimeRemainingColumn, SpinnerColumn,
    )
    from rich.table import Table
    from rich.text import Text
    from rich.align import Align
    from rich.box import ROUNDED, DOUBLE


console = Console()   


_K1 = bytes.fromhex("414753415446")
_K2 = bytes.fromhex("f0e1d2c3b4a5968778695a4b3c2d1e0f")


def _xor(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def _decrypt_blob(blob_b64: str) -> str:
    try:
        step1 = base64.b64decode(blob_b64)
        step2 = _xor(step1, _K2)
        step3 = _xor(step2, _K1)
        return step3.decode("utf-8", errors="ignore")
    except Exception:
        return ""


def _generate_payload(plain_text: str) -> str:
    """Encrypt plain text → base64 string"""
    s1 = _xor(plain_text.encode(), _K1)
    s2 = _xor(s1, _K2)
    return base64.b64encode(s2).decode()


_PAYLOAD_WARNING = _generate_payload(
    "AGS TOR MARE CHUD KANKIR POLA CREDIT CHUR "
    "TORE MARE KUTTA DIYA CHUDAMU BEISSAR BETA"
)
_PAYLOAD_CREDIT  = _generate_payload("AGS")
_PAYLOAD_BANNER  = _generate_payload("AGS PKG")


def _integrity_check():
    try:
        with open(__file__, "r", encoding="utf-8", errors="ignore") as f:
            src = f.read()
    except Exception:
        return

    markers = ["_PAYLOAD_WARNING", "_PAYLOAD_CREDIT", "AGS PKG"]
    forbidden = ["credit: someone_else", "author: someone_else"]

    missing = [m for m in markers if m not in src]
    tampered = [f for f in forbidden if f.lower() in src.lower()]

    if missing or tampered:
        warn = _decrypt_blob(_PAYLOAD_WARNING)
        print()
        print("=" * 70)
        print(warn)
        print("=" * 70)
        print()



BANNER = r"""
   █████╗  ██████╗ ███████╗    ██████╗ ██╗  ██╗ ██████╗
  ██╔══██╗██╔════╝ ██╔════╝    ██╔══██╗██║ ██╔╝██╔════╝
  ███████║██║  ███╗███████╗    ██████╔╝█████╔╝ ██║  ███╗
  ██╔══██║██║   ██║╚════██║    ██╔═══╝ ██╔═██╗ ██║   ██║
  ██║  ██║╚██████╔╝███████║    ██║     ██║  ██╗╚██████╔╝
  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝
"""



PIP_PACKAGES = [
    "aiohttp", "aiofiles", "aiohttp-socks", "requests", "requests-toolbelt",
    "httpx", "urllib3", "websockets", "websocket-client", "PySocks",
    "socksio", "httpcore", "h11", "h2", "anyio", "sniffio", "idna", "certifi",
    "charset-normalizer", "chardet", "dnspython", "publicsuffix2",
    "python-telegram-bot", "pyTelegramBotAPI", "aiogram", "telethon",
    "telebot", "pyrogram", "tgcrypto", "python-socks",
    "pycryptodome", "pycryptodomex", "cryptography", "rsa", "ecdsa",
    "pynacl", "bcrypt", "passlib", "pyjwt", "itsdangerous", "pyopenssl",
    "argon2-cffi", "cffi", "pyasn1", "pyasn1-modules",
    "protobuf>=6.33.1", "mg24-proto", "protobuf-decoder", "betterproto",
    "curl_cffi", "tls-client", "cloudscraper",
    "colorama", "cfonts", "rich", "termcolor", "pyfiglet", "art",
    "tabulate", "tqdm", "prompt-toolkit", "questionary", "inquirer",
    "blessed", "halo", "yaspin", "alive-progress", "enlighten",
    "wcwidth", "colorful", "coloredlogs", "pygments", "click", "typer",
    "python-dotenv", "python-dateutil", "pytz", "tzdata",
    "pandas", "numpy", "beautifulsoup4", "lxml", "html5lib",
    "pyyaml", "toml", "tomli", "orjson", "ujson", "simplejson",
    "msgpack", "xmltodict", "jsonschema", "regex", "emoji", "unidecode",
    "phonenumbers", "pycountry", "iso8601", "babel",
    "psutil", "py-cpuinfo", "distro", "packaging", "virtualenv",
    "filelock", "platformdirs", "importlib-metadata",
    "typing-extensions", "attrs", "six",
    "flask", "fastapi", "uvicorn", "starlette", "jinja2", "werkzeug",
    "gunicorn", "pydantic", "email-validator", "flask-cors",
    "sqlalchemy", "aiosqlite", "redis", "pymongo", "motor",
    "asyncpg", "psycopg2-binary", "aiomysql", "alembic",
    "faker", "shortuuid", "pillow", "qrcode", "openpyxl", "xlsxwriter",
    "humanize", "inflect", "python-slugify", "loguru", "colorlog",
    "structlog", "retrying", "tenacity", "backoff", "cachetools",
    "diskcache", "joblib", "multiprocess", "dill", "cloudpickle",
    "watchdog", "schedule", "apscheduler", "python-multipart",
    "wrapt", "deprecated", "semver", "jsonpath-ng",
    "pytest", "pytest-asyncio", "coverage", "tox",
    "scapy", "netaddr", "mac-vendor-lookup", "netifaces",
    "ifaddr", "speedtest-cli", "whois", "geoip2", "maxminddb",
    "paramiko", "fabric",
    "gitpython", "dulwich", "pathspec", "gitdb", "smmap",
    "treelib", "pyserial", "pymysql", "retry", "pyotp", "texttable",
    "rapidfuzz", "marshmallow", "cerberus", "voluptuous",
    "yarl", "multidict", "frozenlist", "aiosignal", "async-timeout",
]


TERMUX_PACKAGES = [
    "python", "python-pip", "python-dev", "openssl", "openssl-dev",
    "libffi", "libffi-dev", "clang", "make", "cmake", "pkg-config",
    "git", "wget", "curl", "nano", "vim", "htop",
    "nodejs", "npm", "yarn", "rust", "cargo", "binutils",
    "zlib", "zlib-dev", "libxml2", "libxml2-dev", "libxslt", "libxslt-dev",
    "termux-api", "termux-tools", "dnsutils", "traceroute",
    "net-tools", "iproute2", "jq", "unzip", "zip", "tar", "gzip",
    "bzip2", "xz-utils", "sqlite", "aria2", "rsync", "openssh",
    "tmux", "screen", "bat", "fd", "ripgrep", "fzf", "tree", "less",
]


NPM_PACKAGES = [
    "vercel", "nodemon", "pm2", "typescript", "ts-node",
    "http-server", "json-server", "localtunnel", "serve",
    "concurrently", "rimraf", "cross-env", "yarn", "pnpm",
    "esbuild", "prettier", "eslint", "tldr",
]



def run(cmd, timeout=900):
    try:
        r = subprocess.run(
            cmd, check=False,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, timeout=timeout,
        )
        out = (r.stdout or "").lower()
        if "already satisfied" in out:
            return True
        if r.returncode == 100:
            return True
        if "eexist" in out:
            return True
        return r.returncode == 0
    except subprocess.TimeoutExpired:
        return False
    except Exception:
        return False


def is_termux():
    return "com.termux" in os.environ.get("PREFIX", "") or os.path.exists("/data/data/com.termux")


def has_cmd(name):
    return shutil.which(name) is not None


class LiveState:
    def __init__(self):
        self.lock = threading.Lock()
        self.log = deque(maxlen=15)
        self.done = 0
        self.total = 0
        self.failed = []
        self.ok = 0
        self.phase = "starting"
        self.start_time = time.time()

    def push_log(self, text):
        with self.lock:
            self.log.append(text)

    def mark_done(self, pkg, kind, success):
        with self.lock:
            self.done += 1
            if success:
                self.ok += 1
            else:
                self.failed.append((pkg, kind))


STATE = LiveState()


def _install_pip(pkg):
    for _ in range(2):
        ok = run([sys.executable, "-m", "pip", "install",
                  "--upgrade", "--no-cache-dir", pkg], timeout=600)
        if ok:
            STATE.push_log(f"[green]✓[/green] pip install {pkg}")
            STATE.mark_done(pkg, "pip", True)
            return pkg, True, "pip"
        time.sleep(1.0)
    STATE.push_log(f"[red]✗[/red] pip install {pkg}")
    STATE.mark_done(pkg, "pip", False)
    return pkg, False, "pip"


def _install_pkg(pkg):
    for _ in range(2):
        ok = run(["pkg", "install", "-y", pkg], timeout=900)
        if ok:
            STATE.push_log(f"[green]✓[/green] pkg install {pkg}")
            STATE.mark_done(pkg, "pkg", True)
            return pkg, True, "pkg"
        time.sleep(1.0)
    STATE.push_log(f"[red]✗[/red] pkg install {pkg}")
    STATE.mark_done(pkg, "pkg", False)
    return pkg, False, "pkg"


def _install_npm(pkg):
    for _ in range(2):
        ok = run(["npm", "install", "-g", pkg], timeout=900)
        if ok:
            STATE.push_log(f"[green]✓[/green] npm install -g {pkg}")
            STATE.mark_done(pkg, "npm", True)
            return pkg, True, "npm"
        time.sleep(1.0)
    STATE.push_log(f"[red]✗[/red] npm install -g {pkg}")
    STATE.mark_done(pkg, "npm", False)
    return pkg, False, "npm"


def build_ui(progress, task_id):
    with STATE.lock:
        done, total, ok = STATE.done, STATE.total, STATE.ok
        failed = list(STATE.failed)
        phase = STATE.phase
        log_lines = list(STATE.log)

    credit_text = _decrypt_blob(_PAYLOAD_CREDIT) or "AGS"

    header_text = Text()
    header_text.append(BANNER.strip("\n"), style="bold cyan")
    header_text.append("\n")
    header_text.append("        ⚡  AGS PKG  ⚡  ", style="bold bright_cyan")
    header_text.append("Mega Parallel Installer  ", style="italic cyan")
    header_text.append("| Credit: ", style="dim")
    header_text.append(credit_text, style="bold magenta")

    header_panel = Panel(
        Align.center(header_text),
        border_style="bright_cyan", box=DOUBLE, padding=(0, 1),
    )

    stats = Table.grid(expand=True)
    for _ in range(5):
        stats.add_column(justify="center")
    stats.add_row(
        f"[bold green]✓ OK[/] [white]{ok}[/]",
        f"[bold red]✗ Fail[/] [white]{len(failed)}[/]",
        f"[bold cyan]▶ Done[/] [white]{done}/{total}[/]",
        f"[bold yellow]⏱ Elapsed[/] [white]{int(time.time() - STATE.start_time)}s[/]",
        f"[bold magenta]⚙ Phase[/] [white]{phase}[/]",
    )

    progress_panel = Panel(
        progress, title="[bold yellow]Progress[/]",
        border_style="yellow", box=ROUNDED, padding=(0, 1),
    )

    log_render = Group(*[Text.from_markup(l) for l in log_lines]) if log_lines else Text("Waiting…", style="dim")
    log_panel = Panel(
        log_render, title="[bold green]Live Install Log[/]",
        border_style="green", box=ROUNDED, padding=(0, 1), height=17,
    )

    return Group(header_panel, stats, progress_panel, log_panel)


def phase_base_upgrade():
    STATE.phase = "base upgrade"
    with console.status("[bold cyan]Upgrading pip / setuptools / wheel…[/]"):
        for p in ["pip", "setuptools", "wheel"]:
            run([sys.executable, "-m", "pip", "install", "--upgrade", p])


def phase_termux():
    if not is_termux() or not has_cmd("pkg"):
        STATE.push_log("[dim]⤿ Skipping Termux pkg (not on Termux)[/]")
        return []
    STATE.phase = "termux pkg"
    STATE.push_log("[cyan]→ pkg update / upgrade…[/]")
    run(["pkg", "update", "-y"], timeout=1800)
    run(["pkg", "upgrade", "-y"], timeout=1800)
    STATE.total += len(TERMUX_PACKAGES)
    return [(p, (lambda pp=p: _install_pkg(pp))) for p in TERMUX_PACKAGES]


def phase_pip():
    STATE.phase = "pip packages"
    STATE.total += len(PIP_PACKAGES)
    return [(p, (lambda pp=p: _install_pip(pp))) for p in PIP_PACKAGES]


def phase_npm():
    if not has_cmd("npm"):
        STATE.push_log("[dim]⤿ Skipping npm (Node.js not installed)[/]")
        return []
    STATE.phase = "npm global"
    STATE.total += len(NPM_PACKAGES)
    return [(p, (lambda pp=p: _install_npm(pp))) for p in NPM_PACKAGES]


def run_phase(tasks):
    if not tasks:
        return
    phase = STATE.phase
    if phase == "pip packages":
        workers = 4
    elif phase == "termux pkg":
        workers = 2
    elif phase == "npm global":
        workers = 3
    else:
        workers = 4

    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(fn) for _, fn in tasks]
        for _ in as_completed(futures):
            pass


def main():
    _integrity_check()
    console.clear()

    info = Table.grid(expand=True)
    info.add_column(style="cyan")
    info.add_column(style="bold white")
    info.add_row("Platform", f"{platform.system()} {platform.release()}")
    info.add_row("Python", sys.version.split()[0])
    info.add_row("Termux", "Yes" if is_termux() else "No")
    info.add_row("CPU cores", str(os.cpu_count() or "?"))
    info.add_row("Safe concurrency", "4 pip / 2 pkg / 3 npm")
    info.add_row("Total packages",
                 f"{len(PIP_PACKAGES) + len(TERMUX_PACKAGES) + len(NPM_PACKAGES)}")

    console.print(Panel(
        Align.center(Text.from_markup(f"[bold cyan]{BANNER}[/]")),
        border_style="bright_cyan", box=DOUBLE,
    ))
    console.print(Panel(info, title="[bold magenta]System Info[/]",
                        border_style="magenta", box=ROUNDED))
    console.print()
    console.print("[yellow]Starting in 3 seconds… Press Ctrl+C to cancel.[/]")
    try:
        time.sleep(3)
    except KeyboardInterrupt:
        console.print("\n[red]Cancelled.[/]")
        sys.exit(0)

    phase_base_upgrade()

    all_tasks = []
    all_tasks += phase_termux()
    all_tasks += phase_pip()
    all_tasks += phase_npm()

    progress = Progress(
        SpinnerColumn(style="cyan"),
        TextColumn("[bold yellow]{task.description}"),
        BarColumn(bar_width=None, complete_style="green", finished_style="bright_green"),
        TaskProgressColumn(),
        TextColumn("[bold cyan]{task.completed}/{task.total}"),
        TextColumn("[dim]elapsed[/] [yellow]{task.elapsed:.0f}s[/]"),
        TextColumn("[dim]eta[/] [magenta]{task.remaining:.0f}s[/]"),
        console=console, expand=True,
    )
    task_id = progress.add_task("Installing…", total=len(all_tasks) or 1)

    with Live(build_ui(progress, task_id), console=console, refresh_per_second=8) as live:
        def ui_loop():
            last_done = -1
            while True:
                with STATE.lock:
                    d, t = STATE.done, STATE.total
                if d != last_done:
                    progress.update(task_id, completed=d, total=t)
                    last_done = d
                live.update(build_ui(progress, task_id))
                if t > 0 and d >= t:
                    break
                time.sleep(0.12)

        ui_thread = threading.Thread(target=ui_loop, daemon=True)
        ui_thread.start()
        run_phase(all_tasks)
        time.sleep(0.6)

    show_done()


def show_done():
    console.clear()
    done_txt = r"""
     ██████╗  ██████╗ ███╗   ██╗███████╗
     ██╔══██╗██╔═══██╗████╗  ██║██╔════╝
     ██║  ██║██║   ██║██╔██╗ ██║█████╗
     ██║  ██║██║   ██║██║╚██╗██║██╔══╝
     ██████╔╝╚██████╔╝██║ ╚████║███████╗
     ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
    """
    console.print(Align.center(Text(done_txt.strip("\n"), style="bold bright_green")))
    console.print()
    console.print(Panel(
        Align.center(Text.from_markup(
            "[bold bright_green]✅  INSTALLATION COMPLETE[/]\n"
            "[italic cyan]AGS PKG — All systems ready[/]"
        )),
        border_style="bright_green", box=DOUBLE,
    ))

    with STATE.lock:
        done, ok = STATE.done, STATE.ok
        failed = list(STATE.failed)

    elapsed = round(time.time() - STATE.start_time, 1)
    credit_text = _decrypt_blob(_PAYLOAD_CREDIT) or "AGS"

    tbl = Table(title="[bold yellow]Summary[/]", box=ROUNDED,
                border_style="yellow", show_header=False)
    tbl.add_column("Field", style="cyan", no_wrap=True)
    tbl.add_column("Value", style="bold white")
    tbl.add_row("Total packages", str(done))
    tbl.add_row("✓ Successful", f"[green]{ok}[/]")
    tbl.add_row("✗ Failed", f"[red]{len(failed)}[/]")
    tbl.add_row("Time elapsed", f"[yellow]{elapsed}s[/]")
    tbl.add_row("Credit", f"[bold magenta]{credit_text}[/]")
    console.print(tbl)

    if failed:
        ft = Table(title=f"[bold red]⚠ Failed ({len(failed)})[/]",
                   box=ROUNDED, border_style="red")
        ft.add_column("Package", style="bold white")
        ft.add_column("Type", style="yellow")
        for name, kind in failed[:25]:
            ft.add_row(name, kind)
        console.print(ft)
    else:
        console.print(Align.center(Text("🎉  No failures — everything OK!",
                                        style="bold bright_green")))

    console.print()
    console.print(Panel(
        Align.center(Text.from_markup(
            "[dim italic]Thank you for using AGS PKG[/]\n"
            f"[bold magenta]— {credit_text} —[/]"
        )),
        border_style="magenta", box=ROUNDED,
    ))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user.[/]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]Unexpected error: {e}[/]")
        sys.exit(1)