@echo off
set "folder=..\Leetcode\java"
set "output=SolvedViaJava.md"

if exist "%output%" del "%output%"

for /r "%folder%" %%f in (*) do (
  echo %%~nxf|findstr /c:".java"> nul 2>nul &&  echo %%~nxf|findstr /c:"@"> nul 2>nul && echo solve via java && echo %%~nxf && echo %%~nxf >> "%output%"
)

echo "commit -m %1"
git add .
git commit -m %1
git push