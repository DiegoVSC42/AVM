# PowerShell Frontend Deployment Script

# Define variables
$KeyFile = "id_rsa_euvereador"
$ServerUser = "ueuvereuser"
$ServerIP = "159.203.175.56"
$ServerPort = "2244"
$RemotePath = "/home/ueuvereuser/apps/euvereador/client/dist/"

# Function to print colored messages
function Write-Color($Text, $Color) {
    Write-Host $Text -ForegroundColor $Color
}

Write-Color "Starting Frontend Deployment..." "Cyan"

# Ensure key exists
if (-not (Test-Path $KeyFile)) {
    Write-Color "Error: Key file '$KeyFile' not found in current directory." "Red"
    exit 1
}

# Navigate to client directory and build
Write-Color "Building frontend..." "Yellow"
if (-not (Test-Path "EuVereadorAI-client")) {
    Write-Color "Error: Could not find EuVereadorAI-client directory. Make sure you are in the project root." "Red"
    exit 1
}
Push-Location EuVereadorAI-client -ErrorAction SilentlyContinue

npm run build
if ($LASTEXITCODE -ne 0) { Write-Color "Error: Build failed." "Red"; Pop-Location; exit 1 }
Pop-Location

Write-Color "Deploying to server..." "Yellow"

# Clean remote directory
Write-Color "Cleaning remote directory..." "DarkCyan"
ssh -i $KeyFile -p $ServerPort "$ServerUser@$ServerIP" "rm -rf ${RemotePath}*"
if ($LASTEXITCODE -ne 0) { Write-Color "Error: Failed to clean remote directory." "Red"; exit 1 }

# Copy new files from EuVereadorAI-client/dist
Write-Color "Uploading files..." "DarkCyan"
scp -i $KeyFile -P $ServerPort -r EuVereadorAI-client/dist/* "$ServerUser@${ServerIP}:$RemotePath"
if ($LASTEXITCODE -ne 0) { Write-Color "Error: Failed to upload files." "Red"; exit 1 }

# Restart PM2
Write-Color "Restarting frontend application on server..." "DarkCyan"
ssh -i $KeyFile -p $ServerPort "$ServerUser@$ServerIP" "source ~/.nvm/nvm.sh && pm2 restart euvereador-client"
if ($LASTEXITCODE -ne 0) { Write-Color "Error: Failed to restart application." "Red"; exit 1 }

Write-Color "Frontend Deployment complete!" "Green"
