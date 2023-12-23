#!/bin/bash

# python 기준 pyinstaller 경로
PYTHON_PATH=$(command -v python)

# 소스 코드 디렉토리와 메인 파일 설정
SOURCE_DIR="src"
MAIN_FILE="main.py"

# 출력 디렉토리 설정 (원하는 곳으로 변경)
OUTPUT_DIR="dist"

# 실행 파일 이름 설정 (원하는 이름으로 변경)
EXECUTABLE_NAME="EasyGit"

# FIXME:: 이거 맞는지 모르겠다
$PYTHON_PATH -m pyinstaller --onefile --distpath $OUTPUT_DIR --name $EXECUTABLE_NAME $SOURCE_DIR/$MAIN_FILE
