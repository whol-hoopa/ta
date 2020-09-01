from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime, time, random

Trivia_websites = ["Websites, ..."]
Questions = [["Cassie the Ponycorn teaches this kind of spell:", "Ether Shield protects against what?", "How many pips does it cost to cast Dr. Von's Monster?", "How many pips does it cost to cast STORMZILLA?", "If you can cast Storm Trap, Wild Bolt, Catalan, and the Tempest spell, what are you POLYMORPHED as?", "If you're a storm wizard with 4 power pips and 3 regular pips, how powerful would your supercharge charm be?", "MILDRED FARSEER teaches you what kind of spell?", "MORTIS can teach you this.", "Tish'Mah specializes in spells that mostly affect these:", "What does FORSAKEN BANSHEE do?", "What isn't a shadow magic spell?", "What level of spell does ENYA FIREMOON Teach?", "What term best fits STAR MAGIC Spells?", "What term best fits SUN MAGIC Spells?", "What type of spells are ICE, FIRE, and STORM?", "Which FIRE SPELL both damages and heals over time?", "Which spell can't be cast while polymorphed as a Gobbler?", "Which spell would not be very effective when going for the ELIXIR VITAE BADGE?", "Who can teach you the LIFE SHIELD Spell?", "Who teaches you BALANCE magic?"], #Wizard101 Spells Questions
                 ["An unmodified SUN SERPENT does what?", "How long do you have to wait to join a new MATCH after fleeing in PVP?", "In Grizzleheim, the RAVENS want to bring about:", "SHAKA ZEBU is known best as:", "What determines the colors of the MANDERS in Krok?", "What does the TIME RIBBON PROTECT against?", "What hand does LADY ORIEL hold her wand in?", "What is Professor FALMEA’S favorite food?", "What is the name of the book stolen from the ROYAL MUSEUM?", "What is the name of the new DANCE added with KHRYSALIS?", "What is the name of the SECRET SOCIETY in Krokotopia?", "What is unique about Falmea’s CLASSROOM?", "What school is the GURTOK DEMON focused on?", "What school is the spell DARK NOVA?", "What type of rank 8 spell is granted to DEATH students at level 58?", "Which Aztecan ponders the GREAT QUESTIONS of Life?", "Which of these are NOT a LORE spell?", "Which of these is NOT a ZAFARIA ANCHOR STONE?", "Who is in the top level of the TOWER OF THE HELEPHANT?", "Who is the BEAR KING of Grizzleheim?", "What school is the spell Dark Nova", "What is unique about Falmea's Classroom?", "What hand does Lady Oriel hold her wand in?", "An unmodified Sun Serpent does what?", "What is the name of the secret society in Krokotopia", "What is Professor Falmea's favorite food?"], #Wizard101 Adventuring Questions 
                 ["Benevolent", "impetuous", "hegemony", 'Peruse', 'Deleterious', 'Evanescent', 'Antithesis', 'Fortuitous', 'Sensuous', 'Jovial', 'Brazen', 'Loquacious', 'Chicanery', 'Guru', 'Conundrum', 'Enervate'], #Twelfth Grade Vocaulary Questions
                 ['What is the state bird of West Virginia?', 'What is the state bird of Illinois?', 'What is the state bird of Wyoming?', 'What is the state bird of Missouri?', 'What is the state bird of Michigan?', 'What is the state bird of Connecticut?', 'What is the state bird of Idaho?', 'What is the state bird of Arizona?', 'What is the state bird of Oklahoma?', 'What is the state bird of Mississippi?', 'What is the state bird of Nebraska?', 'What is the state bird of Utah?', 'What is the state bird of Minnesota?', 'What is the state bird of South Dakota?', 'What is the state bird of New Jersey?', 'What is the state bird of Delaware?', 'What is the state bird of Oregon?', 'What is the state bird of Tennessee?', 'What is the state bird of Florida?', 'What is the state bird of Maryland?', 'What is the state bird of Massachusetts?', 'What is the state bird of Pennsylvania?', 'What is the state bird of Georgia?', 'What is the state bird of Kansas?', 'What is the state bird of Indiana?', 'What is the state bird of Alaska?', 'What is the state bird of Washington?', 'What is the state bird of Alabama?', 'What is the state bird of New York?', 'What is the state bird of Vermont?', 'What is the state bird of Louisiana?', 'What is the state bird of New Mexico?', 'What is the state bird of North Dakota?', 'What is the state bird of Wisconsin?', 'What is the state bird of Maine?', 'What is the state bird of Ohio?', 'What is the state bird of Nevada?', 'What is the state bird of California?', 'What is the state bird of Colorado?', 'What is the state bird of Iowa?', 'What is the state bird of Texas?', 'What is the state bird of Montana?', 'What is the state bird of South Carolina?', 'What is the state bird of Kentucky?', 'What is the state bird of Arkansas?', 'What is the state bird of Hawaii?', 'What is the state bird of North Carolina?', 'What is the state bird of New Hampshire?', 'What is the state bird of Rhode Island?'], #State Bird Questions
                 ['How many WORLDS of The Spiral are unlocked as of May 21st, 2014?', 'MERLE AMBROSE is originally from which world?', 'What book does Professor Drake send you to the library to check out?', "What can be used to diminish the Nirini's powers in Krokotopia?", 'What color is the DOOR inside the boys dormroom?', 'What did PROSPECTOR ZEKE lose track of in MooShu?', 'What is the shape of the pink piece in POTION MOTION?', 'What is the title of the book that is floating around the Wizard City Library?', "What's the name of the balance tree?", 'Which below are NOT a type of ONI in MooShu?', 'Which is the only school left standing in DRAGONSPYRE?', 'Which of these LOCATIONS is not in Wizard City?', 'Which one of these are not a symbol on the BATTLE SIGIL?', 'Who guards the entrance to UNICORN WAY?', 'Who is the NAMELESS KNIGHT?', 'Who is the REGISTRAR of Pigswick Academy?', 'Who prophesizes this? "The mirror will break, The horn will call, From the shadows I strike , And the skies will fall..."', "Who sells Valentine's Day items in Wizard City?", 'Why are the GOBBLERS so afraid to go home?', 'Why are the PIXIES and FAERIES on Unicorn Way evil?', 'ZAFARIA is home to what cultures?'], #Magical Trivia Answers
                 ['HRUNDLE FJORD is part of what section of Grizzleheim?', "In Reagent's Square, the Professor is standing in front of a:", 'In what world would you find the SPIDER TEMPLE', 'KING AXAYA KNIFEMOON needs what to unify the people around him?', "KING NEZA is Zenzen Seven Star's:?", 'THADDEUS PRICE is the Pigswick Academy Professor of what school?', 'What is used to travel to the ISLE OF ARACHNIS?', 'What was PONCE DE GIBBON looking for in Azteca', 'Where is the only PURE FIRE in the Spiral found?', 'Which VILLAIN terrorizes the fair maidens of MARLEYBONE?', 'Who asks you to find KHRYSANTHEMUMS?', 'Who did FALYNN GREENSLEEVES fall in love with?', 'Who gives you permission to ride the BOAT to the KROKOSPHINX?', 'Who haunts the NIGHT WARRENS?', "Who is the Emperor of Mooshu's Royal Guard?", 'Who is the only person who knows how to enter the TOMB OF STORMS?', 'Who takes you across the RIVER OF SOULS?', 'Who tells you how to get to AQUILA?', 'Who was ordered to guard the SWORD OF KINGS?', 'Who was the greatest AQUILAN GLADIATOR of all time?', "What was Ponce de Gibbon looking for in Azteca?"], #Mystical Trivia Questions
                 ['How many portal summoning candles are in the Burial Mound?', 'Kirby Longspear was once a student of which school of magic?', "Sir Edward Halley is the Spiral's most famous:", 'The Swordsman Destreza was killed by:', 'What book was Anna Flameright accused of stealing?', 'What did Abigail Dolittle accuse Wadsworth of stealing?', 'What is the shape on the weather vanes in the Shopping District?', 'What level must you be to wear Dragonspyre crafted clothing?', 'What was the name of the powerful Grendel Shaman who sealed the runic doors?', 'Which Queen is mentioned in the Marleybone book "The Golden Age"?', "Who is Bill Tanner's sister?", 'Who is NOT a member of the Council of Light?', 'Who is the King of the Burrowers?'], #Conjuring Trivia Questions
                 ['Arthur Wethersfield is A:..', 'What color are the Marleybone mailboxes?', 'What course did Herold Digmoore study?', 'What did Prospector Zeke lose in Marleybone?', 'What event is Abigail Doolittle sending out invitations for?', "What initials were on the doctor's glove?", 'What is a very common last name of the cats in Marleybone?', "What is flying around in Regent's Square?", "What is Sgt. Major Talbot's full name?", 'What sort of beverage is served in Air Dales Hideaway?', 'What style of artifacts are in the Royal Museum?', 'What time of day is it always in Marleybone?', 'What time does the clock always read in Marleybone?', 'What transports you from place to place in Marleybone?', 'What two names are on the Statues in the Marleybone cathedral?', "Which is not a street in Regent's Square?", 'Which of these folks can you find in the Royal Museum?', "Which symbol is not on the stained glass window in Regent's Square?", "Who is not an officer you'll find around Marleybone?", 'Who is the dangerous criminal that is locked up, but escapes from Newgate Prison?'], #Marleybone Trivia Questions
                 ['In AZTECA, MORGANTHE enlisted the help of the:', 'Morganthe got the Horned CROWN from the SPRIGGAN:', 'SUMNER FIELDGOLD twice asks you to recover what for him?', 'The SWALLOWS of Caliburn MIGRATE to Avalon from where each year?', 'What badge do you earn by defeating 100 Samoorai?', "What does Silenus name you once you've defeated Hades?", 'What special plant was BARLEY developing in his Garden?', 'Where has PHARENOR been imprisoned?', 'Who helps Morganthe find the Horn of HURACAN?', 'Who grants the FIRST SHADOW Magic SPELL?', "Who is Haraku Yip's APPRENTICE?", 'Who makes the harpsicord for Shelus?', 'Who needs the HEALING POTION from Master Yip?', 'Who taunts: Why I oughta knock you to the moon, you PESKY LITTLE CREEP!', 'Who taunts you with: "Prepare to be broken, kid!"', 'Who taunts you with: "Wizard, you will know the MEANING of the word PAIN after we battle!"', 'Who tells you: "A SHIELD is just as much a weapon as the sword."', 'Who tells you to speak these words only unto your MENTOR: "Meena Korio Jajuka!"', 'Who thinks you are there to take their precious FEATHERS?', 'Who tries to raise a GORGON ARMY?'], #Spellbinding Trivia Questions
                 ['What are the main COLORS for the MYTH school?', 'What are the school COLORS of BALANCE?', 'What does every ROTTING FODDER in the Dark Caves carry with them?', "What is diego's full name?", "What is Mindy's last name (she's on Colossus Blvd)?", 'What is something that the GOBBLERS are NOT stockpiling in Colossus Way?', 'What is the GEMSTONE for BALANCE?', 'What is the name of the GRANDFATHER tree?', 'What is the name of the ICE TREE in Ravenwood?', 'What is the name of the school newspaper? Boris Tallstaff knows...', 'What school does MALORN ASHTHORN think is the best?', 'What school is all about CREATIVITY?', 'Where is SABRINA GREENSTAR?', 'Who is the FIRE school PROFESSOR?', 'Who is the PRINCESS of the SERAPHS?', 'Who is the Wizard City MILL FOREMAN?', 'Who resides in the HEDGE MAZE?', 'Who sang the Dragons, Tritons and Giants into existance?', 'Who TAUGHT LIFE Magic before Moolinda Wu?', 'What is the name of the BRIDGE in front of the Cave to Nightside?'], #WizardCity Trivia Questions
                 ] 
