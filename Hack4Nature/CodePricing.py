



def Pricing(superficies_total=240,#en kilometre carré,
    superficie_par_image=90*90*(1e-6),# en kilometre caré exemple avec 90 metre ,
    pris_requette_n1=1.6402/1000, #en euro #1,6402 EUR/1 k requests,
    pris_requette_n2=1.31216/1000): #1,31216 EUR/1 k requests,
    nb_requettes=superficies_total/superficie_par_image
    
    pris_total=nb_requettes*pris_requette_n2

    return pris_total

ls=[
[43.356819, 5.482127]
[43.374439, 5.345074]
[43.253117, 5.387901]
[43.292301, 5.453946]]


