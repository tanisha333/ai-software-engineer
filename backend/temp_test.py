from services.project_analyzer import get_project_structure
from services.project_analyzer import group_by_folder

files = get_project_structure(".")

print("PROJECT FILES")
print("=" * 50)

for file in files:
    print(file)

print("\n")

folders = group_by_folder(files)

print("GROUPED BY FOLDER")
print("=" * 50)

for folder, items in folders.items():
    print(f"\n📁 {folder}")

    for item in items:
        print(f"   {item}")