Answers = [["Prism", "Life and Death attacks", "9", "5", "Ptera", "110%", "Dispels", "Tranquilize", "Minions", "375 damage plus a hex trap", "Ebon Ribbons", "80", "Auras", "Enchantment", "Elemental", "Power Link", "Pie in the sky", "Entangle", "Sabrina Greenstar", "Alhazred"], #Wizard101 Spells Trivia Answers
               ["900-1000 Fire Damage + 300 Fire Damage to entire team", "5 minutes", "The Everwinter, to cover the world in ice:", "The Greatest Living Zebra Warrior", "Where they come from and their school of focus.", "Time Flux", "Trick question, she has a sword", "Pasta Arribata", "The Krokonomicon", "The bee dance", "Order of the Fang", "There are scortch marks on the ceiling", "Balance", "Shadow", "Damage + DoT","Philosoraptor", "Fire Dragon", "Rasik Anchor Stone", "Lyon Lorestriker", "Valgard Goldenblade", "Shadow", "There are scorch marks on the ceiling", "Trick question, she has a sword.", "900 � 1000 Fire Damage + 300 Fire Damage to entire team", "Order of the Fang", "Pasta Arrabiata"], #Wizard101 Adventuring Answers
               ["showing or motivated by sympathy and understanding and generosity", "characterized by undue haste and lack of thought or deliberation", 'one country/group has leadership over another', 'reading with careful attention', 'harmful to living things', 'tending to vanish like vapor', 'the direct opposite or contrast to a previously given assertion', 'occurring by happy chance', 'all senses, dealing w/ all senses', 'happy, cheery', 'unrestrained by convention or propriety', 'talkative, chatty', 'deceiving someone, scam', 'religious teacher', 'a difficult problem', 'to weaken, or to take energy from'], #Twelfth Grade Vocabulary Answers
               ['Cardinal', 'Cardinal', 'Western Meadowlark', 'Eastern Bluebird', 'American Robin', 'American Robin', 'Mountain Bluebird', 'Cactus Wren', 'Scissor-Tailed Flycatcher', 'Mockingbird', 'Western Meadowlark', 'California Gull', 'Common loon', 'Ring-necked Pheasant', 'American Goldfinch', 'Blue Hen Chicken', 'Western meadowlark', 'Mockingbird', 'Mockingbird', 'Baltimore Oriole', 'Black-Capped Chickadee', 'Ruffed Grouse', 'Brown Thrasher', 'Western Meadowlark', 'Cardinal', 'Willow Ptarmigan', 'American Goldfinch', 'Yellowhammer', 'Eastern Bluebird', 'Hermit thrush', 'Brown Pelican', 'Roadrunner', 'Western Meadowlark', 'American Robin', 'Black-Capped Chickadee', 'Cardinal', 'Mountain Bluebird', 'California Quail', 'Lark Bunting', 'American Goldfinch', 'Mockingbird', 'Western Meadowlark', 'Carolina Wren', 'Cardinal', 'Mockingbird', 'Nene', 'Cardinal', 'Purple Finch', 'Rhode Island Red'], #State Bird Answers
               ['12', 'Avalon', 'Book on the Wumpus', 'Flame Gems', 'Red', 'Blue Oysters', 'Heart', 'Basic Wizarding & Proper Care of Familiars', 'Niles', 'Ruby', 'Fire', 'Digmore Station', 'Wand', 'Private Stillson', 'Sir Malory', 'Mrs. Dowager', 'Morganthe', 'Valentina Heartsong', 'Witches', 'Rattlebones corrupted them.', 'Gorillas, Zebras, Lions'], #Magical Trivia Answers
               ['Wintertusk', 'Telegraph Box', 'Zafaria', 'The Badge of Leadership', 'Grandfather', 'Tempest', 'Ice Archway', 'The Water of Life', 'Wizard City', 'Jaques the Scatcher', 'Eloise Merryweather', 'Sir Malick de Logres', 'Sergent Major Talbot', 'Nosferabbit', 'Noboru Akitame', "Hetch Al'Dim", 'Charon', 'Harold Argleston', 'The Knights of the Silver Rose', 'Dimachaerus', 'The Water of Life'], #Mystical Trivia Questions
               ['Three', 'Death', 'Aztecosaurologist', 'A Gorgon', 'Advanced Flameology', 'Genuine Imitation Golden Ruby', 'Half moon/moon', '33', 'Thulinn', 'Ellen', 'Sarah Tanner', 'Cyrus Drake', 'Pyat MourningSword'], #Conjuring Trivia Questions Answers
               ['Dog', 'Red', 'Ancient Myths for Parliament', 'The Stray Cats', "Policeman's Ball", 'XX', "O'Leary", 'Newspapers', 'Sylvester Quimby Talbot III', 'Root Beer', 'Krokotopian', 'Night', '1:55', 'Hot Air Balloons', 'Saint Bernard and Saint Hubert', 'Fleabitten Ave', 'Clancy Pembroke', 'A Tennis Ball', 'Officer Digmore', 'Meowiarty'], #Marleybone Trivia Answers
               ['The Black Sun Necromancers', 'Gisela', 'Shrubberies', 'Zafaria and Marleybone', 'Yojimbo', 'Glorious Golden Archon', 'Cultivated Woodsmen', 'Skythorn Tower', 'Belloq', 'Sophia DarkSide', 'Binh Hoa', 'Gretta Darkkettle', 'Binh Hoa', 'Mugsy', 'Clanker', 'Aiuchi', 'Mavra Flamewing', 'Priya the Dryad', 'Takeda Kanryu', 'Phorcys'], #Spellbinding Trivia Answers
               ['Blue and Gold', 'Tan and Maroon', 'A spade', 'Diego Santiago Quariquez Ramirez the Third', 'Pixiecrown', 'Broccoli', 'Citrine', 'Bartleby', 'Kelvin', 'Ravenwood Bulletin', 'Death', 'Storm', 'Fairegrounds', 'Dalia Falmea', 'Lady Oriel', 'Sohomer Sunblade', 'Lady Oriel', 'Bartleby', 'Sylvia Drake', 'Rainbow Bridge'], #WizardCity Trivia Answers
               ]
