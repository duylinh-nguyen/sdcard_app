# """
# This script for editting configuration files before run build command.
# """
import os
import time
import vals

def config_topic(filename, content, broker, isGW_WS = False):
    """This function changes MQTT configuration following configuration content received 

    Args:
        filename ([type]): path to config file
        content ([type]): config content received
        broker ([type]): MQTT broker.
        isGW_WS (bool, optional): is configuring for GateWay, Weather Station. Defaults to False.

    Returns:
        0: If no error occurs
    """
    # if isGW_WS then QC broker is BROKER_DEMO, not BROKER_TEST anymore
    BROKER = ""
    CLIENT_ID_1 = ""
    CLIENT_ID_2 = ""
    TOPIC_SUBSCRIBE = ""
    TOPIC_MONITOR = ""
    TOPIC_SMS = ""

    valid_count = 0
    string_list = content.split('\n')
    for i in range(len(string_list)):
        
        x = string_list[i].split()
        
        if (len(x) == 0):
            continue
        if (x[0]=="#define"):

            # count number of #define line
            valid_count +=1
            # check if any argument is defined
            if (x[1]== "CLIENT_ID_1"):
                CLIENT_ID_1 = x[2]
            elif x[1]== "CLIENT_ID_2":
                CLIENT_ID_2 = x[2]
            elif x[1]== "TOPIC_SUBSCRIBE":
                TOPIC_SUBSCRIBE = x[2]
            elif x[1]== "TOPIC_MONITOR":
                TOPIC_MONITOR = x[2]
            elif x[1]== "TOPIC_SMS":
                TOPIC_SMS = x[2]
        
    # Validate content format
    if (valid_count ==  0):
        return -1

    # Guarantee file exists
    try:
        my_file = open(filename)
    except OSError:
        return -2
    line_list = my_file.readlines()

    my_file.close()

    for i in range(len(line_list)):
        x = line_list[i].split()
        if (len(x) == 0):
            continue
        if (x[0]=="#define"):

            if (x[1]== "BROKER_TEST") or (x[1]== "BROKER_APP") or (x[1]== "BROKER_DEMO") or (x[1]== "BROKER_MGREEN"):

                #Change conditions after topics name

                if (broker == "demo"):
                    BROKER = "BROKER_DEMO"
                elif (broker == "test"):
                    BROKER = "BROKER_TEST"
                elif (broker == "app"):
                    BROKER = "BROKER_APP"
                else:
                    print("[Error]Cannot define broker")
                mark = "\t//Auto edit from this line...\n"
                print("-->#define\t" + BROKER)
                line_list[i] = "#define\t" + BROKER + mark

            elif (x[1]== "CLIENT_ID_1"):
                line_list[i] = "#define\t" + "CLIENT_ID_1\t\t" +CLIENT_ID_1+ "\n"
                print("-->#define\t" + CLIENT_ID_1)
                vals.edited_content += line_list[i]

            elif x[1]== "CLIENT_ID_2":
                line_list[i] = "#define\t" + "CLIENT_ID_2\t\t" +CLIENT_ID_2 + "\n"
                vals.edited_content += line_list[i]

            elif x[1]== "TOPIC_SUBSCRIBE":
                line_list[i] = "#define\t" + "TOPIC_SUBSCRIBE\t\t" +TOPIC_SUBSCRIBE+ "\n"
                vals.edited_content += line_list[i]

            elif x[1]== "TOPIC_MONITOR":
                line_list[i] = "#define\t" + "TOPIC_MONITOR\t\t" +TOPIC_MONITOR+ "\n"
                vals.edited_content += line_list[i]

            elif x[1]== "TOPIC_SMS":
                line_list[i] = "#define\t" + "TOPIC_SMS\t\t" +TOPIC_SMS+ "\n"
                vals.edited_content += line_list[i]


    my_file = open(filename, "w")
    new_file_contents = "".join(line_list)
    my_file.write(new_file_contents)
    my_file.close()

    return 0 

