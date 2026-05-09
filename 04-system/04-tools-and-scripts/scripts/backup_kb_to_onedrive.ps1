# =============================================================================
# backup_kb_to_onedrive.ps1
# Espejo incremental del Knowledge Base de /RAUL/ hacia OneDrive
# =============================================================================
# Fuente:  C:\RAUL\02-knowledge-base   (configurable via $env:RAUL_ROOT)
# Destino: C:\Users\User\OneDrive\RAUL-backup\02-knowledge-base
# Modo:    /MIR (mirror — refleja exactamente el estado de la fuente)
# Recovery: OneDrive conserva historial de versiones ~30 dias
# Frecuencia: diaria (configurada via Task Scheduler)
# =============================================================================

# RAUL_ROOT con fallback a C:\RAUL si la variable de entorno no esta seteada
if ($env:RAUL_ROOT) {
    $root = $env:RAUL_ROOT
} else {
    $root = "C:\RAUL"
}

$source  = Join-Path $root "02-knowledge-base"
$dest    = "C:\Users\User\OneDrive\RAUL-backup\02-knowledge-base"
$logDir  = Join-Path $root "04-system\04-tools-and-scripts\scripts\logs"
$logFile = Join-Path $logDir "backup_kb.log"

# Crear carpeta de logs si no existe
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }

function Write-Log($msg) {
    $line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $msg"
    Add-Content -Path $logFile -Value $line -Encoding utf8
    Write-Host $line
}

Write-Log "=== Backup KB -> OneDrive ==="

# Safety check 1: fuente debe existir
if (-not (Test-Path $source)) {
    Write-Log "ABORT: source not found ($source)"
    exit 1
}

# Safety check 2: fuente debe tener un mínimo de archivos (evita borrar OneDrive si KB se vacía por error)
$fileCount = (Get-ChildItem $source -Recurse -File -ErrorAction SilentlyContinue).Count
if ($fileCount -lt 10) {
    Write-Log "ABORT: source has only $fileCount files (suspiciously low). Aborting to protect OneDrive backup."
    exit 1
}

# Crear destino si no existe
if (-not (Test-Path $dest)) {
    New-Item -ItemType Directory -Path $dest -Force | Out-Null
    Write-Log "Created destination: $dest"
}

# robocopy con flags:
#   /MIR : mirror (incluye eliminacion de archivos que ya no estan en source)
#   /R:2 : reintentar 2 veces
#   /W:5 : esperar 5s entre reintentos
#   /NP  : sin barra de progreso
#   /NFL : no listar nombres de archivos individuales en log
#   /NDL : no listar nombres de directorios en log
#   /TEE : output a consola y log
robocopy $source $dest /MIR /R:2 /W:5 /NP /NFL /NDL /LOG+:$logFile

# robocopy exit codes: 0=no changes, 1=files copied, 2=extra files, 3=both, >=8=error
$rc = $LASTEXITCODE
if ($rc -ge 8) {
    Write-Log "ROBOCOPY ERROR: exit code $rc"
    exit $rc
} else {
    Write-Log "DONE: source files=$fileCount, robocopy exit=$rc"
    exit 0
}
