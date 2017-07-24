import convertcmdwrd1_2
import convertcmdwrd2_2
import convertcmdwrd3_2
import convertcmdwrd4_2
import convertcmdwrd5_2
import convertcmdwrd6_2
import convertcmdwrd7_2
import convertcmdwrd8_2
import convertcmdwrd9_2
import convertcmdwrd10_2
def report(list,commandword):
        file=open("data2//report_"+str(commandword)+".dat","w+")
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
                        file.write(("%0s"%str(convertcmdwrd1_2.convertword(count,temp))+"   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd1_2.convertword(count, temp)) + "   "))
                elif(commandword=="F840"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd2_2.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd2_2.convertword(count, temp)) + "   "))
                elif (commandword == "F860"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd3_2.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd3_2.convertword(count, temp)) + "   "))
                elif (commandword == "F880"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd4_2.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd4_2.convertword(count, temp)) + "   "))
                elif (commandword == "F8A0"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd5_2.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd5_2.convertword(count, temp)) + "   "))
                elif (commandword == "F8C0"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd6_2.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd6_2.convertword(count, temp)) + "   "))
                elif (commandword == "4652"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd7_2.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd7_2.convertword(count, temp)) + "   "))
                elif (commandword == "46453"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd8_2.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd8_2.convertword(count, temp)) + "   "))
                elif (commandword == "4654"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd9_2.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd9_2.convertword(count, temp)) + "   "))
                elif (commandword == "4655"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd10_2.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd10.convertword(count, temp)) + "   "))

        print(count)
