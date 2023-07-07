import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from contextlib import contextmanager
from multiprocessing import Pool
import asyncio
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep
import warnings
from selenium.webdriver.chrome.options import Options

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning) 
from django.http import HttpResponse
import json
import re
import requests
from bs4 import BeautifulSoup
import time
import time
import random
from datetime import datetime, timedelta
import httpx
from lxml import html
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.core.cache import cache
# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer,HistorySerializer
from django.core import serializers
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from django.contrib.auth.models import User
from rest_framework import status
import pickle
import nltk
from nltk.corpus import stopwords
import re
import os
from selectorlib import Extractor
import requests 
import json 
from time import sleep
import gc
from sklearn.feature_extraction.text import CountVectorizer
from .models import History
nltk.download('stopwords')
# Create your views here.
from django.http import JsonResponse
from .models import History
import requests
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random

# e = Extractor.from_yaml_file('search_results.yml')

# def scrape(url):  

#     headers = {
#         'dnt': '1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-user': '?1',
#         'sec-fetch-dest': 'document',
#         'referer': 'https://www.amazon.com/',
#         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     }

#     # Download the page using requests
#     print("Downloading %s"%url)
#     r = requests.get(url, headers=headers)
#     # Simple check to check if page was blocked (Usually 503)
#     if r.status_code > 500:
#         if "To discuss automated access to Amazon data please contact" in r.text:
#             print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
#         else:
#             print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
#         return None
#     # Pass the HTML of the page and create 
#     return e.extract(r.text)

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP
# django ka hisaab hi alg hy thora khapna pary ga ab 
# def send_otp(request):
#      email=request.data['email']
#      print(email)
#      o=generateOTP()
#      htmlgen = '<p>Your OTP is <strong>o</strong></p>'
#      send_mail('OTP request',o,'<your gmail id>',[email], fail_silently=False, html_message=htmlgen)
#      return HttpResponse(o)

# def send_email_api(request):
#     subject = 'Test Email'
#     message = 'This is a test email sent using Django!'
#     from_email = 'fareeha.ashraf01@gmail.com'  # Sender's email address
#     recipient_list = ['rmustafa.hafeez@gmail.com']  # Recipient's email address(es)

#     try:
#         send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#         response = {'message': 'Email sent successfully'}
#         print ("email send ")
#         return JsonResponse(response, status=200)
#     except Exception as e:
#         print("there is something" ,e)
#         response = {'message': 'Failed to send email'}
#         return JsonResponse(response, status=500)
def send_email_api(request):
    subject = 'OTP Verification'
    recipient_email = 'rmustafa.hafeez@gmail.com'  # Recipient's email address

    otp = generateOTP()
    message = f'Your OTP is: {otp}'

    try:
        send_mail(subject, message, 'fareeha.ashraf01@gmail.com', [recipient_email], fail_silently=False)
        response = {'message': 'Email sent successfully'}
        print('Email sent')
        return JsonResponse(response, status=200)
    except Exception as e:
        print('Failed to send email:', e)
        response = {'message': 'Failed to send email'}
        return JsonResponse(response, status=500)
#run karo code pora???project?han ? backend toh chala lo front b bnd hy 

