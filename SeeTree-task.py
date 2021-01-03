import requests
from flask import Flask,Response,render_template
from PIL import ImageStat,Image,ImageOps
import numpy as np
import ImgProp as imageprop
app = Flask(__name__)


#check if a URL of an image is up and exists in the bucket
def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False


# app name 
@app.errorhandler(404) 
  
# inbuilt function which takes error as parameter 
def not_found(e): 
  
# defining function 
  return render_template("404.html"), 404


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/health',methods=['GET'])
def func():
    return render_template('ok.html'),200


@app.route('/stats/<IMAGE_FILE_NAME>/<FUNC_NAME>',methods=['GET'])
def get_result(IMAGE_FILE_NAME,FUNC_NAME):
    url = 'https://storage.googleapis.com/seetree-demo-open/{}'.format(IMAGE_FILE_NAME) #image url
    if not is_url_image(url):          #if the image doesn't exists
        return render_template('img_404.html'),404 

    input_image=Image.open(requests.get(url, stream=True).raw)
    gray_image = ImageOps.grayscale(input_image) #Convert RGB Image to Grayscale image

    
    if FUNC_NAME =='min': 
        return imageprop.ImgProp.Min_value(imageprop,gray_image,FUNC_NAME,url,IMAGE_FILE_NAME)
    
    elif FUNC_NAME =='max':
        return imageprop.ImgProp.Max_value(imageprop,gray_image,FUNC_NAME,url,IMAGE_FILE_NAME)
    
    elif FUNC_NAME =='mean':
        return imageprop.ImgProp.Mean_value(imageprop,gray_image,FUNC_NAME,url,IMAGE_FILE_NAME)
    
    elif FUNC_NAME =='median':
        return imageprop.ImgProp.Median_value(imageprop,gray_image,FUNC_NAME,url,IMAGE_FILE_NAME)

    elif FUNC_NAME[0]=='p' and FUNC_NAME[1:].isnumeric():
        if int(FUNC_NAME[1:])>=0 and int(FUNC_NAME[1:])<=100:
            return imageprop.ImgProp.percentile_value(imageprop,gray_image,FUNC_NAME,url,IMAGE_FILE_NAME,int(FUNC_NAME[1:]))
        else:                                                # the percentile is NOT between 0..100 (function doesn't exists)
            return render_template('func_404.html'),404     

    else:  # the function doesn't exists
         return render_template('func_404.html'),404

    

        
        
    


     
    

    














if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000)



