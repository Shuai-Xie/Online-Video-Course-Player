from selenium import webdriver
from PIL import Image
import time
from utils import ocr_yzm, play_video

chromePath = r'./chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
browser = webdriver.Chrome(executable_path=chromePath, chrome_options=options)

if __name__ == '__main__':
    # 打开网页
    loginUrl = r'http://hnpi.newzhihui.cn/'
    browser.get(loginUrl)
    browser.set_window_size(400, 800)  # 防止广告遮挡验证码

    # 用户名/密码
    username, password = '412927197310241424', '000000'  # 更改为自己的用户名/密码
    # username, password = 'xxxxxx', 'xxxxxx'  # 更改为自己的用户名/密码
    browser.find_element_by_id('username').send_keys(username)
    browser.find_element_by_id('pwd').send_keys(password)

    # 动态验证码
    # 截取网页先保存到本地，再用 tesserocr 识别
    while True:
        browser.get_screenshot_as_file('./imgs/screen.png')
        screen_img = Image.open('./imgs/screen.png')
        yzm = ocr_yzm(screen_img)
        if len(yzm) == 4:  # 如果识别出4位数字，正确几率很大，输入验证码验证
            browser.find_element_by_id('yzm').clear()
            browser.find_element_by_id('yzm').send_keys(yzm)
        else:  # 如果不是，促使验证码刷新，直到 tesserocr 能识别出
            browser.find_element_by_id('yzm').clear()
            browser.find_element_by_id('yzm').send_keys('1234')

        # 登录
        browser.find_element_by_class_name('login_button').click()
        time.sleep(1)
        try:
            print('重新登录...')
            browser.switch_to.alert.accept()
        except:
            print('登录成功!')
            break

    # recover to original window
    browser.maximize_window()
    # 订单页面，显示课程，点击去学习，进入视频课程页面
    curWin = browser.current_window_handle
    # 去学习
    browser.find_element_by_xpath("//a[contains(text(),'去学习')]").click()

    handles = browser.window_handles
    for i in handles:  # i is str
        if curWin == i:
            continue
        else:
            browser.switch_to.window(i)

            course_list = browser.find_elements_by_xpath("//div[@class='course-list']/ul/ul/li")
            print('total videos:', len(course_list))

            for idx, course in enumerate(course_list):
                video_id = course.get_attribute('id')
                video_info = course.find_element_by_class_name('video-info')  # click to play
                # 包括了: 2-1 焦裕禄精神1 100% 所有信息; 把其中的 span 标签值都涵盖了
                video_text = video_info.text.strip()
                video_title = video_text[:video_text.index('\n')]
                video_progress = video_text[video_text.index('\n') + 1:]
                print('{}, id: {}, title: {}, progress:{}'.format(idx + 1, video_id, video_title, video_progress))
                if video_progress != '100%':
                    video_info.click()  # 进入当前视频页面
                    time.sleep(1)  # 等待页面刷新完成
                    play_video(browser)  # 点击播放按钮
                    cnt = 0
                    while True:
                        time.sleep(60 * 1)  # 1min
                        cnt += 1
                        video_progress = video_info.text.strip()[video_text.index('\n') + 1:]
                        # if cnt % 5 == 0:  # 每 5min 记录一次进度
                        print('play {} min, progress: {}'.format(cnt, video_progress))
                        if video_progress == '100%':
                            break