def config_hardware(filename, content, GW_mode):
    """This function for defining hardware peripherals used 

    Args:
        filename ([string]): Name or path to config file
        content ([string]): Config content, define which hardware peripheral is used
        GW_mode ([string]): Gateway mode (gateway or weather station). Only used for GW/WS.

    Returns:
        0: If there was 0 error
    """
    # if isGW_WS then QC broker is BROKER_DEMO, not BROKER_TEST anymore

    NODE_ID = ""
    CHARGER_TYPE = ""
    RF = ""
    FLOW_METER = ""
    FERT_FLOWMETER = ""
    IS_USE_MF = False
    IS_USE_RF = False
    RF_CONFIG =""


    valid_count = 0
    string_list = content.split('\n')
    for i in range(len(string_list)):
        
        x = string_list[i].split()
        
        if (len(x) == 0):
            continue
        if (x[0]=="#define"):

            # count number of #define line
            valid_count +=1
            if x[1]== "NODE_ID":
                NODE_ID = x[2]
                print("--> CLIENT ID:", NODE_ID)
            elif (x[1]== "SOLAR_CHARGER_V1" or  x[1]== "SOLAR_CHARGER_V2"):
                CHARGER_TYPE = x[1]
            elif (x[1]== "_CC1310_" or  x[1]== "_LORA_E32_"):
                RF = x[1]
            elif (x[1]== "FLOW_METER_CLASS_B" or  x[1]== "FLOW_METER_CLASS_2"):
                FLOW_METER = x[1]
                print("--> FLOW METTER: ", FLOW_METER)
            elif (x[1]== "USE_NORMAL_FLOWMETER" or  x[1]== "USE_HUABA_CONTROL_FLOWMETER") :
                FERT_FLOWMETER= x[1]
            elif x[1]== "USE_MAIN_LINE_FLOW":
                IS_USE_MF = True
            elif x[1] == "USE_RF":
                IS_USE_RF = True
            elif (x[1]== "RF433MHz" or x[1]== "RF868MHz"):
                RF_CONFIG = x[1]

        

    # Validate content format
    if (valid_count ==  0):
        return -1

    # Guarantee file exists
    try:
        my_file = open(filename)
    except OSError:
        return -2
    line_list = my_file.readlines()

    my_file.close()

    for i in range(len(line_list)):
        x = line_list[i].split()
        if (len(x) == 0):
            continue
        if (x[0]=="#define"):

            if x[1]== "NODE_ID":
                line_list[i] = "#define\t" + "NODE_ID\t\t" +NODE_ID+ "\n" 

            elif x[1]== "MODE_WS":
                if  GW_mode == "gw":
                    line_list[i] = "//#define\t MODE_WS\n" 
                    line_list[i+1] = "#define\t MODE_GW\n" 
                elif  GW_mode == "ws": 
                    line_list[i] = "#define\t MODE_WS\n" 
                    line_list[i+1] = "//#define\t MODE_GW\n" 
                elif  GW_mode == "gwws":
                    line_list[i] = "#define\t MODE_WS\n" 
                    line_list[i+1] = "#define\t MODE_GW\n" 
                # vals.edited_content is a cross-module variable for storing edited content 
                # later, it will be used as email content.
                vals.edited_content += line_list[i]
                vals.edited_content += line_list[i+1]         
            elif x[1]== "MODE_GW":
                if  GW_mode == "gw":
                    line_list[i-1] = "//#define\t MODE_WS\n" 
                    line_list[i] = "#define\t MODE_GW\n" 
                elif  GW_mode == "ws":  #Hmm here should not do anything if it's "ws" but...
                    line_list[i-1] = "#define\t MODE_WS\n" 
                    line_list[i] = "//#define\t MODE_GW\n" 
                elif  GW_mode == "gwws":
                    line_list[i-1] = "#define\t MODE_WS\n" 
                    line_list[i] = "#define\t MODE_GW\n"  
                vals.edited_content += line_list[i]
                vals.edited_content += line_list[i-1]          
            elif(x[1]== "SOLAR_CHARGER_V2" or x[1] == "SOLAR_CHARGER_V1")  and  CHARGER_TYPE!="":
                line_list[i] = "#define\t" + CHARGER_TYPE +"\n"
                vals.edited_content += line_list[i]
            elif (x[1]== "_CC1310_" or  x[1]== "_LORA_E32_"):
                line_list[i] = "#define\t" + RF +"\n"
                vals.edited_content += line_list[i]
            elif (x[1]== "FLOW_METER_CLASS_B" or  x[1]== "FLOW_METER_CLASS_2") and FLOW_METER != "":
                line_list[i] = "#define\t" + FLOW_METER +"\n"
                vals.edited_content += line_list[i]
                # print("#define\t" + FLOW_METER +"\n")
            elif (x[1]== "USE_NORMAL_FLOWMETER" or  x[1]== "USE_HUABA_CONTROL_FLOWMETER") and FERT_FLOWMETER!="":
                line_list[i] = "#define\t" + FERT_FLOWMETER +"\n"
                vals.edited_content += line_list[i]
            elif (x[1]== "USE_MAIN_LINE_FLOW" and (not IS_USE_MF)):
                line_list[i] = "//#define\t USE_MAIN_LINE_FLOW\n"
                vals.edited_content += line_list[i]
            elif (x[1]== "USE_RF" and (not IS_USE_RF)):
                line_list[i] = "//#define\t USE_RF\n"
                vals.edited_content += line_list[i]
            elif (x[1]== "RF433MHz" or x[1]== "RF868MHz"):
                # print("\t\t#define\t" +RF_CONFIG) 
                line_list[i] = "#define\t" +RF_CONFIG + " \t// And this line\n"
                vals.edited_content += line_list[i]
        elif(x[0]=="//#define"):
            if x[1]== "USE_MAIN_LINE_FLOW" and (IS_USE_MF):
                line_list[i] = "#define\t USE_MAIN_LINE_FLOW\n"
                vals.edited_content += line_list[i]
            if x[1]== "USE_RF" and (IS_USE_RF):
                line_list[i] = "#define\t USE_RF\n"
                vals.edited_content += line_list[i]

                    

    my_file = open(filename, "w")
    new_file_contents = "".join(line_list)
    my_file.write(new_file_contents)
    my_file.close()

    return 0 

