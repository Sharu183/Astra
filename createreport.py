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
import convertcmdwrd11
import convertcmdwrd12
import convertcmdwrd13
import convertcmdwrd14
import convertcmdwrd15
import convertcmdwrd16
import convertcmdwrd17
import convertcmdwrd18
import convertcmdwrd19
import convertcmdwrd20
import convertcmdwrd21
import convertcmdwrd22
import convertcmdwrd23
def report(list,commandword):
        file=open("data//report_"+str(commandword)+".dat","w+")
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
                elif (commandword == "4420"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd6.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd6.convertword(count, temp)) + "   "))
                elif (commandword == "5420"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd7.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd7.convertword(count, temp)) + "   "))
                elif (commandword == "3C20"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd8.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd8.convertword(count, temp)) + "   "))
                elif (commandword == "4C20"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd9.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd9.convertword(count, temp)) + "   "))
                elif (commandword == "38E5"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd10.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd10.convertword(count, temp)) + "   "))
                elif (commandword == "40E5"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd11.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd11.convertword(count, temp)) + "   "))
                elif (commandword == "48E5"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd12.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd12.convertword(count, temp)) + "   "))
                elif (commandword == "50E5"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd13.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd13.convertword(count, temp)) + "   "))
                elif (commandword == "F8C0"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd14.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd14.convertword(count, temp)) + "   "))
                elif (commandword == "3C40"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd15.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd15.convertword(count, temp)) + "   "))
                 elif (commandword == "4440"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd16.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd16.convertword(count, temp)) + "   "))
                elif (commandword == "4C40"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd17.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd17.convertword(count, temp)) + "   "))
                elif (commandword == "5440"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd18.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd18.convertword(count, temp)) + "   "))
                elif (commandword == "3C65"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd19.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd19.convertword(count, temp)) + "   "))
                elif (commandword == "4465"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd20.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd20.convertword(count, temp)) + "   "))
                  elif (commandword == "4C65"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd21.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd21.convertword(count, temp)) + "   "))
                elif (commandword == "5465"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd22.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd22.convertword(count, temp)) + "   "))
                elif (commandword == "5204"):
                    if (count != 0):
                        file.write(("%0s" % str(convertcmdwrd23.convertword(count, temp)) + "   "))
                    else:
                        file.write(("%20s" % str(convertcmdwrd23.convertword(count, temp)) + "   "))
        print(count)
