# ezMove

This is a script for batch migration of Markdown images to image hosting.

## Quick Start

### Step 0

Install required dependencies.

```shell
pip install -r .\requirements.txt
```

### Step 1

Fill in the configuration information of the image hosting in the `.env` file.

For example (use Tencent COS):

```env
NEW_PIC_BED="COS"

COS_SECRET_ID=""
COS_SECRET_KEY=""
COS_BUCKET=""
COS_REGION=""
COS_SAVE_PATH=""
```

### Step 2

Fill in the Markdown file directory of the image hosting service to be migrated in `main.py`

For example:

```python
# Fill in the directory of Markdown files waiting to be migrated here
markdown_files = find_files('./my_blogs')
```

### Step 3

Run `main.py` and have a cup of coffee while waiting for the program to finish running.

```shell
python3 main.py
```


## Todo

- [x] Support Tencent Cloud COS 
- [ ] Support Alibaba Cloud OSS
- [ ] Support Qiniu Cloud Image Hosting
- [ ] ...


