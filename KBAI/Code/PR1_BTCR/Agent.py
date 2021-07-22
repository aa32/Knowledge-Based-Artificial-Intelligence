# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.

from PIL import Image,ImageDraw
from PIL import ImageChops, ImageStat
import numpy as np


class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        
        i =0
        visual =True
        
        if (problem.problemType == '2x2'):
            print(problem.name)
            #a = problem.problemSetName
            #b = problem.name
            res_fig = []
            figA = problem.figures["A"]
            figB = problem.figures["B"]
            figC = problem.figures["C"]
            fig1 = problem.figures["1"]
            fig2 = problem.figures["2"]
            fig3 = problem.figures["3"]
            fig4 = problem.figures["4"]
            fig5 = problem.figures["5"]
            fig6 = problem.figures["6"]
            
            res_fig.append(problem.figures["1"])
            res_fig.append(problem.figures["2"])
            res_fig.append(problem.figures["3"])
            res_fig.append(problem.figures["4"])
            res_fig.append(problem.figures["5"])
            res_fig.append(problem.figures["6"])
            
            #Visual starts here
            figA_pic = figA.visualFilename
            imgA  = Image.open(figA_pic).convert('L')
        
       
            figB_pic = figB.visualFilename
            imgB  = Image.open(figB_pic).convert('L')
        
        
            figC_pic = figC.visualFilename
            imgC  = Image.open(figC_pic).convert('L')
        
        
            fig1_pic = fig1.visualFilename
            img1  = Image.open(fig1_pic).convert('L')
        
        
            fig2_pic = fig2.visualFilename
            img2  = Image.open(fig2_pic).convert('L')
        
        
            fig3_pic = fig3.visualFilename
            img3  = Image.open(fig3_pic).convert('L')
        
       
            fig4_pic = fig4.visualFilename
            img4  = Image.open(fig4_pic).convert('L')
        
        
            fig5_pic = fig5.visualFilename
            img5  = Image.open(fig5_pic).convert('L')
        
        
            fig6_pic = fig6.visualFilename
            img6  = Image.open(fig6_pic).convert('L')
        
        
            A_B = {}
            A_C = {}
            
         
                
            
        
            AT              = self.IdentityT(imgA)
            A90             = self.Rotate90(imgA)
            A180            = self.Rotate180(imgA)
            A270            = self.Rotate270(imgA)
            AflipLR         = self.flip_L_R(imgA)
            AflipTB         = self.flip_T_B(imgA)
            A45             = self.Rotate45(imgA)
            ACF             = self.colorfill(imgA)
    
         
            
            
            #A45.show()
     
        
        
            A_B["IdentityT"]= self.img_diff(AT,imgB)
            A_B["Rotate90"]= self.img_diff(A90,imgB)
            A_B["Rotate180"] = self.img_diff(A180,imgB)
            A_B["Rotate270"] = self.img_diff(A270,imgB)
            A_B["flip_L_R"] = self.img_diff(AflipLR,imgB)
            A_B["flip_T_B"] = self.img_diff(AflipTB ,imgB)
            A_B["Rotate45"] = self.img_diff(A45,imgB)
            A_B["colorfill"] = self.img_diff(ACF,imgB)
            print("A_B")
            print(A_B)
            
        
        
        
        
            A_C["IdentityT"]= self.img_diff(AT,imgC)
            A_C["Rotate90"]= self.img_diff(A90,imgC)
            A_C["Rotate180"] = self.img_diff(A180,imgC)
            A_C["Rotate270"] = self.img_diff(A270,imgC)
            A_C["flip_L_R"] = self.img_diff(AflipLR,imgC)
            A_C["flip_T_B"] = self.img_diff(AflipTB,imgC)
            A_C["Rotate45"] = self.img_diff(A45,imgC)
            A_C["colorfill"] = self.img_diff(ACF,imgC)
            
            print("A_C")
            print(A_C)
        
           
        
        
            B_Min  = min(A_B.values()) 
            print("b_min - %d",B_Min)
            
            keysB = [key for key in A_B if A_B[key] == B_Min]
            print("operartions AB")
            print(keysB)

            C_Min  = min(A_C.values()) 
            print("C_min - %d",C_Min)
            keysC = [key for key in A_C if A_C[key] == C_Min]
        
            if( B_Min < C_Min ):
                for B_res in keysB:
                    if(B_res == 'IdentityT'):
                        imgD = self.IdentityT(imgC)
                    elif(B_res == 'Rotate90'):
                        imgD = self.Rotate90(imgC)
                    elif(B_res == 'Rotate180'):
                        imgD = self.Rotate180(imgC)
                    elif(B_res == 'Rotate270'):
                        imgD = self.Rotate270(imgC)
                    elif(B_res == 'flip_L_R'):
                        imgD = self.flip_L_R(imgC)
                    elif(B_res == 'flip_T_B'):
                        imgD = self.flip_T_B(imgC)
                    elif(B_res == 'Rotate45'):
                        imgD = self.Rotate45(imgC)
                    elif(B_res == "colorfill"):
                        imgD = self.colorfill(imgC)
                    
            else:
                for C_res in keysC:
                    if(C_res == 'IdentityT'):
                        imgD = self.IdentityT(imgB)
                    elif(C_res == 'Rotate90'):
                        imgD = self.Rotate90(imgB)
                    elif(C_res == 'Rotate180'):
                        imgD = self.Rotate180(imgB)
                    elif(C_res == 'Rotate270'):
                        imgD = self.Rotate270(imgB)
                    elif(C_res == 'flip_L_R'):
                        imgD = self.flip_L_R(imgB)
                    elif(C_res == 'flip_T_B'):
                        imgD = self.flip_T_B(imgB)
                    elif(C_res == 'Rotate45'):
                        imgD = self.Rotate45(imgB)
                    elif(C_res == "colorfill"):
                        imgD = self.colorfill(imgB)
                    
     
                
                
                
            
                
                
                
            res = {}
            res_ms = {}
        
            
        
            res["1"] = self.img_diff(imgD,img1)
            res["2"] = self.img_diff(imgD,img2)
            res["3"] = self.img_diff(imgD,img3)
            res["4"] = self.img_diff(imgD,img4)
            res["5"] = self.img_diff(imgD,img5)
            res["6"] = self.img_diff(imgD,img6)
            
            res_ms["1"] = self.MSE(imgD,img1)
            res_ms["2"] = self.MSE(imgD,img2)
            res_ms["3"] = self.MSE(imgD,img3)
            res_ms["4"] = self.MSE(imgD,img4)
            res_ms["5"] = self.MSE(imgD,img5)
            res_ms["6"] = self.MSE(imgD,img6)
            
            #print ("diff to results")
            # print(res)
            
            
        
            res_min  = min(res.values()) 
            print ("print min diff")
            print(res_min)
            
            #print("transformation diff")
            #print(min(ABC_Min,ACB_Min))
            
            resMS_min  = min(res_ms.values()) 
            #print("MS value min")
            #print(resMS_min)
            imgAn  = np.array(imgA)
            imgBn = np.array(imgB)
            imgCn  = np.array(imgC)
            p = True
            q = True
           
 
            
            if (res_min < 4 and (C_Min<4 or B_Min<4) and visual == True):
                print("it is first if")
                res_key = [key for key in res if res[key] == res_min][0]
                i = int(res_key)
                return i
            elif (res_min < 20 and (C_Min<20 or B_Min<20) and problem.hasVerbal == False):
                print("it is second if")
                res_key = [key for key in res if res[key] == res_min][0]
                i = int(res_key)
                return i
            
            elif ((problem.hasVerbal == True) and (res_min > 4 or min(C_Min,B_Min)>4)) :
                print("it is third if")
                visual = False
                
            else:
                visual = False
            
                
                
                
            
            if(visual == False):
                print ("In verbal")
            
                nA = len(figA.objects)
                nB = len(figB.objects)
                nC = len(figC.objects)
                n =[]
                n.append(len(fig1.objects))
                n.append(len(fig2.objects))
                n.append(len(fig3.objects))
                n.append(len(fig4.objects))
                n.append(len(fig5.objects))
                n.append(len(fig6.objects))
                if (nA==1 and nB==1 and nC==1):
                    sideA = self.GetSides(figA.objects["a"].attributes['shape'])
                    sideB = self.GetSides(figB.objects["b"].attributes['shape'])
                    sideC = self.GetSides(figC.objects["c"].attributes['shape'])
                    sides = []
                    sides.append(self.GetSides(fig1.objects['d'].attributes['shape']))
                    sides.append(self.GetSides(fig2.objects['e'].attributes['shape']))
                    sides.append(self.GetSides(fig3.objects['f'].attributes['shape']))
                    sides.append(self.GetSides(fig4.objects['g'].attributes['shape']))
                    sides.append(self.GetSides(fig5.objects['h'].attributes['shape']))
                    sides.append(self.GetSides(fig6.objects['i'].attributes['shape']))
                    if (sideA!=sideB and sideA!=0 and sideB!=0 and figA.objects['a'].attributes['fill']== figB.objects['b'].attributes['fill']):
                        if (sideA > sideB):
                            p = sideA - sideB
                            sideD = sideC - p
                        elif (sideA < sideB):
                            p = sideB - sideA
                            sideD = sideC + p
                        shape = self.GetShape(sideD)
                        figC.objects['c'].attributes['shape'] = shape

                        i = 0
                        for fig in res_fig:
                            i = i + 1
                            if (i == 1):
                                p = 'd'
                            elif (i == 2):
                                p = 'e'
                            elif (i == 3):
                                p = 'f'
                            elif (i == 4):
                                p = 'g'
                            elif (i == 5):
                                p = 'h'
                            elif (i == 6):
                                p = 'i'

                            if fig.objects[p].attributes == figC.objects['c'].attributes:
                                break
                        return i
                    
                    elif (sideA!=sideC and sideA!=0 and sideC!=0 and figA.objects['a'].attributes['fill']== figC.objects['c'].attributes['fill']):
                        if (sideA > sideC):
                            p = sideA - sideC
                            sideD = sideB - p
                        elif (sideA < sideC):
                            p = sideC - sideA
                            sideD = sideB + p
                        shape = self.GetShape(sideD)
                        figB.objects['b'].attributes['shape'] = shape

                        i = 0
                        for fig in res_fig:
                            i = i + 1
                            if (i == 1):
                                p = 'd'
                            elif (i == 2):
                                p = 'e'
                            elif (i == 3):
                                p = 'f'
                            elif (i == 4):
                                p = 'g'
                            elif (i == 5):
                                p = 'h'
                            elif (i == 6):
                                p = 'i'

                            if fig.objects[p].attributes == figB.objects['b'].attributes:
                                break
                        return i
                    
            
                    
                    if (figA.objects['a'].attributes['fill'] and (figA.objects['a'].attributes['fill'] != figB.objects['b'].attributes['fill'])):
                        if (figC.objects['c'].attributes['fill'] == 'yes'):
                            p = 'no'
                        else:
                            p = 'yes'

                        figC.objects['c'].attributes['fill'] = p
                        print(figC.objects['c'].attributes['fill'])
                        i = 0
                        for fig in res_fig:
                            i = i + 1
                            if (i == 1):
                                p = 'd'
                            elif (i == 2):
                                p = 'e'
                            elif (i == 3):
                                p = 'f'
                            elif (i == 4):
                                p = 'g'
                            elif (i == 5):
                                p = 'h'
                            elif (i == 6):
                                p = 'i'

                            if fig.objects[p].attributes == figC.objects['c'].attributes:
                                break
                        return i
                    
                    elif (figA.objects['a'].attributes['fill'] and (figA.objects['a'].attributes['fill'] != figC.objects['c'].attributes['fill'])):
                        if (figB.objects['b'].attributes['fill'] == 'yes'):
                            p = 'no'
                        else:
                            p = 'yes'

                        figB.objects['b'].attributes['fill'] = p
                        print(figB.objects['b'].attributes['fill'])
                        i = 0
                        for fig in res_fig:
                            i = i + 1
                            if (i == 1):
                                p = 'd'
                            elif (i == 2):
                                p = 'e'
                            elif (i == 3):
                                p = 'f'
                            elif (i == 4):
                                p = 'g'
                            elif (i == 5):
                                p = 'h'
                            elif (i == 6):
                                p = 'i'

                            if fig.objects[p].attributes == figB.objects['b'].attributes:
                                break
                        return i
                    else:
                        return -1
                    

                else:
                    r = self.pixelCompare(imgA,imgB,imgC,img1,img2,img3,img4,img5,img6)
                    return r





                            
                        
                        
            else :
                return -1
                        
                    
     
                
       
        else:
            return -1
                
                
            
       
        
   
        
        
        
        
        
        
    
    def IdentityT(self,img):
        return img
    
    def GetSides(self,shape):
        side = 0
        if shape =='square':
            side = 4
        elif shape == 'triangle':
            side = 3
        elif shape == 'pentagon':
            side = 5
        elif shape == 'hexagon':
            side =6
        elif shape == 'heptagon':
            side = 7
        elif shape == 'octagon':
            side =8
        return side
    
    def GetShape(self,sides):
        side = 0
        if sides ==4:
            shape = 'square'
        elif sides == 3:
            shape = 'triangle'
        elif sides == 5:
            shape = 'pentagon'
        elif sides == 6:
           shape = 'hexagon'
        elif sides == 7:
            shape = 'heptagon'
        elif sides == 8:
            shape = 'octagon'
        return shape
        
            
            
            
        

   
    #Start Referenced code:   
    #https://stackoverflow.com/questions/5252170/specify-image-filling-color-when-rotating-in-python-with-pil-and-setting-expand   
    def Rotate45(self,img):
        
        #print("inside 45")
        #print(img.size)
        img1 = img.convert('RGBA')
        rot = img1.rotate(30, expand=1)
        fff = Image.new('RGBA', rot.size, (255,)*4)
        out = Image.composite(rot, fff, rot)
        img_r = out.convert(img.mode)
        img_p = img_r.convert('L')
        img_q = img_p.resize(img.size)
        return img_q
    ##END Referenced Code
        
         
    
    def Rotate90(self,img):
        img_r = img.transpose(Image.ROTATE_90)
        return img_r
    
    def Rotate180(self,img):
        img_r = img.transpose(Image.ROTATE_180)
        return img_r
    
    def Rotate270(self,img):
        img_r = img.transpose(Image.ROTATE_270)
        return img_r
    
    def flip_L_R(self,img):
        img_f = img.transpose(Image.FLIP_LEFT_RIGHT)
        return img_f
        
    def flip_T_B(self,img):
        img_f = img.transpose(Image.FLIP_TOP_BOTTOM)
        return img_f
    
    #Start Referenced Code :https://stackoverflow.com/questions/46083880/fill-in-a-hollow-shape-using-python-and-pillow-pil
    
    def colorfill(self,img):
        im = img.convert('RGB')
        ImageDraw.floodfill(im,xy=(0,0),value=(57,255,20))
        n  = np.array(im)
        n[(n[:, :, 0:3] != [57,255,20]).any(2)] = [0,0,0]
        n[(n[:, :, 0:3] == [57,255,20]).all(2)] = [255,255,255]
        img_r = Image.fromarray(n)
        img_p=img_r.convert('L')
        #img_p.show()
        return img_p
    # End Referenced Code
        
        
       

    

    def SSIM(self,img1,img2):
        sim = compare_ssim(img1,img2)
        return sim
        

