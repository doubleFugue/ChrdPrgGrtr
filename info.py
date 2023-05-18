
print("Welcome to the Chord Progression Generator!") # Welcome message on program startup

class ChordInput:
    def __init__(self):
        # Initialize all instance variables to None so they can be used later
        self.key = None
        self.tempo = None
        self.chord_type = None
        self.progression_length = None

    def get_key(self): # Asks user for desired key (includes enharmonic equivalents)
        keyRange = ['A', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'Ab']
        while self.key is None:
            key = input("Enter the desired key (use 'b' for flats and '#' for sharps): ")
            if key in keyRange:
                self.key = key
            else:
                print("Invalid input. Please enter a valid key (e.g. C, C#, Db, etc).")

        assert self.key in keyRange, "Invalid key"
        return self.key

    def get_tempo(self): # Asks user for desired tempo
        while self.tempo is None:
            # This try/except block was implemented because the flow of the program was disrupted if the user entered the tempo as a string (i.e. "eighty" instead of 80)
            try:
                tempo = int(input("Enter the desired tempo (in beats per minute): "))
                if (50 <= tempo <= 200): # Only accepts values between 50 and 200 (inclusive)
                    self.tempo = tempo
                elif (tempo < 50) or (tempo > 200):
                    print("Please enter a tempo between 50 and 200 beats per minute.") # 50 to 200 beats per minute encompasses a reasonable range of tempo, in my opinion.
                else:
                    print("Invalid input.")
            except ValueError:
                print("Please enter the tempo value as a number.")

        assert isinstance(self.tempo, int) and (50 <= self.tempo <= 200), "Invalid tempo"
        return self.tempo

    def get_chord_type(self): # Asks user if they want to use only triads, seventh, or ninth chords
        chord_types = ["triad", "triads", "seventh", "sevenths", "ninth", "ninths", "7th", "7ths", "9th", "9ths"] # List of chord types (includes some variety of spellings for user convenience)
        while self.chord_type is None:
            use_chord_type = input("Do you want to use triads, 7th, or 9th chords? (triads/7th/9th): ").lower()
            # These if/elif/else statements were implemented for consistency (I didn't want each output to look different depending if the user typed 'seventh' or '7ths', for example)
            if use_chord_type in ["triad", "triads"]:
                self.chord_type = "Triads"
            elif use_chord_type in ["seventh", "sevenths", "7th", "7ths"]:
                self.chord_type = "7ths"
            elif use_chord_type in ["ninth", "ninths", "9th", "9ths"]:
                self.chord_type = "9ths"
            else:
                print("Invalid input. Please enter either 'triads', '7ths', or '9ths'.")

        assert self.chord_type in ["Triads", "7ths", "9ths"], "Invalid chord type"
        return self.chord_type

    def get_progression_length(self): # Asks user for desired chord progression length
        while self.progression_length is None:
            # Another try/except block to prevent flow disruption if ValueError occurs
            try:
                progression_length = int(input("Enter the length of the progression (in bars): "))
                if (4 <= progression_length <= 16): # Only accepts values between 4 and 16 (inclusive)
                    self.progression_length = progression_length
                else:
                    print("Invalid input. Please enter a progression length between 4 and 16 bars.")
            except ValueError:
                print("Please enter the progression length as a number.")

        assert isinstance(self.progression_length, int) and (4 <= self.progression_length <= 16), "Invalid progression length"
        return self.progression_length # Additional note: this function assumes 1 bar = 1 chord, so 4 bars = 4 chords, etc

# Creates a class instance 'chord_input' and then assigns several variables to the results of their respective instance methods
chord_input = ChordInput()
key = chord_input.get_key()
tempo = chord_input.get_tempo()
chord_type = chord_input.get_chord_type()
progression_length = chord_input.get_progression_length()

# Prints the user's new chord progression
print("Results:")
print(f"Key: {key}")
print(f"Tempo: {tempo} beats per minute")
print(f"Chord type: {chord_type}")
print(f"Progression length: {progression_length} bars")
