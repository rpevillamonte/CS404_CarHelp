knockingScore = 0
isPetrol = True

def showDashboardLights():
    print('''
            [1] Oil Pressure Light
            [2] Engine Temperature Light
            [3] ABS Light
            [4] Handbrake/Parking Brake Light
            [5] Traction Control Light
            [6] Engine Warning Light
            [7] Battery Alert Light
            [8] Tire Pressure Light
            [9] Fuel Indicator
            [10] Air Bag Indicator
            [11] Seat Belt Indicator
            [12] Washer Fluid Indicator

            Which of these lights are you seeing on your dashboard? (Type the number of your choice)
            ''')

def showCarProblems():
    print(
            '''
                [1] Knocking on the engine
                [2] Steering wheel is shaking when at use
                [3] Squeaking or grinding noise when braking
                [4] Steering feels heavy
                [5] Car does not accelerate, but RPM goes up
                [6] Car is consuming too much oil
                [7] Battery is not charging (even if it is a newly replaced battery)
                [8] Radiator leaking fluid
                [9] Turning the key and nothing happens
                [10] Too much smoke from the exhaust pipe
                [11] When changing gear, it will not engage easily / it will not stay in gear (Note: Applies to Manual Transmission) 
                [12] Fluid is leaking in the differential part 
                [13] Grinding noise when steering and difficulty in steering
                [14] Dropping gas mileage and loss of power 
                
                What can you feel/see about your car?
            '''
        )

