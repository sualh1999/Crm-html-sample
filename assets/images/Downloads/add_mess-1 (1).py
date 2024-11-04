# from pymongo import MongoClient
#from config import recos, mess_log, user_info, ref_data,custom_state, bot_config
# new_language = "English"  # The new language you want to add
# # a = bot_config.update_one({}, {"$push": {"LANGUAGES": new_language}})
# # print(a)

# bot_config_collection = db.bot_config

# # Find a document where the LANGUAGES field exists
# document_with_languages = bot_config_collection.find_one(
#     {"LANGUAGES": {"$exists": True}})

# # Check if document_with_languages is not None
# if document_with_languages:
#     languages = document_with_languages["LANGUAGES"]
#     print("Languages:", languages)
# else:
#     print("No document found with the LANGUAGES field.")

# Data to insert
bot_messages = {
  #General Messages
  "start_message": {
    "english": """Welcome to Maroset platform! We are dedicated to connecting talented professionals with exciting remote job opportunities. As an employer, you can easily find skilled and experienced professionals. As an employee, you can explore a wide range of remote job opportunities across various industries.\n\nOnly Remote Jobs!\n\nUse /language to change the language \n\nJoin: Maroset""",
    "amharic": """እንኳን ወደ Maroset ፕላትፎርም በሰላም መጡ። ይህ ፕላትፎርም ባለሞያዎች ጊዜ እና ቦታ ሳይገድባቸው ባሉበት ሆነው በኦንላይን ዘርፈ ብዙ የስራ ዕድሎች ላይ ተቀጥረው መስራት የሚችሉበት እንዲሁም ቀጣሪዎች ወይም አሰሪዎች በኦንላይን ብቁ ባለሞያዎችን ቀጥረው ማሰራት የሚችሉበት ምቹ መድረክ ነው።\n\n✨በዚህ ፕላትፎርም ሁሉም ስራዎች የሚሰሩት በኦንላይን ባሉበት ሆነው ነው።\n\nቋንቋዎን ለመቀየር የ /language ን አዝራር ይጫኑn\n\nMaroset ን ይቀላቀሉ""",
    "afaan_oromoo": """Gara plaatfoormii Maroset baga nagaan dhuftan, plaatfoormiin kun namoonni osoo bakki isaan hin daangeesssin bakkuma jiranitti karaa onlinerraan hojiilee fagoo irratti qacaramanii kan itti hojjatan, akkasumas hojjachistoonnis salphumatti ogeessoota barbaadan qacaruu kan itti danda'anidha.\n\nQooqa keessan jijjiiruf maaloo qabduu /language fayyadamaa\n\nMaroset itti makamaa"""
  "procces_canceled": {
    "english": "Your procces has been canceled!",
    "amharic": "እስካሁን የነበረውን ሂደት ሰርዘዋል!",
    "afaan_oromoo": "Adeemsa hanga ammaatti ture haqxaniirtu!"
  },
    "post_job": {
      "english": "Post a Job",
      "amharic": "የስራ ማስታወቂያ ለማውጣት",
      "afaan_oromoo": "Hojii maxxansaa"
    },
    "my_jobs": {
      "english": "My Jobs",
      "amharic": "የስራ ማስታወቂያዎቼ",
      "afaan_oromoo": "Hojiiwwankoo"
    },
    "invite": {
      "english": "Invite",
      "amharic": "ይጋብዙ ይሸለሙ",
      "afaan_oromoo": "affeeraa badhaafamaa"
    },
    "my_company": {
      "english": "My Company",
      "amharic": "ድርጅቶቼ",
      "afaan_oromoo": "Kuubbaaniyaawwankoo"
    },
    "setting": {
      "english": "Setting",
      "amharic": "ዝርዝር/",
      "afaan_oromoo": "Qindaa'ina"
    },
  #Job Posting Messages
    "ask_job_post_type": {
        "english": "Choose how do you want to post the job: \nprivate or company/startup",
        "amharic": "የስራ ማስታወቂያዎትን በምን መልኩ መለጠፍ እንደፈለጉ እባክዎ ይምረጡ: \n ግለሰብ ወይም ኩባንያ/ጀማሪ ድርጅት: \nprivate or company/startup",
        "afaan_oromoo": "Hojii akkamitti maxxansuu akka barbaaddan filadhaa: \nprivate or company/startup"
    },"ask_job_title": {
        "english": "Send job title:",
        "amharic": "የስራ መደብ መጠርያውን ይላኩ.",
        "afaan_oromoo": "Maqaa gita hojii ergaa:"
    },
    "ask_company_name": {
        "english": "Send the company name.(Optional):",
        "amharic": "የድርጅትዎን ስም ይላኩ(ከሌለ ይዝለሉ).",
        "afaan_oromoo": "Maqaa dhaabbata keessanii ergaa.(Yoo hin jiraanne darbaa):"
    },
    "ask_salary": {
        "english": "Salary (For unpaid internship skip it):",
        "amharic": "ደመወዝ(ለማይከፈሉ ስራዎች ይዝለሉ)",
        "afaan_oromoo": "Mindaa (Hojiiwwan hin kaffalamneef darbaa):"
    },
    "ask_deadline": {
        "english": "Job deadline(day-month-year):",
        "amharic": "የስራው ማመልከቻ የማብቂያ ቀን(ቀን-ወር-ዓ.ም):",
        "afaan_oromoo": "Guyyaa dhumaa iyyannoo hojii kanaa(guyyaa-ji'a-bara):"
    },
    "ask_job_field": {
        "english": "Select the job field:",
        "amharic": "የስራውን ዘርፍ ይምረጡ:",
        "afaan_oromoo": "Seektara hojii kanaa filadhaa:"
    },
    "ask_job_description": {
        "english": "Send the Job Description:",
        "amharic": "የስራውን ዝርዝር ማብራርያ ይላኩ",
        "afaan_oromoo": "Ibsa hojii kanaa/description ergaa:"
    },
    "ask_job_requirements": {
        "english": "Requirements(Optional)",
        "amharic": "ግዴታዎች (ከሌለ ይዝለሉ)",
        "afaan_oromoo": "Dirqamoota hojichaa(Yoo hin jiraanne darbaa)"
    },
    "ask_job_responsibilities": {
        "english": "Roles & Responsibilities(Optional)",
        "amharic": "ሚናዎች እና ሃላፊነቶች (ከሌለ ይዝለሉ)",
        "afaan_oromoo": "Gahee fi itti gaafatamummaa hojichaa(Yoo hin jiraanne darbaa)"
    },
    "send_your_new_text": {
      "english": "Send your new text:",
      "amharic": "አዲሱን ጽሑፍ ይላኩ:",
      "afaan_oromoo": "Barreeffama haaraa ergaa:"
    },
    "this_job_has_been_canceled": {
      "english": "This job has been canceled:",
      "amharic": "ይህ የስራ ማስታወቂያ ተሰርዟል:",
      "afaan_oromoo": "Hojiin kun haqameera:"
    },
    "the_job_has_been_sended_to_admin": {
      "english": "Please wait a few moments while we review your job posting and get it posted in the channel. In the meantime, check out our website maroset.com for more info on Maroset and how we can help you. You can also post a job there ",
      "amharic": "ያወጡት የስራ ማስታወቂያ ወደ ፕላትፎርሙ አስተዳዳሪዎች ተልኳል። ታይቶ እስኪፀድቅልዎት ድረስ እባክዎ በትዕግስት ይጠብቁ።",
      "afaan_oromoo": "Beeksisni hojii baastan gara bulchitoota plaatformichatti ergameera, ilaallamee hanga isiniif mirkanaa'utti maaloo obsaan eeggadhaa."
    },
    "this_job_has_been_rejected": {
        "english": "This job post has been rejected!",
        "amharic": "ይህ የስራ ማስታወቂያ ውድቅ ሆኗል!",
        "afaan_oromoo": "Beeksisni hojii kun kufaa taasifameera!"
    },
    "your_job_has_been_rejected": {
        "english": "❗Unfortunately, your job vacancy has been rejected by the admins. \nYour job vacancies might be rejected because of one or all of the following reasons;\n-Using emojis\n-Incomplete/Invalid contents\n-Duplicate listings\n-Violation of posting guidelines\n\nFor further assistance, please use the /help command to contact them.",
        "amharic": "❗ይቅርታ ያስገቡት የስራ ማስታወቂያ ውድቅ ሆኗል። የስራ ማስታወቂያዎ ውድቅ የሆነበት/የሚሆንበት ምክንያት ከታች ከተዘረዘሩት በአንዱ ወይም በሁሉም ሊሆን ይችላል;\n-ኢሞጂ መጠቀም\n-ያልተሟላ/የማይገናኝ መረጃ ማስገባት\n-የተደጋገመ ሃረግ መጠቀም\n-Yeteteyekutin masreja alemelak\n-የስራ ማስታወቂያ ማውጫ ሕግን መጣስ\n\nእባክዎ እንደገና አስተካክለው ይላኩ።ለበለጠ እገዛ እባክዎ የ Helpን አዝራር በመጫን ያግኙን""",
        "afaan_oromoo": "❗Dhiifama, beeksisni hojii baastan kufaa taasifameera, sababni itti kufaa ta'ee fi itti ta'u kanneen armaan gadiitti tarreeffaman keessaa tokkoon yookin hundumaan ta'uu danda'a;\n-Immoojii fayyadamuu\n-Odeeffannoo hir'uu yookiin sirrii hin taane galchuu\n-Jechoota irra deddeebii fayyadamuu\n-ragaa gaafatamtan erguu dhabuu\n-Qajeelfama maxxansa beeksisa hojii cabsuu\n\nMaaloo irra deebitanii sirreessuun maxxansaa. Gargaarsa dabalataaf maaloo qabduu /help cuqaasun nu quunnamaa."    },
  "this_job_has_been_posted": {
      "english": "This job has been posted on the platform!",
      "amharic": "ይህ የስራ ማስታወቂያ ፕላትፎርሙ ላይ ተለጥፏል!",
      "afaan_oromoo": "Hojiin kun plaatformicha gubbaa maxxanfameera!"
  },
  "your_job_has_been_posted": {
      "english": "Congratulations dear employer! your job vacancy has been approved. Please Follow-up the applications, communicate with each applicant and close the job before/on the deadline(This is mandatory!!).\n\nGood Luck!",
      "amharic": "እንኳን ደስ ያልዎት ውድ ደንበኛችን! ያወጡት የስራ ማስታወቂያ ፀድቆሎታል። እባክዎ ማመልከቻዎችን ይከታተሉ፥ ከእያንዳንዱ አመልካች ጋር ይነጋገሩ፥ በስተመጨረሻም የሚፈልጉትን ባለሞያ ከቀጠሩ በኋላ ወዲያው የስራ ማስታወቅያዎትን ይዝጉ (ልብ ይበሉ ይህን ማድረግ ግዴታዎ ነው!) መልካም ዕድል!.\n\nGood Luck!",
      "afaan_oromoo": "Baga gammaddan Kabajamoo maamila keenyaa! beeksisni hojii baastan isinif mirkanaa'eera. Maaloo iyyattoota hojii keessanii waliin quunnamaa, akkasumas ogeessa barbaaddan erga qacartan booda beeksisa hojii keessanii dirqama cufuu qabdu.\n\nCarraa Gaari!"
  },
    "main_menu": {
      "english": "Main Menu",
      "amharic": "ወደ ዋናው ማውጫ",
      "afaan_oromoo": "Baafata"
  },
    "confirm": {
        "english": "Confirm",
        "amharic": "ያረጋግጡ",
        "afaan_oromoo": "Mirkanneessaa"
    },
    "edit": {
        "english": "Edit",
        "amharic": "ያስተካክሉ",
        "afaan_oromoo": "Gulaalaa"
    },
    "cancel": {
        "english": "Cancel",
        "amharic": "ይሰርዙ",
        "afaan_oromoo": "Haqaa"
    },
    "skip": {
        "english": "Skip",
        "amharic": "ይለፉ",
        "afaan_oromoo": "Darbaa"
    },
  "back": {
      "english": "Back",
      "amharic": "ይመለሱ",
      "afaan_oromoo": "Deebi'aa"
  },
  "yes": {
      "english": "Yes",
      "amharic": "አዎ",
      "afaan_oromoo": "Eeyyee"
  },
  "no": {
      "english": "No",
      "amharic": "አይደለም",
      "afaan_oromoo": "Lakki"
  },
  "approve": {
      "english": "Approve",
      "amharic": "ያፅድቁ",
      "afaan_oromoo": "Mirkaneessaa"
  },
  "deny": {
      "english": "Deny",
      "amharic": "ይጣሉ",
      "afaan_oromoo": "Kuffisaa"
  },
  "help": {
      "english": "Help",
      "amharic": "እርዳታ",
      "afaan_oromoo": "Gargaarsa"
  },
  "talk_to_owner": {
      "english": "Talk to the job owner",
      "amharic": "ከስራው ባለቤት ጋር ያውሩ",
      "afaan_oromoo": "Abbaa hojichaatti haasa'aa"
  },
  "talk_to_user": {
      "english": "Talk to the applicant",
      "amharic": "ከአመልካች ጋር ያውሩ",
      "afaan_oromoo": "Iyyataa waliin haasa'aa"
  },
      "broadcaast": {
          "english": "Broadcast",
          "amharic": "ማሰራጫ",
          "afaan_oromoo": "Tamsaasa"
    },
    "close": {
        "english": "Close",
        "amharic": "ይዝጉ",
        "afaan_oromoo": "Cufaa"
    },
    "cv": {
        "english": "CV",
        "amharic": "CV",
        "afaan_oromoo": "CV"
    },
    "upload_cv_button": {
        "english": "Upload CV",
        "amharic": "CV ያስገቡ",
        "afaan_oromoo": "CV fe'aa"
    },
    "profile_info": {
        "english": "Profile",
        "amharic": "ግለታሪክ",
        "afaan_oromoo": "Eenyummaa"
    },
    "language": {
        "english": "Language",
        "amharic": "ቋንቋ",
        "afaan_oromoo": "Qooqa"
    },
    "term_and_condition": {
        "english": "Terms & policies",
        "amharic": "ሕግ እና ደንቦች",
        "afaan_oromoo": "Seeraa fi dambiiwwan",
        },
      "remove": {
          "english": "Remove",
          "amharic": "ያጥፉ",
          "afaan_oromoo": "Kutaa"
      },
    "setting_page_message": {
        "english": "This is setting",
        "amharic": "ይህ ዝርዝር ነው",
        "afaan_oromoo": "kun qindaa'ina"
    },
    "you_dont_have_cv": {
        "english": "You didn't upload a CV yet!",
        "amharic": "እስካሁን 'CV' አልጫኑም!",
        "afaan_oromoo": "Hanga ammaatti 'CV' hin feene!"
    },
    "cv_has_been_uploaded": {
        "english": "Your CV has been uploaded succesfully!\nType your letter again.",
        "amharic": "CVዎ በስኬት ተጭኗል!\nመልዕክትዎን እንደገና ይፃፉ",
        "afaan_oromoo": "CV n keessan milkaa'inaan fe'ameera!\nDeebi'aatii barreessaa."
    },
  "ask_to_join_channel": {
      "english": "Join: <a href='https://t.me/+tU8xZvbddBA3Yzdk'>Maroset</a>\nYou have to Join the Channel First!",
      "amharic": "ይቀላቀሉ: <a href='https://t.me/+tU8xZvbddBA3Yzdk'>Maroset</a>\nመጀመርያ ቻናሉን መቀላቀል አለብዎት!",
      "afaan_oromoo": "Itti Makamaa: <a href='https://t.me/+tU8xZvbddBA3Yzdk'>Maroset</a>\nDursa chaanaalichatti makamuu qabdu!"
  },
  "ask_name": {
      "english": "Write your full name",
      "amharic": "ሙሉ ስምዎትን ይፃፉ",
      "afaan_oromoo": "Maqaa guutuu keessan barreessaa"
  },
  "invalid_name": {
      "english": "Please Write your full name correctly!",
      "amharic": "እባክዎ ሙሉ ስምዎትን አስተካክለው ይፃፉ!",
      "afaan_oromoo": "Maaloo Maqaa guutuu keessan sirreessaatii barreessaa!"
  },
  "ask_phone_number": {
      "english": "If you're not robot, Please press the 'Share your phone number' button here below for security purposes.",
      "amharic": "ሮቦት ካልሆኑ ለደህንነት እባክዎ ከዚህ በታች 'Share your phone number' የሚለውን አዝራር ይጫኑ.",
      "afaan_oromoo": "Roobotii yoo hin taane, maaloo qabduu asiin gadii kan'Share your phone number' jedhu eeggumsaaf cuqaasaa."
  },
  "share_phone_button": {
      "english": "Share your phone number",
      "amharic": "ስልክ ቁጥርዎን ያጋሩን",
      "afaan_oromoo": "Lakkoofsa bilbila keessanii ergaa"
  },
  "invalid_phone_number": {
      "english": "Click the 'Share your phone number' button",
      "amharic": "'Share your phone number' የሚለውን አዝራር ይጫኑ",
      "afaan_oromoo": "Qabduu 'Share your phone number' jedhu cuqaasaa"
  },
  "ask_to_attach_phone": {
      "english": "Do you want to attach this phone number with your profile? (You can change it later in setting)\n=> +{number}",
      "amharic": "ይህንን ስልክ ቁጥር የራስዎ ግለታሪክ ላይ ማካተት ይፈልጋሉ?(በኋላ ዝርዝር/setting ውስጥ መቀየር ይችላሉ)\n=> +{number}",
      "afaan_oromoo": "Lakkoofsa bilbila kana proofaayila keessan waliin hidhuu barbaadduu? (Booddee qindaa'ina/setting keesssatti jijjiiruu dandeessu)\n=> +{number}"
  },
  "ask_email": {
      "english": "Feel free to provide your email address. However, please note that sharing your email address is not mandatory.",
      "amharic": "የኢሜይል አድራሻዎን ሊልኩልን ይችላሉ፥ ሆኖም የኢሜይል አድራሻዎን መላክ ግዴታ አይደለም.",
      "afaan_oromoo": "Teessoo email keessan nuf erguu dnadeessu. Maaloo hubadhaa, email keessan erguun diqamaa miti (darbuu dandeessu)."
  },
  "ask_email_from_setting": {
      "english": "provide your email address.",
      "amharic": "የኢሜይል አድራሻዎን ይላኩ",
      "afaan_oromoo": "Teessoo email keessan ergaa."
  },
  "invalid_email": {
      "english": "Invalid Input! please send a valid email",
      "amharic": "የተሳሳተ ኢሜይል! እባክዎ ትክክለኛ ኢሜይል ይላኩ",
      "afaan_oromoo": "Dogoggora! maaloo email sirrii ergaa"
  },
  "ask_cv": {
      "english": "Please send your cv. Your cv must be .pdf, .doc or .docx format",
      "amharic": "እባክዎ CVዎትን ይላኩ 'CV'ዎ በ .pdf ፥ በ.doc ፥ ወይም በ .docx አይነት መሆን አለበት",
      "afaan_oromoo": "Maaloo 'CV' keessan ergaa. 'Cv'n ergitan gosoota .pdf, .doc yookin .docx ta'uu qaba"
  },
  "invalid_cv": {
      "english": "Invalid CV! Please send only supported document types. Your CV must be in .pdf, .doc, or .docx format",
      "amharic": "የተሳሳተ 'CV'! እባክዎ ከላይ የተባሉትን አይነት 'CV' ብቻ ይላኩ",
      "afaan_oromoo": "CV dogoggoraa! Maaloo gosa 'CV' ajajamtan qofa ergaa. Cvn ergitan gosoota .pdf, .doc yookin .docx ta'uu qaba"
  },
  "ask_bio": {
      "english": "Write something about yourself that will be added to your profile(Bio)",
      "amharic": "በግለታሪክዎ(Bio) ላይ የሚጨመር ስለራስዎ ማብራርያ ይፃፉ",
      "afaan_oromoo": "Waa'ee keessan kan profaayila (Bio)keesssan irratti dabalamu xiqeessaatii barreessaa"
  },
  "ask_gender": {
      "english": "What's your gender?",
      "amharic": "ዖታዎን ይምረጡ",
      "afaan_oromoo": "Koorniyaan keessan maalidha?"
  },
  "male": {
      "english": "Male",
      "amharic": "ወንድ",
      "afaan_oromoo": "Dhiira"
  },
  "female": {
      "english": "Female",
      "amharic": "ሴት",
      "afaan_oromoo": "Dhalaa"
  },
  "type_your_message": {
      "english": "Type your message...",
      "amharic": "መልዕክትዎን ይፃፉ...",
      "afaan_oromoo": "Ergaa keessan barreessaa..."
  },
  "type_your_message_for_admin": {
      "english": "Type your message for the admin",
      "amharic": "ለ Maroset አስተዳዳሪ መልዕክትዎን ይፃፉ",
      "afaan_oromoo": "Bulchaa Marosetif ergaa barreessaa"
  },
  "type_your_message_for_user": {
      "english": "Type your message for [{fname}](tg://user?id={to_id}):", # <a href='tg://user?id={tg_id}'>{name}</a>
      "amharic": "መልዕክትዎን ለ [{fname}](tg://user?id={to_id}):ይፃፉ ",
      "afaan_oromoo": "Ergaa keessan [{fname}](tg://user?id={to_id}):f barreessaa"
  },
    "applying_message": {
        "english": "Type Your application for the job owner", 
        "amharic": "የስራ ማመልከቻዎን ለስራው ባለቤት ይፃፉ:",
        "afaan_oromoo": "Iyyata hojii keessanii abbaa hojichaatif barreessaa:"
    },
    "confirm_applying_without_cv": {
        "english": "You don't have cv, you can upload your cv by clicking the 'upload cv' button below or you can continue applying without cv\nDo you want to send this job application?", 
        "amharic": "CV የለዎትም CVዎን ለመጫን Upload CV የሚለውን አዝራር በመጠቀም መጫን ይችላሉ ሆኖም ማመልከቻዎን ያለ CVም መላክ ይችላሉ\nይህን ማመልከቻ መላክ ፈልገዋል?",
        "afaan_oromoo": "CV hin qabdanu, Cv keessan qabduu asii gadii kan 'upload cv' jedhu cuqaasun erguu dandeessu yookin CV malees iyyata kana erguu dandeessu \nIyyata hojii kana erguu barbaaddanii jirtuu?"
    },
    "confirm_applying_with_cv": {
        "english": "Do you want to send this message? Your cv will be included!", 
        "amharic": "ይህን ማመልከቻ መላክ ይፈልጋሉ?(CVዎም አብሮ ይላካል)",
        "afaan_oromoo": "Iyyata kana erguu barbaadduu? Cvn keessanis itti dabalama!"
    },
    "job_applying_canceled": {
        "english": "Your procces for applying has been canceled!", 
        "amharic": "የማመልከቻ ሂደትዎ ተሰርዟል!",
        "afaan_oromoo": "Adeemsi iyyata keessanii haqameera!"
    },
  "only_text_are_allowed_when_applying": {
      "english": "Only texts are allowed when applying!", 
      "amharic": "ማመልከቻዎ በፊደል ብቻ ነው የሚፃፈው!",
      "afaan_oromoo": "Iyyata hojiitif qubee qofatu eeyyamama!"
  },
    "job_unavailable": {
        "english": "This job is no longer available",
        "amharic": "ይህ ስራ አሁን ላይ የለም!",
        "afaan_oromoo": "Hojiin kun ammatti hin jiru!"
    },
    "user_applying_again_warning": {
        "english": "Sorry! you can't apply for the same job twice", 
        "amharic": "ይቅርታ! ለአንድ ስራ ሁለት ጊዜ ማመልከት አይችሉም!",
        "afaan_oromoo": "Dhiifama! hojii tokkoof si'a lama iyyachuu hin dandeessanu!"
    },
    "applied_successfully": {
        "english": "Your application has been successfully sent to the job owner to be reviewed!", 
        "amharic": "ማመልከቻዎ ወደ ስራው ባለቤት በስኬት ተልኳል",
        "afaan_oromoo": "Iyyanni keessan milkiin gara abbaa hojichaatti madaallif ergameera!",
    "ask_to_close_job_and_broadcast": {
        "english": "Do you want to close this job?\nYou should send message/broadcast to all users who have applied to this job but haven't been hired/shortlisted", 
        "amharic": "ይህን የስራ ማስታወቂያዎትን መዝጋት ይፈልጋሉ?\n(ከሆነ እባክዎ ለሁሉም ላልተመረጡት አመልካቾች አለመመረጣቸውን እና ለቀጣይ የስራ ማመልከቻ ማሻሻል ያለባቸውን ነገር በአንድ ላይ ይፃፉላቸው(ልብ ይበሉ! ይህን ማድረግ ግዴታዎ ነው!",
        "afaan_oromoo": "Beeksisa hojii kana cufuu barbaadduu?\nYoo ta'e maaloo iyyattoota hojii kanaaf iyyatanii garuu hin filatamneef, filatamuu dhabuu isaanii fi yeroo biraatif waan foyyeessuu qaban hundumaafuu si'a tokkoon ergaa erguun beeksisaa\n(Hubachiisa:Kana gochuun dirqama keessanii dha!)"
    },
    "send_the_broadcast_message": {
        "english": "Send the message you want to send to the applicants.", 
        "amharic": "ለ አመልካቾች መልዕክትዎን ይፃፉ.",
        "afaan_oromoo": "Iyyattootaaf ergaa erguu barbaaddan barreessaa."
    },
    "confirm_broadcast_and_close": {
        "english": "Do you want to send this message and close the job?", 
        "amharic": "ይህን መልዕክት መላክ ይፈልጋሉ?",
        "afaan_oromoo": "Ergaa kana erguun beeksisa hojii keessanii cufuu barbaadduu?"
    },
    "no_one_applied_for_this_job": {
        "english": "This feature is not available for old jobs or no one has applied for this job", 
        "amharic": "ይህ ባህሪ አሁን ላይ የለም ወይም ለስራው እስከ አሁን ማንም አላመለከተም",
        "afaan_oromoo": "Amalli kun hojiiwwan darbaniif hin hojjatu yookin namuu hojii kanaaf hin iyyanne",
    "register_new_company": {
      "english": "Register New Company",
      "amharic": "አዲስ ኩባንያ ያስመዝግቡ",
      "afaan_oromoo": "Kuubbaaniyaa haaraa galmeessaa"
    },
    "manage_company": {
      "english": "Manage Company",
      "amharic": "ኩባንያዎትን ያስተዳድሩ",
      "afaan_oromoo": "Kubbaaniyaa hoogganaa"
    },
    "company_page_message": {
      "english": "You can create and manage Company here!",
      "amharic": "እዚህ ኩባንያ መስገባት እና ማስተዳደር ይችላሉ!",
      "afaan_oromoo": "Asitti kuubbaaniyaa galchuu fi hoogganuu dandeessu!"
    },
    "you_dont_have_registerd_company": {
      "english": "You currently don't have a registerd company/startup!\nstart by registering one",
      "amharic": "እስካሁን የተመዘገበ ኩባንያም ሆነ ጀማሪ ድርጅት/Startup የለዎትም!\nበማስመዝገብ ይጀምሩ",
      "afaan_oromoo": "Ammatti Kuubbaaniyaa galmaa'e hin qabdanu/startup!\nGalmeessuun jalqabaa"
    },
    "company": {
      "english": "Company",
      "amharic": "ኩባንያ",
      "afaan_oromoo": "Kuubbaaniyaa"
    },
    "startup": {
      "english": "Startup",
      "amharic": "ጀማሪ ድርጅት",
      "afaan_oromoo": "Dhaabbata eegalaa"
    },
    #     -----------------
    #   Company Registration
    #     -----------------
    "ask_company_type": {
      "english": "Which one represent your bussines?",
      "amharic": "ድርጅትዎን የቱ ይወክለዋል?",
      "afaan_oromoo": "Dhaabbata keessan kamtu bakka bu'a?"
    },"ask_the_company_name": {
      "english": "Send the company name",
      "amharic": "የኩባንያዎትን ስም ይላኩ",
      "afaan_oromoo": "Maqaa Kuubbaaniyaa keessan ergaa"
    },
    "ask_company_logo": {
      "english": "Send the company logo(as picture)",
      "amharic": "የኩባንያዎን አርማ በምስል መልክ ይላኩ",
      "afaan_oromoo": "Asxaa/Faajjii Kuubbaaniyaa keessan fakkiidhan ergaa"
    },
    "ask_industry_field": {
      "english": "Select the company sector, If you do not see your industry or sector listed, please write it in the space provided below. This will help us categorize your business accurately.",
      "amharic": "የኩባንያዎትን ሴክተር ከዚህ በታች ከተዘረዘሩት መካከል ይምረጡ, ከተዘረዘሩት መካከል ካላገኙ, እባክዎ ለምደባ ይጠቅመን ዘንድ ከታች ባለው ባዶ ቦታ ፅፈው ይላኩልን",
      "afaan_oromoo": "Seektara Kuubbaaniyaa keessanii filadhaa, Kanneen asii gadiitti tarreeffaman keessaa yoo dhabdan, Ramaddii seektarootaatif waan nu fayyaduuf maaloo bakka duwwaa asii gadiitti barreessun nuf ergaa. "
    },
    "ask_established_year": {
      "english": "Send the year of establishment\nUse this format 2023-05-24",
      "amharic": "ኩባንያዎት የተመሰረተበትን ጊዜ ይላኩልን (እባክዎ ይህንን ይከተሉ->ዓ.ም/ወር/ቀን",
      "afaan_oromoo": "Yeroo hundeeffama kuubbaaniyaa keessanii ergaa\nFoormaatii kanaan nuf ergaa->bara/ji'a/guyyaa"
    },
    "ask_company_email": {
      "english": "send the company email",
      "amharic": "የኩባንያዎን የ ኢሜይል አድራሻ ይላኩ",
      "afaan_oromoo": "Teessoo email kuubbaaniyaa keessanii ergaa"
    },
    "ask_company_website": {
      "english": "Send the company's website",
      "amharic": "የኩባንያዎን ድህረገፅ ይላኩ",
      "afaan_oromoo": "Marsaaritii Kuubbaaniyaa keessanii ergaa"
    },
    "ask_company_phone": {
      "english": "Send the company's phone number\nPlease use this format +251",
      "amharic": "የኩባንያዎትን ስልክ ቁጥር ይላኩ\nእባክዎ ይህን ይከተሉ +251",
      "afaan_oromoo": "Lakkoofsa bilbila Kuubbaaniyaa keessanii ergaa\nMaaloo formaatii kana fayyadamaa +251"
    },
    "ask_company_country": {
      "english": "Select the company's country",
      "amharic": "ኩባንያዎት የሚገኝበትን ሀገር ይምረጡ",
      "afaan_oromoo": "Biyya Kuubbaaniyichaa filadhaa"
    },
    "type_company_country": {
      "english": "Type the country of the company",
      "amharic": "ኩባንያዎት የሚገኝበትን ሀገር ይፃፉ",
      "afaan_oromoo": "Biyya Kuubbaaniyichaa barreessaa"
    },
    "ask_company_city": {
      "english": "Select the company's city",
      "amharic": "ኩባንያዎት የሚገኝበትን ከተማ ይምረጡ",
      "afaan_oromoo": "Magaalaa Kuubbaniyichaa filadhaa"
    },
    "type_company_city": {
      "english": "Type the company's city",
      "amharic": "ኩባንያዎት የሚገኝበትን ከተማ ይፃፉ",
      "afaan_oromoo": "Magaalaa Kuubbaaniyichaa barreessaa"
    },
    "ask_company_postal_code": {
      "english": "Send the company's postal code",
      "amharic": "የኩባንያዎትን የ ፖስታ ሳጥን ቁጥር ይላኩ",
      "afaan_oromoo": "Lakkoofsa saanduqa poostaa Kuubbaniyichaa ergaa"
    },
    "ask_company_tin_number": {
      "english": "Send the company's TIN",
      "amharic": "የኩባንያዎትን የግብር መለያ ቁጥር/TIN ይላኩ",
      "afaan_oromoo": "Lakkoofsa TIN Kuubbaaniyichaa ergaa\Hubachiisa"
    },
    "ask_company_trade_license": {
      "english": "Send the company's trade license(send it as image)",
      "amharic": "የኩባንያዎትን የንግድ ፍቃድ በምስል መልክ ይላኩ",
      "afaan_oromoo": "Eeyyama daldala Kuubbaaniyaa keessanii ergaa(Fakkiidhan)"
    },
    "ask_company_detail": {
      "english": "Send discription about the company it should have atleast 13 < words",
      "amharic": "ስለኩባንያዎት ማብራርያ ይፃፉ (ማብራርያው ቢያንስ 13 ቃላት እና ከዛ በላይ መሆን አለበት)",
      "afaan_oromoo": "Ibsa waa'ee Kubbaaniyichaa barreessaa, ibsi kun yoo xiqqaate jechoota 13 yookin isaan ol ta'uu qaba"
    },
    "ask_social_links": {
      "english": "Add your social links (Optional)",
      "amharic": "የኩባንያዎትን ማህበራዊ ሚዲያ ማያያዣ/link ይጨምሩ (ከሌለ ይዝለሉ)",
      "afaan_oromoo": "Geessituuwwan miidiyaa hawaasaa dabalaa(Yoo hin jiraanne darbaa)"
    },
    "ask_media_link": {
      "english": "Send the media link",
      "amharic": "የሚዲያ ማያያዣ/link ይላኩ (ከሌለ ይዝለሉ)",
      "afaan_oromoo": "Geessituu miidiyaa ergaa"
    },
    "invalid_logo": {
      "english": "Invalid input!\nMake sure to send a photo",
      "amharic": "የተሳሳተ መረጃ!\nእባክዎ በምስል ይላኩ!",
      "afaan_oromoo": "Galtee hin taane!\Fakkii sirrii erguu keessan mirkaneessaa"
    },
    "invalid_year": {
      "english": "Invalid input!\nMake sure to use this format year-month-day | 2020-01-02",
      "amharic": "የተሳሳተ መረጃ!\n እባክዎ በዚህ መልኩ (ዓ.ም/ወር/ቀን) ማስገባትዎን ያረጋግጡ",
      "afaan_oromoo": "Galtee hin taane!\nFoormaatii isa kana (bara-ji'a-guyyaa) fayyadamuu keessan mirkaneessaa "
    },
    "invalid_link": {
      "english": "Invalid input!\nMake sure to use this format https://maroset.com",
      "amharic": "የተሳሳተ መረጃ!\nእባክዎ በዚህ መልኩ https://maroset.com ማስገባትዎን ያረጋግጡ",
      "afaan_oromoo": "Galtee hin taane!\nFoormaatii kana fayyadamuu keessan mirkanessaa https://maroset.com"
    },
    "invalid_phone": {
      "english": "Invalid input!\nMake sure to start with '+' and length of 13",
      "amharic": "የተሳሳተ መረጃ!\nእባክዎ በ + መጀመርዎን እና 13 የዲጅት ብዛት ማስገባትዎን ያረጋግጡ",
      "afaan_oromoo": "Galtee hin taane!\Mallattoo ida'uu (+)tin jalqabuu keesssanii fi baay'ini diijitii fayyadamtan 13 ta'uu isaa mirkaneessaa"
    },
    "invalid_country": {
      "english": "Use only the buttons to choose country!",
      "amharic": "የተሳሳተ መረጃ! እባክዎ የተቀመጡትን አዝራሮች ብቻ ተጠቅመው ሀገርዎን ይምረጡ!",
      "afaan_oromoo": "Maaloo biyya filachuuf qabduuwwan asii gadii qofa fayyadamaa!"
    },
    "invalid_postal_code": {
      "english": "Invalid input!\nThe length should be between 4-12 and it should contain only numbers",
      "amharic": "የተሳሳተ መረጃ!\nእባክዎ የተጠቀሙት የዲጅት ብዛት ከ4-12 እንዲሁም ሁሉም ቁጥሮች መሆናቸውን ያረጋግጡ",
      "afaan_oromoo": "Galtee hin taane!\nMaaloo baay'ini diijitii fayyadamtan 4-12 fi hundumtuu lakkoofsoota ta'uu qabu"
    },
    "invalid_tin_number": {
      "english": "Invalid input!\nThe length should be greater that 5 and it should contain only numbers",
      "amharic": "የተሳሳተ መረጃ!\nእባክዎ የተጠቀሙት የዲጅት ብዛት ከ 5 በላይ እንዲሁም ሁሉም ቁጥሮች መሆናቸውን ያረጋግጡ",
      "afaan_oromoo": "O Invalid input!\nMaaloo baay'ini diijitii fayyadamtan shanii olii fi hundumtuu lakkofsoota ta'uu qaba"
    },
    "invalid_trade_license": {
      "english": "Invalid input!\nSend photo",
      "amharic": "የተሳሳተ መረጃ!\nእባክዎ በምስል ይላኩ",
      "afaan_oromoo": "Galtee hin taane!\nMaaloo fakkiidhan ergaa"
    },
    "invalid_company_detail": {
      "english": "Try to make it longer!\n it should have atleast 13 < words",
      "amharic": "እባክዎ ጨምረው ይፃፉ \n የሚጠቀሙት ቃላት ብዛት ከ 13 በላይ መሆን አለበት",
      "afaan_oromoo": "Maaloo dabalaatii barreesaa!\nYoo xiqqaate jechoota 13 fi sanaa ol ta'uu qaba"
    },
    "the_registration_has_been_canceled": {
      "english": "The registration has been canceled:",
      "amharic": "ምዝገባው ተቋርጧል!:",
      "afaan_oromoo": "Galmeen haqameera:"
    },
    "The company has been sent to admin": {
      "english": "Your company has been sent to the Maroset admins for approval",
      "amharic": "ያስመዘገቡት ኩባንያ ለግምገማ ወደ Maroset አስተዳዳሪዎች ተልኳል!",
      "afaan_oromoo": "Kuubbaaniyaan galmeesistan gara bulchitoota Maroset itti ergameera!"
    },
    "warning_company": {
      "english": "Remember once the company has approved you can't edit it!",
      "amharic": "እባክዎ ልብ ይበሉ! ያስመዘገቡት ኩባንያ አንዴ ከፀደቀልዎት ማስተካከል/edit አይችሉም!",
      "afaan_oromoo": "Maaloo yaadadhaa, Kuubbaaniyaan keessan takka mirkanoofnaan gulaaluu hin dandeessanu!"
    },
    "this_company_has_been_approved": {
      "english": "Congratulations! your company has been reviewed and approved!",
      "amharic": "እንኳን ደስ ያልዎት! ኩባንያዎ ፀድቆልዎታል!",
      "afaan_oromoo": "Baga gammaddan! Kuubbaaniyaan keessan mirkanaa'eera!"
    },
    "your_company_has_been_approved": {
      "english": "Your company has been approved.\nnow you can post job as a company",
      "amharic": "ኩባንያዎ ስለፀደቀልዎት አሁን እንደ ኩባንያ ስራ መለጠፍ ይችላሉ",
      "afaan_oromoo": "Baga gammaddan Kuubbaaniyaan keessan mirkanaa'eera.\namma akka Kuubbaaniyaatti beeksisa hojii maxxansuu dandeessu"
    },
    "this_company_has_been_rejected": {
      "english": "This company has been rejected!",
      "amharic": "A This company has been rejected!",
      "afaan_oromoo": "Maaloo Kuubbaaniyaan kun hin mirkanoofne!"
    },
    "your_company_has_been_rejected": {
      "english": "Sorry! Your company has been rejected. Please make sure to submit the required inputs and register again",
      "amharic": "ይቅርታ! ኩባንያዎት አልፀደቀልዎትም, እባክዎ የተጠየቁትን መረጃዎች ማስገባትዎን አረጋግጠው እንደገና ያስመዝግቡ",
      "afaan_oromoo": "Dhiifama! Kuubbaaniyaan keessan hin mirkanoofne. Maaloo galtee gaafatamtan galchuu keessan mirkaneessaatii irra deebi'uun galmeessisaa"
    },
    "are_you_sure_you_want_to_delete_this_company": {
      "english": "Do you really wanted to delete your company from the maroset bot!!",
      "amharic": "እርግጠኛ ኖት ኩባንያዎትን ከ Maroset ቦት ላይ ማጥፋት ፈልገዋል?",
      "afaan_oromoo": "Bootii Maroset irraa Kuubbaaniyaa keessan Haquu/delete barbaaddanii jirtuu?"
    },
    "the_company_deleted_succesfully": {
      "english": "Your company has been deleted from maroset database.",
      "amharic": "ኩባንያዎትን ከ Maroset የመረጃ ቇት ላይ በትክክል አጥፍተዋል",
      "afaan_oromoo": "Kuubbaaniyaan keessan kuusa deetaa Maroset irraa haqameera."
    },
    "ask_founders_name": {
      "english": "Send the founders and key members' full name.\nEach full name in new line",
      "amharic": "የመስራቾችን እና ወሳኝ አባላትን መደበኛ እና ሙሉ ስም ይላኩ\nየእያንዳንዱን ስም በአዲስ መስመር ላይ ይፃፉ",
      "afaan_oromoo": "Maqaa guutuu kan hundeessitootaa fi Miseensoota barbaachisoo ergaa.\nmaqaa guutuu tokkoon tokoo sarara haaraa irratti barreessaa"
    },
    "invalid_founders_name": {
      "english": "Invalid name!\ntype each full name in new line like:\nAbiy Ahmed\nAdanech Abebe",
      "amharic": "የተሳሳተ ስም!\nእባክዎ በትክክል ያስገቡ ለምሳሌ:\nአቢይ አህመድ\nአዳነች አቤቤ",
      "afaan_oromoo": "Galtee hin taane!\nMaqaa guutuu tokkoon tokkoo sarara haaraa irratti barreessaa, fakkeenyaaf:\nAbiyy Ahimad\nAdaanach Abeebee\n"
    },"ask_the_startup_name": {
          "english": "Send the startup's name",
          "amharic": "የጀማሪ ድርጅትዎን ስም ይላኩ",
          "afaan_oromoo": "Maqaa kuubbaaniyaa eegalaa keesan ergaa"
        },
        "ask_startup_logo": {
          "english": "Send the logo(as image)",
          "amharic": "የድርጅትዎን አርማ በምስል መልክ ያስገቡ",
          "afaan_oromoo": "Asxaa/Faajjii fakkiidhan ergaa"
        },
        "ask_startup_industry_field": {
          "english": "Select the startup's sector, If you couldn't see your industry or sector listed, please write it in the space provided below. This will help us categorize your business accurately.",
          "amharic": "የጀማሪ ድርጅትዎን ዘርፍ ከታች ከተዘረዘሩት መካከል ይምረጡ፥ የእርሶ ድርጅት ከተዘረዘሩት መካከል ከሌለ ለምደባ ይጠቅም ዘንድ በተቀመጠው ባዶ ቦታ ላይ ይፃፉ",
          "afaan_oromoo": "Seektara dhaabbata keessanii filannoo asii gadii keessaa filadhaa, filannoo asii gadii keessatti yoo hin jiraanne maaloo iddoo duwwaa isiniif kenname irratti barreessuun ergaa kunis dhaabbata keessa akka ramaddii keessa isiniif galchinu nu fayyada "        },
        "ask_startup_established_year": {
          "english": "Send the year of establishment\nUse this format (Year/Month/Day)",
          "amharic": "ጀማሪ ድርጅትዎ የተመሰረተበትን ጊዜ ይላኩ እባክዎ በዚህ መልኩ (ዓ.ም/ወር/ቀን) ይላኩ ",
          "afaan_oromoo": "Bara hundeeffama dhaabbata eegalaa  keessanii ergaa\nfoormaatii kana (Bara/Ji'a/Guyyaa) fayyadamaa "
        },
        "ask_startup_email": {
          "english": "send the startup's email",
          "amharic": "እባክዎ የድርጅትዎን የኢሜይል አድራሻ  ይላኩ",
          "afaan_oromoo": "Teessoo email dhaabbata keessanii ergaa"
        },
        "ask_startup_website": {
          "english": "Send the startup's website",
          "amharic": "የድርጅትዎን ድህረ-ገፅ ይላኩ",
          "afaan_oromoo": "Marsaaritii dhaabbata keessanii ergaa"
        },
        "ask_startup_phone": {
          "english": "Send the startup's phone number\nUse this format +251",
          "amharic": "እባክዎ የጀማሪ ድርጅትዎን የስልክ ቁጥር በዚህ መልኩ +251 ይላኩ",
          "afaan_oromoo": "Lakkoofsa bilbila dhaabbata keessanii ergaa\nFoormaatii kana fayyadamaa +251"
        },
        "ask_startup_country": {
          "english": "Select the startup's country",
          "amharic": "እባክዎ ጀማሪ ድርጅትዎ የሚገኝበትን ሀገር ይምረጡ",
          "afaan_oromoo": "Biyya dhaabbatni keessan itti argamu filadhaa"
        },
        "type_startup_country": {
          "english": "Type the country of the startup",
          "amharic": "እባክዎ ጀማሪ ድርጅትዎ የሚገኝበትን ከተማ ይምረጡ",
          "afaan_oromoo": "Biyya dhaabbatni keessan itti argamu barreessaa"
        },
        "ask_startup_city": {
          "english": "Select the startup's city",
          "amharic": "እባክዎ ድርጅትዎ የሚገኝበትን ከተማ ይምረጡ",
          "afaan_oromoo": "Maaloo magaalaa dhaabbatni keessan itti argamu filadhaa"
        },
        "type_startup_city": {
          "english": "Type the startup's city",
          "amharic": "እባክዎ ድርጅትዎ የሚገኝበትን ከተማ ይፃፉ",
          "afaan_oromoo": "Magaalaa dhaabbatni keessa itti argamu barreessaa"
        },
        "ask_startup_detail": {
          "english": "Send discription about the startup, it should have atleast 13 or more words",
          "amharic": "ስለ ጀማሪ ድርጅትዎ ማብራርያ ይፃፉ, የሚፅፉት ማብራርያ ቃላት ብዛት ከ 13 መብለጥ አለበት",
          "afaan_oromoo": "Maaloo ibsa dhaabbata keessanii ergaa, ibsi ergitan baay'ina jechoota 13 ol ta'uu qaba"
        },
    "type_the_report_detail": {
      "english": "Type detail about your report",
      "amharic": "ስለክስዎ እባክዎ በቂ ማብራርያ ይፃፉ",
      "afaan_oromoo": "Himannaa keessan maaloo ibsaa"
      },
  "confirm_job_report": {
    "english": "Do you really wanted to report this?",
    "amharic": "መክሰስ ፈልገዋል?",
    "afaan_oromoo": "Himachuu barbaaddanii jirtuu?"
  },
  "reported_successfully": {
    "english": "Thank You! Your report has been sent to the admins",
    "amharic": "እናመሰግናለን! ክስዎት ወደ Maroset አስተዳዳሪዎች በስኬት ተልኳል",
    "afaan_oromoo": "Galatoomaa! Himannaan keessan gara bulchitoota Maroset itti ergameera"
  }
  
  

}

# print(bot_messages["ask_title"])
# print(bot_messages["ask_title"]["english"])