def config_rf(filename, content):
    """ This function is for defining which RF module used, called only when build for Mgreen NG

    Args:
        filename ([string]): Name or path to config file
        content ([string]): Config content

    Returns:
        0: If there was no error
    """

    LORA_CONFIG = ""
    RF_CONFIG = ""
    valid_count = 0
    string_list = content.split('\n')
    for i in range(len(string_list)):
        print(string_list[i])
        x = string_list[i].split()
        if (len(x) == 0):
            continue
        if (x[0]=="#define"):
            valid_count +=1
            if x[1]== "_LORA_APC_340_" or x[1]== "_LORA_APC_320_" or x[1]== "_LORA_E32_" or x[1]== "_LORA_LM230H_"or x[1]== "_LORA_RN2483_"or x[1]== "_CC1310_" :
                LORA_CONFIG = x[1]

            elif x[1]== "RF433MHz" or x[1]== "RF868MHz" :
                RF_CONFIG = x[1]

    # Check if valid #define
    if valid_count == 0:
        return -1

    try:
        my_file = open(filename)
    except OSError:
        return -2
    line_list = my_file.readlines()
    my_file.close()

    for i in range(len(line_list)):
        x = line_list[i].split()
        if (len(x) == 0):
            continue
        if (x[0]=="#define"):
            if x[1]== "_LORA_APC_340_" or x[1]== "_LORA_APC_320_" or x[1]== "_LORA_E32_" or x[1]== "_LORA_LM230H_"or x[1]== "_LORA_RN2483_"or x[1]== "_CC1310_" :
                print("--> #define\t" +LORA_CONFIG)
                line_list[i] = "#define\t" +LORA_CONFIG+ "\t" + "// Auto edit this line\n" # Dont delete "\n"

            elif x[1]== "RF433MHz" or x[1]== "RF868MHz" :
                print("--> #define\t" +RF_CONFIG) 
                line_list[i] = "#define\t" +RF_CONFIG + " \t// And this line\n"

    my_file = open(filename, "w")
    new_file_contents = "".join(line_list)
    my_file.write(new_file_contents)
    my_file.close()

    return 0

