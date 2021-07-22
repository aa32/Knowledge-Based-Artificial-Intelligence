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
        if (problem.problemType == '2x2'):
            print(problem.name)
            #a = problem.problemSetName
            #b = problem.name
            figA = problem.figures["A"]
            figB = problem.figures["B"]
            figC = problem.figures["C"]
            fig1 = problem.figures["1"]
            fig2 = problem.figures["2"]
            fig3 = problem.figures["3"]
            fig4 = problem.figures["4"]
            fig5 = problem.figures["5"]
            fig6 = problem.figures["6"]
            
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
            
            if (nA > nB):
                p = nA-nB
                res = nC-p
                for i in range(0,len(n)):
                    if n[i]==res:
                        break
            
                print (i)
                return (i+1)
   
            elif (nA==1 and nB==1 and nC==1 and sideA!=sideB and sideA!=0 and sideB!=0):
                
                if (sideA>sideB):
                    p = sideA-sideB
                    sideD = sideC-p
                elif(sideA <sideB):
                    p = sideB-sideA
                    sideD = sideC+p
                    
                for i in range(0,len(sides)):
                    if sideD==sides[i]:
                        break
            
                print (i)
                return (i+1)
                    
                    
        
            
            #visual starts here
            else :
                figA_pic = figA.visualFilename
                imgA  = Image.open(figA_pic).convert('LA')
            
           
                figB_pic = figB.visualFilename
                imgB  = Image.open(figB_pic).convert('LA')
            
            
                figC_pic = figC.visualFilename
                imgC  = Image.open(figC_pic).convert('LA')
            
            
                fig1_pic = fig1.visualFilename
                img1  = Image.open(fig1_pic).convert('LA')
            
            
                fig2_pic = fig2.visualFilename
                img2  = Image.open(fig2_pic).convert('LA')
            
            
                fig3_pic = fig3.visualFilename
                img3  = Image.open(fig3_pic).convert('LA')
            
           
                fig4_pic = fig4.visualFilename
                img4  = Image.open(fig4_pic).convert('LA')
            
            
                fig5_pic = fig5.visualFilename
                img5  = Image.open(fig5_pic).convert('LA')
            
            
                fig6_pic = fig6.visualFilename
                img6  = Image.open(fig6_pic).convert('LA')
            
            
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
            
            
            
                A_C["IdentityT"]= self.img_diff(AT,imgC)
                A_C["Rotate90"]= self.img_diff(A90,imgC)
                A_C["Rotate180"] = self.img_diff(A180,imgC)
                A_C["Rotate270"] = self.img_diff(A270,imgC)
                A_C["flip_L_R"] = self.img_diff(AflipLR,imgC)
                A_C["flip_T_B"] = self.img_diff(AflipTB,imgC)
            
                A_C["Rotate45"] = self.img_diff(A45,imgC)
                A_C["colorfill"] = self.img_diff(ACF,imgC)
            
                print("Lets see the dictionaries")
                #print (A_B)
                #print(A_C)
            
                B_Min  = min(A_B.values()) 
                keysB = [key for key in A_B if A_B[key] == B_Min]

                C_Min  = min(A_C.values()) 
                keysC = [key for key in A_C if A_C[key] == C_Min]
            
                if( B_Min < C_Min):
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
            
                #imgD.show()
            
                res["1"] = self.img_diff(imgD,img1)
                res["2"] = self.img_diff(imgD,img2)
                res["3"] = self.img_diff(imgD,img3)
                res["4"] = self.img_diff(imgD,img4)
                res["5"] = self.img_diff(imgD,img5)
                res["6"] = self.img_diff(imgD,img6)
            
            
                res_min  = min(res.values()) 
                res_key = [key for key in res if res[key] == res_min][0]
            
                i = int(res_key)
            
                return i
        
        else:
            return -1
                
                
            
       
        
        
        
        
        
        
        
    
            
                
                
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            """
            figA_pic = figA.visualFilename
            imgA  = Image.open(figA_pic).convert('LA')
            
           
            figB_pic = figB.visualFilename
            imgB  = Image.open(figB_pic).convert('LA')
            
            
            figC_pic = figC.visualFilename
            imgC  = Image.open(figC_pic).convert('LA')
            
            
            fig1_pic = fig1.visualFilename
            img1  = Image.open(fig1_pic).convert('LA')
            
            
            fig2_pic = fig2.visualFilename
            img2  = Image.open(fig2_pic).convert('LA')
            
            
            fig3_pic = fig3.visualFilename
            img3  = Image.open(fig3_pic).convert('LA')
            
           
            fig4_pic = fig4.visualFilename
            img4  = Image.open(fig4_pic).convert('LA')
            
            
            fig5_pic = fig5.visualFilename
            img5  = Image.open(fig5_pic).convert('LA')
            
            
            fig6_pic = fig6.visualFilename
            img6  = Image.open(fig6_pic).convert('LA')
            
            
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
            
            
            
            A_C["IdentityT"]= self.img_diff(AT,imgC)
            A_C["Rotate90"]= self.img_diff(A90,imgC)
            A_C["Rotate180"] = self.img_diff(A180,imgC)
            A_C["Rotate270"] = self.img_diff(A270,imgC)
            A_C["flip_L_R"] = self.img_diff(AflipLR,imgC)
            A_C["flip_T_B"] = self.img_diff(AflipTB,imgC)
            
            A_C["Rotate45"] = self.img_diff(A45,imgC)
            A_C["colorfill"] = self.img_diff(ACF,imgC)
            
            print("Lets see the dictionaries")
            #print (A_B)
            #print(A_C)
            
            B_Min  = min(A_B.values()) 
            keysB = [key for key in A_B if A_B[key] == B_Min]

                
            
           
            
            C_Min  = min(A_C.values()) 
            keysC = [key for key in A_C if A_C[key] == C_Min]
            
                
            
            if( B_Min < C_Min):
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
            
            imgD.show()
            
            res["1"] = self.img_diff(imgD,img1)
            res["2"] = self.img_diff(imgD,img2)
            res["3"] = self.img_diff(imgD,img3)
            res["4"] = self.img_diff(imgD,img4)
            res["5"] = self.img_diff(imgD,img5)
            res["6"] = self.img_diff(imgD,img6)
            
            
            res_min  = min(res.values()) 
            res_key = [key for key in res if res[key] == res_min][0]
            
            i = int(res_key)
            
            return i
        
        else:
            return -1
            """
        
        
        
        
        
        
    
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
        
            
            
            
        
    
    """
    def Rotate45(self,img):
        img_r = img.rotate(45,expand = True)
        return img_r
    """
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
        img_p = img_r.convert('LA')
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
        img_p=img_r.convert('LA')
        #img_p.show()
        return img_p
    # End Referenced Code
        
        
       

    
    """  
    def SSIM(self,img1,img2):
        sim = compare_ssim(img1,img2)
        return sim
        

    def MSE(self,img1,img2):
        ms = compare_mse(img1,img2)
        return ms
        
    """
    
    def img_diff(self,img1,img2):

        if (img1.mode != img2.mode) or (img1.size != img2.size) or (img1.getbands() != img2.getbands()):
            return None

        # Generate diff image in memory.
        diff_img = ImageChops.difference(img1, img2)
        
        # Calculate difference as a ratio.
        stat = ImageStat.Stat(diff_img)
        print(stat.mean[0])
        return stat.mean[0]
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        