@api_view(['POST'])
def createUser(request):
    try:
        username = request.data['username']
        password = request.data['password']
        fullname = request.data['fullname']
        email = request.data['email']
    except KeyError:
        return Response({"message":"Invalid Data","status":400}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({"message":"Email Already Exist","status":400}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({"message":"Username is taken","status":400}, status=status.HTTP_400_BAD_REQUEST)

    if not all([username, password, fullname, email]):
        return Response({"message": "Missing Fields","status":400}, status=status.HTTP_400_BAD_REQUEST)

    if not is_valid_password(password):
        return Response({"message": "Password must be 8 characters including special character ","status":400}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.create_user(username=username, password=password, email=email, first_name=fullname)
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    except:
        return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def is_valid_password(password):
    if len(password) != 8:
        return False
    if not re.search("[!@#$%^&*()_+=-]", password):
        return False
    return True



@api_view(['GET'])
def getProfile(request, id):
    try:
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"message": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def getHistory(request,id):
    try:
        history = History.objects.filter(userid=id)
        print(history)
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"message": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def update_profile(request):
    try:
        userid=request.data['id']
        username =request.data['username']
        email =request.data['email']
        first_name =request.data['first_name']
        user= User.objects.get(id=userid)
        user.username=username
        user.email=email
        user.first_name=first_name
        user.save()
        print ("sending mail")
        send_email_api(request)
        serializer=UserSerializer(user,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': "Internal Server Error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def getProduct(request):
    try:
        p = request.data.get("username")
        userid = request.data.get("user_id")
        user = User.objects.get(id=userid)
        history = History(userid=user, keyword=p)
        history.save()
        print(userid)

        split_p = p.replace(" ", "+")
        url = f'https://www.amazon.com/s?k={split_p}'

        data = scrape_product(url)
        serialized_data = json.dumps(data)
        return JsonResponse(serialized_data, safe=False)
    except User.DoesNotExist:
        return HttpResponse("User does not exist", status=400)
    except Exception as e:
        print(f"An error occurred: {e}")
        return HttpResponse("Internal Server Error", status=500)




@api_view(['GET'])
def getProductByCategory(request):
    try:
        print("-----Here----")
        keyword = request.query_params.get('q')
        user_id = request.query_params.get('user')
        print("User id ", user_id)
        user = User.objects.get(id=user_id)
        history = History(userid=user, keyword=keyword)
        history.save()
        split_p = keyword.replace(" ", "+")
        url = f'https://www.amazon.com/s?k={split_p}'
        print("this is url : ", url)
        data = scrape_product(url)
        print("this is data ", data)
        serialized_data = json.dumps(data)
        return HttpResponse(serialized_data, content_type='application/json')
    except Exception as e:
        print(e)
        return JsonResponse({"error": str(e)},safe=False)



@api_view(['POST'])
def get_reviews(request):
     try:
        p=request.data.get("product_url")
        p = p.split("/")
        p=p[3:]
        p = '/'.join(p)
        build_url = "https://www.amazon.com/"+p
        print ("URl BUILD ",build_url)
        print ("Scraping reviews ........")
        # data = scrape_reviews(build_url,15)
        with open('reviews.json') as file:
            data = json.load(file)
        print("these are the reviews ",data)
        if (data == None):
                print ("NO reviews are found ")
                return Response({'message': "Internal Server Error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else: 
            all_reviews = [obj['content'] for obj in data]
            all_reviewcleaned = beforetesting_prediction (all_reviews)
            
           # print("these are the reviews ",all_reviewcleaned)
           
       
            prediction_list=testing_prediction(all_reviewcleaned)
            print (prediction_list)
            extract = []
            for i, prediction in enumerate(prediction_list):
                if prediction == 1:
                    extract.extend(extract_positive([all_reviewcleaned[i]]))  
                else:
                    extract.extend(extract_negative([all_reviewcleaned[i]]))
                    
           
            print ("\n")
            print(extract)
            print ("\n")
            print ("-"*40)
           
         
            for i, obj in enumerate(data):
                obj['cleaned_data'] =extract[i]
                obj['prediction'] = prediction_list[i]
            return Response(data,status=status.HTTP_200_OK)
     except Exception as e:
         print("EXception:  ",e)
         return Response({'message': "Internal Server Error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@contextmanager
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep
import warnings
from selenium.webdriver.chrome.options import Options

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning) 

chrome_options = Options()
# chrome_options.add_argument("--headless")


def scrape_reviews(url,pages):
    
    driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        try:
            driver.get(url)
            sleep(1)
        except:
            pass

        data=[]
        
        for page in range(pages):
            
            revs=driver.find_elements("xpath",'//div[contains(@id,"customer_review")]')
            
            for rev in revs:
                
                objects={}

                content=''
                author=''
                date=''
                

                try:
                    content=rev.find_element("xpath",'.//span[@data-hook="review-body"]').text
                except:
                    pass
                try:
                    author=rev.find_element("xpath",'(.//div[@class="a-profile-content"])[1]').text
                except:
                    pass
                try:
                    date=rev.find_element("xpath",'.//span[@data-hook="review-date"]').text
                    date=date.split(' on ')
                    date=date[1]
                except:
                    pass

                objects={'content':content,'author':author,'date':date}
                
                data.append(objects)
                
            try:
                next_link=driver.find_element("xpath",'//a[contains(text(),"Next page")]').get_attribute('href')
                driver.get(next_link)
                sleep(1)
            except:
                pass

        print(data)
        driver.close()
        return data
        

    except:
        print('Link is not reachable')
    
    print('FINISHED')

# url='https://www.amazon.com/Multiplatform-Amplified-Wireless-Xbox-Nintendo-X/product-reviews/B09VCXMQXF/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
pages=3

# def scrape_reviews(url, pages):
#     headers = {
#         # Add your headers here
#         'dnt': '1',
#         'upgrade-insecure-requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-user': '?1',
#         'sec-fetch-dest': 'document',
#         'referer': 'https://www.amazon.com/',
#         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
#     }
#     extracted_reviews = []
#     count = 0

#     while url and count < pages:
#         try:
#             r = requests.get(url, headers=headers)
#             r.raise_for_status()
#             content = r.content
#             soup = BeautifulSoup(content, 'html.parser')
#             reviews = soup.find_all('div', {'data-hook': 'review'})

#             for review in reviews:
#                 data = {"content": "", "author": "", "date": ""}
#                 text = review.find('span', {'data-hook': 'review-body'})
#                 if text:
#                     text = text.text
#                 author = review.find('span', {"a-profile-name"})
#                 if author:
#                     author = author.text
#                 date = review.find('span', {"review-date"})
#                 if date:
#                     date = date.text
#                 data = {"content": text, "author": author, "date": date}
#                 extracted_reviews.append(data)

#             next_page = soup.find('li', {'class': 'a-last'})
#             if next_page:
#                 next_page_link = next_page.find("a")['href']
#                 url = "https://www.amazon.com" + next_page_link
#             else:
#                 url = None

#             count += 1
#             print("Reviews are being extracted:", count)

#         except requests.exceptions.RequestException as e:
#             print("Exception occurred while fetching page:", e)
#             break
#         except Exception as e:
#             print("An error occurred:", e)
#             break

#     return extracted_reviews



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep
import warnings
from selenium.webdriver.chrome.options import Options

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning) 

chrome_options = Options()
# chrome_options.add_argument("--headless")


def scrape_product(url):
    
    driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        try:
            driver.get(url)
            sleep(1)
        except:
            pass
        
        products_links=[]
        
        while True:
            try:
                products=driver.find_elements("xpath",'//h2/a')
                for product in products:
                    products_links.append(product.get_attribute('href'))
            except:
                pass
            
            try:
                driver.get(driver.find_element("xpath",'//a[contains(@aria-label,"Go to next page, page")]').get_attribute('href'))
                sleep(2)
            except:
                break
                
        #DUPLICATE REMOVAL
        products_links = list(dict.fromkeys(products_links))
        
        objects=[]
        
        for product_link in products_links[:5]:
            
            if product_link=='' or product_link==' ' or product_link=='None' or 'https' not in product_link:
                continue
            
            try:
                driver.get(product_link)
                sleep(0.5)
            except:
                pass


            img=''
            title=''
            price=''
            body=''
            rating=''

            try:
                img=driver.find_element("xpath",'//span[@data-action="main-image-click"]//img').get_attribute('src')
            except:
                pass
            try:
                title=driver.find_element("xpath",'//span[@id="productTitle"]').text
            except:
                pass
            try:
                price=driver.find_element("xpath",'((//div[@id="corePrice_feature_div"])[1]//span)[1]').text
                price=price.replace('\n','.')
            except:
                pass
            try:
                body=driver.find_element("xpath",'//div[@id="productDescription"]').text
            except:
                pass
            try:
                rating=driver.find_element("xpath",'(//div[@id="averageCustomerReviews"])[1]//a[@role="button"]/span').text
            except:
                pass

            objects.append({'product_img':img,'product_title':title,'product_price':price,'product_description':body,'product_rating':rating,'product_url':url})

        print(objects)
        return objects
        driver.close()

    except:
        print('Link is not reachable')
    
    print('FINISHED')

# url='https://www.amazon.com/s?k=Luggage'
# Product_scraper(url)





# def scrape_product(url):
#     objects = []
#     time.sleep(5)
#     headers = {
#         'dnt': '1',
#         'upgrade-insecure-requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-user': '?1',
#         'sec-fetch-dest': 'document',
#         'referer': 'https://www.amazon.com/',
#         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#         # Add your headers here
#     }

#     try:
#         r = requests.get(url, headers=headers)
#         r.raise_for_status()
#     except requests.exceptions.HTTPError as e:
#         print(f"HTTP Error: {e}")
#         return None
#     except requests.exceptions.RequestException as e:
#         print(f"Request Exception: {e}")
#         return None

#     soup = BeautifulSoup(r.text, 'html.parser')
#     exrt = soup.select("div[data-component-type='s-search-result']")
#     print(".............................................................................", exrt)

#     for product in exrt:
#         obj = {"description": "", "price": "", "url": "", "img": ""}
#         laptop_desc = product.select_one(
#             "span.a-size-medium, span.a-size-base-plus.a-color-base.a-text-normal,span.a-section review aok-relative"
#         )
#         obj['description'] = laptop_desc.text if laptop_desc else ""
#         laptop_price = product.select_one("span.a-offscreen")
#         obj['price'] = laptop_price.text if laptop_price else "N/A"
#         link = product.select_one("a.a-link-normal.s-no-outline")
#         obj['url'] = link['href'] if link and 'href' in link.attrs else ""
#         img = product.select_one("img.s-image")
#         obj['img'] = img['src'] if img else ""

#         objects.append(obj)

#     return objects

# In[21]:
# chrome_options = Options()
# chrome_options.add_argument("--headless")


# def scrape_product(url):
#     url='https://www.amazon.com/Multiplatform-Amplified-Wireless-Xbox-Nintendo-X/dp/B09VCXMQXF/ref=sr_1_1_sspa?keywords=gaming%2Bheadsets&pd_rd_r=b3671c29-3982-4eeb-96ba-315e5eb924af&pd_rd_w=1sEFh&pd_rd_wg=4VzhI&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=BH7582P7DXMQKWANK32J&qid=1688465573&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'

#     driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
    
#     try:
#         try:
#             driver.get(url)
#             sleep(1)
#         except:
#             pass

#         objects=[]

#         img=''
#         title=''
#         price=''
#         body=''
#         rating=''

#         try:
#             img=driver.find_element("xpath",'//span[@data-action="main-image-click"]//img').get_attribute('src')
#         except:
#             pass
#         try:
#             title=driver.find_element("xpath",'//span[@id="productTitle"]').text
#         except:
#             pass
#         try:
#             price=driver.find_element("xpath",'((//div[@id="corePrice_feature_div"])[1]//span)[1]').text
#             price=price.replace('\n','.')
#         except:
#             pass
#         try:
#             body=driver.find_element("xpath",'//div[@id="productDescription"]').text
#         except:
#             pass
#         try:
#             rating=driver.find_element("xpath",'(//div[@id="averageCustomerReviews"])[1]//a[@role="button"]/span').text
#         except:
#             pass

#         objects.append({'product_img':img,'product_title':title,'product_price':price,'product_description':body,'product_rating':rating})

#         print(objects)
        
#         driver.close()

#     except:
#         print('Link is not reachable')
    
#     print('FINISHED')

# #  url='https://www.amazon.com/Multiplatform-Amplified-Wireless-Xbox-Nintendo-X/dp/B09VCXMQXF/ref=sr_1_1_sspa?keywords=gaming%2Bheadsets&pd_rd_r=b3671c29-3982-4eeb-96ba-315e5eb924af&pd_rd_w=1sEFh&pd_rd_wg=4VzhI&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=BH7582P7DXMQKWANK32J&qid=1688465573&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'



def clean_texts(texts):
    stwords = stopwords.words('english')
    l = len(texts)/10
    temp_texts = []
    for i in range(len(texts)):
        text = re.sub('\d','0',texts[i])
        if 'www.' in text or 'http:' in text or 'https:' in text or '.com' in text: # remove links and urls
            text = re.sub(r"([^ ]+(?<=\.[a-z]{3}))", " ", text)
        
        text = re.sub('[^a-zA-Z]', ' ', text)
        text = text.lower()
        text = text.split()
        text = [word for word in text if not word in stwords] # remove stopwords 
        text = ' '.join(text)
        temp_texts.append(text)
        if i%l==0:
            print('--'+str(int(i/l)*10)+'%', end='')
    print('--100%--Done !')
    return temp_texts



def testing_prediction(test_list_2):
    count_vect = CountVectorizer()
    lr_model = pickle.load(open('model.pkl', 'rb'))
    count_vect = pickle.load(open('countvect.pkl', 'rb'))
    print ("CountVectorizer .....")
    test_list_vec = count_vect.transform(test_list_2)
    y_pred = lr_model.predict(test_list_vec)
    
    return y_pred



def beforetesting_prediction (test_list_2): 
    print ("Preprocessing the array data....")      
    test_list = clean_texts(test_list_2)
    print ("Cleaning Reviews .......")
    return test_list



def extract_positive (text_list):
  data_list= []
  with open ('words_positive.txt','r') as file:
          for line in file: 
              line = line.strip()
              data_list.append(line)

      
      
      
  positive_words = data_list           
     # Compile a regular expression pattern to match positive words
  pattern = re.compile(r'\b(?:' + '|'.join(positive_words) + r')\b', re.IGNORECASE)
    
  positive_words_list = []
    
    # Iterate over each text in the list
  for text in text_list:
      positive_matches = re.findall(pattern, text)
        # Use the pattern to find positive words in the text
      positive_matches =' '.join(positive_matches)
      positive_words_list.append(positive_matches)
    
  return positive_words_list
      


def extract_negative(text_list):
    data_list = []
    with open('negative_words.txt', 'r') as file:
        for line in file:
            line = line.strip().replace('-', '')
            data_list.append(line)

    negative_words = data_list
    pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, negative_words)) + r')\b', re.IGNORECASE)

    negative_words_list = []

    for text in text_list:
        negative_matches = re.findall(pattern, text)
       
       
        negative_matches =' '.join(negative_matches)
        negative_words_list.append(negative_matches)

    return negative_words_list      
      
      
      
     







      
      
      
      
      
     

   