#start referenced code : https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
    def MSE(self,img1,img2):
        img1 = np.array(img1)
        img2 = np.array(img2)
        err = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
        err /= float(img1.shape[0] * img1.shape[1])
        return err
#End referenced code
      
        

    
    def img_diff(self,img1,img2):

        if (img1.mode != img2.mode) or (img1.size != img2.size) or (img1.getbands() != img2.getbands()):
            return None

        # Generate diff image in memory.
        diff_img = ImageChops.difference(img1, img2)
       
        
        # Calculate difference as a ratio.
        stat = ImageStat.Stat(diff_img)
       
        return stat.mean[0]
    
    def imgXOR_mul(self,im1,im2,im3):
        diff_img = ImageChops.difference(im2, im1)
        diff_im = ImageChops.invert(diff_img)
        comp = ImageChops.multiply(diff_im,im3)

        #comp.show()
        return comp
    
    def pixelCompare(self, imgA,imgB,imgC,img1,img2,img3,img4,img5,img6):
        print("in the new func")
        pixA = self.gP(imgA)
        pixB = self.gP(imgB)
        pixC = self.gP(imgC)

        pix1 = self.gP(img1)
        pix2 = self.gP(img2)
        pix3 = self.gP(img3)
        pix4 = self.gP(img4)
        pix5 = self.gP(img5)
        pix6 = self.gP(img6)

        pix_res = [pix1,pix2,pix3,pix4,pix5,pix6]
        
        A_t_B = self.diff(pixA, pixB)
        A_t_C = self.diff(pixA, pixC)

        pix_diff1 = self.diff(A_t_B, pixC)
        pix_diff2 = self.diff(A_t_C, pixB)
        pix_diff3 = self.diff(pix_diff1, pix_diff2)

        for i, element in enumerate(pix_res):
            r = self.validate(pix_diff1, pix_res)
            if r == -1:
                r = self.validate(pix_diff2, pix_res)
            if r == -1:
                r = self.validate(pix_diff3, pix_res)

        print("New Functio")
        print(r)
        return r
    
     
            
    def validate(self,pix1, pix_res, threshold=0.90):
        ret = -1
        c = 0
        for i, element in enumerate(pix_res):
            a,b = self.perMatch(pix1, element, threshold=threshold)
            if a and (b > c):
                ret = i + 1
                c = b
        return ret
    
    def perMatch(self,pix1, pix2, threshold=0.90):
        m = np.mean(np.equal(pix1, pix2).astype(int))
        t = m > threshold
        return t, m
    
   

    def gP(self,img):
        img_b = img.point(lambda p: 0 if p<126 else 255, '1')
        
        bin = np.array(img_b)
        
        return 1-bin
    
    def diff(self,pix1,pix2):
        return np.abs(pix2-pix1)
    
    
    """
    if np.array_equal(pix_diff1, element) or np.array_equal(pix_diff2, element) or np.array_equal(
                     pix_diff3, element):
                r = i+1
                break
            else :
    """
        

   
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        