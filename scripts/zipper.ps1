$curr_folder = Split-Path -Path $pwd -Leaf
$today = Get-Date -Format "dd.MM.yyyy"

$archive_name = (-join($curr_folder,"_",$today))
$archive_name = (-join($archive_name,"",".zip"))

Set-Location ..
Write-Host Zip Archive $archive_name  -ForegroundColor Yellow


Compress-Archive -Path $curr_folder -DestinationPath $archive_name
Set-Location tg_reposter_iphones