$Source = "D:\17Obsidian\20260306\大二下学期\02 CS61A"
$Destination = "D:\01班级文件与作业\07_CS61A\Notes"

if (!(Test-Path $Destination)) {
    New-Item -ItemType Directory -Path $Destination
}

robocopy $Source $Destination /MIR /R:0 /W:0 /MT:32

Write-Host "✅ 同步完成！现在可以执行 git add 了。" -ForegroundColor Green