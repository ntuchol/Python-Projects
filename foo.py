while True:
  user_input = input("Enter something: ")
  if user_input == "foo":
    print("You entered 'foo'! Now I'm printing this message.")
    break # Exit the loop after the event

text_data = "This is some text with foo inside it."
if "foo" in text_data:
  print("Found 'foo' in the text! Printing this message.")
  
event_triggered = False
# ... some code where an event might happen ...

if "foo" in some_input_or_data:
  event_triggered = True

if event_triggered:
  print("The 'foo' event has occurred! Printing this message.")