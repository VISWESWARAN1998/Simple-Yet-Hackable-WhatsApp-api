# SWAMI KARUPPASWAMI THUNNAI

# ============================================================
# Simple yet Hackable! WhatsApp API [UNOFFICIAL] for Python3
# Note: The author gives permission to use it under Apache 2.0
# Special Thanks To: alecxe, For reviewing my code!
# ============================================================

import time
import datetime as dt
import json
import os
import requests
import shutil
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlencode
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print("Beautiful Soup Library is reqired to make this library work(For getting participants list for the specified group).\npip3 install beautifulsoup4")

#import pyautogui

#pyautogui.PAUSE = 1


class WhatsApp:
    """
    This class is used to interact with your whatsapp [UNOFFICIAL API]
    """
    emoji = {}  # This dict will contain all emojies needed for chatting
    browser = webdriver.Chrome()  # we are using chrome as our webbrowser
    timeout = 10  # The timeout is set for about ten seconds

    # This constructor will load all the emojies present in the json file and it will initialize the webdriver
    def __init__(self, wait, screenshot=None):
        self.browser.get("https://web.whatsapp.com/")
        # emoji.json is a json file which contains all the emojis
        with open("emoji.json") as emojies:
            self.emoji = json.load(emojies)  # This will load the emojies present in the json file into the dict
        WebDriverWait(self.browser,wait).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '._2zCfw')))
        if screenshot is not None:
            self.browser.save_screenshot(screenshot)  # This will save the screenshot to the specified file location

    # This method is used to send the message to the individual person or a group
    # will return true if the message has been sent, false else
    def send_message(self, name, message):
        message = self.emojify(message)  # this will emojify all the emoji which is present as the text in string
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(name+Keys.ENTER)  # we will send the name to the input key box
        try:
            send_msg = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")))
            messages = message.split("\n")
            for msg in messages:
                send_msg.send_keys(msg)
                send_msg.send_keys(Keys.SHIFT+Keys.ENTER)
            send_msg.send_keys(Keys.ENTER)
            return True
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException:
            return False
        except Exception:
            return False

    # This method will count the no of participants for the group name provided
    def participants_count_for_group(self, group_name):
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(group_name+Keys.ENTER)  # we will send the name to the input key box
        # some say this two try catch below can be grouped into one
        # but I have some version specific issues with chrome [Other element would receive a click]
        # in older versions. So I have handled it spereately since it clicks and throws the exception
        # it is handled safely
        try:
            click_menu = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "._19vo_ > span:nth-child(1)")))
            click_menu.click()
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException as e:
            return "None"
        except Exception as e:
            return "None"
        current_time = dt.datetime.now()
        participants_selector = "div._2LSbZ:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)"
        while True:
            try:
                participants_count = self.browser.find_element_by_css_selector(participants_selector).text
                if "participants" in participants_count:
                    return participants_count
            except Exception as e:
                pass
            new_time = dt.datetime.now()
            elapsed_time = (new_time - current_time).seconds
            if elapsed_time > self.timeout:
                return "NONE"

    # This method is used to get all the participants
    def get_group_participants(self, group_name):
        self.participants_count_for_group(group_name)
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(group_name+Keys.ENTER)  # we will send the name to the input key box
        # some say this two try catch below can be grouped into one
        # but I have some version specific issues with chrome [Other element would receive a click]
        # in older versions. So I have handled it spereately since it clicks and throws the exception
        # it is handled safely
        try:
            click_menu = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#main > header > div._1WBXd > div._2EbF- > div > span")))
            click_menu.click()
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException as e:
            return "None"
        except Exception as e:
            return "None"
        participants = []
        scrollbar = self.browser.find_element_by_css_selector("#app > div > div > div.MZIyP > div._3q4NP._2yeJ5 > span > div > span > div > div")
        for v in range(1, 70):
            print(v)
            self.browser.execute_script('arguments[0].scrollTop = '+str(v*300), scrollbar)
            time.sleep(0.10)
            elements = self.browser.find_elements_by_tag_name("span")
            for element in elements:
                try:
                    html = element.get_attribute('innerHTML')
                    soup = BeautifulSoup(html, "html.parser")
                    for i in soup.find_all("span", class_="_3TEwt"):
                        if i.text not in participants:
                            participants.append(i.text)
                            print(i.text)
                except Exception as e:
                    pass
            elements = self.browser.find_elements_by_tag_name("div")
            for element in elements:
                try:
                    html = element.get_attribute('innerHTML')
                    soup = BeautifulSoup(html, "html.parser")
                    for i in soup.find_all("div", class_="_25Ooe"):
                        j = i.find("span", class_="_1wjpf")
                        if j:
                            j = j.text
                            if "\n" in j:
                                j = j.split("\n")
                                j = j[0]
                                j = j.strip()
                                if j not in participants:
                                    participants.append(j)
                                    print(j)
                except Exception as e:
                    pass
        return participants

    # This method is used to get the main page
    def goto_main(self):
        try:
            self.browser.refresh()
            Alert(self.browser).accept()
        except Exception as e:
            print(e)
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '._2zCfw')))

        

    # get the status message of a person
    # TimeOut is approximately set to 10 seconds
    def get_status(self, name):
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(name+Keys.ENTER)  # we will send the name to the input key box
        try:
            group_xpath = "/html/body/div/div/div/div[3]/header/div[1]/div/span/img"
            click_menu = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.XPATH, group_xpath)))
            click_menu.click()
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException:
            return "None"
        except Exception:
            return "None"
        try:
            status_css_selector = ".drawer-section-body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)"   # This is the css selector for status
            WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, status_css_selector)))
            status = self.browser.find_element_by_css_selector(status_css_selector).text
            # We will try for 100 times to get the status
            for i in range(10):
                if len(status) > 0:
                    return status
                else:
                    time.sleep(1) # we need some delay
            return "None"
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException:
            return "None"
        except Exception:
            return "None"

    # to get the last seen of the person
    def get_last_seen(self, name, timeout=10):
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(name+Keys.ENTER)  # we will send the name to the input key box
        last_seen_css_selector = "._315-i"
        start_time = dt.datetime.now()
        try:
            WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, last_seen_css_selector)))
            while True:
                last_seen = self.browser.find_element_by_css_selector(last_seen_css_selector).text
                if last_seen and "click here" not in last_seen:
                    return last_seen
                end_time = dt.datetime.now()
                elapsed_time = (end_time-start_time).seconds
                if elapsed_time > 10:
                    return "None"
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException:
            return "None"
        except Exception:
            return "None"

    # This method does not care about anything, it sends message to the currently active chat
    # you can use this method to recursively send the messages to the same person
    def send_blind_message(self, message):
        try:
            message = self.emojify(message)
            send_msg = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")))
            messages = message.split("\n")
            for msg in messages:
                send_msg.send_keys(msg)
                send_msg.send_keys(Keys.SHIFT+Keys.ENTER)
            send_msg.send_keys(Keys.ENTER)
            return True
        except NoSuchElementException:
            return "Unable to Locate the element"
        except Exception as e:
            print(e)
            return False

    # This method will send you the picture
    def send_picture(self, name, picture_location, caption=None):
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(name+Keys.ENTER)  # we will send the name to the input key box
        try:
            attach_xpath = '//*[@id="main"]/header/div[3]/div/div[2]/div'
            send_file_xpath = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span'
            attach_type_xpath = '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input'
            # open attach menu
            attach_btn = self.browser.find_element_by_xpath(attach_xpath)
            attach_btn.click()

            # Find attach file btn and send screenshot path to input
            time.sleep(1)
            attach_img_btn = self.browser.find_element_by_xpath(attach_type_xpath)

            # TODO - might need to click on transportation mode if url doesn't work
            attach_img_btn.send_keys(picture_location)           # get current script path + img_path
            time.sleep(1)
            if caption:
                caption_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/span/div/div[2]/div/div[3]/div[1]/div[2]"
                send_caption = self.browser.find_element_by_xpath(caption_xpath)
                send_caption.send_keys(caption)
            send_btn = self.browser.find_element_by_xpath(send_file_xpath)
            send_btn.click()

        except (NoSuchElementException, ElementNotVisibleException) as e:
            print(str(e))

    # For sending documents
    def send_document(self, name, document_location):
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(name+Keys.ENTER)  # we will send the name to the input key box
        try:
            attach_xpath = '//*[@id="main"]/header/div[3]/div/div[2]/div'
            send_file_xpath = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span'
            attach_type_xpath = '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button/input'
            # open attach menu
            attach_btn = self.browser.find_element_by_xpath(attach_xpath)
            attach_btn.click()

            # Find attach file btn and send screenshot path to input
            time.sleep(1)
            attach_img_btn = self.browser.find_element_by_xpath(attach_type_xpath)

            # TODO - might need to click on transportation mode if url doesn't work
            attach_img_btn.send_keys(document_location)           # get current script path + img_path
            time.sleep(1)
            send_btn = self.browser.find_element_by_xpath(send_file_xpath)
            send_btn.click()

        except (NoSuchElementException, ElementNotVisibleException) as e:
            print(str(e))

    

    # Clear the chat
    def clear_chat(self, name):
        self.browser.find_element_by_css_selector("._2zCfw").send_keys(name+Keys.ENTER)
        menu_xpath = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]/div/span"
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
                (By.XPATH, menu_xpath)))
        menu = self.browser.find_element_by_xpath(menu_xpath)
        menu.click()
        chains = ActionChains(self.browser)
        for i in range(4):
            chains.send_keys(Keys.ARROW_DOWN)
        chains.send_keys(Keys.ENTER)
        chains.perform()
        clear_xpath = '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]'
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
                (By.XPATH, clear_xpath)))
        self.browser.find_element_by_xpath(clear_xpath).click()
        


    # override the timeout
    def override_timeout(self, new_timeout):
        self.timeout = new_timeout

    # This method is used to emojify all the text emoji's present in the message
    def emojify(self,message):
        for emoji in self.emoji:
            message = message.replace(emoji,self.emoji[emoji])
        return message

    def get_profile_pic(self, name):
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(name+Keys.ENTER)
        try:
            open_profile = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div[3]/div/header/div[1]/div/img")))
            open_profile.click()
        except:
            print("nothing found")
        try:
            open_pic =  WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div[1]/div[3]/span/div/span/div/div/div/div[1]/div[1]/div/img")))
            open_pic.click()
        except:
            print("Nothing found")
        try:
            img = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                    (By.XPATH,'//*[@id="app"]/div/span[2]/div/div/div[2]/div/div/div/div/img')))
        except:
            print("Couldn't find the URL to the image")
        img_src_url = img.get_attribute('src')
        self.browser.get(img_src_url)
        self.browser.save_screenshot(name+"_img.png")

    def create_group(self, group_name, members):
        more = self.browser.find_element_by_css_selector("#side > header > div._20NlL > div > span > div:nth-child(3) > div > span")
        more.click()
        chains = ActionChains(self.browser)
        chains.send_keys(Keys.ARROW_DOWN+Keys.ENTER)
        chains.perform()
        for member in members:
            contact_name = self.browser.find_element_by_css_selector("._16RnB")
            contact_name.send_keys(member+Keys.ENTER)
        time.sleep(3) # little delay to make the process robust
        next_step = self.browser.find_element_by_css_selector("._3hV1n > span:nth-child(1)")
        next_step.click()
        group_text = self.browser.find_element_by_css_selector(".bsmJe > div:nth-child(2)")
        group_text.send_keys(group_name+Keys.ENTER)

    def join_group(self, invite_link):
        self.browser.get(invite_link)
        try:
            Alert(self.browser).accept()
        except:
            print("No alert Found")
        join_chat = self.browser.find_element_by_css_selector("#action-button")
        join_chat.click()
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/span[3]/div/div/div/div/div/div/div[2]/div[2]')))
        join_group = self.browser.find_element_by_xpath('//*[@id="app"]/div/span[3]/div/div/div/div/div/div/div[2]/div[2]')
        join_group.click()

    # This method is used to get an invite link for a particular group
    def get_invite_link_for_group(self, groupname):
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(groupname+Keys.ENTER)
        self.browser.find_element_by_css_selector("#main > header > div._5SiUq > div._16vzP > div > span").click()
        try:
            #time.sleep(3)
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#app > div > div > div.MZIyP > div._3q4NP._2yeJ5 > span > div > span > div > div > div > div:nth-child(5) > div:nth-child(3) > div._3j7s9 > div > div")))
            invite_link = self.browser.find_element_by_css_selector("#app > div > div > div.MZIyP > div._3q4NP._2yeJ5 > span > div > span > div > div > div > div:nth-child(5) > div:nth-child(3) > div._3j7s9 > div > div")
            invite_link.click()
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(
                    (By.ID, "group-invite-link-anchor")))
            link = self.browser.find_element_by_id("group-invite-link-anchor")
            return link.text
        except:
            print("Cannot get the link")

    # This method is used to exit a group
    def exit_group(self, group_name):
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(group_name+Keys.ENTER)
        self.browser.find_element_by_css_selector("._2zCDG > span:nth-child(1)").click()
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._1CRb5:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)")))
        time.sleep(3)
        _exit = self.browser.find_element_by_css_selector("div._1CRb5:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)")
        _exit.click()
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._1WZqU:nth-child(2)")))
        confirm_exit = self.browser.find_element_by_css_selector("div._1WZqU:nth-child(2)")
        confirm_exit.click()
        
    # Send Anonymous message
    def send_anon_message(self, phone, text):
        payload = urlencode({"phone": phone, "text": text, "source": "", "data": ""})
        self.browser.get("https://api.whatsapp.com/send?"+payload)
        try:
            Alert(self.browser).accept()
        except:
            print("No alert Found")
        WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#action-button")))
        send_message = self.browser.find_element_by_css_selector("#action-button")
        send_message.click()
        confirm = WebDriverWait(self.browser, self.timeout+5).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")))
        confirm.clear()
        confirm.send_keys(text+Keys.ENTER)

    # Check if the message is present in an user chat
    def is_message_present(self, username, message):
        search = self.browser.find_element_by_css_selector("._2zCfw")
        search.send_keys(username+Keys.ENTER)
        search_bar = WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._1i0-u > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")))
        search_bar.click()
        message_search = self.browser.find_element_by_css_selector("._1iopp > div:nth-child(1) > label:nth-child(4) > input:nth-child(1)")
        message_search.clear()
        message_search.send_keys(message+Keys.ENTER)
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/span/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div[1]/span/span/span")))
            return True
        except TimeoutException:
            return False

    # Get all starred messages
    def get_starred_messages(self, delay=10):
        starred_messages = []
        self.browser.find_element_by_css_selector("div.rAUz7:nth-child(3) > div:nth-child(1) > span:nth-child(1)").click()
        chains = ActionChains(self.browser)
        time.sleep(2)
        for i in range(4):
            chains.send_keys(Keys.ARROW_DOWN)
        chains.send_keys(Keys.ENTER)
        chains.perform()
        time.sleep(delay)
        messages = self.browser.find_elements_by_class_name("MS-DH")
        for message in messages:
            try:
                message_html = message.get_attribute("innerHTML")
                soup = BeautifulSoup(message_html, "html.parser")
                _from = soup.find("span", class_="_1qUQi")["title"]
                to = soup.find("div", class_="copyable-text")["data-pre-plain-text"]
                message_text = soup.find("span", class_="selectable-text invisible-space copyable-text").text
                message.click()
                selector = self.browser.find_element_by_css_selector("#main > header > div._5SiUq > div._16vzP > div > span")
                title = selector.text
                selector.click()
                time.sleep(2)
                WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._14oqx:nth-child(3) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)")))
                phone = self.browser.find_element_by_css_selector("div._14oqx:nth-child(3) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)").text
                if title in _from:
                    _from = _from.replace(title, phone)
                else:
                    to = to.replace(title, phone)
                starred_messages.append([_from, to, message_text])
            except Exception as e:
                print("Handled: ", e)
        return starred_messages
            

    # This method is used to quit the browser
    def quit(self):
        self.browser.quit()
