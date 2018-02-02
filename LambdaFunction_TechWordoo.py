import random

# ------------------------------------------------------------------------------
# ---------------------------- Main Handler ------------------------------------
# ------------------------------------------------------------------------------

def lambdaHandler(event, context):
    """ 
    This is the Main Handler function that will call other functions.
    We get two inputs : event , context
    """
    print("Reached Here")
    
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])
        
# ------------------------------------------------------------------------------
# ----------------------------- Event Handlers ---------------------------------
# ------------------------------------------------------------------------------

def onLaunch(launchRequest, session):
    """
    This function welcomes the user , if the person does not Know how to 
    interact with the SKill 
    """
    
    return welcomeGuest()
    

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']

    if intentName == "knowWordIntent":
        return newWordInResponse(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeGuest()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")
        
        

def onSessionEnd(sessionEndedRequest, session):
    """ 
    Called when the user ends the session.
    """
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])
        
    
# ------------------------------------------------------------------------------
# --------------------------- Behaviour Handlers -------------------------------
# ------------------------------------------------------------------------------

def welcomeGuest():
    """
    Giving Welcome Instructions to User
    """
    
    sessionAttributes = {}
    cardTitle = " Heya!! Techie "
    speechOutput =  "Welcome to Tech Wordoo " \
                    "You can ask me a new tech word to add to your Vocabulary by saying " \
                    "Tell me a new Tech Term"
    repromptText =  "You can ask me a new tech word to add to your Vocabulary by saying " \
                    "Tell me a new Tech Term"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))
    

def newWordInResponse(intent, session):
    """ 
    Finds a new word in the session and prepares the speech to reply to the user.
    """
    wordOptionsCleaned = [v for v in wordOptions if v[2] == 0]
    newWord = random.choice(wordOptions)
    newWord[2]=1
        
    cardTitle = intent['name']
    sessionAttributes = {}
    shouldEndSession = False
    speechOutput = "A new word for you is " + \
                     newWord[0] + \
                    ". Which means, " + newWord[1]
    repromptText = "You can ask me a new tech word to add to your Vocabulary by saying, " \
                    "Tell me a new Tech Term"
                        
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))



def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for trying Tech Wordoo Alexa Skills Kit. " \
                    "Have a nice day! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))    

# ------------------------------------------------------------------------------
# --------------------------- Response Builders --------------------------------
# ------------------------------------------------------------------------------

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }

# ------------------------------------------------------------------------------
# ---------------------------- Word Dictionary ---------------------------------
# ------------------------------------------------------------------------------

