

line = "return dwc3_endpoint_interrupt dwc, &event->depevt);"

if line.find("return") != -1 and line.find("(") == -1:
    print("find return, not find (")
else:
    print("else")


if line.find("(") != -1:
    print("find (")