def configMgreen(configPath, topicConfigPath, broker, mqttId, rf):

    defineContent ='#define CLIENT_ID_1           "mgreen'+mqttId+'/1_1"\n\
                    #define CLIENT_ID_2           "mgreen'+mqttId+'/1_2"\n\
                    #define TOPIC_SUBSCRIBE       "mgreen/control/'+mqttId+'/1"\n\
                    #define TOPIC_MONITOR         "mgreen/monitor/'+mqttId+'/1"\n\
                    #define TOPIC_SMS             "mgreen/sms/'+mqttId+'/1"'

    editCfgTopicStatus = config_topic(topicConfigPath, defineContent, broker)
    editCfgStatus = config_rf(configPath, rf)

    if editCfgTopicStatus == -1:
        print("[Error] Invalid #define\n")
        return -1
    elif editCfgTopicStatus == -2:
        print("[Error] Invalid file\n")
        return -2
    else:
        print("[OK] Edited topic_config.h")

    if editCfgStatus == -1:
        print("[Error] Invalid LORA RF define")
        return -3
    elif editCfgStatus == -2:
        print("[Error] Invalid file\n")
        return -4
    else:
        print("[OK] Edited config.h")

    return 0

def configGateway(configPath, broker, mqttId, rf,charger_type, mode):

    defineContent ='#define CLIENT_ID_1           "mgreen'+mqttId+'/1_1"\n\
                    #define CLIENT_ID_2           "mgreen'+mqttId+'/1_2"\n\
                    #define TOPIC_SUBSCRIBE       "mgreen/control/'+mqttId+'/1"\n\
                    #define TOPIC_MONITOR         "mgreen/monitor/'+mqttId+'/1"\n\
                    #define TOPIC_SMS             "mgreen/sms/'+mqttId+'/1"\n'
                     
    config_hardware_content = '#define NODE_ID                '+mqttId+'\n' + charger_type + '\n'+rf

    editCfgTopicStatus = config_topic(configPath, defineContent, broker, isGW_WS=True)
    editCfgStatus =  config_hardware(configPath, config_hardware_content, mode)
    # editCfgStatus = config_rf(configPath, rf)

    if editCfgTopicStatus == -1:
        print("[Error] Invalid #define\n")
        return -1
    elif editCfgTopicStatus == -2:
        print("[Error] Invalid file\n")
        return -2
    else:
        print("[OK] Edited topic_config.h")

    if editCfgStatus == -1:
        print("[Error] Invalid LORA RF define")
        return -3
    elif editCfgStatus == -2:
        print("[Error] Invalid file\n")
        return -4
    else:
        print("[OK] Edited config.h")

    return 0

