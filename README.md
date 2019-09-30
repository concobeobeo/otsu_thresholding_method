# otsu_thresholding_method
I.	OTSU THRESHOLDING METHOD:
Otsu thresholding method, named after its inventor Nobuyuki Otsu, is one of many thresholding, binarization method. 
Otsu thresholding involves in statistic and probability theory. So calculated values will relate to histogram (represent distribution of the image). This method basically base on Variances. Suppose, one image has 2 classes: foreground and background. Within Class Variance (Vw) and Between Class Variance (Vb) is considered. 
Vw and Vb is the measure of spread of in a class and between 2 classes respectively for a threshold value. The optimal threshold would make Vw to be smallest (the less dispersed data is in each class) or Vb max (the most dispersed data is between classes). 
Calculate Variance:
Weight of background: /fraq{Wb = Nb/N}
