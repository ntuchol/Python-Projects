

from javax.swing import JFrame, JLabel
from java.awt import BorderLayout

frame = JFrame("My Jython Window")
label = JLabel("Hello, Jython!", JLabel.CENTER)

frame.add(label, BorderLayout.CENTER)
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
frame.setSize(300, 200)
frame.setVisible(True)