def configMiniRata3G_BL(configPath, broker, mqttId, lora_and_fm, isUseRF, fertilizer_fm, isUseMainFlow):
    """Config for mini RATA 3G bootloader 

    Args:
        configPath ([string]): Path to config file
        broker ([type]): MQTT Broker
        mqttId ([type]): MQTT client ID
        lora_and_fm ([type]): Type of lora and flowmetter under format "#define LORA\n#define FLOWMETTER"
        isUseRF (bool): ON/OFF RF
        fertilizer_fm ([type]): Type of ferterlizer flowmetter under format "#define FERT_FLOWMETTER" 
        isUseMainFlow (bool): On/Off main line flow

    Returns:
        -1: MQTT config content is invalid
        -2: MQTT Config file is not found 
        -3: Harware config content is invalid 
        -4: Hardware config file is not found
    """

    defineContent ='#define CLIENT_ID_1           "mgreen'+mqttId+'/1_1"\n\
                    #define CLIENT_ID_2           "mgreen'+mqttId+'/1_2"\n\
                    #define TOPIC_SUBSCRIBE       "mgreen/control/'+mqttId+'/1"\n\
                    #define TOPIC_MONITOR         "mgreen/monitor/'+mqttId+'/1"\n\
                    #define TOPIC_SMS             "mgreen/sms/'+mqttId+'/1"\n'
                     
    hardwareConfigContent = lora_and_fm+'\n'+fertilizer_fm+'\n'

    if isUseMainFlow.find("true") != -1 or isUseMainFlow.find("TRUE") != -1: 
        hardwareConfigContent += '#define\t USE_MAIN_LINE_FLOW\n'
    if isUseRF.find("true") != -1 or isUseRF.find("TRUE") != -1:
        hardwareConfigContent += '#define\t USE_RF\n'

    editCfgTopicStatus = config_topic(configPath, defineContent, broker, isGW_WS=False)
    editCfgHardware = config_hardware(configPath, hardwareConfigContent, GW_mode = "None")

    if editCfgTopicStatus == -1:
        print("[Error] Invalid #define\n")
        return -1
    elif editCfgTopicStatus == -2:
        print("[Error] Invalid file\n")
        return -2
    else:
        print("[OK] Edited topic_config.h")

    if  editCfgHardware == -1:
        print("[Error] Invalid hardware define")
        return -3
    elif  editCfgHardware == -2:
        print("[Error] Invalid config file\n")
        return -4
    else:
        print("[OK] Edited config.h")

    return 0

def configMiniRata3GBroker(configPath, broker):
    """Config broker for Mini RATA 3G Application 

    Args:
        configPath ([string]): Path to config file
        broker ([type]): MQTT Broker

    Returns:
        -1: If errors occur during config process
        
    """

    try:
        my_file = open(configPath)
    except OSError:
        return -1
    line_list = my_file.readlines()
    my_file.close()

    for i in range(len(line_list)):
        x = line_list[i].split()
        if (len(x) == 0):
            continue
        if (x[0]=="#define"):
            if x[1]== "MQTT_SERVER":
                print("--> #define\tMQTT_SERVER\t\"" +broker+".mimosatek.com\"")
                line_list[i] = "#define\tMQTT_SERVER\t\t\t\t\t\t\t\t\""+broker+".mimosatek.com\"\n" # Dont delete "\n"
    
    my_file = open(configPath, "w")
    new_file_contents = "".join(line_list)
    my_file.write(new_file_contents)
    my_file.close()

    return 0

def configMiniFF(configPath, broker, mqttId, lora, isUseRF, isUseMainFlow):
    """ Edit Mini_FF's config  

    Args:
        configPath ([string]): Path to config file
        broker ([string]): MQTT broker
        mqttId ([string]): Client ID
        lora ([string]): Lora type under format like "#define LORA_E32"
        isUseRF (bool): Config on/off RF
        isUseMainFlow (bool): Config on/off Main line flow

    Returns:
        -1: MQTT config content is invalid
        -2: MQTT Config file is not found 
        -3: Harware config content is invalid 
        -4: Hardware config file is not found 
    """

    defineContent ='#define CLIENT_ID_1           "mgreen'+mqttId+'/1_1"\n\
                    #define CLIENT_ID_2           "mgreen'+mqttId+'/1_2"\n\
                    #define TOPIC_SUBSCRIBE       "mgreen/control/'+mqttId+'/1"\n\
                    #define TOPIC_MONITOR         "mgreen/monitor/'+mqttId+'/1"\n\
                    #define TOPIC_SMS             "mgreen/sms/'+mqttId+'/1"\n' 

    hardwareConfigContent = lora+'\n'

    if isUseMainFlow.find("true") != -1 or isUseMainFlow.find("TRUE") != -1: 
        hardwareConfigContent += '#define\t USE_MAIN_LINE_FLOW\n'
    if isUseRF.find("true") != -1 or isUseRF.find("TRUE") != -1:
        hardwareConfigContent += '#define\t USE_RF\n'

    # print(hardwareConfigContent)
    # print(isUseRF)

    editCfgTopicStatus = config_topic(configPath, defineContent, broker, isGW_WS=False)
    editCfgHardware = config_hardware(configPath, hardwareConfigContent, GW_mode = "None")

    if editCfgTopicStatus == -1:
        print("[Error] Invalid #define\n")
        return -1
    elif editCfgTopicStatus == -2:
        print("[Error] Invalid file\n")
        return -2
    else:
        print("[OK] Edited topic_config.h")

    if  editCfgHardware == -1:
        print("[Error] Invalid hardware define")
        return -3
    elif  editCfgHardware == -2:
        print("[Error] Invalid config file\n")
        return -4
    else:
        print("[OK]] Edited config.h")

    return 0

