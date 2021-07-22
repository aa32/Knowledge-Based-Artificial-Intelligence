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
            figA_pic = figA.visualFilename
            imgA  = Image.open(figA_pic).convert('L')
        
       
            figB_pic = figB.visualFilename
            imgB  = Image.open(figB_pic).convert('L')
        
        
            figC_pic = figC.visualFilename
            imgC  = Image.open(figC_pic).convert('L')
            
            figD_pic = figD.visualFilename
            imgD  = Image.open(figD_pic).convert('L')
            
            figE_pic = figE.visualFilename
            imgE  = Image.open(figE_pic).convert('L')
            
            figF_pic = figF.visualFilename
            imgF  = Image.open(figF_pic).convert('L')
            
            figG_pic = figG.visualFilename
            imgG  = Image.open(figG_pic).convert('L')
            
            
            figH_pic = figH.visualFilename
            imgH  = Image.open(figH_pic).convert('L')
        
        
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
        
            
            r = self.pixelCompare2(imgA,imgB,imgC,imgD,imgE,imgF,imgG,imgH,img1,img2,img3,img4,img5,img6,img7,img8,imgs)
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

        #print("New Functio")
        print(r)
        return r
        
    def pixelCompare2(self, imgA,imgB,imgC,imgD,imgE,imgF,imgG,imgH,img1,img2,img3,img4,img5,img6,img7,img8,imgs):
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

        pix1 = self.gP(img1)
        pix2 = self.gP(img2)
        pix3 = self.gP(img3)
        pix4 = self.gP(img4)
        pix5 = self.gP(img5)
        pix6 = self.gP(img6)
        pix7 = self.gP(img7)
        pix8 = self.gP(img8)

        pix_res = [pix1,pix2,pix3,pix4,pix5,pix6,pix7,pix8]
        print ("A size" , pixA.size)
        print("B size",pixB.size)
        print("E Size" , pixE.size)
        print("H size" , pixH.size)
        
        print ("3 size",pix3.size)
        
        darkpixA = np.sum(pixA)
        print("Dark pixels in A" ,darkpixA )
        darkpixB = np.sum(pixB)
        print("Dark pixels in B" ,darkpixB )
        darkpixC = np.sum(pixC)
        print("Dark pixels in C" ,darkpixC )
        darkpixD = np.sum(pixD)
        print("Dark pixels in D" ,darkpixD )
        darkpixE = np.sum(pixE)
        print("Dark pixels in E" ,darkpixE )
        darkpixF = np.sum(pixF)
        print("Dark pixels in F" ,darkpixF )
        darkpixG = np.sum(pixG)
        print("Dark pixels in G" ,darkpixG )
        darkpixH = np.sum(pixH)
        print("Dark pixels in H" ,darkpixH )
        
        darkpix_res = []
        
        darkpix_res.append(np.sum(pix1))
        darkpix_res.append(np.sum(pix2))
        darkpix_res.append(np.sum(pix3))
        darkpix_res.append(np.sum(pix4))
        darkpix_res.append(np.sum(pix5))
        darkpix_res.append(np.sum(pix6))
        darkpix_res.append(np.sum(pix7))
        darkpix_res.append(np.sum(pix8))
        print ("dark pixels" , darkpix_res)
         
        
    
        
        #BA_ratio  = darkpixB/float(darkpixA)
        #print ("B to A ratio",BA_ratio)
        
    
        CB_ratio  = darkpixC/float(darkpixB)
        #print ("C to B ratio",CB_ratio)
        
        ED_ratio  = darkpixE/float(darkpixD)
        #print ("E to D ratio",ED_ratio)
        
        FE_ratio  = darkpixF/float(darkpixE)
        #print ("F to E ratio",FE_ratio)
        
        HG_ratio  = darkpixH/float(darkpixG)
        #print ("H to G ratio",HG_ratio)
        
        
        

        
        H_Ratio_Results = []
        #Horizontal Result Ratios:
        for i, element in enumerate(darkpix_res):
            IH_ratio = np.sum(darkpix_res[i]/float(darkpixH))
            #print("I to H ratio", IH_ratio)
        
            
            H_Ratio_Results.append(IH_ratio)
        
        print("H_Ratio_Results",H_Ratio_Results)
        
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
        
        #print("darkpix_ACDF",darkpix_ACDF)
        
        if len(above_h_thres)==1 :     
            r = np.argmin(H_ratio_diff)+1
        elif(len(above_h_thres)> 1 and (darkpixdiff_AC >100 or darkpixdiff_DF>100)):
            darkpixdiff_AC = abs(darkpixA-darkpixC)
            if (darkpixA<darkpixC):
                darkpixI = darkpixG + darkpixdiff_AC
            else:
                darkpixI = darkpixG - darkpixdiff_AC
            
            darkpixdiff = []
            for i, element in enumerate(darkpix_res):
                darkpixdiff_I = abs(darkpixI-darkpix_res[i])
                darkpixdiff.append(darkpixdiff_I)
                    
            
            if(np.min(darkpixdiff)< 65):    
                r = np.argmin(darkpixdiff)+1
            
            elif(np.min(darkpixdiff)> 65):
                print("Are you in here hello")
                p = darkpixG - 2*(darkpixD-darkpixA)
                print("Is it somethnig like B-08",p)
                darkpixratio_AC = darkpixA/float(darkpixC)
                darkpixratio = []
                for i, element in enumerate(darkpix_res):
                    darkpixratio_I = darkpixG/float(darkpix_res[i])
                    darkpixratio.append(darkpixratio_I)
                
                ratiodiff = []
                
                for i, element in enumerate(darkpix_res):
                    m = abs(darkpixratio_AC -darkpixratio[i])
                    ratiodiff.append(m)
                
                print ("lets see ratio diff",ratiodiff)
                
                if (np.min(ratiodiff)<0.009):
                        r = np.argmin(ratiodiff)+1
                elif(np.min(ratiodiff)>0.009):
                    #print("inside ipr")
                    for i in above_thres_index:
                        p = self.perMatch2(pixH,pix_res[i])
                        print ("no. of matches",p)
                        ipr_p.append(p)
                    if(darkpixB > darkpixC):
                        q = np.argmax(ipr_p)
                    else:
                        q = np.argmin(ipr_p)
                
                    index = above_thres_index[q]
                    r = index+1
                elif(p< 0.008):
                        input_image1 = imgH
                        input_pix1 = input_image1.load()
                        output_image1 = Image.new("L", input_image1.size)
                        draw1 = ImageDraw.Draw(output_image1)
                        a = int(output_image1.width/2)
                        # Copy pixels
                        for x in range(a+1):
                            for y in range(output_image1.height):
                                xp = a + x - 1
                                draw1.point((x, y), input_pix1[xp, y])
                        for x in range(a-1,output_image1.width):
                            for y in range(output_image1.height):
                                #xp = a + x - 1
                                draw1.point((x, y), input_pix1[x, y])
                    
                    
                        output_image1.save("output.png")
                        pixI1 = self.gP(output_image1)
                        comp =[]
                        comp =[]
                        for i, element in enumerate(pix_res):
                            p = pix_res[i]
                            print("shape" ,p.shape)
                            a = int(p.size/4.0)
                            #b = int(imgs[i].width/2.0)
                            print("dark pixels in first quadrant",a, np.sum(p[:a]))
                            
                            if (np.sum(p[:a])>400):
                                m = self.img_diff(output_image1,imgs[i])
                            else:
                                m = 50
                            comp.append(m)
                    
                        print("comp",comp)
                        r = np.argmin(comp)+1
                else :
                    r =-1
                    
                        
                    
                    
                    
                        
        
                       
                    
                
                        
                
            
            
            
            
        elif(len(above_h_thres)> 1 and darkpixdiff_AC <100 and darkpixdiff_DF<100):
            # Create output image
            input_image1 = imgA
            input_pix1 = input_image1.load()
            output_image1 = Image.new("L", input_image1.size)
            draw1 = ImageDraw.Draw(output_image1)
            b = int(output_image1.width/2)
            # Copy pixels
            for x in range(b):
                for y in range(output_image1.height):
                    xq = b - x - 1
                    draw1.point((x, y), input_pix1[xq, y])
                    
            for x in range(b,output_image1.width):
                for y in range(output_image1.height):
                    xq = input_image1.width - (x-b) - 1
                    draw1.point((x, y), input_pix1[xq, y])
            
            pixI1 = self.gP(output_image1)
            equalpixelcount_I1C = np.sum(np.equal(pixI1, pixC).astype(int))/pixA.size
            print ("Equal pixel count I1C" , equalpixelcount_I1C)
            
            
            # Copy pixels
            for x in range(b):
                for y in range(output_image1.height):
                    xq = b - x - 1
                    draw1.point((x, y), input_pix1[xq, y])
                    
            for x in range(b,output_image1.width):
                for y in range(output_image1.height):
                    xq = input_image1.width - (x-b) - 1
                    draw1.point((x, y), input_pix1[xq, y])
            
            pixI1 = self.gP(output_image1)
            equalpixelcount_I1C = np.sum(np.equal(pixI1, pixC).astype(int))/pixA.size
            print ("Equal pixel count I1C" , equalpixelcount_I1C)
            
            
            
            
            
            if (equalpixelcount_I1C >0.899):
                input_image = imgG
                input_pix = input_image.load()
                output_image = Image.new("L", input_image.size)
                draw = ImageDraw.Draw(output_image)
                
                equalpixelcount_AC = np.sum(np.equal(pixA, pixC).astype(int))/pixA.size
                equalpixelcount_DF = np.sum(np.equal(pixD, pixF).astype(int))/pixD.size
                
                print ("Equal pixel count AC" , equalpixelcount_AC)
                print ("Equal pixel count DF" ,  equalpixelcount_DF)
               
                
                
                a = int(output_image.width/2)
                # Copy pixels
                for x in range(a):
                    for y in range(output_image.height):
                        xp = a - x - 1
                        draw.point((x, y), input_pix[xp, y])
                        
                for x in range(a,output_image.width):
                    for y in range(output_image.height):
                        xp = input_image.width - (x-a) - 1
                        draw.point((x, y), input_pix[xp, y])
                
                #output_image.save("output.png")
    
                pixI = self.gP(output_image)
                comp =[]
                for i, element in enumerate(pix_res):
                    m = np.sum(np.equal(pix_res[i], pixI).astype(int))
                    comp.append(m)
                    
                print("comp",comp)
                r = np.argmax(comp)+1
            elif(equalpixelcount_I1C < 0.889):
                img_flipLRA = self.flip_L_R(imgA)
                pixLRA = self.gP(img_flipLRA)
                equalpixelcount_LRCA = np.sum(np.equal(pixLRA, pixC).astype(int))/pixA.size
                
                img_flipTBA = self.flip_T_B(imgA)
                pixTBA = self.gP(img_flipTBA)
                equalpixelcount_TBCA = np.sum(np.equal(pixTBA, pixC).astype(int))/pixA.size
                
                print ("equalpixelcount_LRC",equalpixelcount_LRCA)
                print("equalpixelcount_TBC",equalpixelcount_TBCA)
                
                if (equalpixelcount_LRCA > 0.9):
                    img_flipLRG = self.flip_L_R(imgG)
                    pixLRG = self.gP(img_flipLRG)
                    comp =[]
                    for i, element in enumerate(pix_res):
                        m = np.sum(np.equal(pix_res[i], pixLRG).astype(int))
                        comp.append(m)
                    
                    print("compLR",comp)
                    r = np.argmax(comp)+1
                    
                 
                elif (equalpixelcount_TBC > 0.9):
                    img_flipTBG = self.flip_T_B(imgG)
                    pixTBG = self.gP(img_flipLRG)
                    comp =[]
                    for i, element in enumerate(pix_res):
                        m = np.sum(np.equal(pix_res[i], pixTBG).astype(int))
                        comp.append(m)
                    
                    print("compTB",comp)
                    r = np.argmax(comp)+1
                    
                
                

            
            else :
                r = -1
            
            
            
            
            
            
            
            
            
            
        elif(len(above_h_thres)== 0 or  above_h_thres is None ):
            #check diagnal similarity
            diff_diagnal = abs(darkpixA - darkpixE)
            print("A and E diagnal diff", diff_diagnal)
            if diff_diagnal < 10:
                diff_diag = []
                diag_index = []
                diag_samepix =[]
                for i, element in enumerate(darkpix_res):
                    s = abs(darkpixE - darkpix_res[i])
                    print("difference",s)
                    if(abs(s-diff_diagnal)<40):
                        diff_diag.append(s)
                        diag_index.append(i)
                        
                print("diagnal difference",diff_diag)   
                if (len(diff_diag) ==1):
                    r = np.argmin(diff_diag)+1
                elif(len(diff_diag) >1):
                    print("diff diag")
                    for i, element in enumerate(diag_index):
                        a = pix_res[element]
                        t = np.sum(np.equal(a,pixH).astype(int))

                        diag_samepix.append(t)
                    
                    print("diag_samepix", diag_samepix)
                    u = np.argmax(diag_samepix)
                    r = diag_index[u]+1
            elif(diff_diagnal > 10):
                print("I am here")
                darkpixdiff_AC = abs(darkpixA-darkpixC)
                print("darkpixdiff_AC",darkpixdiff_AC)
                if (darkpixA<darkpixC):
                    darkpixI = darkpixG + darkpixdiff_AC
                else:
                    darkpixI = darkpixG - darkpixdiff_AC
                    
            
                darkpixdiff = []
                for i, element in enumerate(darkpix_res):
                    darkpixdiff_I = abs(darkpixI-darkpix_res[i])
                    darkpixdiff.append(darkpixdiff_I)
                    
                print ("darkpixdiff",darkpixdiff)
                if (np.min(darkpixdiff)<65):
                    r = np.argmin(darkpixdiff)+1
                elif(np.min(darkpixdiff)>65):
                    print("Are you in here")
                    p = darkpixG - 2*(darkpixD-darkpixA)
                    genF = np.bitwise_or(pixC,pixE)
                    diff_or = np.sum(np.equal(genF,pixF).astype(int))/33856.0
                    print("diff_or" , diff_or)
                    print("Is it somethnig like B-08",p)
                    darkpixratio_AC = darkpixA/float(darkpixC)
                    darkpixratio = []
                    for i, element in enumerate(darkpix_res):
                        darkpixratio_I = darkpixG/float(darkpix_res[i])
                        darkpixratio.append(darkpixratio_I)
                
                    ratiodiff = []
                
                    for i, element in enumerate(darkpix_res):
                        m = abs(darkpixratio_AC -darkpixratio[i])
                        ratiodiff.append(m)
                
                    print ("lets see ratio diff",ratiodiff)
                    
                    if (np.min(ratiodiff)<0.009):
                        r = np.argmin(ratiodiff)+1
                        
                    elif(p< 0.008):
                        input_image1 = imgH
                        input_pix1 = input_image1.load()
                        output_image1 = Image.new("L", input_image1.size)
                        draw1 = ImageDraw.Draw(output_image1)
                        a = int(output_image1.width/2)
                        # Copy pixels
                        for x in range(a+1):
                            for y in range(output_image1.height):
                                xp = a + x - 1
                                draw1.point((x, y), input_pix1[xp, y])
                        for x in range(a-1,output_image1.width):
                            for y in range(output_image1.height):
                                #xp = a + x - 1
                                draw1.point((x, y), input_pix1[x, y])
                    
                    
                        output_image1.save("output.png")
                        pixI1 = self.gP(output_image1)
                        comp =[]
                        comp =[]
                        for i, element in enumerate(pix_res):
                            p = pix_res[i]
                            print("shape" ,p.shape)
                            a = int(p.size/4.0)
                            #b = int(imgs[i].width/2.0)
                            print("dark pixels in first quadrant",a, np.sum(p[:a]))
                            
                            if (np.sum(p[:a])>400):
                                m = self.img_diff(output_image1,imgs[i])
                            else:
                                m = 50
                            comp.append(m)
                    
                        print("comp",comp)
                        r = np.argmin(comp)+1
                    elif(diff_or > 0.97):
                        comp = []
                        genI = np.bitwise_or(pixF,pixH).astype(int)
                        for i, element in enumerate(pix_res):
                            diff_or = np.sum(np.equal(pix_res[i],genI).astype(int))
                            comp.append(diff_or)
                            
                        print("comp",comp)
                        r = np.argmax(comp)+1
                        
                            
                        
                    else:
                        r = -1
                
                
                        
            else :
                r = -1
                    
                
      
        else:
            r = -1
            
            
        """
            
        if(r == -1):
            print("inside dpr")
            dpr1 = self.perMatch2(pixE,pixF,darkpixE,darkpixF)
            print("dpr1",dpr1)
            
            dpr2 = []
            
            for i, element in enumerate(pix_res):
                dpr = self.perMatch2(pixH,pix_res[i],darkpixH,darkpix_res[i])
                dpr2.append(dpr)
                
            dpr_diff = []
            
            for i, element in enumerate(pix_res):
                diff = abs(dpr1-dpr2[i])
                dpr_diff.append(diff)
                
            print ("dpr difference",dpr_diff)
            
            r = np.argmin(dpr_diff)+1
            
            
        """
    
            
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
    
    
    """
    if np.array_equal(pix_diff1, element) or np.array_equal(pix_diff2, element) or np.array_equal(
                     pix_diff3, element):
                r = i+1
                break
            else :
    """
        

   
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        