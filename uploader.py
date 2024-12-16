from picbed.cos import cos_upload_img


class Uploader:
    def __init__(self):
        pass

    def upload_web_img(self, img_url, pic_bed):
        if pic_bed == 'COS':
            return cos_upload_img(img_url)
        else:
            print('Unsupported image hosting type')
            exit(1)
