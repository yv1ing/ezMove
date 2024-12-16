from uploader import Uploader
import os
import re

uploader = Uploader()


# find all markdown files in specified directory
def find_files(directory):
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))

    return markdown_files


# replace pic_bed for single markdown file
def replace_pic_bed(markdown_file, new_pic_bed):
    img_pattern = re.compile(r'!\[.*\]\((.*)\)')
    url_pattern = re.compile(r'\((.*)\)')

    old_file = open(markdown_file, 'r', encoding='utf-8')
    old_lines = old_file.readlines()
    old_file.close()

    new_file = open(markdown_file, 'w', encoding='utf-8')
    for line in old_lines:
        img_match = img_pattern.search(line)
        if img_match:
            url_match = url_pattern.search(line)
            if url_match:
                old_url = url_match.group(1)
                new_url = uploader.upload_web_img(old_url, new_pic_bed)

                if new_url != '':
                    line = re.sub(img_pattern, lambda match: f'![]({new_url})', line)
                    print(f'-replaced {old_url} to {new_url}')
                else:
                    print(f'-upload failed {old_url}')

        new_file.write(line)

    new_file.close()
    print(f'!finished {markdown_file}\n')
