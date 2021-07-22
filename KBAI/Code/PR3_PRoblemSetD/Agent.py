from __future__ import division    
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
                        
                    
     
                
       
        elif(problem.problemType == '3x3'):
            r = -1
            print(problem.name)
            #a = problem.problemSetName
            #b = problem.name
            res_fig = []
            figA = problem.figures["A"]
            figB = problem.figures["B"]
            figC = problem.figures["C"]
            figD = problem.figures["D"]
            figE = problem.figures["E"]
            figF = problem.figures["F"]
            figG = problem.figures["G"]
            figH = problem.figures["H"]
           
            fig1 = problem.figures["1"]
            fig2 = problem.figures["2"]
            fig3 = problem.figures["3"]
            fig4 = problem.figures["4"]
            fig5 = problem.figures["5"]
            fig6 = problem.figures["6"]
            fig7 = problem.figures["7"]
            fig8 = problem.figures["8"]
            
            res_fig.append(problem.figures["1"])
            res_fig.append(problem.figures["2"])
            res_fig.append(problem.figures["3"])
            res_fig.append(problem.figures["4"])
            res_fig.append(problem.figures["5"])
            res_fig.append(problem.figures["6"])
            res_fig.append(problem.figures["7"])
            res_fig.append(problem.figures["8"])
            
            imgs = []
            
            #Visual starts here
            prob_img = []
            figA_pic = figA.visualFilename
            imgA  = Image.open(figA_pic).convert('L')
            prob_img.append(imgA)
        
       
            figB_pic = figB.visualFilename
            imgB  = Image.open(figB_pic).convert('L')
            prob_img.append(imgB)
        
        
            figC_pic = figC.visualFilename
            imgC  = Image.open(figC_pic).convert('L')
            prob_img.append(imgC)
            
            figD_pic = figD.visualFilename
            imgD  = Image.open(figD_pic).convert('L')
            prob_img.append(imgD)
            
            figE_pic = figE.visualFilename
            imgE  = Image.open(figE_pic).convert('L')
            prob_img.append(imgE)
            
            figF_pic = figF.visualFilename
            imgF  = Image.open(figF_pic).convert('L')
            prob_img.append(imgF)
            
            figG_pic = figG.visualFilename
            imgG  = Image.open(figG_pic).convert('L')
            prob_img.append(imgG)
            
            
            figH_pic = figH.visualFilename
            imgH  = Image.open(figH_pic).convert('L')
            prob_img.append(imgH)
        
        
            fig1_pic = fig1.visualFilename
            img1  = Image.open(fig1_pic).convert('L')
            imgs.append(img1)
        
        
            fig2_pic = fig2.visualFilename
            img2  = Image.open(fig2_pic).convert('L')
            imgs.append(img2)
        
        
            fig3_pic = fig3.visualFilename
            img3  = Image.open(fig3_pic).convert('L')
            imgs.append(img3)
        
       
            fig4_pic = fig4.visualFilename
            img4  = Image.open(fig4_pic).convert('L')
            imgs.append(img4)
        
        
            fig5_pic = fig5.visualFilename
            img5  = Image.open(fig5_pic).convert('L')
            imgs.append(img5)
        
        
            fig6_pic = fig6.visualFilename
            img6  = Image.open(fig6_pic).convert('L')
            imgs.append(img6)
            
            fig7_pic = fig7.visualFilename
            img7  = Image.open(fig7_pic).convert('L')
            imgs.append(img7)
            
            fig8_pic = fig8.visualFilename
            img8  = Image.open(fig8_pic).convert('L')
            imgs.append(img8)
        
            
            r = self.pixelCompare2(imgA,imgB,imgC,imgD,imgE,imgF,imgG,imgH,img1,img2,img3,img4,img5,img6,img7,img8,imgs,prob_img)
            print(r)
        
            return r
        
        
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
        ImageDraw.floodfill(im,xy=(92,92),value=(57,255,20))
        n  = np.array(im)
        n[(n[:, :, 0:3] != [57,255,20]).any(2)] = [255,255,255]
        n[(n[:, :, 0:3] == [57,255,20]).all(2)] = [0,0,0]
        img_r = Image.fromarray(n)
        img_p=img_r.convert('1')
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

        #print("New Functio")
        print(r)
        return r
        
    def pixelCompare2(self, imgA,imgB,imgC,imgD,imgE,imgF,imgG,imgH,img1,img2,img3,img4,img5,img6,img7,img8,imgs,prob_img):
        #print("in the new func")
        r = -1
        
        
        pixA = self.gP(imgA)
        pixB = self.gP(imgB)
        pixC = self.gP(imgC)
        pixD = self.gP(imgD)
        pixE = self.gP(imgE)
        pixF = self.gP(imgF)
        pixG = self.gP(imgG)
        pixH = self.gP(imgH)
        pix_prob = [pixA,pixB,pixC,pixD,pixE,pixF,pixG,pixH]

        pix1 = self.gP(img1)
        pix2 = self.gP(img2)
        pix3 = self.gP(img3)
        pix4 = self.gP(img4)
        pix5 = self.gP(img5)
        pix6 = self.gP(img6)
        pix7 = self.gP(img7)
        pix8 = self.gP(img8)

        pix_res = [pix1,pix2,pix3,pix4,pix5,pix6,pix7,pix8]
        """
        print ("A size" , pixA.size)
        print("B size",pixB.size)
        print("E Size" , pixE.size)
        print("H size" , pixH.size)
        
        print ("3 size",pix3.size)
        """
        
        darkpixA = np.sum(pixA)
        
        darkpixB = np.sum(pixB)
        
        darkpixC = np.sum(pixC)
        
        darkpixD = np.sum(pixD)
        
        darkpixE = np.sum(pixE)
       
        darkpixF = np.sum(pixF)
        
        darkpixG = np.sum(pixG)
       
        darkpixH = np.sum(pixH)
        darkpix_prob = [darkpixA,darkpixB,darkpixC,darkpixD,darkpixE,darkpixF,darkpixG,darkpixH]
        
      
        
        
        
        darkpix_res = []
        
        darkpix_res.append(np.sum(pix1))
        darkpix_res.append(np.sum(pix2))
        darkpix_res.append(np.sum(pix3))
        darkpix_res.append(np.sum(pix4))
        darkpix_res.append(np.sum(pix5))
        darkpix_res.append(np.sum(pix6))
        darkpix_res.append(np.sum(pix7))
        darkpix_res.append(np.sum(pix8))
        #print ("dark pixels" , darkpix_res)
        
        ######### ImageChops operations:###################
        imgA1  = imgA.convert('1')
        imgB1  = imgB.convert('1')
        imgC1  = imgC.convert('1')
        imgD1  = imgC.convert('1')
        imgE1  = imgE.convert('1')
        imgF1  = imgF.convert('1')
        imgG1  = imgG.convert('1')
        imgH1  = imgH.convert('1')
        

        img11  = img1.convert('1')
        img21  = img2.convert('1')
        img31  = img3.convert('1')
        img41  = img4.convert('1')
      
        img51  = img5.convert('1')
        img61  = img6.convert('1')
        img71  = img7.convert('1')
        img81  = img8.convert('1')
        img_res1 = [img11,img21,img31,img41,img51,img61,img71,img81]
        
       
        
    
        CB_ratio  = darkpixC/float(darkpixB)
        #print ("C to B ratio",CB_ratio)
        
        ED_ratio  = darkpixE/float(darkpixD)
        #print ("E to D ratio",ED_ratio)
        
        FE_ratio  = darkpixF/float(darkpixE)
        #print ("F to E ratio",FE_ratio)
        
        HG_ratio  = darkpixH/float(darkpixG)
        #print ("H to G ratio",HG_ratio)
        
        EA_ratio  = darkpixE/float(darkpixA)
        
        
        #Diagnal ratio results:
        D_Ratio_Results = []
     
        for i, element in enumerate(darkpix_res):
            IE_ratio = np.sum(darkpix_res[i]/float(darkpixE))
            #print("I to H ratio", IH_ratio)
            D_Ratio_Results.append(IE_ratio)
        
        #print("D_Ratio_Results",D_Ratio_Results)
        
        D_ratio_diff = []
        
        for i, element in enumerate(D_Ratio_Results):
                p = abs(D_Ratio_Results[i]-EA_ratio)
                #print("ratio_diff",p)
                D_ratio_diff.append(p)
                
        below_d_thres = []
        below_d_index = []
        
        for i, element in enumerate(D_ratio_diff):
                if(D_ratio_diff[i] < 0.05965):
                    below_d_thres.append(D_ratio_diff[i]) 
                    below_d_index.append(i)
        
        
        
        #print("below d thres",below_d_thres)
        above_h_thres = []
        above_thres_index =[]
        ipr_p = []
    
        #Horizontal Ratio Results
        H_Ratio_Results = []
        #Horizontal Result Ratios:
        for i, element in enumerate(darkpix_res):
            IH_ratio = np.sum(darkpix_res[i]/float(darkpixH))
            #print("I to H ratio", IH_ratio)
        
            
            H_Ratio_Results.append(IH_ratio)
        
        #print("H_Ratio_Results",H_Ratio_Results)
        
        H_ratio_diff = []
        
        
        for i, element in enumerate(H_Ratio_Results):
                p = abs(H_Ratio_Results[i]-CB_ratio)
                #print("ratio_diff",p)
                H_ratio_diff.append(p)
        
        
        
        above_h_thres = []
        above_thres_index =[]
        ipr_p = []
        
        for i, element in enumerate(H_ratio_diff):
                if(H_ratio_diff[i] < 0.07965):
                    above_h_thres.append(H_ratio_diff[i]) 
                    above_thres_index.append(i)
        
        print("ratio values below threshold",above_h_thres)
        print("indexes of values below thres",above_thres_index)
        
        
        darkpixdiff_AC = abs(darkpixA-darkpixC)
        darkpixdiff_DF = abs(darkpixD-darkpixF)
        darkpixratioAC = darkpixA/darkpixC
        
        
        #####Darkpix diff of AC and DF
        diff_ACDF = abs(darkpixdiff_AC -darkpixdiff_DF)
        print("diff_ACDF",diff_ACDF)
        if (diff_ACDF < 10):
            ACGI_diff = []
            for i, element in enumerate(darkpix_res):
                darkpixdiff_GI = abs(darkpixG-darkpix_res[i])
                diff = abs(darkpixdiff_GI - darkpixdiff_AC )
                ACGI_diff.append(diff)
                
            t = np.min(ACGI_diff)
            print ("min ACGI diff",t)
            
        
        
        
        
        ######End Dark Pix Diff of AC and DF
        
        
        n,diffi,ind = self.overall_min(darkpixA,darkpixB,darkpixC,darkpixG,darkpixH,pixB,pixC,pixA,darkpix_res,pix_res,pixG,pixH)
        print("n,diffi,ind",n,diffi,ind)
        
        operation = []
        ###Vertical sum of dark pixels#######
        
        sum_dark_ADG_v = darkpixA+darkpixD+darkpixG
        print("sum_dark_ADG_v",sum_dark_ADG_v)
        
        sum_dark_BEH_v = darkpixB+darkpixE+darkpixH
        print("sum_dark_BEH_v",sum_dark_BEH_v)
        
        ADG_BEH_ratio_v = sum_dark_ADG_v/sum_dark_BEH_v
        print("ADG_BEH_ratio_v",ADG_BEH_ratio_v)
        
        vertical_diff_ratio_ADG = []
        vertical_ind_ratio_ADG = []
        
        for i, element in enumerate(darkpix_res):
            sum_dark_CFI_v = darkpixC+darkpixF+darkpix_res[i]
            ratio_CFI_ADG = sum_dark_CFI_v/sum_dark_ADG_v
            ratio_CFI_BEH = sum_dark_CFI_v/sum_dark_BEH_v
            
            diff_ADG_CFI =  abs(ratio_CFI_ADG - ADG_BEH_ratio_v)
            print("diff_ADG_CFI",diff_ADG_CFI)
            diff_BEH_CFI = abs(ratio_CFI_BEH- ADG_BEH_ratio_v)
            print("diff_BEH_CFI",diff_BEH_CFI)
            if (diff_ADG_CFI< 0.02 ):
                vertical_diff_ratio_ADG .append(diff_ADG_CFI)
                vertical_ind_ratio_ADG.append(i)
                
        if (len(vertical_diff_ratio_ADG)>0)  :      
            print("vertical_diff_ratio_ADG",vertical_diff_ratio_ADG)
            min_vertical_ratio = np.min(vertical_diff_ratio_ADG)
            min_vertical_index = np.argmin(vertical_diff_ratio_ADG)
                
            min_index_v = vertical_ind_ratio_ADG[min_vertical_index]+1
            
        #####################END OF Vertical
        
        #########################Horizontal#################
        
        sum_dark_ABC_h = darkpixA+darkpixB+darkpixC
        print("sum_dark_ABC_v",sum_dark_ABC_h)
        
        sum_dark_DEF_h = darkpixD+darkpixE+darkpixF
        print("sum_dark_DEF_h",sum_dark_DEF_h)
        
        ABC_DEF_ratio_h = sum_dark_ABC_h/sum_dark_DEF_h
        print("ABC_DEF_ratio_h",ABC_DEF_ratio_h)
        
        hor_diff_ratio_ABC = []
        hor_ind_ratio_ABC = []
        
        for i, element in enumerate(darkpix_res):
            sum_dark_GHI_h = darkpixG+darkpixH+darkpix_res[i]
            ratio_GHI_ABC = sum_dark_GHI_h/sum_dark_ABC_h
            ratio_GHI_DEF = sum_dark_GHI_h/sum_dark_DEF_h
            
            diff_ABC_GHI =  abs(ratio_GHI_ABC - ABC_DEF_ratio_h)
            print("diff_ABC_GHI",diff_ABC_GHI)
            diff_DEF_GHI = abs(ratio_GHI_DEF- ABC_DEF_ratio_h)
            print("diff_DEF_GHI",diff_DEF_GHI)
            if (diff_ABC_GHI< 0.02 ):
                hor_diff_ratio_ABC.append(diff_ABC_GHI)
                hor_ind_ratio_ABC.append(i)
                
        if(len(hor_diff_ratio_ABC)>0) :      
            print("hor_diff_ratio_ABC",hor_diff_ratio_ABC)
            min_horizontal_ratio = np.min(hor_diff_ratio_ABC)
            min_horizontal_index = np.argmin(hor_diff_ratio_ABC)
            
            min_index_h = hor_ind_ratio_ABC[min_horizontal_index]+1
        
        
        ###########################END OF Horizontal#################
        
        ###################Diagonal##################
        
        sum_dark_FGB_d = darkpixF+darkpixG+darkpixB
        print("sum_dark_FGB_d",sum_dark_FGB_d)
        
        sum_dark_HCD_d = darkpixH+darkpixC+darkpixD
        print("sum_dark_HCD_d",sum_dark_HCD_d)
        
        FGB_HCD_ratio_d = sum_dark_FGB_d/sum_dark_HCD_d
        print("FGB_HCD_ratio_h",FGB_HCD_ratio_d)
        
        diag_diff_ratio_FGB = []
        diag_ind_ratio_FGB = []
        
        for i, element in enumerate(darkpix_res):
            sum_dark_AEI_d = darkpixA+darkpixE+darkpix_res[i]
            ratio_AEI_FGB = sum_dark_AEI_d/sum_dark_FGB_d
            ratio_AEI_HCD = sum_dark_AEI_d/sum_dark_HCD_d
            
            diff_FGB_AEI =  abs(ratio_AEI_FGB - FGB_HCD_ratio_d)
            print("diff_FGB_AEI",diff_FGB_AEI)
            diff_HCD_AEI = abs(ratio_AEI_HCD- FGB_HCD_ratio_d)
            print("diff_HCD_AEI",diff_HCD_AEI)
            if (diff_FGB_AEI< 0.02 ):
                diag_diff_ratio_FGB.append(diff_FGB_AEI)
                diag_ind_ratio_FGB.append(i)
                
        if(len(diag_diff_ratio_FGB)>0) :      
            print("diag_diff_ratio_FGB",diag_diff_ratio_FGB)
            min_diagnal_ratio = np.min(diag_diff_ratio_FGB)
            min_diagonal_index = np.argmin(diag_diff_ratio_FGB)
            
            min_index_d = diag_ind_ratio_FGB[min_diagonal_index]+1
         
        ##########################END Of Diagnal###############
        
        ############Start of cross Diagnal#######################
        
        sum_dark_FHA_c = darkpixF+darkpixH+darkpixA
        print("sum_dark_FHA_c",sum_dark_FHA_c)
        
        sum_dark_GCE_c = darkpixG+darkpixC+darkpixE
        print("sum_dark_GCE_c",sum_dark_GCE_c)
        
        FHA_GCE_ratio_c = sum_dark_FHA_c/sum_dark_GCE_c
        print("FHA_GCE_ratio_c",FHA_GCE_ratio_c)
        
        diag_diff_ratio_FHA = []
        diag_ind_ratio_FHA = []
        
        for i, element in enumerate(darkpix_res):
            sum_dark_BDI_c = darkpixB+darkpixD+darkpix_res[i]
            ratio_BDI_FHA = sum_dark_BDI_c/sum_dark_FHA_c
            ratio_BDI_GCE = sum_dark_BDI_c/sum_dark_GCE_c
            
            diff_FHA_BDI =  abs(ratio_BDI_FHA - FHA_GCE_ratio_c)
            print("diff_FHA_BDI",diff_FHA_BDI)
            diff_GCE_BDI = abs(ratio_BDI_GCE- FHA_GCE_ratio_c)
            print("diff_GCE_BDI",diff_GCE_BDI)
            if (diff_FHA_BDI< 0.02 ):
                diag_diff_ratio_FHA.append(diff_FHA_BDI)
                diag_ind_ratio_FHA.append(i)
                
        if(len(diag_diff_ratio_FHA)>0) :      
            print("diag_diff_ratio_FHA",diag_diff_ratio_FHA)
            min_diagnal_ratio_c = np.min(diag_diff_ratio_FHA)
            min_diagonal_index_c = np.argmin(diag_diff_ratio_FHA)
            
            min_index_c = diag_ind_ratio_FHA[min_diagonal_index_c]+1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #############################End of cross diagnal###################
        
        
    
        
        if (len(hor_diff_ratio_ABC)>0):
            print("first")
            
            r = min_index_h
            return r
        
        elif (len(vertical_diff_ratio_ADG)>0):
            print("second")
            r = min_index_v
            return r
        elif (len(diag_diff_ratio_FGB)>0):
            print("third")
            r = min_index_d
            return r
        
        elif (len(diag_diff_ratio_FHA)>0):
            print("fourth")
            r = min_index_c
            return r
        
        else :
            r = -1
            return r
            
        
        
        """
        
        ##############Vertical sum of standard deviation##############
        std_dark_ADG_v = pixA.std()+pixD.std()+pixG.std()
        print("std_dark_ADG_v",std_dark_ADG_v)
        #sum_all_v = pixA.size+pixD.size+pixG.size
        #all_ratio_ADG_v = sum_dark_ADG_v/sum_all_v
        #print("all_std_ADG_v",all_ratio_ADG_v)
        
        
        std_dark_BEH_v = pixB.std()+pixE.std()+pixH.std()
        print("std_dark_BEH_v",std_dark_BEH_v)
        #sum_all_v = pixB.size+pixE.size+pixH.size
        #all_ratio_BEH_v = sum_dark_BEH_v/sum_all_v
        #print("all_ratio_BEH_v",all_ratio_BEH_v)
        
        diff_std_ADG_BEH = abs(std_dark_ADG_v-std_dark_BEH_v)
        print("diff_std_ADG_BEH",diff_std_ADG_BEH)
        
        
        dark_CFI_std_diff = []
        diff_std_ind_v =-1
        if(diff_std_ADG_BEH < 0.06):
           
            for i, element in enumerate(darkpix_res):
                    std_dark_CFI_v = pixC.std()+pixF.std()+pix_res[i].std()
                    #ratio = sum_dark_CFI_v/sum_all_v
                    diff_ADG_CFI_std = abs(std_dark_ADG_v-std_dark_CFI_v)
                    dark_CFI_std_diff.append(diff_ADG_CFI_std)
                   
            #diff_all_diff = abs(dark_CFI_ratio_diff - diff_ADG_BEH)
            print("dark_CFI_std_diff",dark_CFI_std_diff)
            diff_std_v = np.min(dark_CFI_std_diff)
            if(diff_std_v < 0.025)  :
                diff_std_ind_v  = np.argmin(dark_CFI_std_diff)+1
       
        
        print("dark_CFI_ratio_diff",dark_CFI_ratio_diff)
        print("lets see std index ",diff_std_ind_v)
      
        
        
        mini_index =-1
        ###############################################################
        
        ############Comparison#####################
        if (len(dark_CFI_std_diff)>0):
            mini_index = diff_std_ind_v
           
        
        ##############################################
        
        ###Diagnal sum of dark pixels#######
        sum_dark_CEG_d = darkpixC+darkpixE+darkpixG
        print("sum_dark_CEG_d",sum_dark_CEG_d)
        sum_all_d = pixC.size+pixE.size+pixG.size
        all_ratio_CEG_d = sum_dark_CEG_d/sum_all_d
        print("all_ratio_CEG_d",all_ratio_CEG_d)
        
        
        sum_dark_HAF_d = darkpixH+darkpixA+darkpixF
        print("sum_dark_HAF_d",sum_dark_HAF_d)
        sum_all_d = pixH.size+pixA.size+pixF.size
        all_ratio_HAF_d = sum_dark_HAF_d/sum_all_d
        print("all_ratio_HAF_d",all_ratio_HAF_d)
        
        diff_CEG_HAF = abs(all_ratio_CEG_d-all_ratio_HAF_d)
        dark_AEI_ratio_diff = []
        diff_all_ind_d =-1
        if(diff_CEG_HAF < 0.0025):
           
            for i, element in enumerate(darkpix_res):
                    sum_dark_AEI_d = darkpixA+darkpixE+darkpix_res[i]
                    ratio = sum_dark_AEI_d/sum_all_d
                    diff_CEG_AEI = abs(all_ratio_CEG_d-ratio)
                    dark_AEI_ratio_diff.append(diff_CEG_AEI)
                   
            #diff_all_diff = abs(dark_CFI_ratio_diff - diff_ADG_BEH)
            print("dark_AEI_ratio_diff",dark_AEI_ratio_diff)
            diff_all_d = np.min(dark_AEI_ratio_diff)
            if(diff_all_d < 0.005)  :
                diff_all_ind_d  = np.argmin(dark_AEI_ratio_diff)+1
       
        
        print("dark_AEI_ratio_diff",dark_AEI_ratio_diff)
        
        ###########################
       
        
        ##############diagnal sum of standard deviation##############
        std_dark_CEG_d = pixC.std()+pixE.std()+pixG.std()
        print("std_dark_CEG_d",std_dark_CEG_d)
        #sum_all_v = pixA.size+pixD.size+pixG.size
        #all_ratio_ADG_v = sum_dark_ADG_v/sum_all_v
        #print("all_std_ADG_v",all_ratio_ADG_v)
        
        
        std_dark_HAF_d = pixH.std()+pixA.std()+pixF.std()
        print("std_dark_HAF_d",std_dark_HAF_d)
        #sum_all_v = pixB.size+pixE.size+pixH.size
        #all_ratio_BEH_v = sum_dark_BEH_v/sum_all_v
        #print("all_ratio_BEH_v",all_ratio_BEH_v)
        
        diff_std_CEG_HAF = abs(std_dark_CEG_d-std_dark_HAF_d)
        print("diff_std_CEG_HAF",diff_std_CEG_HAF)
        
        
        dark_AEI_std_diff = []
        diff_std_ind_d =-1
        if(diff_std_CEG_HAF < 0.06):
           
            for i, element in enumerate(darkpix_res):
                    std_dark_AEI_d = pixA.std()+pixE.std()+pix_res[i].std()
                    #ratio = sum_dark_CFI_v/sum_all_v
                    diff_CEG_AEI_std = abs(std_dark_CEG_d-std_dark_AEI_d)
                    dark_AEI_std_diff.append(diff_CEG_AEI_std)
                   
            #diff_all_diff = abs(dark_CFI_ratio_diff - diff_ADG_BEH)
            print("dark_AEI_std_diff",dark_AEI_std_diff)
            diff_std_d = np.min(dark_AEI_std_diff)
            if(diff_std_d < 0.030)  :
                diff_std_ind_d  = np.argmin(dark_AEI_std_diff)+1
       
        
        print("dark_AEI_std_diff",dark_AEI_std_diff)
        print("lets see std index diagnal ",diff_std_ind_d)
      
        
        
        mini_index3 =-1
        ###############################################################
        
        ############Comparison#####################
        if (len(dark_AEI_std_diff)>0 ):
            mini_index3 = diff_std_ind_d
            
                
   
            
                
                
        
        ##############################################
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ##########################################################
        ###horizontal sum of dark pixels#######
        sum_dark_ABC_h = darkpixA+darkpixB+darkpixC
        print("sum_dark_ABC_h",sum_dark_ABC_h)
        sum_all_h = pixA.size+pixB.size+pixC.size
        all_ratio_ABC_h = sum_dark_ABC_h/sum_all_h
        print("all_ratio_ABC_h",all_ratio_ABC_h)
        
        
        sum_dark_DEF_h = darkpixD+darkpixE+darkpixF
        print("sum_dark_DEF_h",sum_dark_DEF_h)
        sum_all_h = pixD.size+pixE.size+pixF.size
        all_ratio_DEF_h = sum_dark_DEF_h/sum_all_h
        print("all_ratio_DEF_h",all_ratio_DEF_h)
        
        diff_ABC_DEF = abs(all_ratio_ABC_h-all_ratio_DEF_h)
        dark_GHI_ratio_diff = []
        diff_all_ind_h =-1
        if(diff_ABC_DEF < 0.002):
           
            for i, element in enumerate(darkpix_res):
                    sum_dark_GHI_h = darkpixG+darkpixH+darkpix_res[i]
                    ratio =sum_dark_GHI_h/sum_all_h
                    diff_ABC_DEF = abs(all_ratio_DEF_h-ratio)
                    dark_GHI_ratio_diff.append(diff_ABC_DEF)
                   
            #diff_all_diff = abs(dark_CFI_ratio_diff - diff_ADG_BEH)
            print("dark_GHI_ratio_diff",dark_GHI_ratio_diff)
            diff_all_h = np.min(dark_GHI_ratio_diff)
            if(diff_all_h < 0.005)  :
                diff_all_ind_h  = np.argmin(dark_GHI_ratio_diff)+1
       
        
        print("dark_GHI_ratio_diff",dark_GHI_ratio_diff)
        
        ###########################
       
        
        ##############horizontal sum of standard deviation##############
        std_dark_ABC_h = pixA.std()+pixB.std()+pixC.std()
        print("std_dark_ABC_h",std_dark_ABC_h)
        #sum_all_v = pixA.size+pixD.size+pixG.size
        #all_ratio_ADG_v = sum_dark_ADG_v/sum_all_v
        #print("all_std_ADG_v",all_ratio_ADG_v)
        
        
        std_dark_DEF_h = pixD.std()+pixE.std()+pixF.std()
        print("std_dark_DEF_h",std_dark_DEF_h)
        #sum_all_v = pixB.size+pixE.size+pixH.size
        #all_ratio_BEH_v = sum_dark_BEH_v/sum_all_v
        #print("all_ratio_BEH_v",all_ratio_BEH_v)
        
        diff_std_ABC_DEF = abs(std_dark_ABC_h-std_dark_DEF_h)
        print("diff_std_ABC_DEF",diff_std_ABC_DEF)
        
        
        dark_GHI_std_diff = []
        diff_std_ind_h =-1
        if(diff_std_ABC_DEF < 0.0030):
           
            for i, element in enumerate(darkpix_res):
                    std_dark_GHI_h = pixG.std()+pixH.std()+pix_res[i].std()
                    #ratio = sum_dark_CFI_v/sum_all_v
                    diff_ABC_DEF_std = abs(std_dark_ABC_h-std_dark_GHI_h)
                    dark_GHI_std_diff.append(diff_ABC_DEF_std)
                   
            #diff_all_diff = abs(dark_CFI_ratio_diff - diff_ADG_BEH)
            print("dark_GHI_std_diff",dark_GHI_std_diff)
            diff_std_h = np.min(dark_GHI_std_diff)
            if(diff_std_h < 0.025)  :
                diff_std_ind_h  = np.argmin(dark_GHI_std_diff)+1
       
        
        #print("dark_CFI_ratio_diff",dark_CFI_ratio_diff)
        print("lets see std index ",diff_std_ind_h)
      
        
        
        mini_index2 =-1
        ###############################################################
        
        ############Comparison#####################
        if (len(dark_GHI_std_diff)>0):
            mini_index2 = diff_std_ind_h
           
                
   
            
                
         
        
        ##############################################
            
        
        
        
            
        if(len(dark_AEI_std_diff)>0 and np.min(dark_AEI_std_diff) <0.03 ):
            r = mini_index3  
            return r
        elif(len(dark_GHI_std_diff)>0 and np.min(dark_GHI_std_diff) <0.03 ):
            r = mini_index2
            return r
        elif(len(dark_CFI_std_diff)>0 and np.min(dark_CFI_std_diff)<0.03 ):
            r = mini_index
            return r
        elif len(below_d_thres)==1 and below_d_thres[0] < 0.015:
            print("second")
            r = np.argmin(D_ratio_diff)+1
            return r
        elif (min_affine_val < 51):
            print("third")
            r = q
            return r
        elif(len(dark_CFI_std_diff)>0 and len(dark_CFI_ratio_diff)>0):
            r = mini_index
            return r
        elif(len(dark_AEI_std_diff)>0 and len(dark_AEI_ratio_diff)>0):
            r = mini_index3
            return r
        elif(diffi<0.015):
            print("seventh")
            r = ind
            return r
      
        elif(len(dark_GHI_std_diff)>0 and len(dark_GHI_ratio_diff)>0):
            r = mini_index2
            return r
            
            
        else :
            r =-1
                    
                        
            
        if(r == -1):
            r = self.crossDiagnalCheck(darkpixA, darkpixB, darkpixC, darkpixD, darkpixE, darkpixF, darkpixG, darkpixH,darkpix_res)
            imgA1 = imgA.convert('1')
            imgp1 = self.colorfill(imgA)
            imgp2 = ImageChops.logical_xor(imgA1,imgp1)
         
            img_p2 = ImageChops.invert(imgp2)
            
            #img_p2.show()
                
        else :
            r = -1
        
            
            
        return r
        """
            
            
    
     
    def crossDiagnalCheck(self,darkpixA,darkpixB,darkpixC,darkpixD,darkpixE,darkpixF,darkpixG,darkpixH,darkpix_res):
        print("I am in cross diagnal check")
        r = -1
        darkpix_HF_diff = abs(darkpixH - darkpixF)
        print("darkpix_HF",darkpix_HF_diff)
        darkpix_FA_diff = abs(darkpixF - darkpixA)
        print("darkpix_FA",darkpix_FA_diff)
        darkpix_HFA = abs(darkpix_FA_diff - darkpix_HF_diff)
        print("darkpix_HFA",darkpix_HFA)
        
        
        darkpix_CG_diff = abs(darkpixC - darkpixG)
        darkpix_GE_diff = abs(darkpixG - darkpixE)
        
        darkpix_CGE = abs(darkpix_CG_diff - darkpix_GE_diff)
        print("darkpix_CGE",darkpix_CGE)
        
        if (darkpix_CGE< 0.01 or darkpix_HFA <0.01):
            darkpix_DB_diff = abs(darkpixD - darkpixB)
            darkpixI = darkpixB - darkpix_DB_diff
            
            darkpixcross_diff = []
            
            for i, element in enumerate(darkpix_res):
                diff = abs(darkpix_res[i] - darkpixI )
                darkpixcross_diff.append(diff)
                
            print ("darkpixcross_diff",darkpixcross_diff)
            
            r = np.argmin(darkpixcross_diff)+1
                
   
            
        else :
            r = -1
            
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
        
    def matches(self,pix1, pix2):
        
        m = np.sum(np.equal(pix1, pix2).astype(int))
        return 33856-m
    
    def perMatch2(self,pix1, pix2):
        m = np.sum(np.equal(pix1, pix2, where = True).astype(int))
        #b = m/darkpixA
        #c = m/darkpixB
        #dpr = abs(b-c)
        
        return m
    
    def perMatch1(self,pix1, pix2,darkpixA,darkpixB):
        m = abs(darkpixA - darkpixB)
        b = pix1.size
        dpr = m/b
        
        return dpr

    def gP(self,img):
        img_b = img.point(lambda p: 0 if p<126 else 1)
      
        
        binary = np.asarray(img_b.getdata())
        binary ^= 1
        #print("size of binary image",bin.shape,bin.size)
        #print("gp")
        #print(max(binary))
        
        return binary
    
    def diff(self,pix1,pix2):
        return np.abs(pix2-pix1)
    
    
    
    def darkPixelAnd(self,darkpixA,darkpixB,darkpixC,pixA,pixB,pixC):
        n = abs(darkpixA - (darkpixB+darkpixC)) /pixA.size
        return n
    
    def darkPixelor(self,darkpixA,darkpixB,darkpixC,pixA,pixB,pixC):
        p = np.sum(np.equal(pixB,pixC))
        n = abs(darkpixA - (darkpixB+darkpixC -p)) /pixA.size
        return n
    
    def darkPixelNAND(self,darkpixA,darkpixB,darkpixC,pixA,pixB,pixC):
        p = np.sum(np.equal(pixB,pixC))
        n = abs(darkpixA - (darkpixB+darkpixC -2*p)) /pixA.size
        return n
        
    
   
    
    def overall_min(self,darkpixA,darkpixB,darkpixC,darkpixG,darkpixH,pixB,pixC,pixA,darkpix_res,pix_res,pixG,pixH):
        index_diff = []
        min_array_n = []
        
        #horizontal AND ABC
        n = self.darkPixelAnd(darkpixA,darkpixB,darkpixC,pixA,pixB,pixC)
        min_array_n.append(n)
        
        #horizontal AND BAC
        n = self.darkPixelAnd(darkpixB,darkpixA,darkpixC,pixA,pixB,pixC)
        min_array_n.append(n)
        
        #horizontal AND CAB
        n = self.darkPixelAnd(darkpixC,darkpixB,darkpixA,pixA,pixB,pixC)
        min_array_n.append(n)
        
        
        #horizontal OR ABC
        n = self.darkPixelor(darkpixA,darkpixB,darkpixC,pixA,pixB,pixC)
        min_array_n.append(n)
        
        #horizontal OR BAC
        n = self.darkPixelor(darkpixB,darkpixA,darkpixC,pixA,pixB,pixC)
        min_array_n.append(n)
        
        #horizontal OR CAB
        n = self.darkPixelor(darkpixC,darkpixA,darkpixB,pixA,pixB,pixC)
        min_array_n.append(n)
        
        #horizontal NAND ABC
        n = self.darkPixelNAND(darkpixA,darkpixB,darkpixC,pixA,pixB,pixC)
        min_array_n.append(n)
        #horizontal NAND BAC
        n = self.darkPixelNAND(darkpixB,darkpixA,darkpixC,pixA,pixB,pixC)
        min_array_n.append(n)
        
        #horizontal NAND CAB
        n = self.darkPixelNAND(darkpixC,darkpixA,darkpixB,pixA,pixB,pixC)
        min_array_n.append(n)
        
        print("overall min_array_n", min_array_n)
        
        n_min = np.min(min_array_n)
        n_min_index = np.argmin(min_array_n)
        
        #horizontal AND ABC
        
        if (n_min_index == 0):
            temp = []
            print("overall operation index",n_min_index )
            
            diffi1 =[]
            add_diff = []
            add_ini = []
            for i, element in enumerate(darkpix_res):
                diff = abs(darkpixG - (darkpixH+darkpix_res[i]))/pixA.size
                diffi1.append(diff)
                if diff < 0.015:
                    add_diff.append(diff)
                    add_ini.append(i)
            print("add_diff",add_diff)    
            if len(add_diff) >1:
                for  i,element in enumerate(add_diff):
                    q = np.sum(np.equal(pix_res[add_ini[i]],pixG))/pixA.size
                    temp.append(q)
                print("temp",temp)
                max_temp = np.min(temp)
                max_temp_ind = add_ini[np.argmin(temp)]+1
                
                
            elif len(add_diff )==1:
                max_temp = add_diff[0]
                max_temp_ind = add_ini[0]+1
                
            elif len(add_diff )==0:
                max_temp = 0
                max_temp_ind = 1
                
                
                
                    
            diffi = diffi1[max_temp_ind-1]    
            print("max_temp",max_temp)
            #min_add_diff = np.min(add_diff)
            #min_add_index = np.argmin(add_diff)+1
            return (n_min,diffi, max_temp_ind)
        
        #horizontal AND BAC
        elif (n_min_index == 1):
            temp = []
            print("overall operation index",n_min_index )
            add_diff = []
            add_ini = []
            diffi1 = []
            for i, element in enumerate(darkpix_res):
                diff = abs(darkpixH - (darkpixG+darkpix_res[i]))/pixA.size
                diffi1.append(diff)
                if diff < 0.015:
                    add_diff.append(diff)
                    add_ini.append(i)
            print("add_diff",add_diff)    
            if len(add_diff) >1:
                for  i,element in enumerate(add_diff):
                    q = np.sum(np.equal(pix_res[add_ini[i]],pixH))/pixA.size
                    temp.append(q)
                print("temp",temp)
                max_temp = np.max(temp)
                max_temp_ind = add_ini[np.argmax(temp)]+1
                
            elif len(add_diff )==1:
                max_temp = add_diff[0]
                max_temp_ind = add_ini[0]+1
                
            elif len(add_diff )==0:
                max_temp = 0
                max_temp_ind = 1
            
            diffi = diffi1[max_temp_ind-1]   
            return (n_min,diffi, max_temp_ind)
        
        #horizontal AND CAB
        elif (n_min_index == 2):
            temp = []
            print("overall operation index",n_min_index )
            add_diff = []
            add_ini = []
            diffi1 = []
            for i, element in enumerate(darkpix_res):
                diff = abs(darkpix_res[i] - (darkpixG+darkpixH))/pixA.size
                diffi1.append(diff)
                if diff < 0.015:
                    add_diff.append(diff)
                    add_ini.append(i)
            print("add_diff",add_diff,add_ini)    
            if len(add_diff) >1:
                for  i,element in enumerate(add_diff):
                    q = np.sum(np.equal(pix_res[add_ini[i]],pixG))/pixA.size
                    temp.append(q)
                print("temp",temp)
                max_temp = np.max(temp)
                max_temp_ind = add_ini[np.argmax(temp)]+1
                
            elif len(add_diff )==1:
                max_temp = add_diff[0]
                max_temp_ind = add_ini[0]+1
                
            elif len(add_diff )==0:
                max_temp = 0
                max_temp_ind = 1
            
            diffi = diffi1[max_temp_ind-1]   
            return (n_min,diffi,max_temp_ind)
        
        
      
        
        #horizontal OR ABC
        elif (n_min_index == 3):
            print("overall operation index",n_min_index )
            
            add_diff = []
            for i, element in enumerate(darkpix_res):
                p = np.sum(np.equal(pixH,pix_res[i]))
                diff = abs(darkpixG - (darkpixH+darkpix_res[i] - p ))/pixA.size
                add_diff.append(diff)
            
            print("add_diff",add_diff)
            min_add_diff = np.min(add_diff)
            min_add_index = np.argmin(add_diff)+1
            return (n_min,min_add_diff, min_add_index)
        
        #horizontal OR BAC
        elif (n_min_index == 4):
            print("overall operation index",n_min_index )
            
            add_diff = []
            for i, element in enumerate(darkpix_res):
                p = np.sum(np.equal(pixG,pix_res[i]))
                diff = abs(darkpixH - (darkpixG+darkpix_res[i] -p ))/pixA.size
                add_diff.append(diff)
            
            print("add_diff",add_diff)
            min_add_diff = np.min(add_diff)
            min_add_index = np.argmin(add_diff)+1
            return (n_min,min_add_diff, min_add_index)
        
        #horizontal OR CAB
        elif (n_min_index == 5):
            print("overall operation index",n_min_index )
            
            add_diff = []
            for i, element in enumerate(darkpix_res):
                p = np.sum(np.equal(pixG,pixH))
                diff = abs(darkpix_res[i] - (darkpixG+darkpixH -p ))/pixA.size
                add_diff.append(diff)
            
            print("add_diff",add_diff)
            min_add_diff = np.min(add_diff)
            min_add_index = np.argmin(add_diff)+1
            return (n_min,min_add_diff, min_add_index)
        
        
        #horizontal NAND ABC
        elif (n_min_index == 6):
            print("overall operation index",n_min_index )
            
            add_diff = []
            for i, element in enumerate(darkpix_res):
                p = np.sum(np.equal(pixH,pix_res[i]))
                diff = abs(darkpixG - (darkpixH+darkpix_res[i] -2*p ))/pixA.size
                add_diff.append(diff)
            
            print("add_diff",add_diff)
            min_add_diff = np.min(add_diff)
            min_add_index = np.argmin(add_diff)+1
            return (n_min,min_add_diff, min_add_index)
        
        #horizontal NAND BAC
        elif (n_min_index == 7):
            print("overall operation index",n_min_index )
            
            add_diff = []
            for i, element in enumerate(darkpix_res):
                p = np.sum(np.equal(pixG,pix_res[i]))
                diff = abs(darkpixH - (darkpixG+darkpix_res[i] -2*p ))/pixA.size
                add_diff.append(diff)
            
            print("add_diff",add_diff)
            min_add_diff = np.min(add_diff)
            min_add_index = np.argmin(add_diff)+1
            return (n_min,min_add_diff, min_add_index)
        
        #horizontal NAND CAB
        elif (n_min_index == 8):
            print("overall operation index",n_min_index )
            
            add_diff = []
            for i, element in enumerate(darkpix_res):
                p = np.sum(np.equal(pixG,pixH))
                diff = abs(darkpix_res[i] - (darkpixG+darkpixH - 2*p ))/pixA.size
                add_diff.append(diff)
            
            print("add_diff",add_diff)
            min_add_diff = np.min(add_diff)
            min_add_index = np.argmin(add_diff)+1
            
            
        
            return (n_min,min_add_diff, min_add_index)
        
            
        
        
        #vertical AND ADG
        #vertical AND GDA
        #vertical AND DAG
        
        #vertical OR ADG
        #vertical OR GDA
        #vertical OR DAG
        
        #vertical NAND ADG
        #vertical NAND GDA
        #vertical NAND DAG
        
        
        
        
        
        
        
        
        
         
        
        
    
        
        
        
            
            
            
        
    
    """
    if np.array_equal(pix_diff1, element) or np.array_equal(pix_diff2, element) or np.array_equal(
                     pix_diff3, element):
                r = i+1
                break
            else :
    """
        

   
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
