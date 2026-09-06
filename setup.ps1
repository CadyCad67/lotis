# ============================================================================
# LOTIS V1 -- postawienie srodowiska od zera
#
#   .\setup.ps1
#
# Skrypt jest idempotentny: mozna go puscic ponownie na istniejacym
# srodowisku i nic nie zepsuje.
# ============================================================================

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

function Krok($n, $tekst) { Write-Host "`n[$n] $tekst" -ForegroundColor Cyan }
function Ok($tekst)       { Write-Host "  OK  $tekst" -ForegroundColor Green }
function Uwaga($tekst)    { Write-Host "  !!  $tekst" -ForegroundColor Yellow }

Krok 1 "Szukam interpretera Pythona 3.11+"

$kandydaci = @(
    "$PSScriptRoot\.venv\Scripts\python.exe",
    "$env:USERPROFILE\miniconda3\python.exe",
    "$env:USERPROFILE\anaconda3\python.exe",
    "$env:LOCALAPPDATA\anaconda3\python.exe"
)
$bazowy = $null
foreach ($k in $kandydaci) {
    if (Test-Path $k) {
        $w = & $k -c "import sys; print('%d.%d' % sys.version_info[:2])" 2>$null
        if ($w) {
            $czesci = $w.Split('.')
            if ([int]$czesci[0] -ge 3 -and [int]$czesci[1] -ge 11) {
                $bazowy = $k
                Ok "$k  (Python $w)"
                break
            }
        }
    }
}
if (-not $bazowy) {
    throw "Nie znalazlem Pythona 3.11+. Zainstaluj Anaconda/Miniconda albo python.org."
}

Krok 2 "Srodowisko wirtualne .venv"

if (Test-Path "$PSScriptRoot\.venv\Scripts\python.exe") {
    Ok "juz istnieje"
} else {
    & $bazowy -m venv .venv
    Ok "utworzone"
}
$py = "$PSScriptRoot\.venv\Scripts\python.exe"

Krok 3 "Zaleznosci"

# Silnik jest stdlib-only. Jedyna prawdziwa zaleznosc to tzdata: Windows nie ma
# systemowej bazy stref IANA, a caly modul portow stoi na zoneinfo.
& $py -m pip install --quiet --upgrade pip
& $py -m pip install --quiet -e .
Ok "lotis zainstalowany w trybie edytowalnym (import dziala z dowolnego katalogu)"

Krok 4 "Konfiguracja"

if (Test-Path "$PSScriptRoot\.env") {
    Ok ".env juz istnieje -- nie nadpisuje"
} else {
    Copy-Item "$PSScriptRoot\.env.example" "$PSScriptRoot\.env"
    Ok ".env utworzony z wzorca"
    Uwaga "Wklej klucz OPENROUTER_API_KEY do .env, jesli chcesz uzywac warstwy AI"
}

Krok 5 "Dane"

$brakuje = @()
foreach ($plik in @("data\loops.jsx", "data\lot-siatka.json")) {
    if (Test-Path "$PSScriptRoot\$plik") {
        $mb = [math]::Round((Get-Item "$PSScriptRoot\$plik").Length / 1MB, 2)
        Ok "$plik  ($mb MB)"
    } else {
        $brakuje += $plik
    }
}
if ($brakuje.Count -gt 0) {
    Uwaga "Brakuje: $($brakuje -join ', ')"
    Uwaga "Skopiuj je do data\ albo wskaz sciezki w .env"
}

Krok 6 "Kontrola"

& "$PSScriptRoot\.venv\Scripts\lotis.exe" doctor
if ($LASTEXITCODE -ne 0) {
    throw "lotis doctor zglosil bledy -- zobacz wyzej"
}

Write-Host "`n============================================================" -ForegroundColor Green
Write-Host "Gotowe. Aktywuj srodowisko i pracuj:" -ForegroundColor Green
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host "  lotis doctor"
Write-Host "  lotis snapshot --day 4"
Write-Host "  lotis analiza"
Write-Host "  lotis models --free"
Write-Host "============================================================" -ForegroundColor Green