def warningLights(prompt):
    switcher = {
        1: '''
                If your oil pressure indicator is on, it is possible that your engine does not have enough oil in it. 
                Engine oil should be changed 3-6 months or between 3,000 to 5,000 miles (depends on the quality of oil used). 
                Check your oil level first using the dip stick on your engine bay, if the oil level is below the dots of the stick, 
                we are sure that your engine needs to change its oil. Remember to use the quality of oil needed for your car as stated 
                to your user's manual. Changing it's viscosity might not be good to your engine. If ever your oil and oil filter has been changed 
                and the oil indicator light is still visible, let the mechanic check your air filter if it is clogged or there is too much dirt in it. 
                If it is still new and usable, your mechanic just needs to remove the dirt on the air filter by using vaccuum or air spray. If the light 
                is still on, let your mechanic finally check if your oil gauge is faulty or not. After all has been checked and your indicator is working 
                properly, there might be a small chance that your car has engine wear due to misuse or not maintaining your oil properly which can case to 
                reducing oil pressure in your engine. To avoid this, make sure to have your engine oil and oil filter changed regularly at a proper period 
                and proper way and dont stay too long at a lower gear at high rpm range as it can cause a lot of wear and overheating on your engine.''',
        2: '''
                If you see this indicator light up, it means that your engine is overheating. It could be for a couple of reasons: 
                First is that you're staying in lower gear at higher rpm which is too much stress for the engine and can cause overheating. 
                Second would be your coolant, it is important to check your coolant level everytime before you use your vehicle to avoid overheating in the middle of the road. 
                If your coolant level is low than the indicator on its resevoir, check if there is any leak below your engine bay. If there is no leak and your coolant is losing more, 
                have your mechanic check your engine if the coolant is getting inside your engine which is a big problem as it can damage your engine and shorten its life span. Having coolant 
                inside the engine could be caused by headgaskets so make sure that your mechanic will check your headgasket upon opening your engine.
             ''',
        3: '''
                If this indicator light lights up when you suddenly break down during your trip, do not panic, it is doing what it is supposed to do. But if it lights up even when 
                your car is on idle, it could mean that there is something wrong with the system. It is best to have your car checked by the dealership. 
                Make sure to have your insurance company tow your car back to the dealership as it is dangerous to drive it especially if your dealership is not near to your location. 
             ''',
        4: '''
                If the parking brake indicator lights up, make sure to check if you have disenganged it properly. If you are sure that your parking brake is disengaged properly, it means that you need to add brake 
                fluid in your reservoir. Check your brake fluid level on the engine bay. Most modern cars do not lose brake fluid so check if there is any leak in your brake fluid hose. Also check your brake 
                pads if it's still thick and in good condition. Worn-out brake pads could decrease the content of your brake fluid reservoir, but once you replace your brake pads with brand new ones, it will return to 
                its proper fluid level. 
             ''',
        5: '''
                If your traction control indicator lights up, it tells you that your vehicle's traction control system might have a broken or damaged sensor or some other malfunction. There are some cars that have 
                the same control module that operates both the ABS and traction control system, so the light sometimes comes on when there is also a problem with your ABS. Make sure to let your dealership handle 
                this systems as they have specialist for this type of problems. 
             ''',
        6: '''
                If your engine warning light is on, it could have a variety of reasons. It can indicate a serious issue that requires you to stop your car immediately if the indicator is flashing. Try to check if your diesel 
                cap is properly closed. If light is still on, we suggest to let your trusted mechanic do look into it and have them precisely point out where is the root of the problem. Most of the 
                modern scanning tools used by professional mechanics have accurate results and can point out which part of the engine needs service. 
             ''',
        7: '''
                If your battery indicator light is on, it tells you that there is an issue with the vehicle's charging system. Sometimes, its not your battery's fault. 
                You might have a loose or damaged battery cable, a damaged alternator or your alternator's belt is broken. If it is your battery at fault, you'll notice 
                that occassionally, your clock or center display is dimming and your car will sometimes have difficulties starting. If your car suddenly dies in the middle 
                of the road and the battery indicator lights up, try to inform other drivers about your situation and have your battery jumped by their battery so you 
                can start your car again and bring it home or have it serviced by your trusted mechanic. Upon getting to a service shop, have the mechanics check your car's battery
                if whether or not it can be charged again or it needs replacement. Most batteries last 2-5 years depending on how you use your car. Take note that you have to install 
                the right battery type and size for your car for the most efficient performance. Refer to your owner's manual for what type of battery is compatible to your car.
             ''',
        8: '''
                If your tire pressure light is on, try to find gas stations that have air machines available. It means that your tire pressure is too low or too high and 
                needs to be addressed. It is unsafe to drive with too low or too high air pressure. Most sedans, SUV's and pick up trucks have between 30-35 psi of air 
                each tire. Take note to put the right amount of tire pressure on your tires and refer to your owner's manual if you're not sure. 
             ''',
        9: '''
                If your fuel indicator light is on, it simply means that your car is too low on fuel! So make sure to refill your tank again and dont make it a habit on running with too 
                low fuel as your fuel pump might suck air which can cause damage on your fuel system. Always make sure your car is running enough fuel everytime you use it. 
             ''',
        10: '''
                If your airbag indicator light is on, it signals that something is wrong with one of your airbags or the system as a whole. Your airbags keep you safe 
                during accidents, so it is as important as your engine too. Make sure to address this issue immediately by your dealership as this is covered by your 
                warranty or insurance. 
              ''',
        11: '''
                This indicator reminds you to use your seatbelt. It is just a safety measure for you and your passenger. If the light does not turn off even if your seatbelt is already 
                off, let the mechanic check the wiring or module of your seatbelt indicator. 
              ''',
        12: '''
                This indicator reminds you to re-fill your window washer fluid. It is important to always check the level of your washer fluid as it will 
                always help you if there is dirt on your windshield. Remember to always use distilled water or the same washer fluid to ensure that there 
                is no unwanted minerals that might cause corrosion inside the tubing in the long run. 
              ''',
    }
    return switcher.get(prompt, 'I don\'t know that problem. Care to choose another one?')

def p_engineKnockToDo(knockingScore):
    if knockingScore == 0:
        return '''
                * Have your air/fuel mixture scanned if it is still correct
                * Have your engine bearings,pistons, crankshaft checked 
                * Dont rev the engine high at first start
                '''
    else:
        return '''
                * Check and change Sparkplugs if needed
                * Refuel with recommended octane level
                * Regularly change your oil
                '''
    
