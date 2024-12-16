from dotenv import load_dotenv
from markdown import *

load_dotenv()
new_pic_bed = os.getenv('NEW_PIC_BED')

if __name__ == '__main__':
    # Fill in the directory of Markdown files waiting to be migrated here
    markdown_files = find_files('')

    for markdown_file in markdown_files:
        replace_pic_bed(markdown_file, new_pic_bed)