def open_chrome_ublock():
    chrome_options = Options()
    chrome_options.add_extension("C:/uBlock-Origin_v1.16.12.crx")
    driver_path = "C:/chromedriver.exe"
    driver = webdriver.Chrome(executable_path = driver_path, chrome_options = chrome_options)
    driver.set_window_size(640, 480)
    driver.get(Trivia_websites[0])
    driver.implicitly_wait(4)
    return driver

def AutologinEnterer(driver):
                                                                    #PUT Username HERE
    driver.find_element_by_xpath("""//*[@id="userName"]""").send_keys("Username")
                                                                    #PUT Password HERE
    driver.find_element_by_xpath("""//*[@id="password"]""").send_keys("Password")
    driver.find_element_by_class_name("buttonsubmit").click()

def LoginInformation(driver):
    driver.find_element_by_class_name("login").click()
    framename = driver.find_element_by_xpath("""//*[@id="jPopFrame_content"]""").get_attribute("name")
    driver.switch_to_frame(framename)
    AutologinEnterer(driver)

def check_if_already_done(driver):
    try:
        driver.find_element_by_class_name("quizThrottle")
        return True
    except:
        return False

def open_new_tab(window_to_open):
    current_handle = driver.current_window_handle
    driver.execute_script("window.open(arguments[0])", window_to_open);
    for pos, window_handle in enumerate(driver.window_handles):
        if window_handle == current_handle:
            new_tab = driver.window_handles[pos + 1]
    driver.close()
    driver.switch_to_window(new_tab)

