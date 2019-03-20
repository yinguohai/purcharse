from core.browser import Browser
from controller.dingding import Dingding
from selenium.common.exceptions import TimeoutException
from helpers.helpers import *
import time

class Purchase(Browser,Dingding):

    def __init__(self):
        self.url = PATH_INFO.get('purchase')
        self.robot_url = ROBOT.get('ROBOT_URL')
        self.robot_content_prefix = '{0}?c={1}&t={2}&f='.format(ROBOT.get('ROBOT_COMMON_URL'),'purcharse',CURRENT_DATE)
        self.set_load_timeout(30)

    def export(self):
        while True:
            self.select_all()
            self.set_export_filed()
            self.get_export_file()
            set_timer()
            if not self.set_next_page():
                set_timer(True)
                break
        return self


    def index(self):
        self.click_element('//*[@id="first-contents"]/li[4]')
        try:
            self.click_element('//*[@id="M0010700"]/li[4]')
            self.goto_target_url(self.url)
        except TimeoutException:
            self.set_stop_load_page()

        self.swith_iFrame('//*[@id="iframeContent"]')
        self.set_init_page()
        return self

    #
    def set_init_page(self):
        '''
        设置每页显示的条数
        :return:
        '''
        self.click_element('//*[@id="pagediv"]/div/div[1]/button')
        time.sleep(5)
        #每页10条
        # self.click_element('//*[@id="pagemenupagediv"]/li[2]')

        #每页500条
        self.click_element('//*[@id="pagemenupagediv"]/li[7]')
        time.sleep(5)
        #设置下载到第几页了,如果是第一页，就忽略不设置
        if not self.is_disabled('//*[@id="inputgopagepagediv"]'):
            self.set_element_value(
                self.get_element('//*[@id="inputgopagepagediv"]'),
                get_next_timer()
            )
            self.click_element('//*[@id="btngopagepagediv"]')


    def set_next_page(self):
        not_next = self.is_disabled('//*[@id="nextpagepagediv"]')
        print('not_next==>',not_next)
        if not_next:
            return False
        else:
            self.click_element('//*[@id="nextpagepagediv"]')
            return True


    def select_all(self):
        '''
        选择所有记录
        :return:
        '''
        button_xpath = '//*[@id="three-selectAll"]'
        #如果是选中状态则单击两次，确保所有元素都选中了
        if self.is_selected(button_xpath):
            self.click_element(button_xpath)
            self.click_element(button_xpath)
        else:
            self.click_element(button_xpath)


    def set_export_filed(self):

        self.click_element('//*[@id="batchOperation"]/button')
        self.click_element('//*[@id="batchExportPurchase"]')
        is_checked = self.get_element_attr('//*[@id="exportPurchase"]/div/form/div[2]/div/div[1]/label[2]/input','checked')
        if is_checked == 'true':
            self.click_element('//*[@id="exportPurchase"]/div/form/div[2]/div/div[1]/label[2]/input')
            for i in PURCHASE.keys():
                self.click_element('//*[@id="exportPurchase"]/div/form/div[2]/div/div[2]/label[{}]'.format(str(i)))

    def get_export_file(self):
        self.click_element('//*[@id="exportPurchase"]/div/form/div[3]/button[1]')
        self.click_element('//*[@id="exportPurchase"]/div/form/div[3]/button[2]')

    def send_message(self):
        Dingding.send_max_dingding(
            get_download_files(),
            self.robot_url,
            self.robot_content_prefix
        )