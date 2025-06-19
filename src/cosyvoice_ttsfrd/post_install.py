import sys
import subprocess
import pathlib
import zipfile
import urllib.request
import hashlib


def download_with_progress(url, dest_path, expected_sha256=None):
    print(f"Downloading {url}...")

    def progress_hook(block_num, block_size, total_size):
        if total_size > 0:
            percent = min(100, (block_num * block_size * 100) // total_size)
            print(f"\rDownload progress: {percent}%", end="", flush=True)

    urllib.request.urlretrieve(url, dest_path, progress_hook)
    print()

    if expected_sha256:
        print("Verifying file integrity...")
        with open(dest_path, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        if file_hash != expected_sha256:
            raise ValueError(f"File integrity check failed. Expected: {expected_sha256}, Got: {file_hash}")
        print("File integrity verified.")


def main():
    """
    This function will be called when the user runs the `cosyvoice-post-install` command.
    """
    try:
        # Find the directory where this file is located, to locate the entire package
        wrapper_package_dir = pathlib.Path(__file__).parent
        bundled_files_dir = wrapper_package_dir / "bundled_files"
        resource_dir = wrapper_package_dir / "resource"

        print("--- Running Post-Installation Setup for CosyVoice-TTSFRD ---")

        # 1. Download and unzip resource.zip from GitHub releases
        resource_zip_path = wrapper_package_dir / "resource.zip"

        if not resource_dir.exists() or not any(resource_dir.iterdir()):
            print("Downloading resources from GitHub releases...")

            # GitHub release URL
            resource_url = "https://github.com/xingchensong/CosyVoice-ttsfrd/releases/download/v0.4.3/resource.zip"
            expected_sha256 = "dcb3970fd4f52d036f245493360d97d0da1014f917deb4b9d83a3ded97483113"

            try:
                download_with_progress(resource_url, resource_zip_path, expected_sha256)

                print(f"Unzipping resources to {wrapper_package_dir}...")
                with zipfile.ZipFile(resource_zip_path, 'r') as zip_ref:
                    zip_ref.extractall(wrapper_package_dir)

                resource_zip_path.unlink()

                print("Resources downloaded and extracted successfully.")
            except Exception as e:
                print(f"Failed to download resources: {e}")
                print("Please check your internet connection and try again.")
                sys.exit(1)
        else:
            print("Resources already exist, skipping download.")

        # 2. Install the dependency and main program whl files
        pip_command = [sys.executable, "-m", "pip"]

        whl_files = [
            "ttsfrd_dependency-0.1-py3-none-any.whl",
            "ttsfrd-0.4.2-cp310-cp310-linux_x86_64.whl"
        ]

        for whl in whl_files:
            whl_path = bundled_files_dir / whl
            if whl_path.exists():
                print(f"Installing {whl} from bundled file...")
                subprocess.check_call(pip_command + ["install", str(whl_path)])
            else:
                print(f"ERROR: Could not find {whl_path}")
                sys.exit(1)

        print("\n--- ✅ Post-Installation Finished Successfully! ---")
        print("You can now use the 'ttsfrd' module in your Python scripts.")

    except Exception as e:
        print("\n--- ❌ An error occurred during post-installation ---")
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