def choose_answer(driver, answers, questions):
    checktimes = 0
    lists = []
    options = []
    num_Of_Boxes = driver.find_elements_by_class_name("largecheckbox")
    _Answers = driver.find_elements_by_class_name("answerText")
    comparing_question = driver.find_element_by_class_name("quizQuestion")
    while True:
        for _ in range(len(num_Of_Boxes)):
            options.append([num_Of_Boxes[_], _Answers[_], comparing_question])
        for i, v, j in options:
            v = str(v.text).lower()
            j = str(j.text).lower()
            for pos, answer in enumerate(answers):
                answer = answer.lower()
                for pos1, quest in enumerate(questions):
                    quest = quest.lower()
                    if pos == pos1 and answer == v and quest == j:
                        print(j, v)
                        lists.append([i, v, j])
                        return lists[0]
               
def click_answer(lists):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'nextQuestion')))
    lists[0].click()
    driver.find_element_by_id("nextQuestion").click()

def finish_captcha(driver):
    while True:
        try:
            time.sleep(0.25)
            if driver.find_element_by_class_name("quizScore").text != "??":
                open_new_tab(Trivia_websites[i+1])
                time.sleep(1.5)
                return
        except:
            pass

driver = open_chrome_ublock()
LoginInformation(driver)
for i in range(10):
    trivia_done = check_if_already_done(driver)
    if trivia_done == True:
        try:
            open_new_tab(Trivia_websites[i+1])
        except:
            driver.close()
    elif trivia_done == False:
        #chooses the answers for 12 times basically finishes the quiz
        for _ in range(12):
            answer = choose_answer(driver, Answers[i], Questions[i])
            click_answer(answer)
            time.sleep(1)
        driver.find_element_by_xpath("""//*[@id="quizFormComponent"]/div[2]/div[1]/div[2]/a""").click()
        time.sleep(0.175)
        finish_captcha(driver)
driver.close()