def p_engineKnock():
    global knockingScore
    questions = ['Does the knocking sound become louder and faster as you accelerate?', 'Do you use the proper octane level of petrol for your car?', 'How old are your current sparkplugs?']
    questionIndex = 0
    while questionIndex < 3:
        if questionIndex != 2:
            print()
            print(f"{questions[questionIndex]}  (Y/N)")
            prompt = input('Enter your choice here: ')
            if prompt.lower() == 'y':
                knockingScore += 1
        else:
            print(questions[questionIndex])
            print('''
                    [0] - New (Below 10,000 km) 
                    [1] - 10,001 - 25,000 km    
                    [2] - 25,001 - 40,000 km    
                  ''') 
            prompt = int(input('Enter your choice here: '))
            switcher = {0 : 0, 1 : 1, 2 : 2}
            knockingScore += switcher.get(prompt)
        questionIndex += 1
    if knockingScore == 0:
        return '''
                Your engine might not have detonation (incorrect air/fuel mixture) but you might hear knocking sounds. As 
                your pistons move up and down in the engine, they turn the crankshaft which ultimately sends power to the 
                wheels. The rod bearings facilitate smooth piston movement, but if they are worn out, the pistons will start 
                to rattle against the crankshaft which creates a very similar knocking sound. Have your mechanic check the 
                bearings or other work done on the pistons and crankshaft. This could be a lengthy and costly repair. 
                To avoid it from happening again, make sure to: 
                    (1) Change your oil filter regularly with your new oil. 
                    (2) Wait for the oil to travel throughout the engine (modern cars takes 5-10 seconds) unless it is an emergency. 
                    (3) Clean your fuel-injectors regularly by filling your gas tank with fuel-injector cleaner every 2,000 km, and  
                Note: These are just preventive measures and will not ensure that your engine will not have knock problems, 
                but the risk of having knocks will be decreased. 
                '''
    else:
        return '''
                Your engine might been experiencing detonation where the air/fuel mixture is not balanced. More air than 
                fuel means your engine is having lean mixture, while having more fuel than air means that your engine is 
                having rich mixture. Changing your sparkplugs every after 30,000 km is a must in order to prevent these 
                kinds of problems. The sparkplugs are the one responsible for igniting the fuel in your cylinders. If the 
                sparkplugs are worn out or dirty then it will not function very well. Also, the octane level of your fuel 
                is very important. Make sure to follow the recommended octane level for your car, but you can go higher 
                than the recommended octane level, but you cannot go below. Make sure that your fuel is clean by only 
                filling your car into a trusted gas station. To fix this, your mechanic might replace your sparkplugs 
                and tune your car for the right air/fuel mixture. Have your car scanned by their scan tool to find 
                a more accurate result about your air/fuel mixture. 
                To avoid it from happening again, make sure to: 
                    (1) Change your Sparkplugs every after 30,000km 
                    (2) Use the recommended octane for your car or higher, and 
                    (3) Use only clean fuel by refilling with your trusted station. 
                Note: Those are just preventive measures and will not ensure that your engine will not have knock problems, 
                but the risk of having knocks will be decreased. 
                '''
    
