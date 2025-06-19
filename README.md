# CosyVoice-ttsfrd

This package is a wrapper for the `ttsfrd` library used in CosyVoice. It simplifies installation by bundling the required wheels and resources.

## !! Important

- **Platform**: This package will only work on **64-bit Linux with Python 3.10**.
- **License**: This package redistributes software under the [Apache 2.0 License], which is the original license used in CosyVoice.
- **Purpose**: This is a convenience wrapper. All credit goes to the original authors of CosyVoice and the `ttsfrd` library.

## Installation

```bash
# Step 1: Install this wrapper package
pip install -i https://pypi.org/simple/ cosyvoice-ttsfrd
# Step 2: After the wrapper is installed, you must run the following command in your terminal. This will install the actual `ttsfrd` libraries and unzip the required resources.
cosyvoice-post-install
```

The installation process will automatically install the bundled `ttsfrd` wheels and unzip the required resources into the package directory. Installation log looks like:

```bash
▶ cosyvoice-post-install
CosyVoice-ttsfrd initialized. Resources are expected in: /mnt/user-ssd/songxingchen/.conda/envs/touchnet/lib/python3.10/site-packages/cosyvoice_ttsfrd/resource
--- Running Post-Installation Setup for CosyVoice-TTSFRD ---
Downloading resources from GitHub releases...
Downloading https://github.com/xingchensong/CosyVoice-ttsfrd/releases/download/v0.4.3/resource.zip...
Download progress: 100%
Verifying file integrity...
File integrity verified.
Unzipping resources to /mnt/user-ssd/songxingchen/.conda/envs/touchnet/lib/python3.10/site-packages/cosyvoice_ttsfrd...
Resources unzipped. Package contents:
- __init__.py
- __pycache__
- bundled_files
- post_install.py
- resource
Installing ttsfrd_dependency-0.1-py3-none-any.whl from bundled file...
Looking in indexes: https://mirrors.aliyun.com/pypi/simple/
Processing /mnt/user-ssd/songxingchen/.conda/envs/touchnet/lib/python3.10/site-packages/cosyvoice_ttsfrd/bundled_files/ttsfrd_dependency-0.1-py3-none-any.whl
Installing collected packages: ttsfrd-dependency
Successfully installed ttsfrd-dependency-0.1
Installing ttsfrd-0.4.2-cp310-cp310-linux_x86_64.whl from bundled file...
Looking in indexes: https://mirrors.aliyun.com/pypi/simple/
Processing /mnt/user-ssd/songxingchen/.conda/envs/touchnet/lib/python3.10/site-packages/cosyvoice_ttsfrd/bundled_files/ttsfrd-0.4.2-cp310-cp310-linux_x86_64.whl
Installing collected packages: ttsfrd
Successfully installed ttsfrd-0.4.2
--- ✅ Post-Installation Finished Successfully! ---
You can now use the 'ttsfrd' module in your Python scripts.
```

## Usage

After installation, you can import and use `ttsfrd` as you normally would. If you need to access the unzipped resources programmatically, you can do so like this:

```py
import json
import ttsfrd
from cosyvoice_ttsfrd import get_resource_path

resource_dir = get_resource_path()
print(f"Resources are located at: {resource_dir}")

frd = ttsfrd.TtsFrontendEngine()
frd.initialize(resource_dir)
frd.set_lang_type('pinyinvg')

text = "嘿，你是不是在纠结，家里到底是该买个55~60的投影仪呢，还是整个大屏幕电视啊？这俩玩意儿确实各有各的好，选哪个主要就看你的钱袋子、平时都用它干啥、对画质要求高不高，还有家里地方够不够大。"
texts = [i["text"] for i in json.loads(frd.do_voicegen_frd(text))["sentences"]]
text = ''.join(texts)
print(text)
```
