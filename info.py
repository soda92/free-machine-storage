import os


def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


START = os.environ.get("Programfiles")
arr = []

for folder in os.listdir(START):
    size = get_size(os.path.join(START, folder))
    size_mb = size/1024/1024
    if size_mb < 100:
        continue
    arr.append([folder, f"{size_mb:.2f}"])

arr = sorted(arr, key=lambda x: float(x[1]), reverse=True)

for i in arr:
    folder, size = i
    print(folder, size+" MB")