def carToDo(prompt): 
    global knockingScore
    global isPetrol
    if prompt == 1:
        if isPetrol:
            return p_engineKnockToDo(knockingScore)
        else:
            return '''
                    * Have your air/fuel mixture scanned if it is still correct
                    * Have your engine bearings,pistons, crankshaft checked 
                    * Dont rev the engine high at first start
               '''
    else:
        switcher = {
            2: '''
                * Fill your tires with proper tire pressure.
                * Do wheel balancing and alignment 
                * Check balljoints 
            ''',
            3: '''
                * Check brake fluid level
                * Change brake pads (Also brake rotors if necessary) 
            ''',
            4: '''
                * Check for tire damages
                * Check steering fluid condition
                * Flush and replace steering fluid if dirty
            ''',
            5: '''
                * Check the clutch components
                * Replace the clutch set if already worned out
                * Avoid pressing clutch for too long
            ''',
            6: '''
                * Check for any oil leaks
                * Change your oil regularly every 5,000 - 10,000 km
                * Use the recommended oil viscosity and level
            ''',
            7: '''
                * Have your alternator checked if it can be fixed or must be replaced
                * Have voltmeter for monitoring the charging status of battery
            ''',
            8: '''
                * Check of the fluid is the same with your antifreeze coolant
                * If radiator is broken, replace it with the original one from your manufacturer
            ''',
            9: '''
                * Have your starter motor checked 
                * Test it 5-10 times after being fixed 
            ''',
            10: '''
                * Check for any damage on the exhaust system
                * Have your air/fuel mixture checked using scan tool
                * Regularly change your oil every 5,000 - 10,000km
            ''',
            11: '''
                * Check clutch first if there is any wear or damage
                * If clutch is not the problem, you need to let them check your transmission or gearbox for damage
                * Change transmission fluid every 35,000 to 45,000 km
            ''',
            12: '''
                * Check if the fluid is really your transmission fluid
                * If the hole exist, have it fixed immidiately and change new transmission fluid 
                * Regularly clean your underchassis and check for cracks or leaks
            ''',
            13: '''
                * Check if there is any damage on tires
                * Check steering fluid if for any leaks.
                * Have your steering rack checked for any damage
            ''',
            14: '''
                * Check air filter and air filter box for any clogging
                * Replace air filter and cabin filter with original one from manufacturer if needed
                * Replace air filter every after 25,000 to 30,000 km 
            '''
        }
    knockingScore = 0
    return switcher.get(prompt, 'Can\'t provide a solution for this. Maybe choose another one?')