wordOptions = [
    
    ["Payload","When data is sent over the Internet, each unit transmitted \
    includes both header information and the actual data being sent. \
    This actual data is referred to as the payload",0,1],
    
    ["CONTENT CURATION","the process social media sites \
    use to gather and present content relevant to a specific topic or a user’s\
    area of interest",0,2],
    
    ["MICROBLOGGING","a subset of traditional blogs where \
    instead of longform content, short messages, an image, a video, or a link \
    are posted and shared.",0,3],
    
    ["CTR"," click through rate ,that is the percentage of users who click on \
    links in web pages or marketing emails. ",0,4],
    
    ["DATA MINING","practice of examining large amounts of data in user \
    databases and websites to find consumer patterns, behaviors, and \
    relationships that can be useful in marketing goods and services online.",0,5],
    
    ["NFC ","technology that lets mobile devices communicate using radio \
    waves when they’re very close to each other and is used for services like \
    sharing files, pairing accessories, or wireless payments. ",0,6],
    
    ["AllSeen","The technology behind many of the new wireless streaming \
    speakers launching on the market. It's the underlying tech to Qualcomm's\
    AllPlay tech.",0,7],
    
    ["AMOLED","Active-Matrix Organic Light-Emitting Diode.An AMOLED \
    consumes less power than conventional OLED screens, thereby making it a \
    perfect display tech for mobile devices.",0,8],
    
    ["apt X","a device which serves as an audio codec that gives you low \
    latency, high fidelity, Bluetooth transmission. It promises CD-like quality \
    and is widely integrated into wireless headphones, speakers, \
    smartphones and other devices.",0,9],
    
    ["Broadwell","Intel Core's Latest (5th) generation of chipsets.It is already\
    in some laptops from Dell and Acer, and it is expected others like Apple\
    will follow suit very quickly.",0,10],
    
    ["Big.Little","a particular arrangement of cores within a chipset, whereby \
    different cores handle different types of tasks. The aim is to increase\
    efficiency, by letting little cores do some of the little jobs, without\
    the big cores using unnecessary energy.",0,11],
    
    ["Codec","a combination of coder-decoder.\
    Also it is a program that encodes and decodes digital information. \
    You'll need the right codec to read a particular type of file, or\
    receive a particular type of digital stream.",0,12],
    
    ["Continuum mode","A mode available in Microsoft Windows 10 and above \
    .It occurs only on 2-in-1 devices. It basically allows Windows 10 \
    to move easily between keyboard and mouse to touch and tablet. \
    Windows 10 can detect the transition and automatically switch.",0,13],
    
    ["Cherry Trail","The 5th generation Intel Core chipsets for tablets,\
    sitting alongside the Broadwell chipsets designed for notebooks and PCs.",0,14],
    
    ["Dynamic tessellation","solving the problem of a lack of detail in \
    graphics by varying the level of detail on the fly more efficiently.\
    It is a term used in video games",0,15],
    
    ["Nixie","The name of a wearable selfie drone that is worn on the\
    wrist before it launches to take a selfie of yourself from the air.",0,16],
    
    ["Qi","A common wireless charging standard supported by Microsoft/Nokia\
    , LG, BlackBerry, Sony, Samsung and plenty of others.",0,17],
    
    ["RealSense","Intel's new Kinect like 3D-camera technology \
    that can analyse a scene and provide spatial awareness data for objects\
    within that scene, whether they are static like a desk, or moving, \
    like your hand or body.",0,18],
    
    ["Tizen OS","an operating system used by Samsung's new smart TV \
    It is expected to provide greater connectivity with other Samsung \
    products in the future.",0,19],   
    
    ["ZigBee","A wireless protocol common in connected home products \
    operating within a mesh network. It helps them all talk to\
    each other in a standardised fashion",0,20],
    
    ["Zombie Network","a network or collection of compromised \
    computers or hosts that are connected to the Internet",0,21],
    
    ["Write-Only Language","a language in which only the coder can comprehend \
    the code that he/she has written in that language. ",0,22],
    
    ["Vulcan Nerve Pinch","a keyboard combination that hinders a user's \
    ability to complete complicated command functions with a \
    single-hand or accidental keypress.",0,23],
    
    ["Time Sink","task that takes a long time or wastes someone's time.\
    It is often used in gaming and other aspects of IT to talk about tedious, \
    unproductive or annoying processes that are seen as a waste of time.",0,24],
    
    ["Adminispam","messages from managers or executives within an \
    organization that are sent to the majority of employees regardless of\
    whether the information is relevant to a particular employee's work",0,25],
    
    ["Algorithm Economy","the evolution of microservices and the functionality\
    of algorithms to drive sophisticated application designs. ",0,26],
    
    ["Blockchain","recording bitcoin exchange or transaction",0,27],
    
    ["Double Bucky"," pressing two separate modifying keys on a \
    device keyword simultaneously.",0,28],
    
    ["Quux","meta-syntactic variable name invented only as a kind of nickname \
    or placeholder. Like other variable names such as foo, quux may be \
    used in computer programming as a variable name.",0,29],
    
    ["Swirl","the background noise from a digital cellular phone.",0,30],
    
    ["Teardrop Attack","a denial of service (DoS) attack conducted \
    by targeting TCP/IP fragmentation reassembly codes",0,31],
    
    ["Pharming","redirecting website traffic through hacking, \
    whereby the hacker implements tools that redirect a search to a fake website. ",0,32],
    
    ["Munge","alterations or changes to a file or data structure.\
    Common definitions describe “munge” as an action that is \
    “potentially destructive or irrevocable.” ",0,33],

    ["Vampire Tap","device that connects 10BASE5 cabling to Ethernet transceivers.",0,34],

    ["WinTel"," PC built with an Intel microprocessor and a Microsoft OS",0,35],

    ["Yoda Condition","a piece of computer syntax is inverted or swapped around,\
    for example, where instead of declaring a variable equal to a constant,\
    the programmer declares a constant equal to a variable. ",0,36],

    ["Acqhire","a combination of the words acquire and\
    hire that is used to refer to one company's acquisition \
    of another in order to gain talented employees. ",0,37],

    ["Bucky Bit","an extension of binary code representing a \
    character or function that adds an eighth bit to the code \
    through the pressing of a keyboard modifier key. ",0,38],
    
    ["AI","Artificial Intelligence.It refers to the autonomous intelligent \
    behavior of software or machines that have a human-like ability to make\
    decisions and to improve over time by learning from experience.",0,39],
    
    ["Internet of Things","the physical world will become one big information \
    system. Everyday physical objects will be connected to Internet and to each\
    other creating the ambient intelligence. ",0,40],
    
    ["Digital Detox","totally disconnecting from technology",0,41],
    
    ["Serverless Architecture","an application relies on third-party services\
    (or “BaaS”, Backend as a Service), or on custom code run in ephemeral \
    containers (also called “FaaS”, Function as a Service). The name can however\
    be misleading: serverless computing is not running code without servers.\
    It is called serverless from a developer’s point of view: the person\
    or the business who owns the system doesn’t need to buy, rent or provision \
    servers or machines to run the backend code. In short: they don’t have to manage servers.",0,42],
    
    ["Dark Data","the information assets organizations collect, process and \
    store during regular business activities, but generally fail to use for other purposes",0,43],
    
    ["SEO","Search Engine Optimization. It refers to a technique of improving\
    how a website’s page ranks in the search results produced by search engines like Google and Yahoo!",0,44],
    
    ["Wearables","computer devices worn on the body. Some wearables can monitor\
    vital signs like your heart rate, or can be used to monitor physical activity\
    such as running, swimming or even flights of stairs taken. ",0,45],
    
    ["Virtual Reality"," a three dimensional environment that makes a user believe\
    that whatever he or she is experiencing is real",0,46],
    
    ["Net Neutrality","that internet providers and government provides equal access\
    to the internet to all instead of selectively speeding up and down the traffic. ",0,47],
    
    ["DMZ","demilitarized zone .It is sometimes referred to as a perimeter network\
    is a physical or logical subnetwork that contains and exposes an organization's\
    external-facing services to an untrusted network, usually a \
    larger network such as the Internet",0,48],
    
    ["SO-DIMM","Small Outline Dual In-Line Memory Module.A SO-DIMM is about half\
    the length of a regular size DIMM. This allows greater flexibility in\
    designing the memory slots for laptops.",0,49],
    
    ["Ripcording","the process of simultaneously recording and compressing audio",0,50]
    ]
    
    
