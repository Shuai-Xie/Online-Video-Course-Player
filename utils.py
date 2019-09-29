from PIL import Image, ImageEnhance
import locale
import numpy as np
import time

locale.setlocale(locale.LC_ALL, 'C')
import tesserocr  # 识别图片验证码


def preprocess_yzm_img(screen_img, roi):
    # 1.切出验证码
    img_yzm = screen_img.crop(roi)
    img_yzm.save('./imgs/yzm.png')  # RGBA格式不能直接用，先保存本地
    img_yzm = Image.open('./imgs/yzm.png')
    # 2.图像加强：二值化，对比度
    img_yzm = img_yzm.convert('L')
    img_yzm = ImageEnhance.Contrast(img_yzm).enhance(3)  # 对比度增强
    img_yzm.save('./imgs/yzm.png')
    # 3.np array, real 二值
    img = np.asarray(img_yzm)
    new_img = np.ones(img.shape, dtype=np.uint8) * 255
    new_img[np.where(img < 60)] = 0
    img_yzm = Image.fromarray(new_img)
    img_yzm.save('./imgs/yzm.png')

    return Image.open('./imgs/yzm.png')


def parse_yzm(yzm):
    """
    从 ocr 识别结果中，解析出 4 个数字作为验证码
    """
    res = ''
    for c in yzm:
        if c.isnumeric():
            res += c
        if len(res) == 4:  # 4位验证码
            break
    return res


def ocr_yzm(screen_img, roi=(550, 860, 700, 900)):
    """
    :param screen_img: screenshot of (400,800) window
    :param roi: default roi is fit for (400,800) window
    :return: parse yzm result
    """
    yzm_img = preprocess_yzm_img(screen_img, roi)  # 切出验证码
    yzm = tesserocr.image_to_text(yzm_img)
    yzm = parse_yzm(yzm)
    return yzm


def play_video(browser):
    """
    点击播放按钮，播放视频
    """
    while True:
        videos = browser.find_elements_by_tag_name('video')
        if len(videos) > 0:  # =1
            print('找到 video!')
            break
        else:
            time.sleep(3)  # 等待视频加载
            print('等待视频加载')

    # 找到播放 div, 点击
    player = browser.find_element_by_xpath("//div[@data-title='点击播放']")  # 相对路径
    player.click()
    print('开始播放!')