def carProblem(prompt):
    global isPetrol
    if prompt == 1:
        if isPetrol:
            return p_engineKnock()
        else:
            return '''
                    Your engine might not have detonation (incorrect air/fuel mixture) but you might hear knocking sounds. As 
                    your pistons move up and down in the engine, they turn the crankshaft which ultimately sends power to the 
                    wheels. The rod bearings facilitate smooth piston movement, but if they are worn out, the pistons will start 
                    to rattle against the crankshaft which creates a very similar knocking sound. Have your mechanic check the 
                    bearings or other work done on the pistons and crankshaft. This could be a lengthy and costly repair. 
                    To avoid it from happening again, make sure to: 
                        (1) Change your oil filter regularly with your new oil. 
                        (2) Wait for the oil to travel throughout the engine (modern cars takes 5-10 seconds) unless it is an emergency. 
                        (3) Clean your fuel-injectors regularly by filling your gas tank with fuel-injector cleaner every 2,000 km, and  
                    Note: These are just preventive measures and will not ensure that your engine will not have knock problems, 
                    but the risk of having knocks will be decreased. 
                   '''
    else:
        switcher = {
            2: '''
                If youre steering wheel shakes while driving, it is either you have damaged suspension components or wheel 
                bearings are loose. Have your car suspension checked if there is any damage or leak. Also have your wheel 
                parts checked, mainly:
                    (1) balljoints, 
                    (2) wheel balance, or 
                    (3) wheel alignment. 
                To avoid having damaged suspension, ball joints and misaligned wheels, always be gentle on rough roads or 
                humps even if you have a good suspension set. Driving it gently through rough surfaces will prevent your parts 
                from having unecessary shock load. Also, always check your tire pressure, use the recommended tire pressure for 
                your car and always check if there is any leak on the suspension before having long drive to avoid accidents. 
            ''',
            3: '''
                The grinding noise you hear everytime you press the brake pedal will only be due to your brake system. Check the 
                brake fluid level under your hood. If it is below the line level, it is a sign that you need to replace your 
                brake pad set for your car. The grinding noise and the fluid level are the physical indicators that your brake 
                pads need to be changed. Also, have your drum breaks pads (if there is) replaced because it wears too with your 
                front brakes and you'll need it for better park brake grip. Always check your brake rotors if its too thin, the 
                mechanic will recommend you to also replace it, but it usually takes a long time before it wears out.
            ''',
            4: '''
                There are only two things you need to check if your steering wheel feels too hard or heavy to rotate than usual. 
                First, check if your tires have any punctures or if you have a flat tire. If there are no punctures or damage to 
                the tires, have your steering fluid checked if it has leaked out or it is too dirty. Dirty steering fluid makes 
                steering difficult and creates noise when using the steering wheel. Have your steering fluid flushed and replaced by your 
                trusted mechanic or do it yourself if you know the process. 
            ''',
            5: '''
                If your car's RPM gauge goes up, but your car will not accelerate or pull, it tells you that your 
                clutch system is already bad. 
                If you smell something like burning rubber in your car, the problem is your clutch. 
                Bring your car to your trusted mechanic and have your clutch set replaced. It usually includes the Pressure Plate, 
                Driven Plate and the release bearing. 
                Fair warning: it is pretty expensive, but if you replace it early, it will prevent further damage on your 
                transmission. To prolong the life of your clutch system, avoid pressing the clutch when you're in a stop for a 
                long period of time. Also, use the proper gear for proper places. 
                Example is when you're in an uphill, use lower gears like 1st or 2nd gear depending 
                on your speed (Applicable to manual transmission).
            ''',
            6: '''
                Recheck your oil stick when the car has been idle for a couple of hours or more. If the oil level is below the 
                indicator, check if there is any sign of leakage underneath the oil cap or filter. If there is no leakage, 
                then you need to change your oil. Always try to use the best oil or atleast the recommended oil from your car 
                manufacturer and/or use oil with the recommended viscosity based on your owner's 
                manual. Using poor quality oil will corrode your engine and will not properly coat and cool your engine which 
                cause it to easily burn. 
            ''',
            7: '''
                This is a sign that your alternator is failing. Your alternator charges your battery while your car is running. 
                Have your alternator checked if it can still be fixed or replaced. To avoid having issues while on a long trip, 
                always have a voltmeter that checks if your battery is being charged by your alternator. 
            ''',
            8: '''
                Check if the discharged fluid is just antifreeze or water from your air conditioner. If the fluid is just water, no
                need to fret, since that is just normal. But if it's the same texture and smell like your antifreeze, have your 
                radiator replaced immediately. It can cause overheating and worse, an engine fire. Have your coolant flushed and 
                replaced. Always check if there is uncommon leaks from your car before going for a trip. 
            ''',
            9: '''
                If you turn your key and you hear a loud solid click, then you most likely have a faulty starter motor. Have 
                your starter motor checked by a professional mechanic to find out the reason why it failed. If you find that starter motor
                is broken and beyond repair, then have it replaced. Also, keeping your battery terminals clean always will help 
                prevent starter problems. 
            ''',
            10: '''
                The emission system is designed to keep pollution to a minimum while making sure your car runs properly. The 
                system includes a lot of sensitive equipment that can fail from time to time and these cause a variety of 
                different problems in the car. For example, an O2 sensor that is faulty may affect the fuel mixture, 
                leading to inefficiencies in the running and economy of the vehicle. Have your exhaust system checked if there 
                are any components that causes too much emissions. Despite this, dark smoke can be normal for diesel engines, but 
                excessive smoke can be a sign that your car is running rich. Have your car scanned by your mechanic's scan tool 
                to monitor the air-fuel mixture because your car might be running rich, which means more fuel is being wasted 
                than necessary which is responsible for too much smoke emitting on your exhaust. 
            ''',
            11: '''
                This is a sign that there is a problem with your gearbox or clutch system. Have your clutch checked first because 
                it is easier to replace the clutch set than to have your transmission or gearbox to be parted out. If your clutch 
                is still good, then that is the time to have your gearbox or transmission system checked. To avoid having problems 
                with your transmission, replace your transmission fluid every 35,000 to 45,000 km and make sure to use the proper 
                viscosity and enough liters needed. Having your transmission fluid maintained properly is cheaper than fixing your 
                transmission. 
            ''',
            12: '''
                Your differential is part of your transmission system. Leaking fluid from differential is most likely your transmission 
                fluid. Check carefully if its really the fluid from your transmission or just water from your AC. If it is your transmission 
                fluid, have your car serviced and let your mechanic fix the hole where the leak is coming from. Also, have your transmission 
                fluid changed after the fix. To avoid having a cracked oil pan, always clean your underchassis every time after you use your 
                vehicle on rainy days especially during a flood. It can cause corrosion overtime so you must clean your underchassis too, 
                plus you can also see if there are any existing problems underneath. 
            ''',
            13: '''
                If you find your car difficult to steer, make sure that your steering fluid is sufficient and your tires are not flat. 
                If there is a leakage of steering fluid and it is accompanied by a grinding noise when you steer your steering wheel, 
                it is a sign that you have a failing steering rack. The steering rack is the most vital part in your steering system, so it 
                is necessary to have it fixed immediately because it is extremely dangerous to drive with broken steering. Your steering 
                rack will be replaced as its too expensive and hard to repair one. You also dont want to risk having another failure 
                again so its better to replace it with new ones. 
            ''',
            14: '''
                There could be many reasons why you feel the excessive consumption of fuel and loss of power, but the most basic thing 
                we tend to forget is checking the air filter. If your air filter is clogged and dirty, you'll surely feel the loss of power 
                while your car is spending huge amounts of fuel, unlike when it is new. Check your air filter if it is still clean and 
                there is no clogging on the vents where the air passes through. If it is too dirty, replace it with the new one and make 
                sure that it is the same one from your manufacturer to prevent any more issues. You should change your air filter every after 
                25,000-30,000 km or at least once every 2 years. It is also a good idea to change your cabin filter together with your engine 
                air filter. The cabin filter is the filter for your air conditioner and it is necessary to replace it regularly because it keeps
                your air clean inside your car. 
            '''
        }
        return switcher.get(prompt,'Yikes! I have not experienced that problem before.')

