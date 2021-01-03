from flask import render_template
import numpy as np
from numpy import asarray 
from PIL import ImageStat

class ImgProp:
        
    #takes an image in grayscale and return the min value
    def Min_value(self,img,FUNC_NAME,url,IMAGE_FILE_NAME): 
        min_max = ImageStat.Stat(img).extrema #Min/max values of pixles in the image
        min_val=min_max[0][0]
        return render_template('stats_index.html',func=FUNC_NAME,img_url=url,img_name=IMAGE_FILE_NAME, value=min_val,describtion="This function calculates the Min value of pixels in the giving image.")


    #takes an image in grayscale and return the max value
    def Max_value(self,img,FUNC_NAME,url,IMAGE_FILE_NAME): 
        min_max = ImageStat.Stat(img).extrema #Min/max values of pixles in the image
        max_val=min_max[0][1]
        return render_template('stats_index.html',func=FUNC_NAME ,img_url=url,img_name=IMAGE_FILE_NAME, value=max_val,describtion="This function calculates the Max value of pixels in the giving image.")

    #Average (arithmetic mean) pixel level in the image.
    def Mean_value(self,img,FUNC_NAME,url,IMAGE_FILE_NAME): 
        Mean_value = ImageStat.Stat(img).mean[0] 
        return render_template('stats_index.html',func=FUNC_NAME ,img_url=url,img_name=IMAGE_FILE_NAME, value=Mean_value,describtion="This function calculates the Average pixel level in the giving image.")


    #Median pixel level in the image.
    def Median_value(self,img,FUNC_NAME,url,IMAGE_FILE_NAME): 
        Median_value = ImageStat.Stat(img).median[0]
        return render_template('stats_index.html',func=FUNC_NAME ,img_url=url,img_name=IMAGE_FILE_NAME, value=Median_value,describtion="This function calculates the Median pixel level in the giving image.")

    #n'th percentile of the image
    def percentile_value(self,img,FUNC_NAME,url,IMAGE_FILE_NAME,p):
        numpydata = asarray(img) # convert PIL images into NumPy arrays 
        percentile= np.percentile(numpydata,p) # calculate n'th percentile of the image
        return render_template('stats_index.html',func=FUNC_NAME ,img_url=url,img_name=IMAGE_FILE_NAME, value=percentile,describtion="This function calculates the {} Percentile of the giving image.".format(FUNC_NAME))

        