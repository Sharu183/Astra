import convertcmdwrd1
import convertcmdwrd2
import convertcmdwrd3
import convertcmdwrd4
import convertcmdwrd5
import convertcmdwrd6
import convertcmdwrd7
import convertcmdwrd8
import convertcmdwrd9
import convertcmdwrd10
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
                        file.write(("%0s"%str(convertcmdwrd1.convertword(count,temp))+"   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd1.convertword(count, temp)) + "   "))
                elif(commandword=="F840"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd2.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd2.convertword(count, temp)) + "   "))
                elif (commandword == "F860"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd3.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd3.convertword(count, temp)) + "   "))
                elif (commandword == "F880"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd4.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd4.convertword(count, temp)) + "   "))
                elif (commandword == "F8A0"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd5.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd5.convertword(count, temp)) + "   "))
                elif (commandword == "F8C0"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd6.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd6.convertword(count, temp)) + "   "))
                elif (commandword == "F8E0"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd7.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd7.convertword(count, temp)) + "   "))
                elif (commandword == "F8F0"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd8.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd8.convertword(count, temp)) + "   "))
                elif (commandword == "F800"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd9.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd9.convertword(count, temp)) + "   "))
                elif (commandword == "F810"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd10.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd10.convertword(count, temp)) + "   "))
                
        print(count)
