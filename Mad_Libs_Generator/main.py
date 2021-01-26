import random



class Play:
    num = random.randint(1,3)

    if num == 1:
        adjective1 = input("Please Enter An Adjective:")
        adjective2 = input("Please Enter Other Adjective: ")
        type_of_bird = input("Please Enter A Type Of Bird:")
        room_in_a_house = input("Please Enter A Type Of Room In A House:")
        verb_past_tense = input("Please Enter A Past Verb:")
        verb = input("Please Enter a Verb:")
        relative_name = input("Please Enter A Relative's Name:")
        noun = input("Please Enter A Noun:")
        a_liquid = input("Please Enter A Type Of Liquid:")
        verb_ending = input("Please Enter a Verb Ending:")
        part_of_the_body = input("Please Enter A Part Of A Body:")
        plural_noun = input("Please Enter A Plural Noun:")
        verb_ending2 = input("Please Enter A Verb Ending:")
        noun2 = input("Please Enter A Noun:")

        paragraph = "It was a " + adjective1 + ", cold November day. I woke up to the " + adjective2 + " smell of " + type_of_bird + " roasting in the " + room_in_a_house + " downstairs. I " + verb_past_tense + " down the stairs to \"see if I could help " + verb + " the dinner. My mom said,\"See if " + relative_name + " needs a fresh " + noun + ".\" So I carried a tray of glasses full of " + a_liquid + " into the " + verb_ending + " room. When I got there, I couldn\'t believe my " + part_of_the_body + " ! There were " + plural_noun + " " + verb_ending2 + " on the " + noun + " !"
        print(paragraph)

    elif num == 2:
        adjective3 = input("Please Enter An Adjective:")
        nationality = input("Please Enter A Nationality:")
        person = input("Please Enter A Person Name:")
        noun3 = input("Please Enter A Noun:")
        adjective4 = input("Please Enter An Adjective:")
        noun4 = input("Please Enter A Noun:")
        adjective5 = input("Pleas Enter An Adjective:")
        adjective6 = input("Please Enter An Adjective:")
        plural_noun2 = input("Please Enter A Plural Noun:")
        noun5 = input("Please Enter A Noun:")
        number = input("Please Enter A Number:")
        shapes = input("Please Enter A Shape:")
        food = input("Please Enter A Food:")
        food2 = input("Please Enter Other Food:")
        number2 = input("Please Enter A Number:")
        paragraph2 = "Pizza was invented by a " + adjective3 + " " + nationality + " chef named " + person + ". To make a pizza, you need to take a lump of " + noun3 + " , and make a thin, round " + adjective3 + " " + noun4 + ". Then you cover it with " + adjective4 + " sauce, " + adjective5 + " cheese, and fresh chopped " + plural_noun2 + " . Next you have to bake it in a very hot " + noun5 + " . When it is done, cut it into " + number + " " + shapes + " . Some kids like " + food + " pizza the best, but my favorite is the " + food2 + " pizza. If I could, I would eat pizza " + number2 + " times a day!"
        print(paragraph2)

    elif num == 3:
        animal = input("Please Enter An Animal:")
        country = input("Please Enter A Country:")
        plural_noun3 = input("Please Enter A Pural Noun:")
        food3 = input("Please Enter A Food:")
        type_of_screen_device = input("Please Enter A Type Of Screen Device:")
        noun6 = input("Please Enter A Noun:")
        verb2 = input("Pleas Enter A verb:")
        verb3 = input("Please Enter A verb:")
        adjective7 = input("Please Enter An Adjective:")
        paragraph3 = "The majestic " + animal + " has roamed the forests of " + country + " for thousands of years. Today, she wanders in search of " + plural_noun3 + " . She must find food to survive. While hunting for " + food3 + " , she found a/an " + type_of_screen_device + " hidden behind a " + noun6 + ". She has never seen anything like this before. What will she do? With the device in her teeth, she tries to " + verb2 + " , but nothing happens. She takes it back to her family. When her family see it, very quickly " + verb3 + ". Soon, the device becomes " + adjective7 + ", and the family decides to put it back where they found it."
        print(paragraph3)