def configRata3G(configPath, broker, mqttId, lora_and_fm, isUseRF, isUseMainFlow):
    """ Edit RATA_3G's config  

    Args:
        configPath ([string]): Path to config file
        broker ([string]): MQTT broker
        mqttId ([string]): Client ID
        lora_and_fm ([string]): Lora type and flowmeter type under format "#define LORA\n#define FM"
        isUseRF (bool): Config on/off RF
        isUseMainFlow (bool): Config on/off Main line flow

    Returns:
        -1: MQTT config content is invalid
        -2: MQTT Config file is not found 
        -3: Harware config content is invalid 
        -4: Hardware config file is not found 
    """

    defineContent ='#define CLIENT_ID_1           "mgreen'+mqttId+'/1_1"\n\
                    #define CLIENT_ID_2           "mgreen'+mqttId+'/1_2"\n\
                    #define TOPIC_SUBSCRIBE       "mgreen/control/'+mqttId+'/1"\n\
                    #define TOPIC_MONITOR         "mgreen/monitor/'+mqttId+'/1"\n\
                    #define TOPIC_SMS             "mgreen/sms/'+mqttId+'/1"\n' 
    
    hardwareConfigContent = lora_and_fm+'\n'

    if isUseMainFlow.find("true") != -1: 
        hardwareConfigContent += '#define\t USE_MAIN_LINE_FLOW\n'
    if isUseRF.find("true") != -1:
        hardwareConfigContent += '#define\t USE_RF\n'

    editCfgTopicStatus = config_topic(configPath, defineContent, broker , isGW_WS = False)
    editCfgHardware = config_hardware(configPath, hardwareConfigContent, GW_mode = "None")

    if editCfgTopicStatus == -1:
        print("[Error] Invalid #define\n")
        return -1
    elif editCfgTopicStatus == -2:
        print("[Error] Invalid file\n")
        return -2
    else:
        print("[OK] Edited topic_config.h")

    if  editCfgHardware == -1 :
        print("[Error] Invalid hardware define")
        return -3
    elif  editCfgHardware == -2:
        print("[Error] Invalid config file\n")
        return -4
    else:
        print("[OK] Edited config.h")

    return 0





if __name__ == "__main__":
    
    # configGateway("C:\\SourceCode\\stable\\mgreen-gateway-v4\\config.h", "hexrequest/prod", "1343","#define _CC1310_\n#define RF433MHz", "#define SOLAR_CHARGER_V1", "ws")
    # configMiniRata3G("C:\\SourceCode\\stable\\rata-3g\\MGreen_BL\\Inc\\boot_config.h",  "hexrequest/prod", "5555", "#define _CC1310_ \n#define FLOW_METER_CLASS_B", False,"#define USE_HUABA_CONTROL_FLOWMETER",  False)
    # configMiniFF("C:\\SourceCode\\stable\\mini-ff\\MGreen_BL\\Inc\\boot_config.h",  "hexrequest/prod", "5333", "#define _CC1310_", False, False)
    # configRata("C:\\SourceCode\\stable\\fertiflex-controller\\MGreen_BL\\Inc\\boot_config.h",  "hexrequest/prod", "5333")
    # configMiniRata3GBroker('C:\\Users\\NGUYEN DUY LINH\\Desktop\\firmware_config.h', 'app')
    print(chr(25))