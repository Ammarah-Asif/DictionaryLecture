words={"amplitude":"The maximum extent of a vibration or oscillation, measured from the position of equilibrium.",
   "watermark":"a faint design made in some paper during manufacture that is visible when held against the light and typically identifies the maker.",
   "calligraphy":"the art of producing decorative handwriting or lettering with a pen or brush.",
   "chlorophyll":"a green pigment, present in all green plants and in cyanobacteria, which is responsible for the absorption of light to provide energy for photosynthesis.",
   "shrub":"a woody plant which is smaller than a tree and has several main stems arising at or near the ground.",
"herbivorous":"animal feeding on plants.",
   "introvert":"a shy, reticent person.",
   "extrovert":"a person who is friendly and outgoing.",
   "vagabond":"a person who is unable to find a job or a home."
  }
print("This is my dictionary you can find in this list->",words.keys())
a=input("Enter the word you want to search for->")
print(words.get(a))