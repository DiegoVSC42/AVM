# PowerShell Backend Deployment Script

# Define variables
$KeyFile = "id_rsa_euvereador"
$ServerUser = "ueuvereuser"
$ServerIP = "159.203.175.56"
$ServerPort = "2244"
$RemotePath = "/home/ueuvereuser/apps/euvereador/backend/dist/"

# Function to print colored messages
function Write-Color($Text, $Color) {
    Write-Host $Text -ForegroundColor $Color
}

Write-Color "Starting Backend Deployment..." "Cyan"

# Ensure key exists
if (-not (Test-Path $KeyFile)) {
    Write-Color "Error: Key file '$KeyFile' not found in current directory." "Red"
    exit 1
}

# Navigate to server directory and build
Write-Color "Building backend..." "Yellow"
if (-not (Test-Path "EuVereadorAI-server")) {
    Write-Color "Error: Could not find EuVereadorAI-server directory. Make sure you are in the project root." "Red"
    exit 1
}
Push-Location EuVereadorAI-server -ErrorAction SilentlyContinue

npm run build
if ($LASTEXITCODE -ne 0) { Write-Color "Error: Build failed." "Red"; Pop-Location; exit 1 }
Pop-Location

Write-Color "Deploying to server..." "Yellow"

# Copy new files from EuVereadorAI-server/dist
Write-Color "Uploading files..." "DarkCyan"
# Upload dist files
# Note: creating remote directory if it doesn't exist is good practice, but assuming it exists based on user input
scp -i $KeyFile -P $ServerPort -r EuVereadorAI-server/dist/* "$ServerUser@${ServerIP}:$RemotePath"
if ($LASTEXITCODE -ne 0) { Write-Color "Error: Failed to upload dist files." "Red"; exit 1 }

$RemoteRoot = $RemotePath.Replace("/dist/", "/")

# Upload package.json and package-lock.json
Write-Color "Uploading package management files..." "DarkCyan"
scp -i $KeyFile -P $ServerPort "EuVereadorAI-server/package.json" "$ServerUser@${ServerIP}:$RemoteRoot"
scp -i $KeyFile -P $ServerPort "EuVereadorAI-server/package-lock.json" "$ServerUser@${ServerIP}:$RemoteRoot"
if ($LASTEXITCODE -ne 0) { Write-Color "Error: Failed to upload package files." "Red"; exit 1 }

# Upload .env.production to the backend root (one level above dist)
Write-Color "Uploading environment configuration..." "DarkCyan"
scp -i $KeyFile -P $ServerPort "EuVereadorAI-server/.env.production" "$ServerUser@${ServerIP}:$RemoteRoot.env"
if ($LASTEXITCODE -ne 0) { Write-Color "Error: Failed to upload .env.production." "Red"; exit 1 }

# Install dependencies and restart PM2
Write-Color "Updating dependencies and restarting backend application on server..." "DarkCyan"
ssh -i $KeyFile -p $ServerPort "$ServerUser@$ServerIP" "source ~/.nvm/nvm.sh && cd $RemoteRoot && npm install --omit=dev && pm2 restart euvereador-backend"
if ($LASTEXITCODE -ne 0) { Write-Color "Error: Failed to update dependencies or restart application." "Red"; exit 1 }

Write-Color "Backend Deployment complete!" "Green"
