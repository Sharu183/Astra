import convertcmdwrd1_3
import convertcmdwrd2_3
import convertcmdwrd3_3
import convertcmdwrd4_3
import convertcmdwrd5_3
import convertcmdwrd6_3
import convertcmdwrd7_3
import convertcmdwrd8_3
import convertcmdwrd9_3
import convertcmdwrd10_3
def report(list,commandword):
        file=open("data3//report_"+str(commandword)+".dat","w+")
        count=0
        for temp in list:
            if str(commandword) in temp:
                file.write("\n")
                count=0
                pass
            else:
                count=count+1
                if(commandword=="F820"):
                    if(count!=0):
                        file.write(("%0s"%str(convertcmdwrd1_3.convertword(count,temp))+"   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd1_3.convertword(count, temp)) + "   "))
                elif(commandword=="F840"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd2_3.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd2_3.convertword(count, temp)) + "   "))
                elif (commandword == "F860"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd3_3.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd3_3.convertword(count, temp)) + "   "))
                elif (commandword == "F880"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd4_3.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd4_3.convertword(count, temp)) + "   "))
                elif (commandword == "F8A0"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd5_3.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd5_3.convertword(count, temp)) + "   "))
                elif (commandword == "F8C0"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd6_3.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd6_3.convertword(count, temp)) + "   "))
                elif (commandword == "F8E0"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd7_3.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd7_3.convertword(count, temp)) + "   "))
                elif (commandword == "F8F0"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd8_3.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd8_3.convertword(count, temp)) + "   "))
                elif (commandword == "F800"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd9_3.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd9_3.convertword(count, temp)) + "   "))
                elif (commandword == "F810"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd10_3.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd10_3.convertword(count, temp)) + "   "))
                
        print(count)
