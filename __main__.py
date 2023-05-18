
# MAIN Page

from exporter import midiExporter # Imports midiExporter function from exporter.py (since its the last thing to run it will be ran here instead of in its own module)

if __name__ == "__main__": # Calls midiExporter function if this is the __main__ file
    midiExporter()
