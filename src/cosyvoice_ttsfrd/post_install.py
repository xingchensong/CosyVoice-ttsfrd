import sys
import subprocess
import pathlib
import zipfile
import os


def main():
    """
    This function will be called when the user runs the `cosyvoice-post-install` command.
    """
    try:
        # Find the directory where this file is located, to locate the entire package
        wrapper_package_dir = pathlib.Path(__file__).parent
        bundled_files_dir = wrapper_package_dir / "bundled_files"

        print("--- Running Post-Installation Setup for CosyVoice-TTSFRD ---")

        # 1. Unzip resource.zip
        resource_zip_path = bundled_files_dir / "resource.zip"
        unzip_target_dir = wrapper_package_dir

        if resource_zip_path.exists():
            print(f"Unzipping resources to {unzip_target_dir}...")
            with zipfile.ZipFile(resource_zip_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_target_dir)

            print("Resources unzipped. Package contents:")
            for item in os.listdir(unzip_target_dir):
                print(f"- {item}")
        else:
            print(f"ERROR: Could not find {resource_zip_path}")
            sys.exit(1)

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