def solution(is_petrol, light_check, exp_index, knocking_score=0):
    global isPetrol
    if is_petrol == 1: isPetrol = False
    
    if light_check == 0:
        return {'light_solution' : warningLights(exp_index)}
    else:
        return {'problem_solution' : carProblem(exp_index),
                'to_do' : carToDo(exp_index)
                }
    
# q/a portion for petrol problems

#def ask():
#    stillHaveQuestions = True
#    print('''
#            Are there any warning lights on your dashboard?
#            [Y]es | [N]o
#            ''')
#    answer = input("Enter your choice here: ")
#    if answer.lower() == 'y':
#        while stillHaveQuestions == True:
#            showDashboardLights()
#            answer = int(input("Enter your choice here: "))
#            # show the result of the input choice
#            print(warningLights(answer))
#            print()
#            print(
#                'Do you still want to ask about the different lights in your dashboard? [Y] | [N]')
#            answer = input("Enter your choice here: ")
#            if answer.lower() == 'n':
#                stillHaveQuestions = False
#    elif answer.lower() == 'n':
#        while stillHaveQuestions == True:
#            showCarProblems()
#            answer = int(input("Enter your choice here: "))
#            print(carProblem(answer))
#            print("TO DO LIST:")
#            print(carToDo(answer))
#            print()
#            print(
#                'Does your car have other problems besides what you have just searched? [Y] | [N]')
#            answer = input("Enter your choice here: ")
#            if answer.lower() == 'n':
#                stillHaveQuestions = False

# main program starts here

#print('''
#        Hello! This is <insert system name here>, your expert system for your needs. Although
#        I am still a new recruit, so I do not know very much about cars unlike you humans do.
#        Never fret, though! My creators have shown me some common problems you humans have 
#        with cars. 
#
#        I am going to ask you some questions and based from your answers, I will suggest possible 
#        solutions to your problem. 
#
#        Now, is your problem related to your petrol or your diesel?
#
#        [1] Petrol
#        [2] Diesel
#      ''')
#
#flag = True
#
#while flag == True:
#    choice = int(input("Enter your choice here: "))
#    if choice == 1 or choice == 2:
#        if choice == 2: isPetrol = False
#        flag = False
#    else:
#        print("Sorry! I don't much about that problem.")
#ask()
#
#print('''
#        I hope I was able to help you in some way! Obviously, I'm not the best person(?)
#        to ask about your problems about cars. I just gave you an idea about what might be the problem
#        so you can ask your mechanic about it. Hopefully you'll be able to consult a real mechanic soon.
#
#        Thank you for consulting my services!
#      ''')
#
