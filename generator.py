
from info import key, tempo, chord_type, progression_length # Imports variables from info.py
from chordDict import chordsTriads, chordsSevenths, chordsNinths # Imports three dictionaries that will be randomly selected from (based on given parameters)
import random # Imports built-in random module which will be used to select a random series of chords of a given type from the given scale
import datetime # Imports built-in date module which will be used to create logs of when each chord progression was generated

# The chord progression generator function
def chord_generator(chord_type, key, progression_length):
    # These if statements check to see which dictionary currentChordDict will be using (variable renamed to avoid confusion with chordDict.py)
    if chord_type == "Triads":
        currentChordDict = chordsTriads
    elif chord_type == "7ths":
        currentChordDict = chordsSevenths
    elif chord_type == "9ths":
        currentChordDict = chordsNinths
    else:
        return "Something went wrong; invalid chord type!"

    available_chords = currentChordDict[key].copy() # Creates a new list which is a copy of currentChordDict and its corresponding key
    random.shuffle(available_chords) # Shuffles the new list
    newProg = [] # Creates a new and empty list that will store the generated chord progression
    previous_chord = None # Creates a new variable assigned to None so it can be used in the while loop

    # This while loop will continue until the length of the generated chord progression is equal to progression_length
    while len(newProg) < progression_length:
        selected_chord = random.choice(available_chords) # Randomly selects a chord from available_chords
        # Adds (appends) the selected chord to the chord progression list as long as it is not a repeat of the previous chord
        if selected_chord != previous_chord:
            newProg.append(selected_chord)
            previous_chord = selected_chord

    assert len(newProg) == progression_length, "Chord progression lengths do not match!"
    return newProg

# Log recorder function
def log_chord_progression(chord_progression):
    # Gets the current date and time
    now = datetime.datetime.now()

    # Opens the log.txt file in append mode so previous data isn't overwritten
    with open("log.txt", "a") as f:
        f.write(f"\nChord progression generated on {now}:")
        f.write(f"\nKey: {key}\nTempo: {tempo} beats per minute\nChord type: {chord_type}\nProgression length: {progression_length} bars\n{chord_progression}\n") # Use newlines for visual clarity

    # Prints a confirmation message
    print("Chord progression recorded in log.txt")  

chord_progression = chord_generator(chord_type, key, progression_length) # Assigns the generated chord progression to a variable
print(chord_progression) # Prints the variable
log_chord_progression(chord_progression) # Calls log recorder function
