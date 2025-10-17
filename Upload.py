import subprocess
import datetime
import os
import sys

print(" ")
print(" ")
print(" ")
print("Đang thực hiện code...")

# Thư mục chứa 2 file code Unity
# Windows: r"D:\FPT Polytechnic\NhapMonLTGA\Unity Projects"
# macOS: "/Users/khangng/Downloads/Hoc FPT/Unity project/Link-Unity-Projects"
project_path = r"D:\FPT Polytechnic\NhapMonLTGA\Unity Projects" if sys.platform.startswith("win") else "/Users/khangng/Downloads/Hoc FPT/Unity project/Link-Unity-Projects"
os.chdir(project_path)

# Khởi động SSH agent (chỉ cần trên Mac/Linux, Windows thì bỏ dòng này)
if not sys.platform.startswith("win"):
    subprocess.run("eval $(ssh-agent -s)", shell=True)
    subprocess.run("ssh-add ~/.ssh/id_ed25519", shell=True)

# Git add tất cả file (bỏ qua file trong .gitignore)
subprocess.run(["git", "add", "."])

# Commit với timestamp
subprocess.run(["git", "commit", "-m", f"Auto commit {datetime.datetime.now()}"])

# Pull trước để tránh xung đột
subprocess.run(["git", "pull", "--rebase"])

# Push lên repository
subprocess.run(["git", "push"])

print("Upload complete!")

input("Nhấn Enter để thoát...")